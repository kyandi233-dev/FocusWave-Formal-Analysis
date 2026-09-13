# Cardiopulmonary 心肺结果与资产

本文件登记当前毫米波心率、呼吸率相关的真实资产、可用性、估计器审计和验证资源。当前证据仍属于测量与算法验证阶段，不等于第 5.5 节已经形成正式心理生理结果。

## 1. 当前证据身份

当前 integration snapshot v1 已覆盖正式 116 场总体，其中 109 场、2,180 个探针具有有限 HR/BR 估计，7 场、140 个探针因真实来源问题保留为空。现有估计器仍存在系统性心率低估和稳定性问题；5 个带 ECG/RSP 参考的开发场次已经用于估计器诊断，不能承担独立验证。

毫米波权威仓库在 2026-09-13 进一步确认：正式 FocusWave 实验总体从设计上没有同步 ECG 参考，因此先前设想“在正式总体上补做独立 ECG 主要验证”的路线不可执行。当前 HR/BR 继续保持 `HOLD / SUPPORTING_ONLY`，HRV 保持 `BLOCKED`；心率改进验证线暂停，重新启动需要新采集、与现有开发样本参与者和场次均独立、且同步包含毫米波与 ECG 的数据。

尚无正式 Q1/Q2 心肺效应或监督学习结果。

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

同样，当前有限 HR/BR 数值不进入正式多模态监督学习主模型。Behavior、Ocular 和 Movement 的正式分析可以继续推进，毫米波心肺验证线的暂停不阻塞这三类已经合格信息的统一特征登记和后续多模态比较。

## 8. 本地资产

- estimator improvement：`D:\Project\厚粲杯\11_数据\derived\mmwave_estimator_improvement_v1_20260912_r1\final_r6\`
- low-bias mechanism：`D:\Project\厚粲杯\11_数据\derived\mmwave_low_bias_mechanism_audit_v1_20260913\`
- VS_DATASET 历史基准：`D:\Project\厚粲杯\11_数据\derived\vitalsense_c1b_benchmark_v1\`
- 外部公开数据总根：`D:\Project\厚粲杯\11_数据\`

逐探针 ECG/RSP 参考与诊断明细保留 local-only；总账只记录用途和路径。

## 9. Google Drive 证据链

- integration snapshot v1：`_AI_HANDOFF/2026-09-12_mmwave_integration_snapshot_v1/`  
  https://drive.google.com/drive/folders/1eAClViAQxtDGl0jnfb88-ivtYSSH-AXj
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

## 11. 当前停止线

- HR/BR：`HOLD / SUPPORTING_ONLY`
- HRV：`BLOCKED`
- 正式心肺心理效应：未形成
- 正式心肺监督学习特征：未取得资格
- 新一轮独立生理验证：`PAUSED_PENDING_NEW_COLLECTION`
- Behavior / Ocular / Movement 主分析：继续推进，不受该暂停阻塞
