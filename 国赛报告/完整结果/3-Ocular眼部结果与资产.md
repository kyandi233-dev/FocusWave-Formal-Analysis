# Ocular 眼部结果与资产

本文件记录 Ocular（眼部）信息当前已经完成的测量资格、表示冻结、覆盖率、时间支持、同步与来源限制，以及后续正式心理效应结果应从哪里接入。眼部科学信息由**瞳孔动态**和**眨眼**两部分组成；近红外视频负责瞳孔测量，RGB 可见光视频提供眨眼事件并辅助排除眨眼污染。

## 1. 当前证据身份

当前 Ocular 已完成：

- G1 真实测量审计；
- 瞳孔主表示冻结；
- 眨眼缓冲、固定时间箱、动态指标最低时间跨度冻结；
- 第一轮 pupil level / variability / slope / curvature / blink rate 候选物化；
- feature handoff 与 coverage 输出；
- 2,320 probe canonical identity 闭环；
- Behavior + Ocular + Movement 三模态 P5 interface smoke（接口冒烟测试）真实通过。

因此当前 Ocular 的**测量资格结果已经可以写入报告**，冻结后 Ocular 指标与 Q1/Q2、任务进程和近期行为之间的正式效应结果也已在 `4fdb1a2` 的运行中形成，并在本文件第 10 节登记。两者身份不同：测量资格回答“指标能否稳定形成”，心理效应回答“指标与注意状态怎样对应”，不得互相替代。

## 2. 正式样本、NIR 结构性缺失与覆盖结构

正式研究总体为 61 名参与者、116 个实验场次、2,320 个思维探针。Ocular 的设备可用性不同于总体治理样本：

- 近红外瞳孔测量 source manifest 覆盖 109 个实验场次；
- 7 个治理场次的 NIR 当前不可用：`sub-086`、`sub-087`、`sub-088`、`sub-089`、`sub-090`、`sub-091`、`sub-099`；
- `sub-086`～`sub-091` 的原始 NIR 视频存在，但只有旧 schema producer 产物，缺少当前 fullclass-final/G1 必需字段；`sub-099` 原始视频存在，但当前正式 producer 根目录没有可用产物；
- 这 7 场不是 G1 QC 淘汰，也不是 probe identity 缺失；对应 140 probes 在 Behavior/RGB 中完整存在；
- 当前正式决定为：7 场作为**结构性 NIR availability 缺失**保留，不重跑 producer，不补零、不插补、不改变 cohort membership；
- 最终同时具备近红外瞳孔与 RGB 眨眼辅助清洗条件的场次为 108 个；108 个联合覆盖场次理论上对应 2,160 个思维探针窗口。

因此 Ocular 的 probe universe 始终保持 61 人 / 116 场 / 2,320 probes；NIR 只在真实可用范围产生有限值。

第一轮冻结后的 5 个主要 Ocular 特征覆盖为：

| 正式眼部特征 | 有限值 / 2,320 | 占总体探针 | 参与者 | 场次 | 角色 |
|---|---:|---:|---:|---:|---|
| 瞳孔总体水平（hard R_seg，均值） | 1,936 | 83.45% | 61 | 108 | first-round selected |
| 瞳孔波动（hard R_seg，MAD） | 1,936 | 83.45% | 61 | 108 | first-round selected |
| 瞳孔线性变化 | 1,857 | 80.04% | 61 | 107 | first-round selected |
| 瞳孔二次曲率 | 1,855 | 79.96% | 61 | 107 | first-round selected |
| 眨眼频率 | 2,200 | 94.83% | 60 | 110 | first-round selected |

以联合覆盖的 2,160 个潜在瞳孔窗口为分母时，瞳孔总体水平/MAD 的有效比例为 89.63%，线性变化为 85.97%，二次曲率为 85.88%。

## 3. 第一轮瞳孔表示冻结

第一轮正式瞳孔表示采用**硬分割瞳孔—虹膜区域内的瞳孔面积比例**：

