# Cardiopulmonary 心肺结果与资产

本文件登记当前毫米波（mmWave）心率、呼吸率相关的真实资产、可用性、估计器审计和外部验证资源。**当前这些证据仍属于测量与算法验证阶段，不等于第 5.5 节已经形成正式心理生理结果。**

## 1. 当前证据身份

当前 Cardiopulmonary（心肺）状态为：

- mmWave integration snapshot v1 已能在正式 116 场治理样本上物化心率/呼吸率字段；
- 109 场、2,180 个探针具有有限 HR/BR 估计，7 场/140 探针因真实来源问题保留为空；
- 现有估计器仍存在系统性心率低估和稳定性问题；
- 有 ECG/RSP 参考的校准/审计数据已用于诊断，因此不能把这些开发数据当作 untouched 外部验证；
- 外部公开数据资产已完成可行性审计，但没有任何一个外部数据集可以同时承担完整 primary C1/C2 untouched validation；
- **HR/BR 仍为 HOLD / SUPPORTING_ONLY；HRV 仍 BLOCKED；尚无正式 Q1/Q2 心肺效应结果。**

因此本模块目前主要属于：**测量资格审计 + 算法诊断 + 外部验证资产审计**。

## 2. integration snapshot v1 的正式样本覆盖

当前快照保持整个正式治理分母：61 名参与者、116 场、2,320 个思维探针。

| 状态 | 探针 | 场次 | HR 有限值 | BR 有限值 |
|---|---:|---:|---:|---:|
| AVAILABLE | 2,180 | 109 | 2,180 | 2,180 |
| SOURCE_MALFORMED | 100 | 5 | 0 | 0 |
| SOURCE_UNAVAILABLE | 40 | 2 | 0 | 0 |
| 总计 | 2,320 | 116 | 2,180 | 2,180 |

这里的 109 场/2,180 probes 只说明当前毫米波快照能够形成有限 HR/BR 数值，不等于这些数值已经通过独立生理准确性验证。

## 3. 当前科学字段与禁止解释范围

integration snapshot v1 中预留的心肺科学预测变量为：

- 毫米波估计心率：`mmwave_hr_fused_bpm_median`；
- 毫米波估计呼吸率：`mmwave_breath_rate_breaths_per_min_median`。

其他字段如时域/频域 HR、bin、channel、距离代理、target switch、motion proxy 属于诊断/QC 信息，不进入正式心理科学模型。

当前没有合格的 mmWave Movement 科学特征；mmWave motion proxy 仍是诊断信息。IBI、RMSSD、SDNN、LF/HF 等 HRV 指标均未获得正式资格，不得从当前快照派生后直接写入报告。

## 4. 时间与窗口合同

当前 mmWave 科学时间对齐使用 DLL host receive/enqueue 时钟。正式窗口为探针前名义 30 s 的右开区间，截止于 probe onset，不跨正式 Block；靠近 Block 起点时按实际可用起点截断。

该时间合同用于保持与 Behavior/Ocular/Movement 的 pre-probe 逻辑一致，但**不能单凭时间合同通过就视为生理测量有效**。

## 5. 当前心率估计器的真实负面结果

### 5.1 estimator improvement v1

在 5 个已具有 ECG/RSP gold-clean reference 的 session、100 个 probe windows 上，当前基线与 bounded repair 候选进行了配对审计。

关键结果：

| 估计路线 | HR MAE / bpm | HR bias / bpm | 说明 |
|---|---:|---:|---|
| 当前 fused | 10.457 | −9.033 | 当前融合基线，存在明显低估 |
| 当前 time path | 8.997 | −6.738 | 平均误差更低，但不因此事后替换正式 fused 字段 |
| 当前 spectral path | 15.124 | −13.351 | 低估更明显 |
| H1 observed-best 候选 | 9.619 | — | 总体稍改善，但引入新的 AE>10 bpm 灾难失败，因此被拒绝 |

H1/H3 会把控制条件下原本可接受的窗口变成灾难失败；H2 又未达到预先要求的跨 session 稳定改善。因此：

