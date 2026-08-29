# Behavior 与 NIR 科学分析完整性修复记录（2026-08-29）

## 1. 本记录的作用

本文件持续登记 `kyandi233-dev/Attention-Analysis@codex/formal-analysis-v2-portable` 对照本仓库 `分析设计/` 后进行的科学分析完整性修复。这里记录的是代码实现、合成测试、真实数据待验收和科学结论之间的边界，不把工程完成误写成正式结果。

当前用户尚未提供最终版问卷回答 CSV、重复被试识别 CSV 和新的重复被试读取逻辑。因此本轮明确冻结身份映射读取适配：不改 mapping adapter，不按 session/sub 编号猜参与者身份或 visit 顺序，不运行正式 44 场数据。

## 2. 基线与当前代码进度

- 证据仓库分支：`codex/code-fix-ledger`
- 本记录建立前证据 HEAD：`8bfc05dff0feeba851a8e15b556800923cf5365f`
- 正式代码分支：`codex/formal-analysis-v2-portable`
- 本轮修改前代码 HEAD：`e1b79c05029f70a73230d57d8265952fe728a71b`
- Behavior 第一批修复后代码 HEAD：`2b9b6bd6fc153d3fbc794437d0a4f5edad57cf15`
- NIR candidate / probe / adjusted-model 第二批记录时代码 HEAD：`73857a156bbeaf0b3948ce6c4fc012088abbb457`

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

## 4. 已完成：NIR pupil-only 候选指标信息保留层

重新审计发现，fullclass-final pupil-only adapter 本身已经保留：

- `pupil_geom_mean_diameter`；
- `pupil_equivalent_diameter`；
- `pupil_axis_a` / `pupil_axis_b`；
- `pupil_contour_area`；
- `pupil_ellipse_area`；
- `hard_pupil_fraction`；
- `soft_pupil_fraction`。

但旧 `10_analysis_ready` 主宽表只真正把 `pupil_geom_mean_diameter` 标准化并送入既有 `11_analysis_tables` 轨道，所以“left/right/strict 轨道比较”并不等于“pupil metric 候选比较”。

为避免破坏已有 frame-level schema，本轮没有直接推翻旧主表，而是在同一 `nir_analysis_ready` package 内增加 candidate sidecar：

- `src/attention_pipeline/nir_analysis_ready/candidate_metrics.py`

并由：

- `scripts/nir_materialize_analysis_ready.py`
- `scripts/nir_formal_pipeline.py`

随正式 `10_analysis_ready` 物化一起执行。

候选 sidecar 对每个 session × eye × metric 分别建立 primary / strict：

- raw；
- valid flag；
- session-eye median centered；
- robust z；
- baseline N / valid fraction / MAD / robust sigma。

重复场次绝不共享 baseline。

明确排除：

- PIR；
- OAR；
- iris diameter；
- iris fraction 作为 geometry candidate。

Iris fraction 仍只允许作为 segmentation QC，不能转义为 iris diameter。

同时修复 `scripts/nir_materialize_analysis_ready.py` 的一个既有 fail-closed 错误：旧入口读取不存在的 `n_subjects_failed`，可能把失败 session 当成 0；现改为真实 manifest 字段 `n_sessions_failed_this_run`，candidate materialization 失败也会返回非 0。

## 5. 已完成：NIR candidate validation / within-between / repeat boundary

新增：

- `src/attention_pipeline/nir_formal_analysis/candidate_validation.py`

输出到 `11_analysis_tables/candidate_validation/`：

- `nir_candidate_session_block_metrics.csv`
- `nir_candidate_within_between.csv`
- `nir_candidate_metric_validation.csv`
- `nir_candidate_metric_redundancy.csv`
- `nir_candidate_metric_decisions.csv`
- `nir_candidate_repeat_stability.csv`
- `nir_candidate_failures.csv`
- `nir_candidate_validation_manifest.json`

候选验证当前只做科学 admission audit，不把 outcome p-value 当筛选规则。最终 endpoint 字段始终为：

`pending_real_data_scientific_review`

within / between 使用当前既有 `analysis_group_token` 作为匿名推断组接口，但**没有修改它的读取和映射逻辑**。用户后续提供正式 `participant_key` registry 读取方案后，才允许替换上游 adapter。

