# 附录 D　动作完整结果附表

对应正文第 5 章。本附录只登记**聚合表**；逐探针预测、逐折审计与行级大表按仓库规则保留本地，
路径与 SHA-256 在各任务 manifest 与 `完整结果/` 中登记。

数据来源：`FormalScience/Movement/tables/`（当前权威；RT 变异系数为 `rt_cv_min_n = 2` 口径）
生成方式：由源表直接转换为 Markdown 表，未手工转录、未重新拟合任何模型。

---

## D.1 动作指标的区块、区块内进程与交互项系数

来源文件：`movement_task_progression.csv`（16 行）

| analysis | metric | term | estimate | se | ci_low | ci_high | participant_group_n | session_n | n_rows | correlation_structure | status |
|---|---|---|---|---|---|---|---|---|---|---|---|
| block_cycle_gee | body_motion_energy_median | Intercept | 0.0917135 | 0.00686622 | 0.0782557 | 0.105171 | 61 | 115 | 1380 | Exchangeable within participant_group_id | estimable |
| block_cycle_gee | body_motion_energy_median | block2 | -0.000988465 | 0.000517753 | -0.00200326 | 2.63313e-05 | 61 | 115 | 1380 | Exchangeable within participant_group_id | estimable |
| block_cycle_gee | body_motion_energy_median | cycle_bin | -0.000163732 | 6.869e-05 | -0.000298365 | -2.91002e-05 | 61 | 115 | 1380 | Exchangeable within participant_group_id | estimable |
| block_cycle_gee | body_motion_energy_median | block2:cycle_bin | 0.000167348 | 9.16585e-05 | -1.23028e-05 | 0.000346998 | 61 | 115 | 1380 | Exchangeable within participant_group_id | estimable |
| block_cycle_gee | pose_lateral_right_per_sec_median | Intercept | 4.14354e-05 | 4.41702e-05 | -4.51383e-05 | 0.000128009 | 61 | 115 | 1380 | Exchangeable within participant_group_id | estimable |
| block_cycle_gee | pose_lateral_right_per_sec_median | block2 | 9.8576e-06 | 6.66863e-05 | -0.000120848 | 0.000140563 | 61 | 115 | 1380 | Exchangeable within participant_group_id | estimable |
| block_cycle_gee | pose_lateral_right_per_sec_median | cycle_bin | -8.01417e-06 | 1.26512e-05 | -3.28106e-05 | 1.67823e-05 | 61 | 115 | 1380 | Exchangeable within participant_group_id | estimable |
| block_cycle_gee | pose_lateral_right_per_sec_median | block2:cycle_bin | -5.95999e-06 | 1.83751e-05 | -4.19752e-05 | 3.00552e-05 | 61 | 115 | 1380 | Exchangeable within participant_group_id | estimable |
| block_cycle_gee | pose_vertical_up_per_sec_median | Intercept | -7.23531e-05 | 8.74678e-05 | -0.00024379 | 9.90838e-05 | 61 | 115 | 1380 | Exchangeable within participant_group_id | estimable |
| block_cycle_gee | pose_vertical_up_per_sec_median | block2 | -4.08243e-05 | 0.000122302 | -0.000280536 | 0.000198887 | 61 | 115 | 1380 | Exchangeable within participant_group_id | estimable |
| block_cycle_gee | pose_vertical_up_per_sec_median | cycle_bin | 1.65994e-05 | 2.59922e-05 | -3.43454e-05 | 6.75442e-05 | 61 | 115 | 1380 | Exchangeable within participant_group_id | estimable |
| block_cycle_gee | pose_vertical_up_per_sec_median | block2:cycle_bin | 1.55775e-05 | 3.42072e-05 | -5.14687e-05 | 8.26237e-05 | 61 | 115 | 1380 | Exchangeable within participant_group_id | estimable |
| block_cycle_gee | pose_radial_proximity_direction_score_median | Intercept | -0.0222549 | 0.0266135 | -0.0744173 | 0.0299075 | 61 | 115 | 1380 | Exchangeable within participant_group_id | estimable |
| block_cycle_gee | pose_radial_proximity_direction_score_median | block2 | 0.0519807 | 0.0359176 | -0.0184179 | 0.122379 | 61 | 115 | 1380 | Exchangeable within participant_group_id | estimable |
| block_cycle_gee | pose_radial_proximity_direction_score_median | cycle_bin | 0.00575569 | 0.00682092 | -0.0076133 | 0.0191247 | 61 | 115 | 1380 | Exchangeable within participant_group_id | estimable |
| block_cycle_gee | pose_radial_proximity_direction_score_median | block2:cycle_bin | -0.0139545 | 0.0090363 | -0.0316656 | 0.0037567 | 61 | 115 | 1380 | Exchangeable within participant_group_id | estimable |

