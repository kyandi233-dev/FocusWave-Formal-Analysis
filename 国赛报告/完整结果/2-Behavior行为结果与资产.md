# Behavior 行为结果与资产

本文件记录 Behavior（行为）正式分析当前已经形成的科学结果、输入输出表、图件和证据位置。行为信息主要来自 SART（持续性注意反应任务）任务日志，并以思维探针出现前 30 s 为主要近期状态窗口。

## 1. 结果身份与样本

**证据身份：正式结果 + 测量资格结果。**

正式行为分析覆盖：

- 61 名参与者；
- 116 个实验场次；
- 232 个正式任务区块；
- 1,392 个 cycle；
- 2,320 个思维探针；
- 100,224 个正式试次。

主探针表 `probe_primary_30s.csv` 为 2,320 行、82 列，思维探针主键无重复。正式模型失败表 `model_failures.csv` 当前为 0 行。

## 2. 主要行为变量

行为指标按科学含义分为：

1. **反应速度水平**：正确 Go 反应时均值、正确 Go 反应时中位数；
2. **反应稳定性**：RT-CV（反应时变异系数）为主要波动指标，SD、MAD、IQR 为补充；
3. **近期时间趋势**：探针前正确 Go 反应时 Theil–Sen 稳健斜率；
4. **Go 遗漏**：原始 Go 遗漏率为正式主要表示，更细的明确遗漏与时序歧义遗漏用于质量解释；
5. **No-Go 误按**：No-Go 机会中的按键比例；
6. **辨别表现**：d′ 为综合辨别力，c、β 为补充信号检测指标。

所有比例都保留实际机会数。探针前 30 s 是主要窗口，10 s 与 20 s 是预先规定的时间尺度敏感性窗口。

## 3. 数据覆盖与分布结果

| 指标 | 可估窗口 / 2,320 | 覆盖率 | 说明 |
|---|---:|---:|---|
| 正确 Go RT 均值 | 2,318 | 99.91% | 反应速度水平 |
| 正确 Go RT 中位数 | 2,318 | 99.91% | 反应速度稳健表示 |
| RT-CV | 2,318 | 99.91% | 主要波动指标 |
| Theil–Sen RT slope | 2,316 | 99.83% | 近期反应速度变化趋势 |
| Go omission | 2,320 | 100% | 分母为有效 Go 机会 |
| No-Go commission | 2,320 | 100% | 分母为有效 No-Go 机会 |
| d′ | 2,320 | 100% | 信号检测辨别力 |

每个探针窗口平均有 19.94 个有效正确 Go 反应时，中位数为 21。RT-CV 探针级均值为 0.259，SD = 0.165，中位数为 0.215，第 95 百分位为 0.661。

Theil–Sen RT slope 在 2,316 个可估窗口中的均值为 0.331 ms/s，SD = 4.209，中位数为 0.231 ms/s，第 5–95 百分位为 −4.28 至 4.82 ms/s；54.8% 为正、45.2% 为负。主体分布接近 0，但存在较长尾部，因此极端窗口需要结合有效反应数和实际时间跨度解释。

Go omission 在探针前 30 s 中均值为 0.0241，80.2% 的窗口为 0。No-Go commission 均值为 0.3228；由于单个 30 s 窗口平均只有 2.60 个 No-Go 机会，该比例天然呈现明显离散格点，不能把“100% 可估计”误解为高精度连续测量。

## 4. RT 均值与中位数的冗余

行为冻结前已经预先规定：如果 RT 均值与中位数高度冗余，不把二者同时作为独立首轮行为构念。

| 分析尺度 | Spearman ρ（均值 vs 中位数） | 解释 |
|---|---:|---|
| session | .94 | 高度冗余 |
| block | .93 | 高度冗余 |
| cycle | .93 | 高度冗余 |
| probe | .91 | 高度冗余 |

场次层描述统计：正确 Go RT 中位数平均为 309.31 ms（SD = 116.06），均值平均为 318.93 ms（SD = 88.88），均值减中位数平均为 9.63 ms。该差异说明均值更容易受到少量慢反应影响。

## 5. Q1 即时注意内容结果

Q1 为四分类名义变量，以 Q1=1“聚焦当前分类任务”为参照。连续预测变量在模型前标准化，模型使用参与者聚类稳健标准误。

