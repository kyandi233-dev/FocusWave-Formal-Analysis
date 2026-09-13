# Cardiopulmonary 心肺结果与资产

本文件登记当前毫米波心率、呼吸率相关的真实资产、可用性、估计器审计和验证资源。当前证据仍属于测量与算法验证阶段，不等于第 5.5 节已经形成正式心理生理结果。

## 1. 当前证据身份

当前 integration snapshot v1 已覆盖正式 116 场总体，其中 109 场、2,180 个探针具有有限 HR/BR 估计，7 场、140 个探针因真实来源问题保留为空。现有估计器仍存在系统性心率低估和稳定性问题；5 个带 ECG/RSP 参考的开发场次已经用于估计器诊断，不能承担独立验证。

毫米波权威仓库在 2026-09-13 进一步确认：正式 FocusWave 实验总体从设计上没有同步 ECG 参考，因此先前设想“在正式总体上补做独立 ECG 主要验证”的路线不可执行。当前 HR/BR 继续保持 `HOLD / SUPPORTING_ONLY`，HRV 保持 `BLOCKED`；心率改进验证线暂停，重新启动需要新采集、与现有开发样本参与者和场次均独立、且同步包含毫米波与 ECG 的数据。

尚无正式 Q1/Q2 心肺效应或监督学习结果。

2026-09-13 的 M1 生成链工作为本文件新增了两批可审计资产：生产端合同审计（`mmwave_producer_contract_m1_01da845e_20260913`）与心肺端点守卫（`mmwave_cardiopulmonary_endpoint_guard_e352dce_20260913`）。两者均属**生成链合同、身份与时间对齐**层面的证据，不提升生理效度，因此本文件的停止线不变。登记见第 11、12 节。

## 2. integration snapshot v1 覆盖

| 状态 | 探针 | 场次 | HR 有限值 | BR 有限值 |
|---|---:|---:|---:|---:|
| AVAILABLE | 2,180 | 109 | 2,180 | 2,180 |
| SOURCE_MALFORMED | 100 | 5 | 0 | 0 |
| SOURCE_UNAVAILABLE | 40 | 2 | 0 | 0 |
| 总计 | 2,320 | 116 | 2,180 | 2,180 |

这些数值只说明当前快照能够形成有限 HR/BR 数值，不表示生理准确性已经通过独立验证。

## 3. 当前科学字段与解释边界

当前预留的心肺科学变量为毫米波估计心率和毫米波估计呼吸率。时域/频域 HR、距离代理、目标切换、运动代理等仅作诊断或质量控制；当前没有合格的毫米波动作科学特征。IBI、RMSSD、SDNN、LF/HF 等心率变异性指标均未获得正式资格。

## 4. 时间与窗口

毫米波科学对齐采用 DLL 主机接收/入队时间。正式窗口为探针前名义 30 s 的右开区间，截止于探针出现时点，不跨正式任务区块；靠近区块起点时按实际可用起点截断。时间对齐合同通过不等于生理测量资格通过。

## 5. 当前估计器审计结果

在 5 个具有 ECG/RSP 参考的开发场次、100 个探针窗口上，当前融合心率估计的平均绝对误差为 10.457 bpm、平均偏差为 −9.033 bpm；时域路径的平均绝对误差为 8.997 bpm、平均偏差为 −6.738 bpm；频域路径的平均绝对误差为 15.124 bpm、平均偏差为 −13.351 bpm。已测试的有限修复没有形成稳定的新版本，因此当前 integration snapshot v1 保持不变。

机制审计显示，总体负偏主要集中在部分失败类别；频域路径偏低更明显，融合步骤在部分窗口进一步叠加负偏，现有质量字段不能跨场次稳定解释该偏差，也没有单一简单谐波机制能够解释全部问题。

这些数值属于开发与测量诊断证据，不进入国赛报告第 5.5 节作为注意相关心肺结果。

> **来源边界（2026-09-13 补充）**：本节数字来自 pre-M1 开发集，属第 13.3 节明确排除的范围。保留本节文字是为了解释 integration snapshot v1 为何保持不变，属方法审查记录；**不得**作为表 5-8 的任何一行，也不得写成心肺测量结果。

## 6. 验证资源与当前路线