注：参与者聚类广义估计方程（GEE）。`progression` 为区块内等距居中进程，一个单位相当于跨越整个区块。

## D.2 动作与即时注意内容（Q1）的关系

来源文件：`movement_q1_models.csv`（12 行）

| model_name | model_family | outcome | predictor | contrast_category | reference_category | estimate_per_predictor_sd | se | ci_low | ci_high | status | observation_unit | participant_group_n | session_n | n_rows |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Q1_body_motion_energy_median | MNLogit_cluster_robust | q1_nominal_4class | body_motion_energy_median | 2 | 1 | 0.0126541 | 0.113987 | -0.210761 | 0.236069 | estimable | probe | 61 | 115 | 2300 |
| Q1_body_motion_energy_median | MNLogit_cluster_robust | q1_nominal_4class | body_motion_energy_median | 3 | 1 | -0.392209 | 0.252857 | -0.887809 | 0.10339 | estimable | probe | 61 | 115 | 2300 |
| Q1_body_motion_energy_median | MNLogit_cluster_robust | q1_nominal_4class | body_motion_energy_median | 4 | 1 | 0.244408 | 0.287171 | -0.318446 | 0.807262 | estimable | probe | 61 | 115 | 2300 |
| Q1_pose_lateral_right_per_sec_median | MNLogit_cluster_robust | q1_nominal_4class | pose_lateral_right_per_sec_median | 2 | 1 | -0.119152 | 0.0511729 | -0.219451 | -0.0188535 | estimable | probe | 61 | 115 | 2300 |
| Q1_pose_lateral_right_per_sec_median | MNLogit_cluster_robust | q1_nominal_4class | pose_lateral_right_per_sec_median | 3 | 1 | -0.108483 | 0.131385 | -0.365999 | 0.149032 | estimable | probe | 61 | 115 | 2300 |
| Q1_pose_lateral_right_per_sec_median | MNLogit_cluster_robust | q1_nominal_4class | pose_lateral_right_per_sec_median | 4 | 1 | -0.0873814 | 0.0600174 | -0.205016 | 0.0302527 | estimable | probe | 61 | 115 | 2300 |
| Q1_pose_vertical_up_per_sec_median | MNLogit_cluster_robust | q1_nominal_4class | pose_vertical_up_per_sec_median | 2 | 1 | -0.10146 | 0.0555286 | -0.210296 | 0.00737561 | estimable | probe | 61 | 115 | 2300 |
| Q1_pose_vertical_up_per_sec_median | MNLogit_cluster_robust | q1_nominal_4class | pose_vertical_up_per_sec_median | 3 | 1 | -0.0754517 | 0.0813942 | -0.234984 | 0.0840809 | estimable | probe | 61 | 115 | 2300 |
| Q1_pose_vertical_up_per_sec_median | MNLogit_cluster_robust | q1_nominal_4class | pose_vertical_up_per_sec_median | 4 | 1 | -0.220218 | 0.102999 | -0.422096 | -0.0183405 | estimable | probe | 61 | 115 | 2300 |
| Q1_pose_radial_proximity_direction_score_median | MNLogit_cluster_robust | q1_nominal_4class | pose_radial_proximity_direction_score_median | 2 | 1 | -0.0862456 | 0.0576867 | -0.199312 | 0.0268203 | estimable | probe | 61 | 115 | 2300 |
| Q1_pose_radial_proximity_direction_score_median | MNLogit_cluster_robust | q1_nominal_4class | pose_radial_proximity_direction_score_median | 3 | 1 | -0.0859692 | 0.100998 | -0.283925 | 0.111987 | estimable | probe | 61 | 115 | 2300 |
| Q1_pose_radial_proximity_direction_score_median | MNLogit_cluster_robust | q1_nominal_4class | pose_radial_proximity_direction_score_median | 4 | 1 | -0.14888 | 0.0815732 | -0.308764 | 0.0110034 | estimable | probe | 61 | 115 | 2300 |

