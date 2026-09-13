# Cardiopulmonary 心肺结果与资产

本文件登记当前毫米波心率、呼吸率相关的真实资产、可用性、估计器审计和外部验证资源。当前证据仍属于测量与算法验证阶段，不等于第 5.5 节已经形成正式心理生理结果。

## 1. 当前证据身份

当前 integration snapshot v1 已覆盖正式 116 场治理样本，其中 109 场、2,180 个探针具有有限 HR/BR 估计，7 场、140 个探针因真实来源问题保留为空。现有估计器仍存在系统性心率低估和稳定性问题；有 ECG/RSP 参考的校准/审计数据已经用于诊断，因此不能再作为 untouched 外部验证。当前 HR/BR 仍为 `HOLD / SUPPORTING_ONLY`，HRV 为 `BLOCKED`，尚无正式 Q1/Q2 心肺效应结果。

## 2. integration snapshot v1 覆盖

| 状态 | 探针 | 场次 | HR 有限值 | BR 有限值 |
|---|---:|---:|---:|---:|
| AVAILABLE | 2,180 | 109 | 2,180 | 2,180 |
| SOURCE_MALFORMED | 100 | 5 | 0 | 0 |
| SOURCE_UNAVAILABLE | 40 | 2 | 0 | 0 |
| 总计 | 2,320 | 116 | 2,180 | 2,180 |

这些数值只说明当前快照能形成有限 HR/BR 数值，不等于生理准确性已经通过独立验证。

## 3. 当前科学字段与解释边界

当前预留的心肺科学变量为毫米波估计心率和毫米波估计呼吸率。时域/频域 HR、距离代理、目标切换、运动代理等仅作诊断或质量控制；当前没有合格的 mmWave Movement 科学特征。IBI、RMSSD、SDNN、LF/HF 等 HRV 指标均未获得正式资格。

## 4. 时间与窗口

毫米波科学对齐采用 DLL host receive/enqueue 时钟。正式窗口为探针前名义 30 s 的右开区间，截止于 probe onset，不跨正式 Block；靠近 Block 起点时按实际可用起点截断。时间合同通过不能替代生理测量资格。

## 5. 当前估计器审计结果

在 5 个具有 ECG/RSP 参考的 session、100 个 probe windows 上，当前 fused HR 的 MAE 为 10.457 bpm、bias 为 −9.033 bpm；time path 的 MAE 为 8.997 bpm、bias 为 −6.738 bpm；spectral path 的 MAE 为 15.124 bpm、bias 为 −13.351 bpm。已测试的 bounded repair 没有形成稳定的新版本，因此 snapshot v1 和正式 producer 均未替换。

机制审计显示，总体负偏主要集中在部分失败类别；spectral 路径偏低更明显，fusion 在部分窗口进一步叠加负偏，现有 QC 字段不能跨 session 稳定解释该偏差，也没有单一简单谐波机制能够解释全部问题。

## 6. 外部验证资产审计

| 数据集 | 参考信号 | 雷达输入 | 30 s 可行 | 当前用途结论 |
|---|---|---|---|---|
| VS_DATASET_healthy_v1 | ECG Lead II 500 Hz + 呼吸 | 已提取单通道位移 | 是 | 可作 C2 secondary evidence；不能承担 C1；已被历史基准使用 |
| AgeBalanced_60GHz | ECG 约 250 Hz | range-FFT 帧 | 是 | 已参与历史 HR 路线选型，不再是 untouched primary validation |
| mmWave_Heartbeat TI gby | 无 ECG/RSP | 原始 ADC | 当前不可判定 | 缺参考、时间戳与采集配置，当前不可作为验证集 |

当前没有外部资产可以承担完整 C1 primary validation；C2 只有 VS_DATASET 在格式上可用，但只能作为 secondary external evidence。primary validation 仍需按正式 cohort 的预注册路线执行。

## 7. 当前不能写入第 5.5 的内容

在生理测量资格正式冻结、primary validation 完成、正式 feature handoff 形成、HR/BR 与任务进程和 Q1/Q2 的重复测量结果形成之前，不能把 mmWave HR/BR 写成正式心理生理结果。若声称准确测量心率或呼吸率，还必须有独立参考证据。

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

## 10. 图表状态

目前没有可以直接进入国赛报告 5.5 的正式“心肺与注意状态”结果图。现有图表属于可用性、估计器诊断、失败机制和外部资产评估，只能作为方法审查或补充证据。

## 11. 当前停止线

- HR/BR：`HOLD / SUPPORTING_ONLY`
- HRV：`BLOCKED`
- `models_trained = false`
- 当前不把 mmWave 可用性直接等同于 Cardiopulmonary 正式资格；
- 当前不进入正式多模态监督学习性能比较。