重复场次在没有 verified visit order 时只输出：

- 两次 session 的 unordered absolute difference；

不输出：

- visit1 → visit2 的方向性变化。

方向性字段明确登记：

`not_estimable_without_verified_visit_order`

## 6. 已完成：NIR 动态窗口候选扩展

更新：

- `src/attention_pipeline/nir_behavior/features.py`

在原有：

- median / mean；
- MAD / IQR / SD；
- P10 / P90；
- robust-ish slope；
- successive-difference MAD；
- difference-rate MAD/sec；

基础上增加：

- peak-to-trough amplitude；
- dilation velocity median/sec；
- constriction velocity median/sec；
- dilation/constriction step N；
- valid rate-pair N；
- explicit dynamic estimability status。

速度定义使用相邻有效时间点的 `Δpupil / Δt`：正值定义为 dilation，负值取绝对值后定义为 constriction magnitude。至少需要 2 个有效 rate pair 才进入 velocity family；不足时输出 `not_estimable_low_valid_pairs`。

当前**没有**把 peak latency / recovery time 机械塞进所有普通窗口。它们属于 event-response 专属特征，必须等明确事件窗口语义后再计算。频域指标也未放行，因为仍需 timestamp / gap 充分审计。

## 7. 重要新发现并已修：NIR probe anchor trial 仍存在真实泄漏条件

审计 `nir_formal_analysis/pupil_tables.py::build_probe_windows()` 时发现：旧代码虽然在 record 中写：

`anchoring_probe_trial_excluded = True`

但真正筛选只用了：

`trial_onset >= window_start && trial_onset < probe_onset`

没有像 Behavior science-v3 那样同时要求：

`trial_num < anchor_trial_num`

因此当 probe_onset 晚于锚定 trial 的 absolute_onset 时，anchor trial 仍可能进入所谓 pre-probe behavior window。注释与实际逻辑不一致。

新增：

- `src/attention_pipeline/nir_formal_analysis/probe_contract.py`

并接入：

- `scripts/nir_build_analysis_tables.py`
- `scripts/nir_formal_pipeline.py`

现在严格 pre-probe 必须同时满足：

1. 同一 Block；
2. trial onset 在窗口内；
3. `trial_onset < probe_onset`；
4. `trial_num < probe_trial_num`。

随后重新计算 probe-window Behavior 指标并覆写**derived 11_analysis_tables 的 probe 表**，同时输出：

- `probe_behavior_window_audit.csv`
- `probe_contract_failures.csv`
- `probe_contract_manifest.json`

审计表还会记录：

`anchor_would_enter_old_temporal_rule`

用于真实 smoke 时检查旧规则到底污染了多少 probe/window。

## 8. 已完成：probe 前视觉暴露的时间方向

同一个 `probe_contract.py` 现在不再把 anchor trial 的 current stimulus 当作 pre-probe visual proxy，而是对严格 pre-event window 中**实际经历的每个 trial**连接现有：

`D:/_AttentionData/Beijing-NIR/analysis/nir-behavior-v1/stimulus_visual_properties.csv`

并按 probe × window 汇总：

- brightness mean / median；
- contrast mean / median；
- visible-area mean / median；
- visual trial N；
- successfully joined trial N；
- visual coverage。

输出：

- `probe_visual_exposure.csv`

明确：probe 发生之后的信息不允许进入，anchor trial 不允许进入严格 pre-probe exposure。

## 9. 已完成：trial 级 reference unadjusted vs adjusted model interface

新增：

- `src/attention_pipeline/nir_formal_analysis/scientific_models.py`

当前使用既有 `binocular_primary / pre_200ms` **仅作为 reference signal 进行模型接口验收**，不是宣布 geom-mean diameter 为最终主 pupil endpoint。

每条 trial-level pupil predictor 被拆成：

- `pupil_between`：participant-group mean；
- `pupil_within`：当前观测相对 participant-group mean 的偏离。

分别建：

- Go correct RT：LMM；
- Go omission：binomial GEE；
- No-Go commission：binomial GEE。

每个 outcome 都有：

- unadjusted；
- adjusted。

adjustment 接口可纳入：