- `BEST_CANDIDATE = NONE`；
- `V2_CANDIDATE_STATUS = NOT_FORMED`；
- snapshot v1 和正式 producer 均未替换。

这是一项**负面但重要的正式开发审计结果**：当前没有稳定、可泛化的毫米波-only 修复可以升级为 v2。

### 5.2 低估机制审计

同一 100 个 ECG-valid probe windows 上，机制审计复现当前 fused MAE 10.457 bpm、bias −9.033 bpm。被分为 correct/near-correct 的窗口 fused bias 约 0.215 bpm，说明总体 −9 bpm 低估并不是所有窗口都统一偏低，而是由少数失败类别集中贡献。

当前证据支持**多因素失败机制**：

- spectral 路径偏低最明显；
- fusion 在部分窗口进一步叠加负偏；
- 既有 QC 字段不能跨 session 稳定解释偏差；
- 未观察到简单的 0.5×/2× 谐波锁定可以单独解释全部失败；
- 距离只呈弱关系且与 session/失败类别混淆。

因此不能通过一个简单固定校正量把当前 HR 低估“修正掉”。

## 6. 外部验证资产审计

当前本地已审计三个外部资产：

| 数据集 | 参考信号 | 雷达输入 | 30 s 可行 | 当前用途结论 |
|---|---|---|---|---|
| VS_DATASET_healthy_v1 | ECG Lead II 500 Hz + 呼吸等 | 已提取单通道位移 VitalSig | 是 | 可作 C2 secondary external evidence；不能承担 C1；且已被历史基准暴露 |
| AgeBalanced_60GHz | Movesense ECG ~250 Hz | range-FFT 帧 | 是 | 已参与历史 HR 路线选型，不再是 untouched primary validation |
| mmWave_Heartbeat TI gby | 无 ECG/RSP | 原始 ADC | 当前不可判定 | 缺参考、时间戳与采集配置，当前不可作为验证集 |

当前结论：

- **没有任何外部资产可以承担完整 C1 primary validation**；
- C2 只有 VS_DATASET 在格式上可用，但只能作为 secondary external evidence；
- primary untouched validation 仍需要正式 cohort 的预注册 OPT_A 路线。

## 7. 当前不能写入第 5.5 的内容

在以下条件满足之前，国赛报告结果章不能把 mmWave HR/BR 写成正式心理生理结果：

1. 生理测量资格和准入门正式冻结；
2. primary validation 完成；
3. 正式 feature handoff 形成并进入统一 registry；
4. HR/BR 与任务进程、Q1/Q2 的正式重复测量结果形成；
5. 若声称“准确测量心率/呼吸率”，必须有独立参考证据支持相应准确性范围。

因此当前 5.5 应保持为空或仅在内部结果总账记录测量审计状态，不能把开发集 MAE/bias 直接作为注意力研究主结果。

## 8. 当前主要本地资产

### 8.1 integration snapshot /正式 cohort

当前逐探针 snapshot 与 smoke 明细包含参与者关联信息，为 local-only。其正式云端跟踪包见下方 Drive bundle。

### 8.2 estimator improvement 本地 probe-level 资产

根目录：

