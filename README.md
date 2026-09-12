# FocusWave 正式分析与报告证据库

更新日期：2026-09-12。

本仓库是 FocusWave 当前分析计划、研究决策、协作治理、报告规范与证据映射的权威入口。可执行分析代码只维护在对应代码仓库；本仓库不复制第二份源码。历史报告、旧分析方案和旧运行记录继续保留用于 provenance（来源追踪），但与后出的正式决策冲突时不得覆盖当前口径。

## 当前权威仓库与分支

- 正式实验程序：`kyandi233-dev/FocusWave@formaltest`
- Behavior（行为）、NIR（近红外）、RGB（可见光视频）正式下游代码：`kyandi233-dev/Attention-Analysis`
- 本仓库方法/治理/报告唯一当前工作分支：`kyandi233-dev/FocusWave-Formal-Analysis@codex/code-fix-ledger`
- mmWave（毫米波）与多模态外部代码来源：`greenboo26/focuswave-multimodal-attention-analysis`

当前正式下游代码的长期基础分支仍为 `Attention-Analysis@codex/formal-analysis-v2-portable`；监督学习 A/B/C/D、A/B 集成修复与 1.16.3 NIR 修改仍通过独立 Draft PR（草稿拉取请求）开发，尚未全部合并到该基础分支。任何“当前代码事实”必须读取对应开发 PR / HEAD，而不能只看基础分支。

Formal 历史专题分支 `codex/1.16.1-supervised-interpretation-review` 已停止作为工作入口。Git 当前显示它与 `codex/code-fix-ledger` 已分叉；其独立提交保留为历史 provenance，但当前 1.16 方法、状态与后续修改统一维护在 `codex/code-fix-ledger`，不通过强制移动历史分支制造表面同步。

## 当前 cohort 与身份口径

当前 `Attention-Analysis` 正式配置声明 **116 sessions（场次）、61 participant groups（参与者组）**。cohort manifest 是当前 governed cohort（治理队列）的唯一场次来源；问卷缺失或某单一模态缺失不得反向删除 Behavior 场次或改变参与者身份。`participant_group_id` 是正式推断、bootstrap（自助法）与 participant-disjoint prediction（参与者互斥预测）的统一内部统计键。

历史 `44/38/6` 与先前 `115/61/11` 均不得继续写成当前代码事实。参与次数分布、恰好双场组等细节须从当前 cohort manifest / repeat registry 重新审计；模态 availability（可用性）须与 governed cohort 分开报告。

当前 NIR 1.16.3 测量审计链记录 **109 个 current-compatible NIR source records（当前兼容近红外源记录）**。109 只表示当前可运行 NIR 来源，不是监督学习总体样本数。

## 当前方法主线：1.16 系列

当前先读总入口：

1. [`分析设计/1.16-当前方法总状态与执行入口_20260912.md`](分析设计/1.16-当前方法总状态与执行入口_20260912.md)：当前研究主线、代码状态、四个剩余监督学习协议风险、特征选择逻辑、两条工作线与真实数据运行门。
2. [`分析设计/1.16.1-监督学习心理意义、训练权重与多层评价修订_20260911.md`](分析设计/1.16.1-监督学习心理意义、训练权重与多层评价修订_20260911.md)：首轮 Q1 监督学习的心理学解释、参与者等权训练/预处理/评价、具体特征解释、M0–M7 与时间轨迹报告。
3. [`分析设计/1.16.2-瞳孔相关_眨眼联合清洗与探针前动态分析当前决策_20260912.md`](分析设计/1.16.2-瞳孔相关_眨眼联合清洗与探针前动态分析当前决策_20260912.md)：NIR 瞳孔、RGB 眨眼、联合清洗、线性/二次动态的当前科学决策。
4. [`分析设计/1.16.3-瞳孔与眨眼测量审计及代码修改实施计划_20260912.md`](分析设计/1.16.3-瞳孔与眨眼测量审计及代码修改实施计划_20260912.md)：把 1.16.2 转成代码与真实数据 measurement audit（测量审计）的执行合同。
5. [`协作治理/6.3-1.16系列单一Formal分支与代码任务治理_20260912.md`](协作治理/6.3-1.16系列单一Formal分支与代码任务治理_20260912.md)：1.16 系列的单一 Formal 分支治理。

`1.15.x` 系列继续保留为监督学习方案形成、A/B/C/D 初始并行实现与历史审计依据。若其旧 NIR 基础信号、旧斜率、覆盖率、训练权重或评价口径与 1.16 后出决策冲突，以 1.16 为准。

