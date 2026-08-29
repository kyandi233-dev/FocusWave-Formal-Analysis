# Behavior 与 NIR 科学分析完整性修复记录（2026-08-29）

## 1. 本记录的作用

本文件持续登记 `kyandi233-dev/Attention-Analysis@codex/formal-analysis-v2-portable` 对照本仓库 `分析设计/` 后进行的科学分析完整性修复。这里记录的是代码实现、合成测试、真实数据待验收和科学结论之间的边界，不把工程完成误写成正式结果。

当前用户尚未提供最终版问卷回答 CSV、重复被试识别 CSV 和新的重复被试读取逻辑。因此本轮明确冻结身份映射读取适配：不改 mapping adapter，不按 session/sub 编号猜参与者身份或 visit 顺序，不运行正式 44 场数据。

## 2. 基线

- 证据仓库分支：`codex/code-fix-ledger`
- 本记录建立前证据 HEAD：`8bfc05dff0feeba851a8e15b556800923cf5365f`
- 正式代码分支：`codex/formal-analysis-v2-portable`
- 本轮修改前代码 HEAD：`e1b79c05029f70a73230d57d8265952fe728a71b`
- Behavior 第一批修复后代码 HEAD：`2b9b6bd6fc153d3fbc794437d0a4f5edad57cf15`

## 3. 已完成：Behavior 候选结局验证层

本轮首先修复一个不依赖新 CSV、但属于《分析设计》核心缺口的环节：现有 science-v3 runner 已经能够计算 trial/probe/cycle/block/session 指标并完成 B1/B2、block×cycle、Q1、Q2、error trajectory 和 participant-disjoint folds，但此前没有正式的候选结局验证与冻结前审计表。

新增：

- `src/attention_pipeline/behavior_formal/candidate_validation.py`
- `tests/test_behavior_candidate_validation.py`

更新：

- `scripts/sart_formal_analysis.py`

新增机器可读产物：

- `behavior_candidate_metric_validation.csv`
- `behavior_metric_redundancy.csv`
- `behavior_endpoint_decisions.csv`
- `behavior_sensitivity_status.csv`
- `probe_primary_30s_within_between.csv`
- `session_metrics_within_between.csv`

### 3.1 候选验证现在覆盖什么

候选表逐尺度登记：

- 可计算行数与 coverage；
- participant N / session N；
- 分布摘要（均值、SD、5/50/95 分位数）；
- omission/commission 的 floor/ceiling 支配情况；
- between-participant variance；
- within-participant variance；
- 若有明确时间轴则登记与 time-on-task 的秩相关描述；
- admission status 与失败原因。

筛选不使用 p-value。`behavior_endpoint_decisions.csv` 只给出基于预设优先级、覆盖、分布和冗余的 candidate role recommendation，最终字段固定为 `pending_real_data_scientific_review`，避免合成测试或单次脚本运行直接宣布“主结局已冻结”。

### 3.2 指标冗余

新增同尺度 Spearman 冗余矩阵，默认 `|r| >= 0.90` 仅标记为高度冗余候选。高相关不会自动删除原始列，也不会被解释成心理学关系；最终保留仍需真实数据和科学审查。

### 3.3 within / between 分解

对 probe 与 session 的 canonical behavior metrics 新增：

- `<metric>__participant_mean`
- `<metric>__within_participant`

其中 within 值为当前观测减去该参与者均值。这为后续解释模型区分稳定个体差异和同一参与者当下偏离提供数据接口。

### 3.4 敏感性分析 fail-closed

当前没有最终版、可验证的 visit/session 顺序输入时：

- `all_eligible_sessions`：ready；
- `first_session_only`：`not_estimable`；
- `visit_order_adjusted`：`not_estimable`。

代码明确禁止从 `session_id` / `subid` 数值大小猜实验先后。未来只有在正式输入出现 `visit_order`、`session_order` 或等价已验证字段后才放行这两条 sensitivity 轨道。

## 4. 新增测试

`tests/test_behavior_candidate_validation.py` 当前覆盖：

1. within-participant centered deviation 在每个参与者内部和为 0；
2. candidate validation 输出 coverage、between/within variance；
3. 高度重复的 RT mean / median 被冗余审计捕获；
4. endpoint freeze 始终保持 `pending_real_data_scientific_review`；
5. 缺少真实 visit order 时 first-session sensitivity fail closed；
6. 只有显式提供 verified visit order 后对应 sensitivity 才进入 ready。

截至本记录建立时，这些测试已提交到代码仓库，但尚未把 GitHub Actions 或本地 pytest 结果登记为通过；必须等实际 CI / 测试结果后更新，不提前写“测试通过”。

## 5. 明确未改

本批没有修改：

- cohort CSV / mapping adapter；
- `participant_key` / `repeat_participant_id` 新读取逻辑；
- 任何具体重复参与者映射；
- 44 场真实数据；
- Q1 nominal 和 Q2 ordinal 的既有正式建模语义；
- Go omission / No-Go commission 分母；
- NIR producer、YOLO、RITnet；
- PIR / iris_outer。

## 6. 下一批

接下来继续在同一 `codex/formal-analysis-v2-portable` 上审计和修复不依赖新 CSV 的 NIR 科学分析层，优先顺序：

1. pupil-only 候选指标注册与候选比较，而不是只比较 left/right/strict 质量轨道；
2. 通用 within/between decomposition；
3. probe 前视觉暴露严格使用 pre-event 时间方向；
4. unadjusted vs visual/time adjusted model contract；
5. 动态候选特征的定义、最低采样要求和 not-admitted gate；
6. 中文正式图表 contract。

仍然不在这一阶段擅自运行正式 44 场数据，也不利用未定稿身份文件补任何真实映射。
