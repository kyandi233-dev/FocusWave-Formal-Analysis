"""Read-only real-data checks. Not a model fit or an independent physiology test."""
import hashlib
import json
import zipfile
from pathlib import Path
import argparse
import numpy as np
import pandas as pd


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input-root', type=Path, required=True)
    parser.add_argument('--repaired-source', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    k = ['session_id', 'block_id', 'probe_index_in_block']
    hr = 'mmwave_hr_fused_bpm_median'
    br = 'mmwave_breath_rate_breaths_per_min_median'
    m = pd.concat([pd.read_csv(args.input_root / n) for n in ['mmwave_probe_merge_ready.csv', 'mmwave_probe_merge_ready_E.csv']], ignore_index=True)
    m['block_id'] = 'b' + m.legacy_block_num.astype(str)
    bridge = pd.read_csv(args.input_root / 'mmwave_cardiopulmonary_taskb_source.csv')
    out = pd.read_csv(args.repaired_source)
    x = out.merge(m, on=k, suffixes=('_out', '_in'), validate='one_to_one')
    assert len(x) == len(out) == len(m)
    fields = [hr, br, 'mmwave_hr_usable_window_fraction', 'window_effective_start_unix_ms', 'window_end_unix_ms', 'probe_onset_unix_ms', 'mmwave_state', 'mmwave_missing_reason', 'mmwave_source_commit', 'mmwave_source_run_id']
    checks = {}
    for c in fields:
        a, b = x[c+'_out'], x[c+'_in']
        checks[c] = int((~(a.eq(b) | (a.isna() & b.isna()))).sum())
    assert all(v == 0 for v in checks.values())
    z = zipfile.ZipFile(args.input_root / 'archive_predictions.zip')
    universe = pd.read_csv(z.open('AS.standalone__behavior.nogo_commission.raw.v1__archive.csv'))
    base = pd.read_csv(z.open('AS.behavior_reference__archive.csv'))
    sensor = pd.read_csv(z.open('AS.sensor_only_joint__archive.csv'))
    full = pd.read_csv(z.open('AS.full__archive.csv'))
    full = full[full.model_id.eq('full')]
    keyset = lambda d: set(d[k].itertuples(index=False, name=None))
    assert keyset(m) == keyset(universe) == keyset(bridge)
    identity = out.merge(universe[k+['participant_group_id']], on=k, suffixes=('', '_universe'), validate='one_to_one')
    assert identity.participant_group_id.eq(identity.participant_group_id_universe).all()
    eligible = out.loc[np.isfinite(out[hr]) & np.isfinite(out[br])]
    coverage = []
    for label, frame in [('full13', full), ('sensor8_independent', sensor), ('behavior_plus_cardiopulmonary', base), ('standalone_hr_or_br', universe)]:
        matched = frame[k].merge(eligible[k+['participant_group_id']], on=k, validate='one_to_one')
        coverage.append({'comparison': label, 'n_probes': len(matched), 'n_participants': int(matched.participant_group_id.nunique()), 'n_sessions': int(matched.session_id.nunique())})
    recomputed = []
    for name in z.namelist():
        d = pd.read_csv(z.open(name))
        for mid, g in d.groupby('model_id'):
            assert not g.duplicated(k).any()
            assert g.participant_group_id.eq(g.outer_fold_group).all()
            assert not g.model_failed.any()
            assert g.q1_binary.eq(g.q1_nominal_4class.eq(1).astype(int)).all()
            assert g.p_q1_equals_1.between(0, 1).all()
            p = g.p_q1_equals_1.clip(np.finfo(float).eps, 1 - np.finfo(float).eps)
            y = g.q1_binary
            losses = -(y*np.log(p)+(1-y)*np.log(1-p))
            value = float(losses.groupby(g.participant_group_id).mean().mean())
            recomputed.append({'analysis_set_id': g.analysis_set_id.iloc[0], 'model_id': mid, 'computed_loss': value, 'computed_n_probes': len(g), 'computed_n_participants': g.participant_group_id.nunique()})
    reference = pd.read_csv(args.input_root / 'headline_model_performance.csv')
    joined = pd.DataFrame(recomputed).merge(reference, on=['analysis_set_id', 'model_id'], validate='one_to_one')
    assert len(joined) == len(reference) == 43
    # The reference CSV stores SIX decimals, so exact full-precision equality is unavailable.
    assert joined.computed_loss.map(lambda v: format(v, '.6f')).eq(joined.participant_equal_log_loss.map(lambda v: format(v, '.6f'))).all()
    assert joined.computed_n_probes.eq(joined.n_probes).all()
    assert joined.computed_n_participants.eq(joined.n_participants).all()
    report = {
        'status': 'SOURCE_FIX_REAL_DATA_PASS_V3_ARCHIVE_PENDING',
        'm1_rows': len(m), 'finite_hr_n': int(np.isfinite(out[hr]).sum()), 'finite_br_n': int(np.isfinite(out[br]).sum()),
        'source_field_mismatches': checks, 'governed_identity_mismatches': 0,
        'coverage_from_frozen_v1_memberships_and_m1': coverage,
        'v1_archive_model_rows_recomputed': 43, 'v1_loss_agreement_at_reported_decimals': 6,
        'v1_loss_max_abs_difference_from_rounded_summary': float((joined.computed_loss-joined.participant_equal_log_loss).abs().max()),
        'v3_prediction_archive_read': False, 'models_retrained': False,
        'repaired_source_sha256': hashlib.sha256(args.repaired_source.read_bytes()).hexdigest(),
        'source_files': {n: hashlib.sha256((args.input_root / n).read_bytes()).hexdigest() for n in ['archive_predictions.zip', 'headline_model_performance.csv', 'mmwave_probe_merge_ready.csv', 'mmwave_probe_merge_ready_E.csv', 'mmwave_cardiopulmonary_taskb_source.csv']},
        'limitations': ['Uses archived accepted v1 membership, not final v3 input archives.', 'Does not reprocess raw radar or claim independent physiological validity.', 'The 1705-probe independent sensor model requires re-evaluation; its prior 1703-probe predictions cannot be relabeled.'],
    }
    with args.output.open('x', encoding='utf-8') as handle:
        json.dump(report, handle, ensure_ascii=False, indent=2)
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