| 数据集 | 参考信号 | 雷达输入 | 当前用途结论 |
|---|---|---|---|
| VS_DATASET_healthy_v1 | ECG Lead II 500 Hz + 呼吸 | 已提取单通道位移 | 仅可作次级外部佐证；已被历史开发使用，不能承担未触碰主要验证 |
| AgeBalanced_60GHz | ECG 约 250 Hz | range-FFT 帧 | 已参与历史心率路线选型，保留为历史外部基准 |
| mmWave_Heartbeat TI gby | 无 ECG/RSP | 原始 ADC | 缺少所需参考和完整时间条件，当前不可用于正式验证 |
| FocusWave 正式总体 | **无同步 ECG** | 当前毫米波正式记录 | 可用于现有系统内的可用性与注意相关探索；不能补造独立 ECG 主要验证 |

当前没有现成数据集可以完成所需的独立主要验证。原先计划在正式 FocusWave 总体中补做 ECG 参考的方案已经撤销，因为相应参考信号从实验设计起就不存在。

若重新启动心率验证线，需要新采集的数据同时满足：参与者和场次与当前开发集不重叠、同步记录毫米波与 ECG、符合正式 30 s 探针窗口和时间对齐要求，并在运行前冻结评价标准。现有 VS_DATASET 只保留为次级外部佐证，不能单独授权新的正式心率估计版本。

## 7. 第 5.5 节与多模态分析的当前边界

在心率和呼吸率取得正式测量资格、形成正式科学特征交接，并完成与任务进程和 Q1/Q2 的解释性分析之前，不把当前毫米波估计写成正式心理生理结果。

**因此第 5.5 节只写测量评估与应用边界，不写任何与任务进程或 Q1/Q2 的心肺效应。** 具体只填入 `工作表/第5章结果表格模板.md` 中**表 5-8 的前两行**（毫米波估计心率、毫米波估计呼吸率，分析层次为“数据覆盖、稳定性与运动影响”），数据来源为本文件第 12 节。表 5-8 的后两行（任务进程或 Q1/Q2 关系）与“与参考测量的误差/一致性”行保持空缺，因为前者未形成、后者缺少独立参考测量。

同样，当前有限 HR/BR 数值不进入正式多模态监督学习主模型。Behavior、Ocular 和 Movement 的正式分析可以继续推进，毫米波心肺验证线的暂停不阻塞这三类已经合格信息的统一特征登记和后续多模态比较。Cardiopulmonary 在统一特征登记表中**未登记任何特征**，因此在监督学习层通过 `unavailable_modalities` 机械地表现为不可用，而不是通过人工声明。

## 8. 本地资产

**当前权威（M1 期，可用于接口、覆盖、身份与时间对齐登记）**