## 当前监督学习与测量实现状态

当前已经不是“重新设计监督学习”，而是进入**协议收口、上游特征冻结、跨分支集成和真实数据验证**阶段。

| 模块 | 当前状态 |
|---|---|
| Task A / Draft PR #33 | 参与者等权训练/预处理、内外层评价、OOF（折外）预测、fixed-OOF participant-cluster bootstrap（固定折外参与者簇自助法）、feature registry（特征登记表）框架、具体特征比较和 D4–D7 报告层已基本实现 |
| Task B / Draft PR #35 | comparison-specific analysis set（按比较分析集合）、质量/缺失状态和 prediction archive（预测归档）基础合同已存在 |
| #42 / Draft PR #46 | 权威 Q1 回联、期望 `analysis_set × model × outcome` 全集、失败行、`run_id / feature_set_id / membership_type` 等归档合同已实现 |
| #48 / Draft PR #49 | Task B 审计产物可物化为 Task A 一行一 probe 宽表；仍需补 `required_features` 与 Task A 实际模型的一致性合同 |
| #41 / Draft PR #47 | Behavior 权威 probe-key mapper 已实现；最终 NIR alignment 接线等待 #44 schema 冻结 |
| Task C / Draft PR #37 | Behavior 30 s probe 接口与主要纠偏基本完成；最终 Behavior reference `B` 仍待科学冻结 |
| #44 / Draft PR #45 | pupil×blink 测量审计代码已建立；真实审计后冻结 buffer、bin、趋势时间支持、`R_seg` QC 和正式清洗轨道 |
| #40 | 等 #44 冻结最终 NIR feature/status 后接入 Task B |

当前还需优先修四类监督学习科研语义风险：A/B `required_features` 一致性；fold 内被研究特征实际缺失时的比较可估性；feature registry 布尔字段严格解析；missing-aware 中真正缺失与 malformed value（格式坏值）的区分。详细合同见 1.16 总入口页。

## 当前执行顺序

当前两条工作线并行：

- **Behavior/NIR 上游线**：收尾 Behavior 语义 → 冻结 Behavior `B` → 完成 #44 真实测量审计 → 冻结 NIR 特征/status 与真实设备依赖；
- **监督学习协议线**：修四个剩余语义风险 → 保持 #42/#48 已建立合同 → 不继续无依据扩模型。

随后统一：

`Behavior/NIR feature freeze`
→ `真实 feature registry`
→ `#41 最终 probe-key 接线`
→ `#40 NIR status 接线`
→ `A + B + #41 + #42 + #48 integration test（集成测试）`
→ `少量真实 schema / LOSO smoke test（冒烟测试）`
→ `正式 governed-cohort 监督学习运行`
→ `问卷探索性时间对应与正式报告`。

在真实 feature registry、A/B 协议、NIR 最终合同和纵向真实数据验证完成前，相关 PR 继续保持 Draft，不因单模块 CI 通过而放行正式科学结果。

## 推荐阅读顺序

1. [`分析设计/1.16-当前方法总状态与执行入口_20260912.md`](分析设计/1.16-当前方法总状态与执行入口_20260912.md)：当前总状态与执行门。
2. [`分析设计/README.md`](分析设计/README.md)：分析设计目录导航。
3. [`协作治理/6.2-P0修复任务单_20260911.md`](协作治理/6.2-P0修复任务单_20260911.md)：原始 P0 代码证据与验收合同。
4. [`协作治理/6.3-1.16系列单一Formal分支与代码任务治理_20260912.md`](协作治理/6.3-1.16系列单一Formal分支与代码任务治理_20260912.md)：当前分支/任务治理。
5. `资产导航/README.md`：资产、路径和来源。
6. `行为分析/README.md`、`NIR分析/README.md`、`RGB分析/README.md`、`毫米波分析/README.md`：各模态证据与方法。
7. `跨模态融合/README.md`：统一键、共同集合与增量/融合分析。
8. `正式报告/README.md`：报告准入、文字、图表和章节融合。
9. `运行记录与证据/README.md`：真实运行命令、环境、失败和验收证据。

## 证据边界

代码存在、合成测试通过、CI（持续集成）通过、配置声明某项规则，都不等同于真实科学结果已经产生。正式结果必须基于当前 governed cohort、当前代码/配置、真实运行输出和对应 QC 分母形成。未完成真实运行或仍待方法冻结的内容，只能写成计划、候选或待验证状态。