# 毫米波分析

更新日期：2026-09-13。

本目录同时包含毫米波早期工程输入审计、当前 integration snapshot（集成快照）和正式方法边界。阅读时必须区分“历史 44 场工程审计”“当前 116 场 governed cohort（治理队列）”“毫米波/心肺当前可用特征”和“尚未合入 Formal 权威分支的状态同步提案”。

## 当前状态先读

当前总体队列由 Formal / Attention-Analysis 的 governed cohort 决定，为 **116 sessions（场次）、61 participant groups（参与者组）、2,320 probes（思维探针）**。毫米波 availability（可用性）不能反向改变该总体队列。

当前分析设计中的 mmWave integration snapshot v1 保留 116 场 / 2,320 probes 的完整骨架；其中临时 cardiopulmonary（心肺）候选特征覆盖约 109 场 / 2,180 probes。该状态仍是 **provisional / physiology-limited（暂定集成可用 / 生理验证受限）**：HR（心率）与 respiration rate / breathing rate（呼吸率）可以继续验证和组织，HRV（心率变异性）仍受逐搏质量与外部生理验证约束，mmWave motion proxy（毫米波运动代理）主要承担诊断、伪迹与辅助解释角色。

因此：`MMWAVE_INTEGRATION = READY` 只表示当前数据接口能够继续集成工作，不自动等于任何正式毫米波 predictor（预测变量）已经通过 feature qualification（特征资格审查）或 producer-side time-legality（生产端时间合法性）。

## 当前隔离 Formal 状态同步分支

毫米波 Formal 状态同步目前停放在：

`codex/mmwave-formal-state-sync-v1`  
远端 HEAD：`8f9bb62593b440e88b42ffd0d047bfd12c4b90e9`

该分支当前只修改 3 份 `分析设计/` 文档，没有代码、数据和 `01_管理/` 追溯文件改动，也没有合入 `codex/code-fix-ledger`。

当前状态：

- `FORMAL_MMWAVE_STATE_SYNC = PARTIAL`；
- `BRANCH_ISOLATION = DONE`；
- `MERGE = NOT_YET`；
- `TRACEABILITY_SYNC = PENDING`；
- `1.15.8 GOVERNANCE ROLE = SUPERSEDED`；
- `1.15.8 TECHNICAL FIXES = NOT_VERIFIED_CLOSED`。

该分支待合并的核心边界为：

1. `MAIN_ANALYSIS = PROCEED` 表示主分析工作可以继续，但不表示正式毫米波 predictor 已经无条件放行；
2. 依赖当前 adapter（适配器）probe 切片结果的毫米波特征，不能仅凭 `MMWAVE_INTEGRATION = READY` 标记为 `verified_pre_probe_only`；
3. 1.15.8 已被后续治理方法 superseded（取代），但其中尚未验证关闭的技术合同问题仍保持 open / not verified closed（开放 / 未验证关闭），不能改写成 resolved（已解决）；
4. `TRACEABILITY_SYNC` 在该分支 PR 合入之后再单独处理，当前 `01_管理/分析记录.md` 与 `01_管理/版本对应.md` 不属于该分支修改范围。

在 rebase / PR / merge 完成前，上述内容是**隔离分支上的待合并状态同步**，当前 Formal 权威正文仍以 `codex/code-fix-ledger` 为准。

## 历史 44 场工程输入审计

[1-当前管线与44场次输入审计](1-当前管线与44场次输入审计.md)、[1.1-单场次试跑与质量门验证](1.1-单场次试跑与质量门验证.md) 和 [1.2-后续样本合并与复现契约](1.2-后续样本合并与复现契约.md) 记录的是早期阶段工程事实。

当时核验队列为 44 个场次、38 个匿名分析组，其中 6 个双场重复组；毫米波可加载队列为 39 个场次、33 个匿名分析组。`sub-036`、`sub-038`、`sub-040`、`sub-041` 为无效占位，`sub-047` 目录为空。这些数字继续保留用于 provenance（来源追踪）和旧数据工程复现，但**不得写成当前 FocusWave 总体样本规模**。

早期文档中的 HR、RR/BR、质量覆盖、行为对齐、RGB motion gate（可见光动作门）等合同仍可作为 producer 和 QC（质量控制）历史依据；若与后出的 1.15.8 / 1.16 系列方法边界冲突，以当前方法文件和实际代码为准。

## 科学解释边界

毫米波当前至少包含三类性质不同的信息：

- cardiopulmonary（心肺）：HR、呼吸率，以及仍受限的逐搏/HRV 信息；
- motion-related（动作相关）：运动代理与信号受动作影响的诊断信息；
- device/QC（设备/质量控制）：可加载性、覆盖率、信号质量、时间切片和对齐合法性。

这些信息不能因为来自同一毫米波设备就自动合并成一个科学模态。当前科学模态组织把 HR / 呼吸等归入 Cardiopulmonary（心肺），运动相关信息依据具体定义进入 Movement（动作）或 QC，设备来源继续记为 `source_namespace = mmwave`。

“能计算”“通过工程 QC”“通过外部生理验证”“具有心理统计关系”“可进入监督学习”是不同状态，必须逐层区分。

## 正式报告与当前国赛报告

旧 `正式报告/` 中的毫米波章节保留历史写作和证据规范价值；新版国赛报告工作区为 `国赛报告/`。当前报告中的心肺与毫米波内容必须严格区分：

- 心率/呼吸的心理生理意义；
- 毫米波是否能可靠测量这些量；
- FocusWave 当前真实数据中是否已经通过对应 QC、外部验证与时间合法性审计。

工程文献中的生命体征误差、动作识别准确率或疲劳分类性能不能直接替代持续注意效度证据。

正式毫米波探针效标模型与外部金标准验证的历史证据路径仍见 [结果索引](结果索引.md)。当前全局方法状态与后续停止点优先读取 [`../分析设计/1.16-state-snapshot-20260913.md`](../分析设计/1.16-state-snapshot-20260913.md)。

## 阶段性工程验收

本轮代码验收：[1.3-PR20生产契约加固验收记录](1.3-PR20生产契约加固验收记录.md)。该记录确认字段契约、全 NaN 拒绝、严格 JSON、依赖预检和占位输入门控；仍需本地最小复跑。
