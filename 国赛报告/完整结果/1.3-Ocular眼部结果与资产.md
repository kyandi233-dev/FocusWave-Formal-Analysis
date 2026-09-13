# Ocular 眼部结果与资产

本文件记录 Ocular（眼部）信息当前已经完成的测量资格、表示冻结、覆盖率、时间支持、同步与来源限制，以及后续正式心理效应结果应从哪里接入。眼部科学信息由**瞳孔动态**和**眨眼**两部分组成；近红外视频负责瞳孔测量，RGB 可见光视频提供眨眼事件并辅助排除眨眼污染。

## 1. 当前证据身份

当前 Ocular 已完成：

- G1 真实测量审计；
- 瞳孔主表示冻结；
- 眨眼缓冲、固定时间箱、动态指标最低时间跨度冻结；
- 第一轮 pupil level / variability / slope / curvature / blink rate 候选物化；
- feature handoff 与 coverage 输出。

因此当前 Ocular 的**测量资格结果已经可以写入报告**；但冻结后的 Ocular 指标与 Q1/Q2、任务进程和近期行为之间的正式效应结果尚未在当前结果总账中形成，不能用测量资格表代替心理学效应。

## 2. 正式样本与覆盖结构

正式研究总体为 61 名参与者、116 个实验场次、2,320 个思维探针。Ocular 的设备可用性不同于总体治理样本：

- 近红外瞳孔测量 source manifest 覆盖 109 个实验场次；
- 最终同时具备近红外瞳孔与 RGB 眨眼辅助清洗条件的场次为 108 个；
- 108 个联合覆盖场次理论上对应 2,160 个思维探针窗口。

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
R_{\mathrm{seg,hard}}=
\frac{N_{\mathrm{pupil}}}
{N_{\mathrm{pupil}}+N_{\mathrm{iris}}}。
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

瞳孔波动曾同时比较：

- 标准差（SD）；
- 中位数绝对偏差（MAD）；
- 四分位距（IQR）。

最终第一轮正式波动指标采用 **MAD**，原因是它与 IQR 的一致性高，同时比 SD 更不易被少量残余极端值支配。SD 保留为敏感性表示，IQR 不再作为单独第一轮 predictor，但仍可作为测量比较证据。

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

同时存在少量 frame-nearest residual 极端场次，例如 `sub-083` 可出现约 182 s 的 frame p95 residual。这里必须区分：

- 场次整体 clock boundary 是否一致；
- 某些时段是否存在 coverage gap；
- 最近帧残差是否因局部缺失而变大。

因此极端 nearest residual 不自动等同于整场时钟失配，也不据此全场剔除；具体探针窗口按真实覆盖和质量标准自然决定可估计性。

### 7.2 左右眼来源模式

NIR QC 后，示例总体构成约为：

- binocular：约 37.9%；
- left-only + right-only：合计约 37.3%；
- missing：约 24.8%。

单眼来源不是少数例外，因此不要求所有有效数据必须双眼同时存在。现有 G1 摘要不能估计 left-only、right-only 与 binocular 之间的稳定数值偏移，所以不进行未经证据支持的来源模式校正；来源模式只作为 QC / sensitivity limitation 携带。

## 8. 正式输入资产

### 8.1 权威 G1 根目录