### 5.1 No-Go 误按率

| 对比 | 标准化系数 B | 95% CI | 结果 |
|---|---:|---|---|
| Q1=2 vs Q1=1 | 0.598 | [0.384, 0.812] | 区间不跨 0 |
| Q1=3 vs Q1=1 | 0.729 | [0.481, 0.976] | 区间不跨 0 |
| Q1=4 vs Q1=1 | 0.127 | [−0.314, 0.567] | 区间跨 0 |

较高 No-Go 误按更明确对应“注意仍围绕实验但已离开当前分类目标”和“任务无关思维”，对“大脑空白”没有同等清楚的区间证据。

这一模式在 10 s 与 20 s 敏感性窗口中保持方向一致：Q1=2 与 Q1=3 的区间仍不跨 0，Q1=4 仍没有清楚证据。

### 5.2 d′

| 对比 | 标准化系数 B | 95% CI |
|---|---:|---|
| Q1=2 vs Q1=1 | −0.448 | [−0.700, −0.196] |
| Q1=3 vs Q1=1 | −0.620 | [−0.940, −0.300] |

Q1=4 的区间跨 0。RT 水平、RT 波动与 RT slope 对 Q1 的多数区间也跨 0。这说明行为不同维度与主观注意内容并不同步变化，不能把全部行为压缩为一个单一“注意分数”。

## 6. Q2 困倦—清醒结果

Q2 作为有序等级变量，以参与者为聚类单位使用有序广义估计方程。No-Go commission 的 30 s 标准化系数为：

- **B = −0.299，95% CI [−0.397, −0.201]**。

即较高近期 No-Go 误按对应较低的主观警觉等级。RT-CV、RT slope 和部分遗漏指标也有方向明确的关系，完整结果以正式 `q2_ordinal_gee_models.csv` 为准。

## 7. 任务进程结果

Block 间参与者聚类结果中，任务后期最明确的变化集中在反应稳定性：

| 指标 | B2−B1 | 95% CI | 解释 |
|---|---:|---|---|
| RT-CV | +0.029 | [0.007, 0.055] | 第二个区块波动增加 |
| 正确 Go RT SD | +8.9 ms | [1.4, 17.2] | 第二个区块反应时离散度增加 |

RT 均值/中位数、原始 Go omission、No-Go commission 和 d′ 的 Block 间差异没有出现同等明确的区间证据。因此任务持续带来的变化更集中体现为**反应稳定性下降**，而不是所有行为指标同步变差。

### 7.1 错误事件前后的近期行为变化

除区块尺度的变化之外，`formal_v3` 还输出了错误事件附近的短时行为过程。对每个 Go 遗漏与 No-Go 误按事件，取该事件前后各 3 个试次位置，统计这些位置上的正确 Go 反应时相对于**该参与者自身典型水平**（参与者内正确 Go 反应时中位数）的偏离。相对位置 0 为错误事件本身，该试次没有正确 Go 反应时，因此不产生估计值。

| 错误类型 | 相对位置 | 效应估计（ms） | 标准误（ms） | 参与者 | 场次 | 事件数 |
|---|---:|---:|---:|---:|---:|---:|
| Go 遗漏 | −3 | +32.8 | 15.1 | 54 | 93 | 1,944 |
| Go 遗漏 | −2 | +48.8 | 12.3 | 54 | 93 | 1,949 |
| Go 遗漏 | −1 | +76.6 | 19.2 | 54 | 93 | 1,955 |
| Go 遗漏 | +1 | −38.3 | 10.7 | 54 | 93 | 1,951 |
| Go 遗漏 | +2 | +6.7 | 7.1 | 54 | 93 | 1,945 |
| Go 遗漏 | +3 | +10.3 | 7.6 | 54 | 93 | 1,941 |
| No-Go 误按 | −3 | +4.4 | 5.3 | 61 | 116 | 3,724 |
| No-Go 误按 | −2 | +8.6 | 5.0 | 61 | 116 | 3,724 |
| No-Go 误按 | −1 | +9.7 | 5.0 | 61 | 116 | 3,724 |
| No-Go 误按 | +1 | −6.1 | 9.1 | 61 | 116 | 3,724 |
| No-Go 误按 | +2 | −18.3 | 7.1 | 61 | 116 | 3,724 |
| No-Go 误按 | +3 | −6.6 | 7.0 | 61 | 116 | 3,724 |

