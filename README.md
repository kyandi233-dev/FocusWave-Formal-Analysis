# FocusWave 正式分析与报告证据库

更新日期：2026-09-12。

本仓库是 FocusWave 当前分析计划、研究决策、协作治理、报告规范与证据映射的权威入口。可执行分析代码只维护在对应代码仓库；本仓库不复制第二份源码。历史报告、旧分析方案和旧运行记录继续保留用于 provenance（来源追踪），但与后出的正式决策冲突时不得覆盖当前口径。

## 当前权威仓库

- 正式实验程序：`kyandi233-dev/FocusWave@formaltest`
- Behavior（行为）、NIR（近红外）、RGB（可见光视频）正式下游代码：`kyandi233-dev/Attention-Analysis`
- 本仓库方法/治理/报告：`kyandi233-dev/FocusWave-Formal-Analysis@codex/code-fix-ledger`
- mmWave（毫米波）与多模态外部代码来源：`greenboo26/focuswave-multimodal-attention-analysis`

当前正式下游代码的长期基础分支仍为 `Attention-Analysis@codex/formal-analysis-v2-portable`；监督学习 A/B/C/D 与 1.16.3 修改仍通过独立 draft PR（草稿拉取请求）开发，尚未全部合并到该基础分支。任何“当前代码事实”必须读取对应开发 PR / HEAD，而不能只看基础分支。

## 当前 cohort 与身份口径

当前 `Attention-Analysis` 正式配置声明 **116 sessions（场次）、61 participant groups（参与者组）**。cohort manifest 是当前 governed cohort（治理队列）的唯一场次来源；问卷缺失或某单一模态缺失不得反向删除 Behavior 场次或改变参与者身份。`participant_group_id` 是正式推断、bootstrap（自助法）与 participant-disjoint prediction（参与者互斥预测）的统一内部统计键。

历史 `44/38/6` 与先前 `115/61/11` 均不得继续写成当前代码事实。参与次数分布、恰好双场组等细节须从当前 cohort manifest / repeat registry 重新审计；模态 availability（可用性）须与 governed cohort 分开报告。

## 当前方法主线：1.16 系列

当前优先阅读：

1. [`分析设计/1.16.1-监督学习心理意义、训练权重与多层评价修订_20260911.md`](分析设计/1.16.1-监督学习心理意义、训练权重与多层评价修订_20260911.md)：首轮 Q1 监督学习的心理学解释、参与者等权训练/预处理/评价、特征级解释、M0–M7 设备/信息包比较与不确定性。
2. [`分析设计/1.16.2-瞳孔相关_眨眼联合清洗与探针前动态分析当前决策_20260912.md`](分析设计/1.16.2-瞳孔相关_眨眼联合清洗与探针前动态分析当前决策_20260912.md)：NIR 瞳孔、RGB 眨眼、联合清洗、线性/二次动态的当前科学决策。
3. [`分析设计/1.16.3-瞳孔与眨眼测量审计及代码修改实施计划_20260912.md`](分析设计/1.16.3-瞳孔与眨眼测量审计及代码修改实施计划_20260912.md)：把 1.16.2 转成代码与真实数据 measurement audit（测量审计）的执行合同。
4. [`协作治理/6.3-1.16系列单一Formal分支与代码任务治理_20260912.md`](协作治理/6.3-1.16系列单一Formal分支与代码任务治理_20260912.md)：1.16 系列在 Formal 仓库统一维护于 `codex/code-fix-ledger`，不再为每个 1.16.x 新建独立 Formal 分支。

`1.15.x` 系列继续保留为监督学习方案形成、A/B/C/D 并行实现与历史审计依据。若其旧 NIR 基础信号、旧斜率、覆盖率或评价口径与 1.16 后出决策冲突，以 1.16 为准。

## 当前代码问题单

`Attention-Analysis` 经过 2026-09-12 清理后只保留 5 个 active issue（当前开放问题单）：

| Issue | 当前职责 | 状态关系 |
|---|---|---|
| #41 | A/B/D probe（探针）键统一 | 集成前置；必须回到 Behavior 权威 probe 表显式映射 |
| #42 | prediction archive（预测归档）回联权威 Q1 标签、期望全集和空归档处理 | 可与 #41 并行 |
| #44 | 瞳孔×眨眼 measurement audit 与 NIR 动态接口 | 当前 Draft PR #45；真实数据审计后回本仓库冻结参数 |
| #40 | B 消费 NIR 显式可估计状态 | 核心缺陷成立；最终字段映射等待 #44 冻结后统一接线 |
| #43 | 参与者等权正式评价、bootstrap、特征级解释与 M0–M7 | 核心代码可继续开发；正式结果受 #41/#42/#40 与 feature freeze（特征冻结）约束 |

旧 #19/#20/#21/#22/#30/#32/#34/#36/#38 已按“历史调研 / 已取代 / 已完成”退出 active 队列。关闭 issue 不删除历史证据。

## 当前 NIR 1.16.3 实现边界

PR #39 保留为旧 1.15.7 Task D 的 draft 基线，不代表最终 1.16 NIR 科学合同。Issue #44 / Draft PR #45 在其上新增 `R_seg,hard`、RGB blink mask（眨眼掩码）、候选 blink buffer（眨眼缓冲）、probe-locked fixed bins（探针锁定固定时间箱）、linear slope（线性斜率）与 quadratic curvature（二次曲率）的测量审计代码。

这些参数当前仍未由 116 场真实数据审计冻结。不得利用 Q1/Q2、行为显著性或 outer-test（外层测试）预测性能选择 buffer、bin、时间支持或 `R_seg` QC（质量控制）。真实审计完成后先更新 1.16.2/1.16.3，再修改 B/A 正式接口。

## 推荐阅读顺序

1. [`分析设计/README.md`](分析设计/README.md)：当前研究问题、监督学习与 NIR 方法入口。
2. [`协作治理/6.2-P0修复任务单_20260911.md`](协作治理/6.2-P0修复任务单_20260911.md)：#40–#43 的原始 P0 证据与验收合同。
3. [`协作治理/6.3-1.16系列单一Formal分支与代码任务治理_20260912.md`](协作治理/6.3-1.16系列单一Formal分支与代码任务治理_20260912.md)：当前 1.16 文档/代码任务治理。
4. `资产导航/README.md`：资产、路径和来源。
5. `行为分析/README.md`、`NIR分析/README.md`、`RGB分析/README.md`、`毫米波分析/README.md`：各模态证据与方法。
6. `跨模态融合/README.md`：统一键、共同集合与增量/融合分析。
7. `正式报告/README.md`：报告准入、文字、图表和章节融合。
8. `运行记录与证据/README.md`：真实运行命令、环境、失败和验收证据。

## 证据边界

代码存在、合成测试通过、CI（持续集成）通过、配置声明某项规则，都不等同于真实科学结果已经产生。正式结果必须基于当前 governed cohort、当前代码/配置、真实运行输出和对应 QC 分母形成。未完成真实运行或仍待方法冻结的内容，只能写成计划、候选或待验证状态。