`D:\Project\厚粲杯\11_数据\_FormalAnalysis\NIR_G1\NIR_G1_20260912_fixed\`

关键输入：

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

## 9. P3 冻结后的正式输出

本地根目录：

`D:\Project\厚粲杯\11_数据\_FormalAnalysis\FormalScience\Ocular\`

| 输出文件 | 规模 | 用途 | 正文身份 |
|---|---:|---|---|
| `ocular_science_output_manifest.json` | 小型 JSON | 冻结参数、表示角色、输入证据与停止线 | 追溯/QC |
| `ocular_feature_handoff.csv` | 25 行 | 眼部候选、required devices、角色、时间合法性、registry readiness | 后续统一 registry 输入 |
| `ocular_feature_coverage.csv` | 25 行 | 每个候选的有限值覆盖、参与者数、场次数 | 5.1 / 测量资格 |
| `ocular_probe_features_wide.csv` | 2,320 × 28 | 探针级 Ocular 宽表，后续 P5/监督学习接口输入 | 大型正式数据表，不复制全文 |
| `g1_temporal_support_freeze_grid.csv` | 72 行 | 冻结证据归档副本 | 测量资格 |
| `g1_cross_signal_representation_summary.csv` | 168 行 | 表示一致性归档副本 | 测量资格 |
| `g1_sync_semantics_split.csv` | 109 行 | 同步/覆盖诊断归档副本 | QC |
| `g1_source_mode_limit_summary.csv` | 6 行 | 来源模式限制归档副本 | QC |

注意：P3 Ocular 目录内的四张 freeze-support 归档副本在写入时发生过 1e−16 量级浮点末位重写；若需要权威原始精度，应引用 `NIR_G1_20260912_fixed\freeze_support\` 中的原表。

## 10. 当前 Ocular 图件状态

P3 冻结 bundle 主要完成**表格与 feature handoff 物化**，当前并没有一套已经冻结的 Ocular Q1/Q2 正式心理效应图包。因此结果总账暂不虚构“正式眼部效果图”。

当前正文可以使用：

- 表 5.3-1：hard R_seg 与 geometry 一致性；
- 表 5.3-2：最低时间跨度与动态指标保留率。

未来正式 Ocular 科学结果形成后，建议主文只保留 2–3 类真正有解释价值的图：

1. 瞳孔主表示与几何表示的一致性/关系图；
2. 探针前 30 s 瞳孔轨迹及 slope/curvature 图；
3. 瞳孔和眨眼与 Q1/Q2 的效应区间图。

所有来源模式、同步极端场次和清洗参数全排列图应保留在补充/QC 层，不应挤入正文主图。

## 11. Google Drive 证据

### 11.1 冻结前的原始精度证据

`_AI_HANDOFF/2026-09-13_ocular-g1-freeze-support-9b9a0ec/`  
https://drive.google.com/drive/folders/1KAHwOt3-7S3MdnMzBVVxQeGo0qUd5dWP

包含：

- `g1_temporal_support_freeze_grid.csv`（72 行）；
- `g1_cross_signal_representation_summary.csv`（168 行）；
- `g1_sync_semantics_split.csv`（109 行）；
- `g1_source_mode_limit_summary.csv`（6 行）；
- HANDOFF、运行日志和实际入口脚本。

这四张表是方法裁决时应优先引用的原始精度版本。

### 11.2 P3 冻结物化证据

`_AI_HANDOFF/2026-09-13_p3-ocular-frozen-49d2f9a/`  
https://drive.google.com/drive/folders/1GOJF7LEJns5qVpELqvs_NZkt_5069rJT

HANDOFF 单文件：  
https://drive.google.com/file/d/1uc1TsW6MvOUdbnTYypB8I3zcpC8vsRI_/view

包含：

- `ocular_science_output_manifest.json`；
- `ocular_feature_handoff.csv`；
- `ocular_feature_coverage.csv`；
- `ocular_probe_features_wide.csv`；
- 四张冻结证据归档副本；
- Ocular 物化入口脚本与运行日志；
- `bundle_manifest.csv`。

### 11.3 早期 Ocular × Movement 交叉伪迹证据

`_AI_HANDOFF/2026-09-13_p4-movement-ocular-materialization/`  
https://drive.google.com/drive/folders/1tZwZtxA-FNVCVqOzGXjMUjCtanLZePYe

该历史 bundle 包含 `ocular_cross_artifact_audit.csv` 和 `ocular_movement_artifact_sensitivity.csv` 等交叉伪迹敏感性证据。它们只用于判断身体运动/成像条件是否可能污染 Ocular 测量，不用于决定 Q1/Q2 心理效应方向。

## 12. GitHub 方法与代码来源

- G1 freeze-support 运行：`codex/nir-g1-summary-hardening @ 9b9a0ec170ab7e54198293bed181b134e492f4bc`
- P3 冻结物化：`codex/1.16.10-modality-device-separation @ 49d2f9a231bd1436b543ebc93f61541db24d2c53`
- 方法裁决：`分析设计/1.16.15-Ocular_G1补充证据裁决与P3冻结_20260913.md`
- 报告方法：`国赛报告/章节草稿/4.4-科学变量形成、窗口化与质量控制.md`
- 当前结果草稿：`国赛报告/章节草稿/5.3-眼部测量资格与瞳孔动态_20260913.md`

## 13. 已知限制与后续更新点

1. 当前正式科学结果只冻结到“眼部指标如何可靠形成”，尚未形成冻结后 Ocular 对 Q1/Q2 的最终效应结果。
2. 眨眼频率仅覆盖 60 名参与者 / 110 场 / 2,200 probes，分母与瞳孔主指标不同，后续模型不得假设二者完全同样本。
3. 个别场次存在极端 nearest-frame residual；当前处理为窗口级实际可用性 + QC，而不是自动全场剔除。
4. source mode 的数值偏倚无法从现有小表估计，只能作为限制与敏感性条件报告。
5. 当前 P3 handoff manifest 曾出现顶层 `formal_minimum_span_frozen=false` 与 freeze-evidence 中 `true/20s` 的字段语义冲突；实际输出覆盖已按 20 s 规则生成。该记录属于追溯问题，不改变当前科学裁决；后续如新 bundle 修正 manifest，应更新本文件的权威证据指针。
