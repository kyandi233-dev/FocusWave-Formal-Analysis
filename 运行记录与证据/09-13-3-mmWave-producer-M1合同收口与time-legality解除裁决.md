# 09-13-3 mmWave producer M1 合同收口与 time-legality 解除裁决

- 记录时间：2026-09-13（Asia/Shanghai）
- 范围：`greenboo26/focuswave-multimodal-attention-analysis`（producer M1）、Formal `codex/code-fix-ledger`、下游 `kyandi233-dev/Attention-Analysis`
- 结果边界：**producer 时间合同与来源追溯 `PASS`；`time_legality_status` 由 `blocked_upstream_contract_mismatch` 解除为 `verified_pre_probe_only`**。本记录**不**构成任何生理效度结论。

## 1. 目标

执行 Formal `分析设计/1.15.9-毫米波生成链合同修复与time-legality处置_20260913.md` 预授权的条件式状态转换：该文件规定 `blocked_upstream_contract_mismatch` 只有"同时完成上游合同修复、边界测试、old-vs-new 逐 probe 审计、**source-code provenance 闭环**并留下非空 evidence 后，才允许转为 `verified_pre_probe_only`"。

本记录判定这四项条件是否已满足，并登记结论与其边界。

## 2. Provenance 分层（本次最重要的结构事实）

```text
producer_execution_commit    = 01da845e70e255b6537f8d03220aac2e6cc0bf31
audit_interpretation_commit  = 37f5d8e32fbc63fa3ba8bca05221b534089bcec9
```

- J/E 全部 2,320 行原始结果由 `producer_execution_commit` 生成。两份 manifest 均记录该 commit、`source_worktree_clean = true`、`source_code_provenance_closed_for_this_run = true`。
- `audit_interpretation_commit` **只**表示审计解释层，**不得**写为 J/E 的 `source_commit`。
- 已核验 `01da845e..37f5d8e` 仅改动 3 个文件：audit 脚本、audit 测试、implementation 文档。J runner、E runner、`scripts/maintenance/mmwave_probe_contract.py`、`scripts/process_vital_signs_v3_1_1.py` 四个文件 git blob 完全相同。
- 源码 SHA-256（本地独立核算，与两份 manifest 一致）：

```text
adapter (J)  a29badb6aced4241b369185c19aef356901c163d0447929ce8c22a00daf4b49e
adapter (E)  3244e341a90064ec681d38c1c6dd900eca90f5f193a4e551290de9d5445bd106
contract     227edfc8922622fedbcf13a494bc9432800a299d0a2350461b05c62e2d72206d
producer     bc65c2d2c99ebdfedea2500579caeb45cb8918466cf788ade718806bdd351fda
```

这一层解决了 Formal 先前记录的 provenance 缺口：历史 `16729b2...` corrected replay 仍作历史证据，但 GitHub 无法解析该提交、且其历史 manifest hash 与所声明 source commit 不一致；本次 M1 结果由**当前可远程检索的提交**生成，并记录四个源码 SHA-256。

## 3. 运行环境与输入

| 项 | 值 |
|---|---|
| 本机 clone | `D:\Project\厚粲杯\08_算法`（`greenboo26/focuswave-multimodal-attention-analysis`） |
| producer worktree | `D:\Project\厚粲杯\08_算法_worktrees\mmwave_producer_contract_m1_01da845e`（detached，运行前后 `git status --short` 为空） |
| audit worktree | `D:\Project\厚粲杯\08_算法_worktrees\mmwave_m1_audit_v2_37f5d8e`（detached，干净） |
| 解释器 | `D:\Project\厚粲杯\08_算法\.venv_t0\Scripts\python.exe`（Python 3.14.6） |
| 输入 | 本机 local-only snapshot：2,320 probes / 116 sessions；pre-M1 对照表同根目录 |
| 样本冻结 | J 1,440 probes（72 sessions）+ E 880 probes（44 sessions）= 2,320 |

## 4. 命令与结果

### 4.1 focused tests

```powershell
python -m pytest tests/test_mmwave_producer_contract_m1.py `
                 tests/test_mmwave_producer_contract_m1_audit.py -q