表注：正值为慢于参与者自身典型水平。**正式输出只提供效应估计与参与者层标准误，不提供置信区间**；本表因此不列 95% CI，避免用派生区间冒充正式统计量。Go 遗漏的可用参与者（54）与场次（93）少于治理总体（61 人 / 116 场），因为只有至少出现一次 Go 遗漏的场次才贡献事件；No-Go 误按在每个相对位置上的事件数相同，因为误按事件本身不消耗正确 Go 试次。

来源表：`D:\Project\厚粲杯\11_数据\_FormalAnalysis\Behavior\formal_v3\error_trajectory_summary.csv`（14 行）；事件级明细为同目录 `error_event_trajectories.csv`（39,710 行）。

结果形态：Go 遗漏之前正确 Go 反应时逐步变慢，在紧邻错误的前一个试次达到最大偏离（+76.6 ms），错误之后立即转为快于参与者自身水平（−38.3 ms）并随后回到接近 0；No-Go 误按之前的变慢幅度小得多（+9.7 ms），错误之后的偏离幅度也较小且方向不一致。该分析为描述性局部过程分析，同一事件同时贡献多个相对位置，各位置估计并不独立，因此只描述错误附近的行为形态，不用于错误预测，也不支持因果解释。

## 8. 正式输入资产

### 8.1 Behavior formal_v3 的主要输入

本地结果根目录：