- current / previous brightness；
- current / previous contrast；
- visible area；
- current / previous stimulus size；
- time-in-block；
- pupil coverage；
- internal coverage；
- binocular / single-eye source-mode fraction。

当前 visual 时间语义写入 manifest：

- current stimulus visual 绝不参与构造 pre-stimulus pupil predictor；
- 因 Behavior outcome 出现在刺激之后，current visual 只允许作为 post-stimulus outcome nuisance；
- previous visual 可以作为 pre-stimulus pupil / behavior nuisance。

机器可读输出：

- `trial_reference_model_table.csv`
- `trial_unadjusted_adjusted_effects.csv`
- `model_failures.csv`
- `deferred_endpoint_models.csv`
- `reference_adjusted_models_manifest.json`

效应表登记 estimate、SE、95% CI、participant-group N、session N、row N、visual support 和 covariates。p-value 字段明确命名为 `p_value_not_for_endpoint_selection`。

### 为什么 probe Q1/Q2 与 block/session 没有现在机械全跑

两份当前正式规范都要求：

candidate validation → limited endpoint freeze → formal association

因此当前代码没有重新走回 predictor × outcome 全排列。`deferred_endpoint_models.csv` 明确把：

- probe：Q1 nominal / Q2 ordinal / validated local Behavior endpoints；
- block/session：d′ / c / β / omission / commission / RT level / variability / slope；

登记为：

`pending_behavior_and_pupil_endpoint_freeze`

待真实 candidate validation 后冻结有限主/次结局，再放行这些正式解释模型。

## 10. 新增/更新测试

Behavior：

- `tests/test_behavior_candidate_validation.py`

NIR：

- `tests/test_nir_pupil_candidate_layer.py`
- `tests/test_nir_dynamic_features.py`
- `tests/test_nir_probe_contract.py`
- `tests/test_nir_reference_adjusted_models.py`

覆盖的关键 contract 包括：

1. pupil candidate registry 不含 iris/PIR；
2. candidate baseline 按 session × eye 分开；
3. fraction 越界只使该 candidate invalid，不篡改基础 pupil quality flag；
4. NIR candidate within deviation 在参与者内正确中心化；
5. dynamic velocity 的方向、单位和最低 pair gate；
6. 证明“仅用 onset < probe onset”的旧规则可让 anchor trial 泄漏；
7. strict rule 明确排除 anchor；
8. probe visual exposure 只使用 strict pre-probe trial；
9. reference pupil within/between decomposition；
10. 模型样本不足时必须写 `not_estimable` failure table；
11. omission 与 commission 仍作为两个独立 outcome，绝不合并为 correct。

### 测试状态边界

截至本次更新：

- 代码和测试已经提交；
- GitHub 当前 HEAD 的 combined status 返回空 status 集合；
- 因此**没有证据可以写“CI 已通过”**；
- 尚未运行本地 pytest；
- 尚未运行真实 session smoke；
- 尚未运行 44-session 正式数据。

这些状态不能互相替代。

## 11. 明确仍未改

本轮仍然没有修改：

- 最终版问卷 CSV 读取；
- 最终版 repeat registry / participant_key 读取；
- 当前 `analysis_group_token` 的上游映射 adapter；
- 任何真实 participant_key ↔ session 对照；
- visit order；
- YOLO / RITnet；
- production fullclass-final；
- PIR / OAR / iris_outer 恢复；
- 44-session 正式运行。

## 12. 当前剩余代码层任务

在最终 CSV / mapping logic 到来前，仍可继续做的主要工作：

1. event-response 专属 pupil amplitude / peak latency / recovery 定义与 gate；
2. formal Chinese figure contract 与 candidate/QC 支持图；
3. 把 adjusted reference effect 做成“调整前 vs 调整后”的正式机器可读 comparison table/图接口；
4. 补 provenance / manifest contract tests；
5. 检查当前新增模块的本地 pytest / representative session smoke。

需要等待最终输入后才能完成：

1. participant_key / repeat mapping adapter；
2. verified visit order sensitivity；
3. questionnaire 正式 join；
4. candidate real-data endpoint freeze；
5. probe 与 block/session 有限主/次结局正式推断；
6. 44-session release。
