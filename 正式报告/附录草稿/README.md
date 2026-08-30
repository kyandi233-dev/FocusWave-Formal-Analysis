# 附录草稿

本目录承载正式报告附录 A–D 的草稿。附录只收"正文压缩掉的完整统计细节、实现参数与可核查证据"，正文负责回答研究问题所需的描述统计、核心方法与主要效应。本 README 是附录登记文件：列出现有附录、正文引用位置、每个附录对应的本地证据文件路径，以及当前登记缺口。证据文件均在本地 `D:/Project/厚粲杯/11_数据/` 与 `_t0_vmd_worktree`，不进 git。

## 现有附录与正文引用对应

| 附录 | 文件 | 正文引用位置 | 对应本地证据（不进 git） |
|---|---|---|---|
| A 分析算法与关键实现参数 | [A-分析算法与关键实现参数.md](A-分析算法与关键实现参数.md) | 4.5 数据处理与统计分析（2 处） | 实现参数来自 Attention-Analysis 生产代码与 `configs/` 配置，无行级结果表；毫米波实现参数在报告冻结前需与权威生产代码再核对（附录 A 正文已注明） |
| B 两阶段预实验补充结果 | [B-两阶段预实验补充结果.md](B-两阶段预实验补充结果.md) | 5.3 近红外瞳孔结果（3 处） | 预实验：两份行为报告（文件名与 SHA256 见 [`资产导航/1.5`](../../资产导航/1.5-两阶段预实验结果与正式任务形成依据.md)）；NIR 正式全表：见下方缺口 1 |
| C 正式行为分析补充结果 | [C-正式行为分析补充结果.md](C-正式行为分析补充结果.md) | 5-结果章节骨架（5.2 行为部分，4 处，含 C.5） | `11_数据/_FormalAnalysis/Behavior/formal_v3/`（`block_cycle_gee.csv`、`error_trajectory_summary.csv`、`probe_primary_30s.csv`、`b1_b2_participant_cluster_bootstrap.csv` 等 66 个文件，索引见 [`行为分析/结果索引`](../../行为分析/结果索引.md)） |
| D 毫米波外部验证与算法重现 | [D-毫米波外部验证与算法重现.md](D-毫米波外部验证与算法重现.md) | 5.4 正文未显式引用（附录 D.1 反向指向正文 5.4.1） | `_t0_vmd_worktree/docs/results/2026-08-31_MMWAVE_PRE30S_SELECTOR_HR/`、`2026-08-30_MMWAVE_HRV_BEAT_LEVEL_GATE/`（含 2026-08-31 扩样文件），索引见 [`毫米波分析/结果索引`](../../毫米波分析/结果索引.md) |

## 登记缺口（待负责人裁决，本代理不改正文与附录正文）

1. **附录 B 缺 NIR 正式结果章节**。5.3 正文三处写"完整参数与调整前后对照见附录 B""敏感性指标与全部 40 行 Block 层效应的结果见附录 B""六个敏感性指标保留于附录"，但附录 B 现有 B.1–B.3 只覆盖两阶段预实验。NIR 正式全表证据已落盘：`11_数据/_FormalAnalysis/NIR/11_analysis_tables/probe_pupil_models/probe_pupil_model_table.csv`（2180 行长格式）与 `block_session_models/block_session_model_table.csv`（436 行长格式，含正文引用的 40 行 Block 层效应）。需负责人决定：在附录 B 增加 NIR 章节，或另立附录承载。
2. **RGB 96 行模型与融合逐折性能表无附录载体**。5.5 正文（RGB）与 5.6 正文（表 7 为八种组合汇总）均未引用附录。RGB 5.5 运行共 96 行可估计模型（block_cycle 24 + Q1 mnlogit 18 + Q2 ordinal 6 + behavior window 30 + mmwave window 18），证据在 `11_数据/_FormalAnalysis/RGB/21_analysis_tables_5.5/models/`；融合逐折性能明细在 `11_数据/_FormalAnalysis/MultiModal/full-20260831/performance/performance_by_fold.csv`。是否新建附录 E 或并入现有附录，由负责人决定。
3. **正文无附录 E 引用**。全仓库 grep 未发现"附录 E"字样，当前无需建附录 E（除非按缺口 2 的裁决另立）。
4. **附录 D 无正文引用指针**。5.4 正文未写"见附录 D"；建议后续定稿时在 5.4 增加指引，本代理不改正文。
