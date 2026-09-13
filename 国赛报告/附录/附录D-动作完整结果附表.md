# 附录 D　动作完整结果附表

对应正文第 5 章。数据来源：`FormalScience/Movement/tables/`（当前权威）

本附录只登记**可读的整理表**：字段名为中文、只保留必要列、统一小数位。机器原始表（含内部字段名与逐探针/逐折明细）按仓库规则保留在 local-only 源目录，不进入报告附录。

---

## D.1 任务进程系数

来源文件：`movement_task_progression.csv`（16 行）

| **指标** | **项** | **系数** | **95% CI 下限** |
|---|---|---|---|
| Intercept | 0.07826 | 0.1052 | 1380 |
| block2 | -0.002003 | 2.633e-05 | 1380 |
| cycle_bin | -0.0002984 | -2.91e-05 | 1380 |
| block2:cycle_bin | -1.23e-05 | 0.000347 | 1380 |
| Intercept | -4.514e-05 | 0.000128 | 1380 |
| block2 | -0.0001208 | 0.0001406 | 1380 |
| cycle_bin | -3.281e-05 | 1.678e-05 | 1380 |
| block2:cycle_bin | -4.198e-05 | 3.006e-05 | 1380 |
| Intercept | -0.0002438 | 9.908e-05 | 1380 |
| block2 | -0.0002805 | 0.0001989 | 1380 |
| cycle_bin | -3.435e-05 | 6.754e-05 | 1380 |
| block2:cycle_bin | -5.147e-05 | 8.262e-05 | 1380 |
| Intercept | -0.07442 | 0.02991 | 1380 |
| block2 | -0.01842 | 0.1224 | 1380 |
| cycle_bin | -0.007613 | 0.01912 | 1380 |
| block2:cycle_bin | -0.03167 | 0.003757 | 1380 |

注：源表为当前权威 `FormalScience/Movement`；反应时变异系数行采用 `rt_cv_min_n = 2` 口径。

## D.2 与即时注意内容（Q1）的关系

来源文件：`movement_q1_models.csv`（12 行）

| **对比类别（参照：任务聚焦）** | **标准化系数** | **95% CI 下限** | **95% CI 上限** | **行数** |
|---|---|---|---|---|
| 2 | 0.01265 | -0.2108 | 0.2361 | 2,300 |
| 3 | -0.3922 | -0.8878 | 0.1034 | 2,300 |
| 4 | 0.2444 | -0.3184 | 0.8073 | 2,300 |
| 2 | -0.1192 | -0.2195 | -0.01885 | 2,300 |
| 3 | -0.1085 | -0.366 | 0.149 | 2,300 |
| 4 | -0.08738 | -0.205 | 0.03025 | 2,300 |
| 2 | -0.1015 | -0.2103 | 0.007376 | 2,300 |
| 3 | -0.07545 | -0.235 | 0.08408 | 2,300 |
| 4 | -0.2202 | -0.4221 | -0.01834 | 2,300 |
| 2 | -0.08625 | -0.1993 | 0.02682 | 2,300 |
| 3 | -0.08597 | -0.2839 | 0.112 | 2,300 |
| 4 | -0.1489 | -0.3088 | 0.011 | 2,300 |

注：源表为当前权威 `FormalScience/Movement`；反应时变异系数行采用 `rt_cv_min_n = 2` 口径。

## D.3 与主观警觉（Q2）的关系

来源文件：`movement_q2_models.csv`（4 行）

| **累积标准化系数** | **95% CI 下限** | **95% CI 上限** | **行数** |
|---|---|---|---|
| 0.0536 | -0.1183 | 0.2255 | 2,300 |
| -0.02375 | -0.08531 | 0.03781 | 2,300 |
| 0.02901 | -0.03392 | 0.09194 | 2,300 |
| 0.003795 | -0.05579 | 0.06338 | 2,300 |

注：源表为当前权威 `FormalScience/Movement`；反应时变异系数行采用 `rt_cv_min_n = 2` 口径。

## D.4 与近期行为的关系（正式伴随结果）

来源文件：`movement_behavior_links.csv`（20 行）