注：对照类别为任务聚焦状态。

## D.3 动作与主观警觉（Q2）的关系

来源文件：`movement_q2_models.csv`（4 行）

| model_name | model_family | outcome | predictor | estimate_per_predictor_sd | se | ci_low | ci_high | status | observation_unit | participant_group_n | session_n | n_rows |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Q2_body_motion_energy_median | OrdinalGEE | q2_ordinal_4level | body_motion_energy_median | 0.0535989 | 0.0876897 | -0.118273 | 0.225471 | estimable | probe | 61 | 115 | 2300 |
| Q2_pose_lateral_right_per_sec_median | OrdinalGEE | q2_ordinal_4level | pose_lateral_right_per_sec_median | -0.0237513 | 0.0314085 | -0.085312 | 0.0378093 | estimable | probe | 61 | 115 | 2300 |
| Q2_pose_vertical_up_per_sec_median | OrdinalGEE | q2_ordinal_4level | pose_vertical_up_per_sec_median | 0.0290097 | 0.0321073 | -0.0339206 | 0.09194 | estimable | probe | 61 | 115 | 2300 |
| Q2_pose_radial_proximity_direction_score_median | OrdinalGEE | q2_ordinal_4level | pose_radial_proximity_direction_score_median | 0.00379499 | 0.0304015 | -0.055792 | 0.063382 | estimable | probe | 61 | 115 | 2300 |

注：Q2 按有序变量建模。

## D.4 动作与近期行为指标的关系（正式伴随结果）

来源文件：`movement_behavior_links.csv`（20 行）

