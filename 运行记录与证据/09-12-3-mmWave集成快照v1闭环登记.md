# 09-12-3 mmWave 集成快照 v1 闭环登记

## 目标与范围

本记录登记毫米波（millimeter wave [mmWave]）`mmwave_integration_snapshot_v1` 的接口闭环。该任务复用既有 corrected DLL-time 回放，不修改 producer、selector、estimator、原始数据或注意状态模型，不执行心率变异性（heart rate variability [HRV]）分析。

## 输入与版本

- mmWave canonical repository：`greenboo26/focuswave-multimodal-attention-analysis@main`，任务起点 `e4c77ceed887ea0d06f21e067914d6f8e0f8aba4`；producer 固定 `16729b2ef245f9304dae8674f3bac433bc02e98c`。
- Attention-Analysis review tree：`kyandi233-dev/Attention-Analysis@codex/1.16-abcd-integration-review`，`5c7c82c53fd06477b8eef3b3ffedb7c630ead1a5`。
- 冻结分母：J72 + E44 = 116 sessions、61 participant groups、2,320 probes。
- 时间合同：CSV 零基索引第 1 列动态链接库（dynamic-link library [DLL]）主机接收/入队时间；第 2 列 Python 处理时间仅质量控制；`[effective_start, probe_onset)`；30 s nominal；block-truncated。

## 结果与质量控制

- 键守恒：expected/observed=2,320/2,320，duplicate/missing/extra=0/0/0。
- 可估计：109 sessions / 2,180 probes。
- malformed：5 sessions / 100 probes；source unavailable：2 sessions / 40 probes；全部保留为空。
- 科学特征：Cardiopulmonary（心肺）模态的 fused HR 与 BR；两者均 `PROVISIONAL / PHYSIOLOGY_LIMITED`。
- Movement（动作）模态：无合格毫米波特征；motion proxy 仅 diagnostic。
- HRV：`BLOCKED`。

## 接口 smoke

使用 sub-031（可用）、sub-047（来源不可用）、sub-099（NPZ/时间戳数量不匹配）共 60 个真实探针。Task B、analysis set 与 materialize 均通过；完整案例 20 probes，重复键 0，`models_trained=false`。科学模态使用 `behavior` 与 `cardiopulmonary`，设备依赖单列 `required_devices=[mmwave]`。

当前 Attention-Analysis 仍缺 `RegisteredFeature.modality`、`PlannedModel.modalities`、FeatureScheme modality/device 分离、comparison plan 与 reporting 迁移。因此接口可用，但 1.16.10 下游迁移仍 pending，不授权正式监督学习。

## 证据位置与决策

Git-safe 报告、schema、manifest、feature registry、field-role map、error log、replacement contract 和 handoff 位于 canonical repository 的 `docs/results/2026-09-12_MMWAVE_INTEGRATION_SNAPSHOT_V1/`。逐探针表及 smoke 明细为 local-only；其路径和 SHA-256 由 manifest 登记。Google Drive 使用 Issue #41 已指定的既有文件夹并执行上传后读回核验。

决策：`PROVISIONAL_INTEGRATION_READY / PHYSIOLOGY_LIMITED`。Issue #35/#36 保持开放；不冻结算法，不切换 HR 表示，不运行 HRV，不训练模型。