\[
R_{\mathrm{seg,hard}}=\frac{N_{\mathrm{pupil}}}{N_{\mathrm{pupil}}+N_{\mathrm{iris}}}。
\]

该指标是无量纲相对面积比例，不是“瞳孔直径 / 虹膜直径”。

同时保留基于椭圆拟合的几何平均直径作为 cross-representation sensitivity（跨表示敏感性）：

\[
D_{\mathrm{geom}}=\sqrt{d_1d_2}。
\]

soft R_seg 只作为 segmentation sensitivity（分割方法敏感性），不进入第一轮主要结果。

### 3.1 hard R_seg 与 geometry 的一致性

在相同清洗、时间箱和探针窗口中，两种表示共同可用率超过 99.5%，但相关程度仅为中等：

| 特征 | 配对窗口 | 配对可用率 | Spearman ρ | 动态方向一致率 |
|---|---:|---:|---:|---:|
| level mean | 1,931 | 99.74% | .664 | — |
| level median | 1,931 | 99.74% | .695 | — |
| variability SD | 1,916 | 99.53% | .720 | — |
| variability MAD | 1,931 | 99.74% | .660 | — |
| linear slope | 1,902 | 99.53% | .592 | 74.13% |
| quadratic curvature | 1,892 | 99.79% | .656 | 76.27% |

跨全部冻结候选配置，geometry vs hard R_seg 的 Spearman ρ 大致落在 .57–.74。由于配对可用率很高，差异主要不是由缺失结构造成。因此两者应视为同一瞳孔构念的不同测量表示，而不是可以任意互换的同一数值变量。

## 4. 波动指标冻结

瞳孔波动曾同时比较：标准差（SD）、中位数绝对偏差（MAD）和四分位距（IQR）。最终第一轮正式波动指标采用 **MAD**，原因是它与 IQR 的一致性高，同时比 SD 更不易被少量残余极端值支配。SD 保留为敏感性表示，IQR 不再作为单独第一轮 predictor，但仍可作为测量比较证据。

## 5. 眨眼缓冲与清洗轨道

正式联合清洗冻结为：

- 每次眨眼事件前 **200 ms**；
- 眨眼结束后 **200 ms**；
- 与近红外自身质量控制无效时段合并；
- 被排除时段保持缺失，**不进行线性或样条插值**。

第一轮主要瞳孔结果使用 `RGB blink + NIR QC` 联合清洗。与此同时，保留仅依赖 NIR QC 的 hard R_seg 版本作为 NIR-only device alternative（仅近红外设备替代版本），用于未来设备组合评价，而不是与联合版并列为两个主心理特征。

## 6. 固定时间箱与 20 s 动态支持规则

每个探针前 30 s 窗口固定划分为 **15 个 2 s 时间段**。每段用有效瞳孔值的中位数表示，空时间段保持缺失。

线性 slope 和 quadratic curvature 除需要满足拟合所需数据点外，还必须：

1. 窗口前半段存在真实有效时间段；
2. 窗口后半段存在真实有效时间段；
3. 首末有效时间点至少相隔 **20 s**。

冻结前对 10、15、20、25 s 四档最低跨度进行了标签盲描述性比较：

| 最低真实时间跨度 | linear 可用率 | quadratic 可用率 |
|---:|---:|---:|
| 10 s | 86.90% | 86.76% |
| 15 s | 86.71% | 86.57% |
| **20 s** | **85.97%** | **85.88%** |
| 25 s | 84.72% | 84.68% |

分母为 108 个联合覆盖场次中的 2,160 个潜在窗口。10→20 s 仅损失约 0.93 个百分点的线性趋势覆盖，但明显提高了轨迹时间支持；20→25 s 又进一步损失约 1.25 个百分点，因此最终冻结 20 s。

低于 20 s 的窗口仍可以保留瞳孔总体水平和波动结果，但不解释其 slope 或 curvature。

## 7. 同步与来源模式 QC

### 7.1 RGB–NIR 同步

在具有整体边界证据的场次中，大多数 RGB 与 NIR 时间边界差异处于几十毫秒量级。当前汇总中，整体边界最大绝对差的中位数约为 32 ms，第 95 百分位约 63.6 ms。

