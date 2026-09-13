# 附录索引

本目录按 `工作表/第4章完整修订与结果口径核对_20260913.md` 的规范组织：**方法补充、全部成对表、敏感性与来源表置附录**，附录置于**第 7 章之后**，**不另造独立第 8 章**；引用、术语、图号与分母与正文统一。

附录内容不进入正文结论；正文只引用附录编号与其来源表。

| 附录 | 主题 | 文件 | 状态 |
|---|---|---|---|
| **A** | **事后问卷**（场次级有序模型完整系数表、结局分布、来源清单） | `附录A-事后问卷完整结果附表.md` | 已建 |
| **B** | **眼部**（冻结后 95 项人内/人际估计、22 项正式成对比较、43 行模型评价） | `第5章-眼部与预测完整结果附表.md` | 已存在 |
| C | 行为（区块配对、错误事件轨迹、指标分布与覆盖） | `附录C-行为完整结果附表.md` | 源表已定位，待生成 |
| D | 动作（任务进程、Q1/Q2 模型、行为关系、姿态敏感性、曝光与覆盖 QC） | `附录D-动作完整结果附表.md` | 源表已定位，待生成 |
| **E** | **毫米波心肺**（低估归因分解、QC 分解、覆盖与状态、外部资产审计） | `附录E-毫米波心肺完整结果附表.md` | 已建 |
| F | 监督学习与设备组合（43 行模型评价、22 项成对比较、校准分箱与分母） | `附录F-监督学习完整结果附表.md` | 源表已定位，待生成 |

## 附录归属的裁决依据

按 `分析设计/1.16.19`：

- 全部 `ocular_between_z`（参与者之间）结果**保留为正式伴随附录**，角色 `formal_companion`，**不是 sensitivity**；`ocular_within_z`（人内）进正文，两者**不得混画**。
- 行为 RT 水平一致性、mean−median 分布、RT 变异系数分布、RT 趋势分布与覆盖率 → **资格/QC 附录**。
- 动作姿态横向/纵向方向与径向代理 → **sensitivity 附录**；曝光与来源覆盖 → QC。
- 动作主指标与近期行为的关系 → `formal_companion`，放附录（**"放附录"不等于"敏感性"**）。

## 待生成附录的源表位置

| 附录 | 源表（本地） |
|---|---|
| C | `Behavior/formal_v3/b1_b2_participant_cluster_bootstrap.csv`（15 行）、`error_trajectory_summary.csv`（14 行）、`probe_primary_30s.csv`（2,320 行，局部大表） |
| D | `_handoff/2026-09-13_p4-movement-final-6955ad9/movement_task_progression.csv`（16）、`movement_q1_models.csv`（12）、`movement_q2_models.csv`（4）、`movement_behavior_links.csv`（20）、`movement_feature_coverage.csv`（7） |
| F | `SupervisedRunsV1/report_tables/headline_model_performance.csv`（43）、`paired_increments.csv`（22）、`probability_diagnostics/probability_diagnostics.csv`（43）、`calibration_bins.csv` |

**tracked 与 local-only 边界**：附录只收**聚合表**；逐探针预测、逐折审计、逐帧与行级大表按仓库规则保留本地，
路径与 SHA-256 在各任务的 manifest 与 `完整结果/` 中登记，不进入 Git 与云盘主包。

## 云盘交接

附录文件随图件与素材包一并上传至 Google Drive `_AI_HANDOFF`；包内附 manifest 与 SHA-256。