`D:\Project\厚粲杯\11_数据\derived\mmwave_estimator_improvement_v1_20260912_r1\final_r6\`

local-only 文件：

- `REFERENCE_QC_ELIGIBILITY_100_PROBES_LOCAL_ONLY.csv`：100 行，逐探针 reference/QC eligibility；
- `CONTROL_VS_CANDIDATES_100_PROBES_LOCAL_ONLY.csv`：100 行，当前控制路线与候选逐窗配对估计；
- `LARGEST_ERROR_PROBES_TOP20_LOCAL_ONLY.csv`：20 行，最大误差窗口诊断。

这些表含逐 probe 参考与诊断细节，不上传 Drive/GitHub。

### 8.3 low-bias mechanism probe-level 资产

`D:\Project\厚粲杯\11_数据\derived\mmwave_low_bias_mechanism_audit_v1_20260913\PROBE_LEVEL_MECHANISM_100_PROBES.csv`

100 行，含 ECG 参照与失败机制诊断，local-only。

### 8.4 外部公开数据资产

三个外部数据集位于：

`D:\Project\厚粲杯\11_数据\`

其中已知：

- VS_DATASET：24 subjects，Resting + Apnea 共 48 段；
- AgeBalanced_60GHz：110 subjects；
- mmWave_Heartbeat TI gby：10 个原始 ADC 文件，无参考信号。

已有 VS_DATASET C1b 历史基准本地证据：

`D:\Project\厚粲杯\11_数据\derived\vitalsense_c1b_benchmark_v1\`

该历史基准已使 VS_DATASET 不再属于 untouched primary validation。

## 9. Google Drive 证据链

### 9.1 integration snapshot v1

`_AI_HANDOFF/2026-09-12_mmwave_integration_snapshot_v1/`  
https://drive.google.com/drive/folders/1eAClViAQxtDGl0jnfb88-ivtYSSH-AXj

正式报告：  
https://drive.google.com/file/d/1cCCPLfL81n7XNxtFiPFc5MgycMNGOazo/view

状态：`PROVISIONAL_INTEGRATION_READY / PHYSIOLOGY_LIMITED`。

### 9.2 estimator improvement v1

`_AI_HANDOFF/2026-09-12_mmwave_estimator_improvement_v1/`  
https://drive.google.com/drive/folders/1gZC80XNklehALcuJ6U8NJe_aKy5iwzPd

HANDOFF：  
https://drive.google.com/file/d/1K8hl74hD2AG8JOKeztG39iPkY-upS-u3/view

状态：`NO_STABLE_IMPROVEMENT`。

### 9.3 low-bias mechanism audit v1

`_AI_HANDOFF/2026-09-13_mmwave_low_bias_mechanism_audit_v1/`  
https://drive.google.com/drive/folders/1mWx_dxpv8mAxuwItxFcavTWtl3bh7x4Z

HANDOFF：  
https://drive.google.com/file/d/1jwgK5VUsK_M02vSd7qjdZ8ERIGAvN-js/view

状态：`MULTIFACTOR_MECHANISM_SUPPORTED`。

### 9.4 external validation asset audit v1

`_AI_HANDOFF/2026-09-13_mmwave_external_validation_asset_audit_v1/`  
https://drive.google.com/drive/folders/1NhvFFPEEKsQb8AfhAqAx07G_nk1hDCf0

报告：  
https://drive.google.com/file/d/17surVFOf6s28nlukiZjuRXrbGt5ucTgY/view

状态：资产审计完成；没有候选运行、没有 producer 变更。

### 9.5 更早故障归因 bundle

`_AI_HANDOFF/2026-09-12_mmwave_hr_recovery_p2_failure_attribution/`  
https://drive.google.com/drive/folders/1CxG4Uj9kWXXDPjIULqI_zyYjUxKKM-vV

该目录保留 HR recovery/P2 的历史故障归因，用于追溯，不应覆盖后续 estimator improvement / mechanism audit 的最新结论。

## 10. 当前图表状态

目前没有可以直接进入国赛报告 5.5 的正式“心肺与注意状态”结果图。

现有 mmWave 图表/表格属于：

- integration schema 与可用性；
- estimator 诊断；
- 失败机制；
- 外部资产评估。

它们可以作为内部方法审查或附录材料，但不应放在 5.5 主结果中冒充心理生理效应图。

未来 5.5 至少需要形成：

1. HR/BR 正式测量覆盖与资格表；
2. 任务进程结果；
3. Q1/Q2 重复测量效应表/图；
4. 如果有参考测量，正式的误差/一致性结果；
5. 与大身体运动相关的测量敏感性/QC 图。

## 11. 当前停止线

- HR/BR：`HOLD / SUPPORTING_ONLY`
- HRV：`BLOCKED`
- `models_trained = false`
- 当前不把 mmWave 可用性直接等同于 Cardiopulmonary 正式资格；
- 当前不进入正式多模态监督学习性能比较。