同时存在少量 frame-nearest residual 极端场次，例如 `sub-083` 可出现约 182 s 的 frame p95 residual。这里必须区分场次整体 clock boundary 是否一致、某些时段是否存在 coverage gap，以及最近帧残差是否因局部缺失而变大。因此极端 nearest residual 不自动等同于整场时钟失配，也不据此全场剔除；具体探针窗口按真实覆盖和质量标准自然决定可估计性。

### 7.2 左右眼来源模式

NIR QC 后，示例总体构成约为：binocular 37.9%；left-only + right-only 合计 37.3%；missing 24.8%。单眼来源不是少数例外，因此不要求所有有效数据必须双眼同时存在。现有 G1 摘要不能估计 left-only、right-only 与 binocular 之间的稳定数值偏移，所以不进行未经证据支持的来源模式校正；来源模式只作为 QC / sensitivity limitation 携带。

## 8. 正式输入资产

### 8.1 权威 G1 根目录

`D:\Project\厚粲杯\11_数据\_FormalAnalysis\NIR_G1\NIR_G1_20260912_fixed\`

| 文件 | 用途 | 是否大型 |
|---|---|---|
| `probe_measurement_candidates.csv` | 每个探针 × signal × cleaning track × bin 的瞳孔候选；P3 物化核心输入 | 是，约 76 MB |
| `probe_fixed_bin_trajectories.csv` | 固定时间箱瞳孔轨迹 | 是，约 609 MB |
| `blink_recovery_bins.csv` | 眨眼附近恢复轨迹 | 是，约 203 MB |
| `freeze_support/g1_temporal_support_freeze_grid.csv` | 10/15/20/25 s 时间支持比较，72 行 | 否 |
| `freeze_support/g1_cross_signal_representation_summary.csv` | geometry vs hard R_seg 一致性，168 行 | 否 |
| `freeze_support/g1_sync_semantics_split.csv` | 逐场次同步语义拆分，109 行 | 否 |
| `freeze_support/g1_source_mode_limit_summary.csv` | 左右眼来源限制，6 行 | 否 |

### 8.2 RGB 眨眼输入

`D:\Project\厚粲杯\11_数据\_FormalAnalysis\RGB\21_analysis_tables_5.5\tables\rgb_probe_pre30s_strict_features.csv`

用于提供探针前眨眼频率等 Ocular 眼部行为信息。RGB 眨眼同时参与瞳孔眨眼污染区间清洗，但眨眼科学上仍归入 Ocular，不归入 Movement。

## 9. P3 冻结与 P5 身份闭环后的正式输出

本地根目录：`D:\Project\厚粲杯\11_数据\_FormalAnalysis\FormalScience\Ocular\`

| 输出文件 | 规模 | 用途 | 正文身份 |
|---|---:|---|---|
| `ocular_science_output_manifest.json` | 小型 JSON | 冻结参数、表示角色、输入证据与停止线 | 追溯/QC |
| `ocular_feature_handoff.csv` | 25 行 | 眼部候选、required devices、角色、时间合法性、registry readiness | 后续统一 registry 输入 |
| `ocular_feature_coverage.csv` | 25 行 | 每个候选的有限值覆盖、参与者数、场次数 | 5.1 / 测量资格 |
| `ocular_probe_features_wide.csv` | **2,320 × 27** | 探针级 Ocular 宽表；含 canonical identity；P5/后续接口输入 | 大型正式数据表，不复制全文 |
| `g1_temporal_support_freeze_grid.csv` | 72 行 | 冻结证据归档副本 | 测量资格 |
| `g1_cross_signal_representation_summary.csv` | 168 行 | 表示一致性归档副本 | 测量资格 |
| `g1_sync_semantics_split.csv` | 109 行 | 同步/覆盖诊断归档副本 | QC |
| `g1_source_mode_limit_summary.csv` | 6 行 | 来源模式限制归档副本 | QC |

最新物化后，canonical key 缺失/重复均为 0；G1 覆盖 2,180 probes，140 个 G1 缺失治理 probes 的 NIR predictor 全部保持 missing。四张 freeze-support 归档副本已按 byte-exact（字节一致）方式保存，不再存在旧 bundle 中约 1e−16 的 CSV 浮点末位重写问题。

## 10. 冻结后眼部心理效应正式结果

### 10.1 证据身份与版本

| 项 | 值 |
|---|---|
| 分析代码 | `kyandi233-dev/Attention-Analysis` `codex/1.16.10-modality-device-separation @ 4fdb1a22f99afaad604d6023a34796e9663fd4dd` |
| 运行 manifest | `manifests/run_manifest.json`（`status = complete`，`created_at_utc = 2026-09-13T04:42:14Z`） |
| 科学输出 manifest | `manifests/science_output_manifest.json`（`schema = ocular-postfreeze-science-v1`，`status = complete`，`authoritative = true`） |
| 输入 | `tables/ocular_probe_features_wide.csv`（sha256 `f0d7b231…`）与 `Behavior/formal_v3/probe_primary_30s.csv`（sha256 `b15acd4b…`） |
| 身份审计 | 眼部探针 2,320、行为探针 2,320、合并后 2,320；单侧独有 key 均为 0；61 参与者 / 116 场次；`key_universe_exact_match = true` |
| 停止线 | `final_feature_registry_mutated = false`、`supervised_model_run = false`、`multimodal_model_run = false`、`performance_metric_computed = false`、`nir_producer_rerun = false` |

`run_manifest.json` 登记了 6 张结果表的 SHA-256。已现场逐文件重算并与登记值比对，**6/6 完全一致**，因此本节表格与冻结运行字节对应。

### 10.2 五张正式结果表

| 结果表 | 行数 | 用途 | 报告角色 |
|---|---:|---|---|
| `ocular_task_progression.csv` | 15 | 五个维度 × 区块、区块内进程、二者交互 | 正文（5.3.5） |
| `ocular_q1_models.csv` | 30 | Q1 四类别 × 五个维度 × 参与者内/之间 | 正文（人内）＋正式伴随附录（人际） |
| `ocular_q2_models.csv` | 10 | Q2 有序等级 × 五个维度 × 参与者内/之间 | 正文（人内）＋正式伴随附录（人际） |
| `ocular_behavior_links.csv` | 40 | 四个近期行为结果 × 五个维度 × 参与者内/之间 | 正文（人内）＋正式伴随附录（人际） |
| `ocular_feature_analysis_coverage.csv` | 5 | 五个冻结维度的有限值覆盖与分母 | 5.1 / 测量资格 |
| `model_failures.csv` | 0 | 不可估计模型登记 | QC：**本次无失败模型** |

`ocular_sensitivity_role_audit.csv`（20 行）机械登记了全部替代表示的 `analysis_role` 与 `main_model_eligible`，其中 `significance_can_promote_to_main` 在**每一行都为 False**：几何瞳孔、瞳孔标准差、仅近红外清洗轨道等替代表示不会因统计判据进入主结果。

### 10.3 模型口径（源自 `science_output_manifest.json`，不得改写）

- **任务进程**：`每个冻结眼部维度 ~ block_b2 + progression_centered + block_b2 × progression_centered`，Gaussian GEE exchangeable；`progression_centered = (probe_index_in_block − 1) / 9 − 0.5`；聚类单位 `participant_group_id`。
- **Q1**：结果变量 `q1_nominal_4class`，参照类别 1；参与者聚类稳健多项逻辑回归；眼部同时纳入参与者均值（between）与探针偏离（within）；伴随项 `block_b2`、`progression_centered`。
- **Q2**：结果变量 `q2_ordinal_4level`，**累积 Logit 有序模型**配合参与者聚类稳健协方差；**不作为连续变量处理**。
- **眼部—行为联系**：方向为 `近期行为结果 ~ 眼部 within + 眼部 between + block + progression`，**仅为关联，不作因果主张**；连续结果用 Gaussian GEE，比率结果用由明确分子分母构造的 binomial GEE；每个模型只纳入一个眼部维度。
- **多重比较**：Benjamini–Hochberg 分别在任务进程 / Q1 / Q2 / 行为四个族内校正，**从不用于重新选择眼部特征**。
- **缺失处理**：逐模型完整观测；不补零、不插补；治理身份保持。

### 10.4 当前正式效应结果

按 `分析设计/1.16.19` 的裁决，正文以参与者内部（`ocular_within_z`）效应为主叙事，全部参与者之间（`ocular_between_z`）结果完整保留为 `formal_companion` 伴随结果，**不是**敏感性分析。

参与者内部结果中，只有眨眼频率出现明确的注意内容相关效应：相对于“聚焦当前分类任务”，任务无关思维（*OR* = 1.258，95% CI [1.096, 1.444]，族内 *q* = .016）与思维空白（*OR* = 1.348，95% CI [1.157, 1.570]，族内 *q* = .004）都对应更高的眨眼频率。四个瞳孔维度的 12 个参与者内部对比区间全部包含 0。Q2 主观警觉方面，五个维度的参与者内部区间全部包含 0。眼部—行为的参与者内部关系中，眨眼频率与近期 Go 遗漏率的关联通过族内校正（*OR* = 1.154，95% CI [1.085, 1.228]，族内 *q* < .001）。

任务进程方面，瞳孔波动与眨眼频率在区块间与区块内进程上均呈上升方向，但**整个任务进程族没有任何一项通过族内校正**（最小 *q* = .057），只能作为方向性观察报告。

参与者之间（伴随）结果中，Q1 与 Q2 共 20 个对比均未通过族内校正；眼部—行为的人际关系中有两项通过族内校正：瞳孔二次时间曲率与正确 Go 反应时 Theil–Sen 斜率（*b* = −0.130，95% CI [−0.204, −0.057]，族内 *q* = .010）以及眨眼频率与 No-Go 误按率（*OR* = 0.772，95% CI [0.658, 0.905]，族内 *q* = .019）。**注意方向**：眨眼频率与 No-Go 误按率的人内方向为正而人际方向为负，两类结果不得互相外推。

以上全部数字可在第 5.3 节对应表格中逐项复核；本总账不重复全部 95 行效应。

## 11. 当前 Ocular 图件状态

P3 冻结 bundle 主要完成**表格与 feature handoff 物化**。冻结后分析（`4fdb1a2`）生成了 7 张图与 7 份图件审计，但按 `分析设计/1.16.19` 的裁决，这些图把参与者内与参与者之间的结果混在同一图内，**不符合当前报告层级**，因此不作为正文主图。正文主图集 `O-M1` 至 `O-M4` 尚未重绘。

因此结果总账仍然只登记正式表格，不虚构已冻结的“正式眼部效果图”。当前正文可以使用表 5.3-1（hard R_seg 与 geometry 一致性）、表 5.3-2（最低时间跨度与动态指标保留率）以及 5.3.5–5.3.9 的效应表（对应第 10 节登记的正式结果表）。

`O-M1` 需由同一冻结 Gaussian GEE（`feature ~ block_b2 * progression_centered`）派生预测值与 95% 置信区间，属独立图件工作，且需要获批后才能实现；该工作不重新开放 P3 表示选择，也不改变本文件第 10 节的统计结果。

## 12. Google Drive 证据

### 12.1 冻结前的原始精度证据

`_AI_HANDOFF/2026-09-13_ocular-g1-freeze-support-9b9a0ec/`  
https://drive.google.com/drive/folders/1KAHwOt3-7S3MdnMzBVVxQeGo0qUd5dWP

### 12.2 P3 冻结物化证据

`_AI_HANDOFF/2026-09-13_p3-ocular-frozen-49d2f9a/`  
https://drive.google.com/drive/folders/1GOJF7LEJns5qVpELqvs_NZkt_5069rJT

HANDOFF：  
https://drive.google.com/file/d/1uc1TsW6MvOUdbnTYypB8I3zcpC8vsRI_/view

### 12.3 早期 Ocular × Movement 交叉伪迹证据

`_AI_HANDOFF/2026-09-13_p4-movement-ocular-materialization/`  
https://drive.google.com/drive/folders/1tZwZtxA-FNVCVqOzGXjMUjCtanLZePYe

### 12.4 P5 三模态接口真实通过

当前权威 bundle：

`_AI_HANDOFF/2026-09-13_p5-interface-smoke-pass-4205b8c/`

历史失败 bundle 保留用于追溯，不作为当前权威结果：

- `2026-09-13_p5-interface-smoke-BLOCKED-dd94a13/`
- `2026-09-13_p5-interface-smoke-BLOCKED-2-13dbead/`

### 12.5 冻结后眼部心理效应（`4fdb1a2`）

`_AI_HANDOFF/2026-09-13_ocular-postfreeze-analysis-4fdb1a2/`  
https://drive.google.com/drive/folders/1sioMXbaU4tzzUus4AB9PjVYyRK8poLmP

## 13. GitHub 方法与代码来源

- G1 freeze-support 运行：`codex/nir-g1-summary-hardening @ 9b9a0ec170ab7e54198293bed181b134e492f4bc`
- P3 初始冻结物化：`codex/1.16.10-modality-device-separation @ 49d2f9a231bd1436b543ebc93f61541db24d2c53`
- P5 身份闭环与真实通过：`codex/1.16.10-modality-device-separation @ 4205b8c903f33e372c1459a6186b4efa6a686293`
- **冻结后眼部心理效应（本文件第 10 节来源）**：`codex/1.16.10-modality-device-separation @ 4fdb1a22f99afaad604d6023a34796e9663fd4dd`
- 方法裁决：`分析设计/1.16.15-Ocular_G1补充证据裁决与P3冻结_20260913.md`
- P5 身份/缺失裁决：`分析设计/1.16.18-P5_Ocular探针宇宙与NIR缺失身份桥接裁决_20260913.md`
- 绘图与汇报角色裁决：`分析设计/1.16.19-Behavior_Movement_Ocular科研绘图与结果汇报第一阶段裁决_20260913.md`
- 报告方法：`国赛报告/章节草稿/4.4-科学变量形成、窗口化与质量控制.md`、`国赛报告/章节草稿/4.5-解释性统计与主观信息关联分析.md`
- 当前结果草稿：`国赛报告/章节草稿/5.3-眼部测量资格与瞳孔动态_20260913.md`
- 表格装配脚本（第 5.3 节数字由此从冻结结果表生成，非手工誊写）：`D:\Project\厚粲杯\.harness\build_ocular_chapter_tables.py`、`build_5_3_chapter.py`

## 14. 已知限制与后续更新点

1. 冻结后 Ocular 对 Q1/Q2、任务进程和近期行为的正式效应结果**已经形成**并登记于第 10 节。但正文主图集（`O-M1` 至 `O-M4`）尚未按 `分析设计/1.16.19` 的层级重绘：当前 `figures/main` 中的 7 张图把参与者内与参与者之间的结果混在同一图内，**不得直接作为正文主图使用**。`O-M1` 需由同一冻结 Gaussian GEE 派生预测值，属独立图件工作，不在本轮结果登记范围内。
2. 7 个治理场次的 NIR 作为结构性缺失正式接受，不重跑 producer；这不改变 116 场治理总体，也不允许使用旧 schema 产物补值。
3. 眨眼频率仅覆盖 60 名参与者 / 110 场 / 2,200 probes，分母与瞳孔主指标不同，后续模型不得假设二者完全同样本。
4. 个别场次存在极端 nearest-frame residual；当前处理为窗口级实际可用性 + QC，而不是自动全场剔除。
5. source mode 的数值偏倚无法从现有小表估计，只能作为限制与敏感性条件报告。
6. P5 已通过但只证明 Behavior / Ocular / Movement 三模态接口、身份、时间合法性和缺失语义一致；它不是正式监督学习结果，也未修改 unified feature registry。