| model_name | model_family | analysis | outcome | predictor | estimate_per_predictor_sd | se | ci_low | ci_high | status | observation_unit | correlation_structure | participant_group_n | session_n | n_rows |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rgb_behavior_window_gee_body_motion_energy_median__go_correct_rt_median_ms | GaussianGEE_cluster | rgb_behavior_window_gee | body_motion_energy_median | go_correct_rt_median_ms | 0.00236102 | 0.00248495 | -0.00250947 | 0.00723152 | estimable | probe | Exchangeable within participant_group_id | 61 | 115 | 2298 |
| rgb_behavior_window_gee_body_motion_energy_median__go_correct_rt_cv | GaussianGEE_cluster | rgb_behavior_window_gee | body_motion_energy_median | go_correct_rt_cv | 0.00113643 | 0.00169346 | -0.00218275 | 0.00445562 | estimable | probe | Exchangeable within participant_group_id | 61 | 115 | 2298 |
| rgb_behavior_window_gee_body_motion_energy_median__omission_rate | GaussianGEE_cluster | rgb_behavior_window_gee | body_motion_energy_median | omission_rate | -0.00205854 | 0.00244071 | -0.00684233 | 0.00272524 | estimable | probe | Exchangeable within participant_group_id | 61 | 115 | 2300 |
| rgb_behavior_window_gee_body_motion_energy_median__commission_rate | GaussianGEE_cluster | rgb_behavior_window_gee | body_motion_energy_median | commission_rate | 0.000550249 | 0.00209239 | -0.00355084 | 0.00465133 | estimable | probe | Exchangeable within participant_group_id | 61 | 115 | 2300 |
| rgb_behavior_window_gee_body_motion_energy_median__dprime_loglinear | GaussianGEE_cluster | rgb_behavior_window_gee | body_motion_energy_median | dprime_loglinear | 0.000483792 | 0.00239547 | -0.00421133 | 0.00517891 | estimable | probe | Exchangeable within participant_group_id | 61 | 115 | 2300 |
| rgb_behavior_window_gee_pose_lateral_right_per_sec_median__go_correct_rt_median_ms | GaussianGEE_cluster | rgb_behavior_window_gee | pose_lateral_right_per_sec_median | go_correct_rt_median_ms | 1.71705e-06 | 1.83203e-05 | -3.41907e-05 | 3.76248e-05 | estimable | probe | Exchangeable within participant_group_id | 61 | 115 | 2298 |
| rgb_behavior_window_gee_pose_lateral_right_per_sec_median__go_correct_rt_cv | GaussianGEE_cluster | rgb_behavior_window_gee | pose_lateral_right_per_sec_median | go_correct_rt_cv | 1.60223e-06 | 1.77223e-05 | -3.31334e-05 | 3.63379e-05 | estimable | probe | Exchangeable within participant_group_id | 61 | 115 | 2298 |
| rgb_behavior_window_gee_pose_lateral_right_per_sec_median__omission_rate | GaussianGEE_cluster | rgb_behavior_window_gee | pose_lateral_right_per_sec_median | omission_rate | 3.04392e-05 | 1.15471e-05 | 7.80692e-06 | 5.30714e-05 | estimable | probe | Exchangeable within participant_group_id | 61 | 115 | 2300 |
| rgb_behavior_window_gee_pose_lateral_right_per_sec_median__commission_rate | GaussianGEE_cluster | rgb_behavior_window_gee | pose_lateral_right_per_sec_median | commission_rate | 4.24824e-05 | 2.35831e-05 | -3.74047e-06 | 8.87053e-05 | estimable | probe | Exchangeable within participant_group_id | 61 | 115 | 2300 |
| rgb_behavior_window_gee_pose_lateral_right_per_sec_median__dprime_loglinear | GaussianGEE_cluster | rgb_behavior_window_gee | pose_lateral_right_per_sec_median | dprime_loglinear | -4.50483e-05 | 1.9151e-05 | -8.25843e-05 | -7.51238e-06 | estimable | probe | Exchangeable within participant_group_id | 61 | 115 | 2300 |
| rgb_behavior_window_gee_pose_vertical_up_per_sec_median__go_correct_rt_median_ms | GaussianGEE_cluster | rgb_behavior_window_gee | pose_vertical_up_per_sec_median | go_correct_rt_median_ms | 4.10862e-05 | 2.8768e-05 | -1.52991e-05 | 9.74716e-05 | estimable | probe | Exchangeable within participant_group_id | 61 | 115 | 2298 |
| rgb_behavior_window_gee_pose_vertical_up_per_sec_median__go_correct_rt_cv | GaussianGEE_cluster | rgb_behavior_window_gee | pose_vertical_up_per_sec_median | go_correct_rt_cv | 2.65034e-05 | 2.45104e-05 | -2.15371e-05 | 7.45438e-05 | estimable | probe | Exchangeable within participant_group_id | 61 | 115 | 2298 |
| rgb_behavior_window_gee_pose_vertical_up_per_sec_median__omission_rate | GaussianGEE_cluster | rgb_behavior_window_gee | pose_vertical_up_per_sec_median | omission_rate | 6.96025e-05 | 4.44989e-05 | -1.76152e-05 | 0.00015682 | estimable | probe | Exchangeable within participant_group_id | 61 | 115 | 2300 |
| rgb_behavior_window_gee_pose_vertical_up_per_sec_median__commission_rate | GaussianGEE_cluster | rgb_behavior_window_gee | pose_vertical_up_per_sec_median | commission_rate | 1.67243e-05 | 4.32537e-05 | -6.8053e-05 | 0.000101502 | estimable | probe | Exchangeable within participant_group_id | 61 | 115 | 2300 |
| rgb_behavior_window_gee_pose_vertical_up_per_sec_median__dprime_loglinear | GaussianGEE_cluster | rgb_behavior_window_gee | pose_vertical_up_per_sec_median | dprime_loglinear | -3.64036e-05 | 4.55924e-05 | -0.000125765 | 5.29575e-05 | estimable | probe | Exchangeable within participant_group_id | 61 | 115 | 2300 |
| rgb_behavior_window_gee_pose_radial_proximity_direction_score_median__go_correct_rt_median_ms | GaussianGEE_cluster | rgb_behavior_window_gee | pose_radial_proximity_direction_score_median | go_correct_rt_median_ms | -0.0100965 | 0.00479238 | -0.0194896 | -0.000703456 | estimable | probe | Exchangeable within participant_group_id | 61 | 115 | 2298 |
| rgb_behavior_window_gee_pose_radial_proximity_direction_score_median__go_correct_rt_cv | GaussianGEE_cluster | rgb_behavior_window_gee | pose_radial_proximity_direction_score_median | go_correct_rt_cv | -0.000300546 | 0.00875832 | -0.0174668 | 0.0168658 | estimable | probe | Exchangeable within participant_group_id | 61 | 115 | 2298 |
| rgb_behavior_window_gee_pose_radial_proximity_direction_score_median__omission_rate | GaussianGEE_cluster | rgb_behavior_window_gee | pose_radial_proximity_direction_score_median | omission_rate | -0.00931442 | 0.00611986 | -0.0213093 | 0.0026805 | estimable | probe | Exchangeable within participant_group_id | 61 | 115 | 2300 |
| rgb_behavior_window_gee_pose_radial_proximity_direction_score_median__commission_rate | GaussianGEE_cluster | rgb_behavior_window_gee | pose_radial_proximity_direction_score_median | commission_rate | 0.00851875 | 0.00669106 | -0.00459573 | 0.0216332 | estimable | probe | Exchangeable within participant_group_id | 61 | 115 | 2300 |
| rgb_behavior_window_gee_pose_radial_proximity_direction_score_median__dprime_loglinear | GaussianGEE_cluster | rgb_behavior_window_gee | pose_radial_proximity_direction_score_median | dprime_loglinear | -0.00351558 | 0.00728428 | -0.0177928 | 0.0107616 | estimable | probe | Exchangeable within participant_group_id | 61 | 115 | 2300 |