# collected 11 / passed 11 / failed 0 / exit 0
```

（producer contract 8 + stateful audit 3。Issue #43 早期评论中的 “13 passed” 不成立，已在本轮更正。）

### 4.2 J / E 真实运行（`producer_execution_commit`）

```powershell
python scripts/maintenance/run_mmwave_probe_merge_ready_20260831.py    --output-root <M1_OUT>
python scripts/maintenance/run_mmwave_probe_merge_ready_E_20260831.py  --output-root <M1_OUT>
# J exit 0：处理 72 sessions / 1440 probe，状态分布 OBSERVED 1420 / STRUCTURAL_MISSING 20
# E exit 0：状态分布 OBSERVED 780 / STRUCTURAL_MISSING 100
```

### 4.3 old-vs-new 审计（`audit_interpretation_commit`）

**v1（`old_vs_new/`，`status = FAIL`，exit 2）——证据保留，未删除、未覆盖。**

失败项为 `deterministic_violation_when_membership_same_n = 54`。根因**不是** producer 时间合同错误，而是 v1 的确定性判据把**有状态**的 HR 估计器当成无状态算法检查：冻结代码中 HR selector 读取同一 Block 累计的 `previous_bpm` 作为 anchor，并在本 probe 结束后按 fused HR 与 confidence 更新该状态（`first finite fused HR seeds state; subsequent finite fused HR updates at confidence >= 0.12 using 0.8*previous + 0.2*fused`）。因此"本 probe 帧成员相同"并不蕴含"完整估计器输入相同"。

**v2（`old_vs_new_v2_stateful_anchor/`，`status = PASS`，exit 0）**，判据拆为两层：

```text
stateless fields : same frame membership ⇒ outputs must match
stateful HR      : same frame membership AND same incoming previous_bpm ⇒ HR must match
                   （incoming previous_bpm 已因同 Block 更早的合法 membership change 分叉时，
                     记为 explained state propagation，不构成时间合同失败）
```

该修订未改变 Formal `1.15.9` 的标准：原文即为"对 frame membership 完全相同的 probe，确定性派生量必须保持一致；**否则必须单独解释**"，并未要求所有差异一律判 FAIL。

## 5. audit v2 结果与硬门槛

```json
{
  "status": "PASS",
  "expected_probe_n": 2320, "old_probe_n": 2320, "new_probe_n": 2320, "frame_audit_probe_n": 2320,
  "only_in_old_n": 0, "only_in_new_n": 0, "missing_frame_audit_n": 0, "extra_frame_audit_n": 0,
  "membership_changed_n": 1745,
  "strict_new_frame_membership_violation_n": 0,
  "stateless_deterministic_violation_when_membership_same_n": 0,
  "raw_stateful_hr_difference_when_membership_same_n": 54,
  "stateful_hr_difference_explained_by_anchor_divergence_n": 54,
  "stateful_hr_violation_when_membership_and_anchor_same_n": 0,
  "hr_fused_changed_n": 1202, "br_changed_n": 1611, "usable_fraction_changed_n": 0
}
```

等式核验：`54 = 54 + 0` ✓

`state_transitions`：`OBSERVED -> OBSERVED` 2200；`STRUCTURAL_MISSING:load_failed:FileNotFoundError -> 同` 40；`STRUCTURAL_MISSING:load_failed:ValueError -> 同` 80。

**54 条的重新分类**（逐行证据在 `audit_v2_detail.csv`）：全部转入 `explained_by_anchor_divergence`。54/54 `incoming_previous_bpm_same = False`；54/54 `stateful_hr_violation_when_membership_and_anchor_same = False`；旧/新 anchor 数值确实分叉（例 `sub-031/block-1/probe-05`：旧 `70.732200` → 新 `79.497224`）；只涉及 HR 字段（`hr_freq` / `hr_time` / `hr_fused` / `hr_mean_confidence`）；不涉及 BR / state / observed / missing_reason / loadable / bin / channel / distance / phase / motion；无 stateless 违规。**不存在未解释的确定性违规。**

| 门槛 | 结果 |
|---|---|
| probes = 2,320（old / new / frame audit 三者一致） | PASS |
| only_old / only_new / missing_frame / extra_frame = 0 | PASS |
| strict_new_frame_membership_violation_n = 0 | PASS |
| stateless_deterministic_violation_when_membership_same_n = 0 | PASS |
| stateful_hr_violation_when_membership_and_anchor_same_n = 0 | PASS |

## 6. 合同逐项确认（来自两份 manifest）

| 合同项 | manifest 记录 |
|---|---|
| 科学时钟 = DLL host receive/enqueue | `science_clock_source = dll_host_receive_enqueue`；`science_timestamp_column_index = 1`；`qc_timestamp_column_index = 2` |
| 严格右开窗口 | `window_contract = [window_effective_start_unix_ms,probe_onset_unix_ms)`；`right_endpoint_exclusive = true` |
| effective start 真正进入切片 | `effective_start_used_for_slicing = true` |
| J/E 同一合同 | 两份 manifest 上述字段一致 |
| usable fraction 语义 | `hr_usable_window_fraction_semantics = producer estimate_hr_time_course signal_quality.usable_ratio` |
| 未越界 | `models_trained = false`、`q1_q2_used_for_acceptance = false`、`snapshot_v2_formed = false` |

## 7. 裁决

**producer 时间合同与来源追溯四项条件全部满足**，因此依 `1.15.9` 的预授权条件执行：

```text
Cardiopulmonary time_legality_status:
  blocked_upstream_contract_mismatch  →  verified_pre_probe_only