- M1 生产端合同审计：`D:\Project\厚粲杯\11_数据\_FormalAnalysis\mmWave\mmwave_producer_contract_m1_01da845e_20260913\`
- 心肺端点守卫（当前权威）：`D:\Project\厚粲杯\11_数据\_FormalAnalysis\mmWave\mmwave_cardiopulmonary_endpoint_guard_e352dce_20260913\`
- 心肺端点守卫 v1（**已被取代，保留追溯**）：`D:\Project\厚粲杯\11_数据\_FormalAnalysis\mmWave\mmwave_cardiopulmonary_endpoint_guard_v1_20260913\`
- integration snapshot v1 探针表：`D:\Project\厚粲杯\11_数据\_FormalAnalysis\mmWave\mmwave_integration_snapshot_v1_20260912_r4\MMWAVE_INTEGRATION_SNAPSHOT_V1_PROBES_LOCAL_ONLY.csv`

**pre-M1 / 历史开发资产（本报告不作为第 5.5 节证据，见 13.3）**

- estimator improvement：`D:\Project\厚粲杯\11_数据\derived\mmwave_estimator_improvement_v1_20260912_r1\final_r6\`
- low-bias mechanism：`D:\Project\厚粲杯\11_数据\derived\mmwave_low_bias_mechanism_audit_v1_20260913\`
- VS_DATASET 历史基准：`D:\Project\厚粲杯\11_数据\derived\vitalsense_c1b_benchmark_v1\`
- 外部公开数据总根：`D:\Project\厚粲杯\11_数据\`

逐探针 ECG/RSP 参考与诊断明细保留 local-only；总账只记录用途和路径。

## 9. Google Drive 证据链

- integration snapshot v1：`_AI_HANDOFF/2026-09-12_mmwave_integration_snapshot_v1/`  
  https://drive.google.com/drive/folders/1eAClViAQxtDGl0jnfb88-ivtYSSH-AXj
- **M1 生产端合同审计**：`_AI_HANDOFF/2026-09-13_mmwave-producer-contract-m1-01da845e/`  
  https://drive.google.com/drive/folders/1V-z8LXen7_NQEg0m0KsX6YgGSyzEs8_d
- **M1 生产端合同审计 v2（old-vs-new 状态化解）**：`_AI_HANDOFF/2026-09-13_mmwave-producer-contract-m1-audit-v2/`  
  https://drive.google.com/drive/folders/1QvIKAZFVtcpdO0BKfHMUYGOY1QzH_XSN
- **心肺端点守卫（当前权威）**：`_AI_HANDOFF/2026-09-13_mmwave-cardiopulmonary-endpoint-guard-e352dce/`  
  https://drive.google.com/drive/folders/1dk_PyXAtAHKPTeNUX6kPzd5PDg-A92Fz
- 心肺端点守卫 v1（已被取代，保留追溯）：`_AI_HANDOFF/2026-09-13_mmwave-cardiopulmonary-endpoint-guard-53f642a/`  
  https://drive.google.com/drive/folders/1ZwbbzeJC2ZpgnWd_Gnwjzcsu_w1jTwvq
- estimator improvement v1：`_AI_HANDOFF/2026-09-12_mmwave_estimator_improvement_v1/`  
  https://drive.google.com/drive/folders/1gZC80XNklehALcuJ6U8NJe_aKy5iwzPd
- low-bias mechanism audit：`_AI_HANDOFF/2026-09-13_mmwave_low_bias_mechanism_audit_v1/`  
  https://drive.google.com/drive/folders/1mWx_dxpv8mAxuwItxFcavTWtl3bh7x4Z
- external validation asset audit：`_AI_HANDOFF/2026-09-13_mmwave_external_validation_asset_audit_v1/`  
  https://drive.google.com/drive/folders/1NhvFFPEEKsQb8AfhAqAx07G_nk1hDCf0
- 更早 HR recovery / P2 故障归因：`_AI_HANDOFF/2026-09-12_mmwave_hr_recovery_p2_failure_attribution/`  
  https://drive.google.com/drive/folders/1CxG4Uj9kWXXDPjIULqI_zyYjUxKKM-vV

当前最新“正式总体无 ECG、验证线暂停”的裁决以毫米波权威仓库 `docs/canonical/MMWAVE_IMPROVEMENT_LINE_CLOSURE_V1.md` 为准；若后续形成新的 Drive handoff，应在本节追加而不覆盖既有证据链。

## 10. 图表状态

目前没有可以直接进入国赛报告 5.5 的正式“心肺与注意状态”结果图。现有图表属于可用性、估计器诊断、失败机制和外部资产评估，只作为方法审查或补充证据。

第 5.5 节因此只使用**表格**（表 5-8 前两行，数据见第 12 节），不配图；在正式心肺结果形成前不新绘图件。

## 11. M1 生成链合同与端点合同审计登记（2026-09-13）

### 11.1 两批资产

| 资产 | 本地根目录 | 内容 | Drive bundle |
|---|---|---|---|
| 生产端合同审计（M1） | `D:\Project\厚粲杯\11_数据\_FormalAnalysis\mmWave\mmwave_producer_contract_m1_01da845e_20260913\` | `mmwave_probe_merge_ready{,_E}.csv`（55 列）、两份 manifest、`mmwave_probe_frame_membership_audit{,_E}.csv`、`old_vs_new\` 与 `old_vs_new_v2_stateful_anchor\` 逐 probe 审计、`_run_j.log` / `_run_e.log` | `2026-09-13_mmwave-producer-contract-m1-01da845e`、`2026-09-13_mmwave-producer-contract-m1-audit-v2` |
| 心肺端点守卫 | `D:\Project\厚粲杯\11_数据\_FormalAnalysis\mmWave\mmwave_cardiopulmonary_endpoint_guard_e352dce_20260913\` | `ingest_audit.csv`（2,320 × 44）、`coverage.csv`、`endpoint_delta_ms.csv`、`endpoint_delta_summary.json`、`feature_handoff.csv`、`taskb_source.csv`、`interface_smoke\*` | `2026-09-13_mmwave-cardiopulmonary-endpoint-guard-e352dce` |

同一目录下另有 `mmwave_cardiopulmonary_endpoint_guard_v1_20260913\`（**v1**）。v1 已被 `e352dce` 取代，**保留不删**，仅作追溯；当前权威结果为 `e352dce`。生产端合同审计的 `old_vs_new\`（**v1，状态 FAIL**）同样保留不删，其 FAIL 证据是 v2 修订的依据。

### 11.2 生产端合同审计结果

| 批 | 行数 | 场次 | OBSERVED | STRUCTURAL_MISSING |
|---|---:|---:|---:|---:|
| J（`mmwave_probe_merge_ready.csv`） | 1,440 | 72 | 1,420 | 20 |
| E（`mmwave_probe_merge_ready_E.csv`） | 880 | 44 | 780 | 100 |
| 合计 | **2,320** | **116** | 2,200 | 120 |

逐 probe old-vs-new 审计：

| 版本 | 状态 | 关键字段 |
|---|---|---|
| `old_vs_new\` | **FAIL** | `deterministic_violation_when_membership_same_n = 54` |
| `old_vs_new_v2_stateful_anchor\` | **PASS** | 五项计数门槛全部为 0（`only_in_old_n` / `only_in_new_n` / `missing_frame_audit_n` / `extra_frame_audit_n` / `strict_new_frame_membership_violation_n`），
并解释 v1 的 54：`raw_stateful_hr_difference_when_membership_same_n = 54`、`stateful_hr_difference_explained_by_anchor_divergence_n = 54`、`stateful_hr_violation_when_membership_and_anchor_same_n = 0` |

其余 v2 事实：`membership_changed_n = 1745`、`hr_fused_changed_n = 1202`、`br_changed_n = 1611`、`usable_fraction_changed_n = 0`；状态转移仅有 `OBSERVED → OBSERVED`（2,200）、`FileNotFoundError`（40）、`ValueError`（80）三类自反转移，**无任何状态被静默改写**。

**方法学含义**：`stateful_hr` 字段的确定性合同必须同时固定 frame membership 与传入的 `previous_bpm` 锚点；v2 的 `determinism_contract` 明确记录锚点更新规则（首个有限融合 HR 播种状态；后续在置信度 ≥ 0.12 时按 `0.8 × 前值 + 0.2 × 融合值` 更新）。因此"同一 frame membership 必须给出同一输出"这一断言对 stateless 字段成立，对 stateful HR 字段必须写成"同一 frame membership **且**同一锚点才给出同一输出"。v1 的 54 例正是漏掉锚点条件造成的假 FAIL。

两批 manifest 均记录 `models_trained = false`、`q1_q2_used_for_acceptance = false`、`snapshot_v2_formed = false`、`source_code_provenance_closed_for_this_run = true`，并给出 adapter / contract / producer 的 SHA-256。**这两批审计只证明生成链合同与可追溯性，不是生理效度证据**（`scientific_scope` 字段原文即如此声明）。

### 11.3 端点守卫结果

| 项 | 值 |
|---|---|
| 治理总体 | 2,320 probes / 116 sessions / 61 participant groups |
| key 审计 | `duplicate_key_n = 0`、`missing_key_n = 0`、`extra_key_n = 0`、`identity_mismatch_n = 0` |
| 可用 | 2,180 probes / 109 sessions |
| 来源不可用 | 40 probes / 2 sessions |
| 来源损坏 | 100 probes / 5 sessions |
| 保留为缺失或错误 | 140 probes（**不补 0、不静默删行**） |
| 端点合同 | `exact_integer_equality`，`endpoint_atol_ms = 0`，`endpoint_rtol = 0`，已冻结 |
| 端点差审计 | `n_total = 2,320`、`n_finite = 2,320`、`n_zero = 2,320`、**`n_nonzero = 0`**、`abs_max_delta_ms = 0` |
| `time_legality_status` | `blocked_upstream_contract_mismatch` |
| `physiology_qualification` | `LIMITED_SUPPORTING_ONLY` |
| 两个特征的 `prediction_eligibility` | 均为 **false** |
| 禁止升级字段 | `HF`、`LF`、`LF_HF`、`mmwave_ibi_median_ms`、`mmwave_motion_proxy_median`、`mmwave_rmssd_ms`、`mmwave_sdnn_ms` |
| 停止线字段 | `final_feature_registry_modified = false`、`models_trained = false`、`q1_q2_used_for_ingest_decision = false`、`source_unavailable_zero_imputed = false`、`source_malformed_zero_imputed = false`、`participant_identity_inferred_from_folder = false` |

**`54 = 54 + 0`**：`old_vs_new` v1 的 54 例确定性差异在 v2 中全部由锚点分歧解释，剩余无法解释的确定性违反为 **0**。这就是 v1 FAIL → v2 PASS 的完整闭环。

**身份有两层，不得混用**：生产端 `repeat_participant_id` 为 **62** 个（`R…` 形式，由 `session_id` 映射派生），下游治理 `participant_group_id` 为 **61** 个；两者都对应 116 个 `session_id` 与 2,320 个探针。任何跨层连接必须显式声明使用哪一层身份。

### 11.4 `分析设计/1.15.9` §3 第五状态与代码枚举的差异（**仅登记，不修改代码**）

`分析设计/1.15.9` §3 裁决新增第五个 time-legality 状态 `blocked_upstream_contract_mismatch`，且要求严格 fail-closed。当前状态：

- 该字符串**已经被真实使用**：`mmwave_cardiopulmonary_coverage.csv` 与 `feature_handoff.csv` 均写入 `time_legality_status = blocked_upstream_contract_mismatch`，并配 `physiology_qualification = LIMITED_SUPPORTING_ONLY`、全部预测资格字段为 `False`。
- 但 Attention-Analysis 的 `src/attention_pipeline/supervised_learning/time_legality.py` 中 `ALLOWED_TIME_LEGALITY_STATUSES` **仍只有四个状态**（`verified_pre_probe_only`、`pending_upstream_freeze`、`blocked_future_information`、`blocked_temporal_scope_unknown`），**不含该第五状态**。
- 因此若把 mmWave 特征送入该登记/校验链，它会因状态不在枚举内而**失败关闭**——结果方向与 1.15.9 一致（fail-closed），但原因是"枚举缺失"而不是"语义显式拒绝"。
- **本次仅登记该差异，不修改代码**，理由是它不阻塞任何当前交付：Cardiopulmonary 未登记任何特征，mmWave 也不进入正式预测。补枚举属后续代码任务，须同时补测试。

## 12. 心肺测量评估（`表 5-8` 前两行数据来源）

以下描述性统计全部来自 M1 期的 `mmwave_integration_snapshot_v1` 探针表（2,320 行）与上述端点守卫，只描述**覆盖、稳定性与运动影响**，不含任何生理效度结论，也不含任何与任务进程或 Q1/Q2 的关系。可复现脚本：`D:\Project\厚粲杯\.harness\summarise_mmwave_measurement.py`。

### 12.1 数据覆盖

| 项 | 值 |
|---|---|
| 治理探针 / 场次 / 参与者组 | 2,320 / 116 / 61 |
| 可用探针 / 场次 | **2,180（93.97%）** / **109** |
| 来源不可用 | 40 探针 / 2 场次 |
| 来源损坏 | 100 探针 / 5 场次 |
| 保留为缺失 | 140 探针（不补 0、不静默删行） |
| HR 与 BR 的有限值数 | 均为 **2,180** |
| 生产端参与者身份 | 62 个 `repeat_participant_id`（与下游 61 个 `participant_group_id` 不同层） |

### 12.2 稳定性与运动影响（可用 2,180 个探针）

| 变量 | 中位数 | 第 5–95 百分位 | 最小–最大 |
|---|---:|---|---|
| 毫米波估计心率（bpm） | 75.2 | 57.7 – 93.7 | 50.8 – 110.2 |
| 毫米波估计呼吸率（次/min） | 20.09 | 8.08 – 24.28 | 6.06 – 26.32 |
| 窗口内时间戳覆盖率 | 0.990 | 0.988 – 0.995 | 0.988 – 0.996 |
| 心率估计平均置信度 | 0.361 | 0.007 – 0.718 | 0.002 – 0.922 |
| 相位稳定性中位数 | 0.954 | 0.927 – 0.971 | 0.833 – 0.988 |
| 运动代理中位数 | 0.0268 | 0.0131 – 0.0602 | 0.0059 – 0.1812 |
| 目标切换率 | **该快照中该列完全为空，无可用值** | — | — |

运动代理与估计稳定性的秩相关（Spearman ρ，*n* = 2,180）：

| 关联对 | ρ |
|---|---:|
| 运动代理 ↔ 心率估计平均置信度 | **−.142** |
| 运动代理 ↔ 窗口内时间戳覆盖率 | −.032 |
| 运动代理 ↔ 参与者内绝对心率偏离 | +.013 |

运动代理越高，心率估计置信度略低（ρ = −.14），而它与参与者内心率偏离几乎无关（ρ = +.01）。也就是说，在本快照中运动记录主要与**估计置信度**这一软件层指标弱相关，而没有表现为对估计值本身的明显影响。这一结论的适用边界必须写明：运动代理是**毫米波自身导出的未验证代理**，不是独立运动测量；本表也没有任何生理参考真值，因此**不能**据此断言"运动不影响真实心肺活动"。

### 12.3 `mmwave_hr_usable_window_fraction` 不是比例

该字段在 2,180 个可用探针上**只有一个取值 1.0**，与 `分析设计/1.15.9` §2 第 5 条的核实完全一致：它当前承载的是 0/1 可用性标记，而不是真实的可用窗口比例。因此本文件**不报告该字段的均值或分布**（报告均值会把它误读成"平均 100% 可用"），只登记其取值集合。

## 13. 报告边界、lineage 决定与 pre-M1 排除

### 13.1 报告措辞（按 `分析设计/1.15.9` §4）

> 毫米波设备用于非接触获得心率与呼吸率的设备推导估计。当前分析采用 `mmwave_integration_snapshot_v1` 作为接口基线，其分母、身份键和时间对齐已形成可审计的集成证据；但 HR/BR 的独立生理效度证据仍有限，因此仅作为 Cardiopulmonary 支持性指标解释，不作为已验证的生理真值。

不得写成"已完成生理效度验证""真实心率/呼吸率"或"独立金标准已验证"。报告**不必**一律写"producer-side time-legality 未完全验证"；更准确的限制是：时间窗口有 corrected DLL-time replay 的生产端审计证据，但当前 canonical main 与该历史执行 lineage 的源码收口尚未完成。

### 13.2 lineage 待决 = **路径 3（暂不解除，等 M1 接入统一 snapshot 流程时一并处理）**

下游 `time_legality_status` **维持 `blocked_upstream_contract_mismatch`**，本次**不解除**。理由：`分析设计/1.15.9` §3 明确要求"上游合同修复、边界测试、old-vs-new 逐 probe 审计、**source-code provenance 闭环**"四项同时完成并留下非空 evidence 才允许转为 `verified_pre_probe_only`；而旧的 `codex/mmwave-formal-state-sync-v1` 隔离分支中的状态同步提案尚未并入 canonical 线。因此本报告的 lineage 处置统一为：**保持 fail-closed，问题随 M1 接入统一 snapshot 流程时一并处理**。

该决定对本报告是**中性的**：Cardiopulmonary 本来就未登记任何特征、不进入正式预测，因此维持 fail-closed 不改变第 5.5 节可写的内容，也不改变 5.6–5.8 的任何数字。

### 13.3 pre-M1 lineage 明确排除

以下目录属于 pre-M1 lineage，**本报告不使用**，不作为第 5.5 节的结果、图件或证据来源：

- `D:\Project\厚粲杯\11_数据\_FormalAnalysis\mmWave\mmwave_probe_criterion_models_20260831\`
- `D:\Project\厚粲杯\11_数据\_FormalAnalysis\mmWave\behavior_assoc_20260831\`
- `D:\Project\厚粲杯\11_数据\derived\`（含 `mmwave_estimator_improvement_v1_*`、`mmwave_low_bias_mechanism_audit_v1_*`、`vitalsense_c1b_benchmark_v1` 等历史开发产物）
- `D:\Project\厚粲杯\11_数据\MultiModal\`、`focuswave_canonical_v1`、`Behavior\formal_v3_backup_*`

本文件第 5 节登记的估计器诊断数字（MAE 10.457 bpm 等）来自 **pre-M1 开发集**，其来源属上述排除范围。保留该节文字的原因是它解释了当前 integration snapshot v1 为何保持不变，属**方法审查记录**；但该节数字**不得**进入第 5.5 节作为心肺测量结果，也不得作为表 5-8 的任何一行。

## 14. 当前停止线

- HR/BR：`HOLD / SUPPORTING_ONLY`
- HRV：`BLOCKED`
- 正式心肺心理效应：未形成
- 正式心肺监督学习特征：未取得资格
- 新一轮独立生理验证：`PAUSED_PENDING_NEW_COLLECTION`
- Behavior / Ocular / Movement 主分析：继续推进，不受该暂停阻塞