注：该组在 `分析设计/1.16.19` 下登记为 `formal_companion`，放附录——**「放附录」不等于「敏感性分析」**。RT 变异系数行采用 `rt_cv_min_n = 2` 的当前口径。

## D.5 动作指标的覆盖与角色

来源文件：`movement_feature_coverage.csv`（7 行）

| predictor_column | report_role | probe_total_n | finite_probe_n | finite_fraction | participant_group_n | session_n |
|---|---|---|---|---|---|---|
| body_motion_energy_median | primary_candidate | 2320 | 2300 | 0.991379 | 61 | 115 |
| pose_lateral_right_per_sec_median | sensitivity_auxiliary | 2320 | 2300 | 0.991379 | 61 | 115 |
| pose_vertical_up_per_sec_median | sensitivity_auxiliary | 2320 | 2300 | 0.991379 | 61 | 115 |
| pose_radial_proximity_direction_score_median | qc_sensitivity_only | 2320 | 2300 | 0.991379 | 61 | 115 |
| exposure_change_abs_median | device_qc_only | 2320 | 2300 | 0.991379 | 61 | 115 |
| global_motion_energy_median | device_qc_only | 2320 | 2300 | 0.991379 | 61 | 115 |
| gray_mean_median | device_qc_only | 2320 | 2300 | 0.991379 | 61 | 115 |

注：含主候选、敏感性辅助、QC 与设备 QC 各类角色。

---

**写作边界**：本附表内容不得改写为正文结论；正文只引用附录编号与其来源表。不同分析集合的分母不同，**不得跨集合比较优劣**。
