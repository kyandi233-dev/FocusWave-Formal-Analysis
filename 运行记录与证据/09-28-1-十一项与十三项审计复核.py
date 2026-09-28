"""Recheck archived aggregate outputs and M1 membership-audit records.
No raw signal processing or model fitting is performed. Requires pandas/numpy.
Input directory contains the seven named downloaded evidence files. Outputs are
aggregate only; no participant identifiers or per-probe records are exported.
"""
from pathlib import Path
import hashlib
import json
import argparse
import numpy as np
import pandas as pd


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def recheck(input_root: Path, output_root: Path) -> dict:
    output_root.mkdir(parents=True, exist_ok=True)
    names = ['cardiopulmonary_model_evaluation.csv', 'headline_model_performance.csv',
             'audit_v2_detail.csv', 'audit_v2_summary.json',
             'mmwave_probe_frame_membership_audit.csv', 'mmwave_probe_frame_membership_audit_E.csv',
             'm1_source_report.json']
    missing = [n for n in names if not (input_root / n).is_file()]
    if missing:
        raise FileNotFoundError(missing)
    v3 = pd.read_csv(input_root / names[0])
    v1 = pd.read_csv(input_root / names[1])
    detail = pd.read_csv(input_root / names[2])
    declared = json.loads((input_root / names[3]).read_text(encoding='utf-8-sig'))
    frame = pd.concat([pd.read_csv(input_root / names[4]), pd.read_csv(input_root / names[5])], ignore_index=True)
    source = json.loads((input_root / names[6]).read_text(encoding='utf-8-sig'))
    key = ['repeat_participant_id','session_id','block_id','probe_id','window_name']
    assert not frame.duplicated(key).any()
    assert not detail.duplicated(key).any()
    membership_join = frame[key].merge(detail[key], on=key, how='outer', indicator=True, validate='one_to_one')
    assert membership_join['_merge'].eq('both').all()
    selected = frame[frame.audit_status.eq('SELECTED')].copy()
    assert selected.new_n_frames.notna().all()
    lower_violation = int((selected.new_first_science_timestamp_ms < selected.window_effective_start_unix_ms).sum())
    upper_violation = int((selected.new_last_science_timestamp_ms >= selected.probe_onset_unix_ms).sum())
    frame_count_mismatch = int((selected.new_n_frames != selected.new_i1_exclusive-selected.new_i0).sum())
    hash_mismatch = 0
    for row in selected.itertuples(index=False):
        indices = ','.join(map(str,range(int(row.new_i0),int(row.new_i1_exclusive))))
        expected = hashlib.sha256(indices.encode('ascii')).hexdigest()
        hash_mismatch += expected != row.new_membership_digest_sha256
    membership_changed = selected.new_membership_digest_sha256.ne(selected.legacy_membership_digest_sha256)
    valid = detail.new_membership_digest_sha256.notna() & detail.legacy_membership_digest_sha256.notna()
    same = valid & detail.new_membership_digest_sha256.eq(detail.legacy_membership_digest_sha256)
    old_anchor = detail.old_incoming_previous_bpm_reconstructed
    new_anchor = detail.new_incoming_previous_bpm_reconstructed
    equal_anchor = (old_anchor.eq(new_anchor) | (old_anchor.isna() & new_anchor.isna()))
    stateful = ['mmwave_hr_freq_bpm_median__changed','mmwave_hr_time_bpm_median__changed',
                'mmwave_hr_fused_bpm_median__changed','mmwave_hr_mean_confidence__changed']
    changed_hr = detail[stateful].fillna(False).astype(bool).any(axis=1)
    stateless = ['mmwave_breath_rate_breaths_per_min_median__changed','mmwave_selected_bin_mode__changed',
                 'mmwave_selected_channel_mode__changed','mmwave_selected_bin_distance_proxy_m__changed',
                 'mmwave_phase_stability_median__changed','mmwave_motion_proxy_median__changed']
    stateless_violation = int((same & detail[stateless].fillna(False).astype(bool).any(axis=1)).sum())
    raw_stateful = int((same & changed_hr).sum())
    explained_stateful = int((same & changed_hr & ~equal_anchor).sum())
    stateful_same_anchor_violation = int((same & changed_hr & equal_anchor).sum())
    report = {
        'scope':'Archived audit-table and aggregate-result recheck; NOT raw-signal validation or model refitting',
        'date':'2026-09-28',
        'frame_audit':{
            'records':int(len(frame)), 'sessions':int(frame.session_id.nunique()),
            'producer_participant_ids':int(frame.repeat_participant_id.nunique()),
            'selected_windows':int(len(selected)), 'nonselected_windows':int(len(frame)-len(selected)),
            'duplicate_keys':0, 'key_set_mismatch_between_audit_tables':0,
            'science_clock_columns': sorted(frame.science_timestamp_column_index.unique().tolist()),
            'selected_lower_endpoint_violations':lower_violation,
            'selected_upper_endpoint_violations':upper_violation,
            'frame_count_mismatches':frame_count_mismatch,
            'reconstructed_index_hash_mismatches':int(hash_mismatch),
            'membership_changed_vs_legacy':int(membership_changed.sum()),
            'same_membership_stateless_changed_flag_violations':stateless_violation,
            'same_membership_stateful_changed_flag_windows':raw_stateful,
            'stateful_differences_with_unequal_incoming_anchor':explained_stateful,
            'same_membership_equal_anchor_stateful_violations':stateful_same_anchor_violation,
            'limits':['Original raw timestamp vectors and signals were not read.',
                      'First/last timestamps and frame indices are stored audit values.',
                      'Output-value equality uses archived field-change flags; only incoming anchors and membership hashes were independently compared.']},
        'source_construction':{
            'm1_total_rows':source['m1_rows'], 'm1_hr_finite':source['m1_hr_finite'],
            'm1_br_finite':source['m1_br_finite'], 'behavior_complete_base_rows':source['base_rows'],
            'joined_source_rows':source['m1_rows_joined_to_base'],
            'joined_hr_finite':source['m1_hr_finite_after_join'], 'joined_br_finite':source['m1_br_finite_after_join'],
            'excluded_otherwise_finite_hr_windows':source['m1_hr_finite']-source['m1_hr_finite_after_join'],
            'scope_limit':'Source-report is the earlier M1 intake build; exact final-v3 source routing/keys require its input manifest and source table.'}
    }
    assert report['frame_audit']['records']==declared['expected_probe_n']==2320
    assert lower_violation==upper_violation==frame_count_mismatch==hash_mismatch==0
    assert membership_changed.sum()==declared['membership_changed_n']==1745
    assert stateless_violation==stateful_same_anchor_violation==0
    assert raw_stateful==explained_stateful==declared['raw_stateful_hr_difference_when_membership_same_n']==54
    assert not v1.duplicated(['analysis_set_id','model_id']).any()
    assert not v3.duplicated(['analysis_set_id','model_id']).any()
    assert np.isfinite(v3.participant_equal_log_loss).all()
    full = v3.loc[(v3.analysis_set_id=='AS.full') & (v3.model_id=='full')].iloc[0]
    ff=v3[v3.analysis_set_id.eq('AS.full')].copy()
    assert ff.n_probes.eq(1703).all() and ff.n_participants.eq(57).all()
    def get(model):
        return float(v3.loc[v3.model_id.eq(model),'participant_equal_log_loss'].iloc[0])
    eqs={'M7_equals_full':get('M7')==float(full.participant_equal_log_loss),
         'M2_equals_behavior_plus_cardiopulmonary':get('M2')==get('behavior_plus_modality::cardiopulmonary'),
         'sensor_joint_equals_full_minus_behavior_point_only':get('sensor_only_joint')==get('full_minus_modality::behavior')}
    assert all(eqs.values())
    ids=['analysis_set_id','model_id']; cols=['n_participants','n_probes','participant_equal_log_loss']
    merged=v1[ids+cols].merge(v3[ids+cols],on=ids,how='outer',suffixes=('_v1','_v3'),indicator=True)
    merged['report_action']=merged['_merge'].map({'left_only':'reuse_v1_unchanged_model_and_sample','right_only':'add_v3_result','both':'replace_v1_result_for_current_full_or_sensor_model'})
    merged.drop(columns='_merge').to_csv(output_root/'model_version_crosswalk.csv',index=False,encoding='utf-8-sig')
    modern=v3.copy(); modern['source_version']='v3_recorded_run'
    unchanged=v1.merge(v3[ids],on=ids,how='left',indicator=True).query('_merge == "left_only"')[ids+cols].copy()
    unchanged['source_version']='v1_unchanged_model_reused'
    combined=pd.concat([unchanged,modern],ignore_index=True)
    combined.to_csv(output_root/'proposed_binary_model_inventory.csv',index=False,encoding='utf-8-sig')
    ablation=ff[ff.model_id.str.startswith('full_minus')].copy()
    ablation['loss_removed_minus_full']=ablation.participant_equal_log_loss-float(full.participant_equal_log_loss)
    ablation['ci_status']='not_recomputed_no_v3_oof_or_participant_scores_in_current_runtime'
    ablation.to_csv(output_root/'v3_full_ablation_point_estimates.csv',index=False,encoding='utf-8-sig')
    report['model_inventory']={'v1_rows':len(v1),'v1_sets':int(v1.analysis_set_id.nunique()),
      'v3_recomputed_or_added_rows':len(v3),'v3_recomputed_or_added_sets':int(v3.analysis_set_id.nunique()),
      'same_name_rows_with_changed_model_or_sample':int(merged['_merge'].eq('both').sum()),
      'unchanged_v1_rows_for_reuse':len(unchanged),'new_model_set_rows':int(merged['_merge'].eq('right_only').sum()),
      'proposed_current_inventory_rows':len(combined),'proposed_current_inventory_sets':int(combined.analysis_set_id.nunique()),
      'proposed_distinct_model_ids':int(combined.model_id.nunique()),
      'full_model_n_features_from_registry':13,'sensor_joint_n_features_from_registry':8,
      'full_loss':float(full.participant_equal_log_loss), 'point_equalities':eqs,
      'limits':'Proposed inventory merges archived summaries; it is not a newly validated complete OOF archive.'}
    report['input_hashes']={n:{'sha256':sha256(input_root/n),'bytes':(input_root/n).stat().st_size} for n in names}
    (output_root/'aggregate_recheck.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
    return report

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--input-root',type=Path,required=True);p.add_argument('--output-root',type=Path,required=True)
    args=p.parse_args();result=recheck(args.input_root,args.output_root)
    print(json.dumps(result,ensure_ascii=False,indent=2))