`D:\Project\厚粲杯\11_数据\_FormalAnalysis\Behavior\formal_v3\`

关键上游来源：

| 输入/来源 | 用途 |
|---|---|
| 正式实验原始任务日志（由 `formal_raw_roots` 指定） | 形成试次、区块、cycle 和思维探针行为记录 |
| `configs/behavior_formal_v2.yaml` | 正式行为窗口、指标与输出合同 |
| cohort manifest / repeat registry | 冻结 116 场 / 61 参与者组治理样本与重复参与者身份 |

### 8.2 formal_v3 中进入紧凑科学层的源表

| 文件 | 主要用途 | 本地位置 |
|---|---|---|
| `probe_primary_30s.csv` | 2,320 个探针前 30 s 行为主表；Q1/Q2 与窗口结果的核心输入 | `...\Behavior\formal_v3\probe_primary_30s.csv` |
| `block_metrics.csv` | 区块层行为描述 | 同上 |
| `cycle_metrics.csv` | cycle/任务阶段描述 | 同上 |
| `b1_b2_pairs.csv` | 场次内 B1/B2 配对 | 同上 |
| `b1_b2_participant_cluster_bootstrap.csv` | 参与者优先的 B2−B1 聚类 bootstrap 结果 | 同上 |
| `q1_nominal_models.csv` | Q1 四分类多项逻辑回归效应与 CI | 同上 |
| `q2_ordinal_gee_models.csv` | Q2 有序 GEE 效应与 CI | 同上 |
| `model_failures.csv` | 正式模型失败审计；当前 0 行 | 同上 |
| `run_manifest.json` | 运行分母、输入/输出与状态快照 | 同上 |

大型 `trial_metrics.csv` 约 76 MB，为可再生中间结果，不复制进 GitHub 或 Drive 结果总账。

## 9. Behavior 紧凑科学输出

当前代码把正式 producer 大表留在 `formal_v3`，在 `FormalScience/Behavior` 只保存紧凑表、图和源表指针。

本地根目录：

`D:\Project\厚粲杯\11_数据\_FormalAnalysis\FormalScience\Behavior\`

### 9.1 紧凑输出表/manifest

| 文件 | 用途 |
|---|---|
| `tables/behavior_feature_handoff.csv` | 行为候选特征定义、单位、角色、设备依赖、时间合法性、是否仍需研究者冻结 |
| `tables/behavior_feature_coverage.csv` | 行为候选有限值覆盖率摘要 |
| `manifests/producer_source_pointers.csv` | 指向 formal_v3 的权威源表，不复制大型结果 |
| `manifests/figure_manifest.csv` | 每张行为科学图的问题、样本、源表、图注与路径 |
| `manifests/science_output_manifest.json` | 行为科学输出状态、候选角色与图件清单 |

### 9.2 当前紧凑图件：8 张

| figure_id | 身份 | 科学用途 | 主要源表 |
|---|---|---|---|
| `behavior_rt_level_mean_median_agreement` | qualification | 检查 RT 均值与中位数是否描述同一速度水平以及偏离恒等线的位置 | `probe_primary_30s.csv` |
| `behavior_rt_level_difference_ecdf` | qualification | 展示均值−中位数差异的尾部和非对称性 | `probe_primary_30s.csv` |
| `behavior_rt_cv_ecdf` | qualification | 展示 RT-CV 分布和尾部 | `probe_primary_30s.csv` |
| `behavior_rt_slope_ecdf` | qualification | 展示探针前 Theil–Sen RT slope 分布 | `probe_primary_30s.csv` |
| `behavior_q1_candidate_coefficients` | main | 行为候选与 Q1 四分类的标准化系数及 95% CI | `q1_nominal_models.csv` |
| `behavior_q2_candidate_coefficients` | main | 行为候选与 Q2 有序自评的标准化系数及 95% CI | `q2_ordinal_gee_models.csv` |
| `behavior_b1_b2_compact_effects` | main | 核心无量纲行为指标的 B2−B1 变化 | `b1_b2_participant_cluster_bootstrap.csv` |
| `behavior_candidate_coverage` | qc | 审计首轮候选的探针覆盖率 | `behavior_feature_handoff.csv` |

每张图均生成 PNG 300 dpi 与 SVG；具体相对路径记录在 `manifests/figure_manifest.csv`。

## 10. Google Drive 证据

当前 `_AI_HANDOFF` 中已定位到的 Behavior 主要云端证据为：

**`2026-09-12_behavior116-nir-g1-audit/`**  
https://drive.google.com/drive/folders/1e93XTRCW31O6ASne7pNasS4y3pjP5P4t

其中：

- `HANDOFF.md`：Behavior 116 场全量运行、mean vs median 冗余、NIR G1 初始测量审计与本地绝对路径；
- `资源索引.md`：bundle 与本地大资产导航；
- 两个 run manifest、失败表、Behavior 端点决策与冗余审计等小文件；
- bundle 共 27 个内容文件 + `bundle_manifest.csv`，约 2.02 MiB。

该 bundle **不包含 `formal_v3` 全量输出**，也不是当前 Behavior 紧凑科学层全部图件的专门 handoff。当前报告中的正式行为数值还应同时以：

- `国赛报告/章节草稿/5.2-行为表现与即时主观状态_20260913.md`；
- 本地 `Behavior\formal_v3\` 权威表；
- 当前 `FormalScience\Behavior\` 紧凑层

共同核对。后续如生成专门 Behavior final bundle，应在本文件中把它提升为当前云端权威证据，同时保留 2026-09-12 bundle 作为历史审计来源。

## 11. GitHub 方法与代码来源

- 分析仓库：`kyandi233-dev/Attention-Analysis`
- formal_v3 全量运行记录对应历史运行：`codex/1.16-abcd-integration-review @ 5c7c82c53fd06477b8eef3b3ffedb7c630ead1a5`
- 当前紧凑科学输出实现：`src/attention_pipeline/behavior_formal/science_output.py`
- 重绘/物化入口：`scripts/sart_formal_redraw.py`
- 当前报告方法：`国赛报告/章节草稿/4.4-科学变量形成、窗口化与质量控制.md`、`4.5-解释性统计与主观信息关联分析.md`
- 当前报告结果：`国赛报告/章节草稿/5.2-行为表现与即时主观状态_20260913.md`

## 12. 当前已知限制与后续更新点

1. RT mean 与 median 已证明高度冗余，但最终首轮 Behavior RT-level 表示仍需与统一 feature registry 冻结动作保持一致；不能同时当作两个独立科学维度解释。
2. No-Go commission 单窗口机会数低，因此其比例虽然覆盖完整，却具有明显离散分辨率限制。
3. RT slope 极端尾部需要支持度审计，不应仅凭极端斜率作心理解释。
4. 本文件记录的是解释性结果，不等于正式监督学习性能；后续 Q1 跨参与者预测必须在独立结果模块登记。