| **行为结局** | **预测变量** | **标准化系数** | **95% CI 下限** | **95% CI 上限** | **行数** |
|---|---|---|---|---|---|
| body_motion_energy_median | go_correct_rt_median_ms | 0.002361 | -0.002509 | 0.007232 | 2298 |
| body_motion_energy_median | go_correct_rt_cv | 0.001136 | -0.002183 | 0.004456 | 2298 |
| body_motion_energy_median | omission_rate | -0.002059 | -0.006842 | 0.002725 | 2300 |
| body_motion_energy_median | commission_rate | 0.0005502 | -0.003551 | 0.004651 | 2300 |
| body_motion_energy_median | dprime_loglinear | 0.0004838 | -0.004211 | 0.005179 | 2300 |
| pose_lateral_right_per_sec_median | go_correct_rt_median_ms | 1.717e-06 | -3.419e-05 | 3.762e-05 | 2298 |
| pose_lateral_right_per_sec_median | go_correct_rt_cv | 1.602e-06 | -3.313e-05 | 3.634e-05 | 2298 |
| pose_lateral_right_per_sec_median | omission_rate | 3.044e-05 | 7.807e-06 | 5.307e-05 | 2300 |
| pose_lateral_right_per_sec_median | commission_rate | 4.248e-05 | -3.74e-06 | 8.871e-05 | 2300 |
| pose_lateral_right_per_sec_median | dprime_loglinear | -4.505e-05 | -8.258e-05 | -7.512e-06 | 2300 |
| pose_vertical_up_per_sec_median | go_correct_rt_median_ms | 4.109e-05 | -1.53e-05 | 9.747e-05 | 2298 |
| pose_vertical_up_per_sec_median | go_correct_rt_cv | 2.65e-05 | -2.154e-05 | 7.454e-05 | 2298 |
| pose_vertical_up_per_sec_median | omission_rate | 6.96e-05 | -1.762e-05 | 0.0001568 | 2300 |
| pose_vertical_up_per_sec_median | commission_rate | 1.672e-05 | -6.805e-05 | 0.0001015 | 2300 |
| pose_vertical_up_per_sec_median | dprime_loglinear | -3.64e-05 | -0.0001258 | 5.296e-05 | 2300 |
| pose_radial_proximity_direction_score_median | go_correct_rt_median_ms | -0.0101 | -0.01949 | -0.0007035 | 2298 |
| pose_radial_proximity_direction_score_median | go_correct_rt_cv | -0.0003005 | -0.01747 | 0.01687 | 2298 |
| pose_radial_proximity_direction_score_median | omission_rate | -0.009314 | -0.02131 | 0.002681 | 2300 |
| pose_radial_proximity_direction_score_median | commission_rate | 0.008519 | -0.004596 | 0.02163 | 2300 |
| pose_radial_proximity_direction_score_median | dprime_loglinear | -0.003516 | -0.01779 | 0.01076 | 2300 |

注：源表为当前权威 `FormalScience/Movement`；反应时变异系数行采用 `rt_cv_min_n = 2` 口径。 该组按 `分析设计/1.16.19` 登记为 `formal_companion`，**「放附录」不等于「敏感性分析」**。

## D.5 指标覆盖与角色

来源文件：`movement_feature_coverage.csv`（7 行）

| **指标** | **报告角色** | **有限值探针数** | **有效率** | **参与者数** | **场次数** |
|---|---|---|---|---|---|
| body_motion_energy_median | primary_candidate | 2300 | 0.9914 | 61 | 115 |
| pose_lateral_right_per_sec_median | sensitivity_auxiliary | 2300 | 0.9914 | 61 | 115 |
| pose_vertical_up_per_sec_median | sensitivity_auxiliary | 2300 | 0.9914 | 61 | 115 |
| pose_radial_proximity_direction_score_median | qc_sensitivity_only | 2300 | 0.9914 | 61 | 115 |
| exposure_change_abs_median | device_qc_only | 2300 | 0.9914 | 61 | 115 |
| global_motion_energy_median | device_qc_only | 2300 | 0.9914 | 61 | 115 |
| gray_mean_median | device_qc_only | 2300 | 0.9914 | 61 | 115 |

注：源表为当前权威 `FormalScience/Movement`；反应时变异系数行采用 `rt_cv_min_n = 2` 口径。

---

**写作边界**：本附表内容不得改写为正文结论；正文只引用附录编号与其来源表。