```

**唯一且仅此一项发生变化。** 该转换表示：毫米波 probe 级表的时间窗口合同与来源追溯已通过生产端修复、边界测试、逐 probe 审计和源码 hash/commit 闭环，因此该来源的具体特征可以在 registry 中声明时间合法性。

**该转换不等于、也不得被解释为：**

- HR 已验证为真实心率；
- BR 已验证为真实呼吸率；
- Cardiopulmonary 生理效度通过；
- HRV 可用；
- mmWave motion proxy 可进入 Movement 特征；
- 已放行正式监督学习。

继续维持：

```text
HR / BR = LIMITED_SUPPORTING_ONLY
HRV     = BLOCKED
physiology_qualification = LIMITED_SUPPORTING_ONLY
MMWAVE_INTEGRATION = READY
MAIN_ANALYSIS = PROCEED
C1 / C2 = PAUSED_PENDING_NEW_COLLECTION
snapshot v2 = NOT_FORMED
1.15.8 = SUPERSEDED_BUT_TECHNICAL_ITEMS_NOT_CLOSED
```

**time-legality 与 physiology validity 是两个独立门。** 本次只关闭前者。

## 8. 身份口径（两层，不得混用）

| 层 | probes | sessions | 身份键 | 基数 |
|---|---|---|---|---|
| producer J/E 原表 | 2,320 | 116 | `repeat_participant_id` | **62**（pre-M1 与 M1 一致，属既有 producer 层方案，非 M1 回归） |
| governed cohort（下游 Cardiopulmonary ingest / identity bridge 之后） | 2,320 | 116 | `participant_group_id` | **61** |

## 9. 产物与证据落点

| 类型 | 位置 |
|---|---|
| M1 输出（local-only） | `D:\Project\厚粲杯\11_数据\_FormalAnalysis\mmWave\mmwave_producer_contract_m1_01da845e_20260913\` |
| audit v1（FAIL，保留） | 同上 `old_vs_new\` |
| audit v2（PASS） | 同上 `old_vs_new_v2_stateful_anchor\` |
| Drive bundle（producer M1） | `_AI_HANDOFF/2026-09-13_mmwave-producer-contract-m1-01da845e`，folder id `1V-z8LXen7_NQEg0m0KsX6YgGSyzEs8_d` |
| Drive bundle（audit v2） | `_AI_HANDOFF/2026-09-13_mmwave-producer-contract-m1-audit-v2`，folder id `1QvIKAZFVtcpdO0BKfHMUYGOY1QzH_XSN`（11 files；`rclone check --checksum` → 0 differences / 11 matching，exit 0） |
| GitHub 证据 | Issue #43 评论、PR #44 评论（producer 仓库，均记录 producer/audit 两个 commit） |

两份 bundle 均未覆盖对方；v1 FAIL 证据随 v2 bundle 以 `audit_v1_summary_FAIL_preserved.json` 归档。

## 10. 失败与重试

- v1 audit `FAIL`（exit 2）：判据遗漏有状态 HR anchor。**未修改 producer、未重跑 J/E**；改为修订审计解释层，v1 结果与摘要完整保留。
- 无其他失败。无重试性失败被静默删除。

## 11. 下一步（下游，独立分支）

下游 `kyandi233-dev/Attention-Analysis` 的 Cardiopulmonary ingest 当前在代码中硬编码 `TIME_LEGALITY_STATUS = "blocked_upstream_contract_mismatch"`（PR #76 已实现并验收，但仍是 Draft/OPEN，未合并）。依本裁决，下一步应在该仓库开**独立分支**做最小修改：

- `time_legality_status` → `verified_pre_probe_only`；
- evidence reference 指向本记录与两个 Drive bundle / producer_execution_commit；
- prediction / device-package eligibility 中**仅**与 time-legality 相关的字段。

**必须继续保持** `physiology_qualification = LIMITED_SUPPORTING_ONLY`，不得因时间合同通过而把 HR/BR 变为正式生理金标准。

### 11.1 未决：本裁决适用于哪条输入 lineage（需裁决，不得默认继承）

本记录的解除，适用于 **M1 producer lineage**，即由 `producer_execution_commit = 01da845e...` 生成的那份 2,320-probe J/E 表。

但下游 adapter 当前消费的输入是 **`MMWAVE_INTEGRATION_SNAPSHOT_V1`**，它来自历史 corrected replay（`source_commit 16729b2...`）——而该 lineage 的源码 hash 不一致问题**并未由 M1 解决**（M1 是另起一条可远程检索的生产线，不是重建 snapshot v1）。

因此存在一个尚未裁决的问题：

> 下游 ingest 是否可以把自身的 `time_legality_status` 直接解除？

- 若解除，等于对一份 provenance 尚未闭环的输入声明时间合法性，与 `1.15.9` 的 provenance 要求相抵触；
- 若要真正解除，需要把下游输入改为 M1 产物（即重建集成快照），而这又触及"不得形成 snapshot v2"的禁止项。

**这是输入 lineage 的口径选择，属于方法裁决，本记录不自行认定。** 在裁决前，下游 `time_legality_status` 保持 `blocked_upstream_contract_mismatch` 不变。

## 12. 明确未做

未重选 HR estimator；未调 HR/BR 算法或阈值；未重启 C1/C2；未做 HRV；未做 VMD/SSA；未用 Q1/Q2 决定毫米波算法；未运行监督学习；未修改 unified feature registry；未形成 snapshot v2；未把 mmWave motion 提升为 Movement 特征；未删除或覆盖第一次 FAIL 的证据；未重跑 J/E。
