# 附录 F　监督学习与设备组合完整结果附表

对应正文第 5 章。数据来源：`SupervisedRunsV1/report_tables/`、`SupervisedRunsV1/probability_diagnostics/`

本附录只登记**可读的整理表**：字段名为中文、只保留必要列、统一小数位。机器原始表（含内部字段名与逐探针/逐折明细）按仓库规则保留在 local-only 源目录，不进入报告附录。

---

## F.1 各分析集合上的模型性能

来源文件：`headline_model_performance.csv`（43 行）

| **分析集** | **模型** | **参与者数** | **探针数** | **参与者宏平均对数损失** | **95% CI 下限** | **95% CI 上限** | **状态** |
|---|---|---|---|---|---|---|---|
| 行为 + 动作 | behavior_plus::movement.body_motion_energy.median.pre30s.v1 | 61 | 2296 | 0.6276 | 0.5806 | 0.6799 | estimable |
| 行为 + 动作 | behavior_plus_modality::movement | 61 | 2296 | 0.6276 | 0.5806 | 0.6799 | estimable |
| 行为 + 动作 | behavior_reference | 61 | 2296 | 0.6242 | 0.5769 | 0.6752 | estimable |
| 行为 + 动作 | modality::movement | 61 | 2296 | 0.6465 | 0.6015 | 0.695 | estimable |
| 行为 + 眼部 | behavior_plus::ocular.blink_rate.rgb_event_rate.pre30s.v1 | 60 | 1775 | 0.6223 | 0.5712 | 0.668 | estimable |
| 行为 + 眼部 | behavior_plus::ocular.pupil_level.rseg_hard.rgb_nir_qc.v1 | 60 | 1775 | 0.622 | 0.5728 | 0.6669 | estimable |
| 行为 + 眼部 | behavior_plus::ocular.pupil_linear_trend.rseg_hard.rgb_nir_qc.v1 | 60 | 1775 | 0.6241 | 0.5725 | 0.6691 | estimable |
| 行为 + 眼部 | behavior_plus::ocular.pupil_quadratic_curvature.rseg_hard.rgb_nir_qc.v1 | 60 | 1775 | 0.6246 | 0.5728 | 0.6699 | estimable |
| 行为 + 眼部 | behavior_plus::ocular.pupil_variability.rseg_hard.rgb_nir_qc.v1 | 60 | 1775 | 0.6172 | 0.5687 | 0.6612 | estimable |
| 行为 + 眼部 | behavior_plus_modality::ocular | 60 | 1775 | 0.616 | 0.5695 | 0.661 | estimable |
| 行为 + 眼部 | behavior_reference | 60 | 1775 | 0.6236 | 0.5721 | 0.6686 | estimable |
| 行为 + 眼部 | modality::ocular | 60 | 1775 | 0.6456 | 0.5983 | 0.6925 | estimable |
| 行为参照 | behavior_reference | 61 | 2316 | 0.6237 | 0.5768 | 0.6733 | estimable |
| 设备包 M0 | M0 | 61 | 2316 | 0.6237 | 0.5768 | 0.6733 | estimable |
| 设备包 M3 | M3 | 60 | 2196 | 0.6236 | 0.5745 | 0.672 | estimable |
| 设备包 M5 | M5 | 60 | 1775 | 0.618 | 0.5708 | 0.6619 | estimable |
| 完整组合 | full | 60 | 1775 | 0.618 | 0.5708 | 0.6619 | estimable |
| 完整组合 | full_minus::behavior.go_omission.raw.v1 | 60 | 1775 | 0.6132 | 0.5673 | 0.6589 | estimable |
| 完整组合 | full_minus::behavior.nogo_commission.raw.v1 | 60 | 1775 | 0.6495 | 0.6033 | 0.6947 | estimable |
| 完整组合 | full_minus::behavior.rt_level.median.v1 | 60 | 1775 | 0.6164 | 0.5692 | 0.6614 | estimable |
| 完整组合 | full_minus::behavior.rt_trend.theilsen.v1 | 60 | 1775 | 0.6176 | 0.5703 | 0.6613 | estimable |
| 完整组合 | full_minus::behavior.rt_variability.cv.v1 | 60 | 1775 | 0.6151 | 0.569 | 0.6589 | estimable |
| 完整组合 | full_minus::movement.body_motion_energy.median.pre30s.v1 | 60 | 1775 | 0.616 | 0.5695 | 0.661 | estimable |
| 完整组合 | full_minus::ocular.blink_rate.rgb_event_rate.pre30s.v1 | 60 | 1775 | 0.6189 | 0.5726 | 0.6619 | estimable |
| 完整组合 | full_minus::ocular.pupil_level.rseg_hard.rgb_nir_qc.v1 | 60 | 1775 | 0.6187 | 0.5698 | 0.665 | estimable |
| 完整组合 | full_minus::ocular.pupil_linear_trend.rseg_hard.rgb_nir_qc.v1 | 60 | 1775 | 0.6177 | 0.5704 | 0.6614 | estimable |
| 完整组合 | full_minus::ocular.pupil_quadratic_curvature.rseg_hard.rgb_nir_qc.v1 | 60 | 1775 | 0.6177 | 0.5717 | 0.6626 | estimable |
| 完整组合 | full_minus::ocular.pupil_variability.rseg_hard.rgb_nir_qc.v1 | 60 | 1775 | 0.6244 | 0.5748 | 0.6708 | estimable |
| 完整组合 | full_minus_modality::behavior | 60 | 1775 | 0.6469 | 0.6 | 0.6912 | estimable |
| 完整组合 | full_minus_modality::movement | 60 | 1775 | 0.616 | 0.5695 | 0.661 | estimable |
| 完整组合 | full_minus_modality::ocular | 60 | 1775 | 0.6212 | 0.5721 | 0.6654 | estimable |
| 仅传感信息联合 | sensor_only_joint | 60 | 1779 | 0.6467 | 0.5998 | 0.6914 | estimable |
| AS.standalone::behavior.go_omission.raw.v1 | standalone::behavior.go_omission.raw.v1 | 61 | 2320 | 0.6435 | 0.5987 | 0.6923 | estimable |
| AS.standalone::behavior.nogo_commission.raw.v1 | standalone::behavior.nogo_commission.raw.v1 | 61 | 2320 | 0.6122 | 0.5668 | 0.6586 | estimable |
| AS.standalone::behavior.rt_level.median.v1 | standalone::behavior.rt_level.median.v1 | 61 | 2318 | 0.6445 | 0.6001 | 0.6929 | estimable |
| AS.standalone::behavior.rt_trend.theilsen.v1 | standalone::behavior.rt_trend.theilsen.v1 | 61 | 2316 | 0.6429 | 0.5979 | 0.6912 | estimable |
| AS.standalone::behavior.rt_variability.cv.v1 | standalone::behavior.rt_variability.cv.v1 | 61 | 2318 | 0.6436 | 0.599 | 0.6919 | estimable |
| AS.standalone::movement.body_motion_energy.median.pre30s.v1 | standalone::movement.body_motion_energy.median.pre30s.v1 | 61 | 2300 | 0.6461 | 0.6011 | 0.6948 | estimable |
| AS.standalone::ocular.blink_rate.rgb_event_rate.pre30s.v1 | standalone::ocular.blink_rate.rgb_event_rate.pre30s.v1 | 60 | 2200 | 0.6404 | 0.5908 | 0.6871 | estimable |
| AS.standalone::ocular.pupil_level.rseg_hard.rgb_nir_qc.v1 | standalone::ocular.pupil_level.rseg_hard.rgb_nir_qc.v1 | 61 | 1936 | 0.6497 | 0.6066 | 0.6989 | estimable |
| AS.standalone::ocular.pupil_linear_trend.rseg_hard.rgb_nir_qc.v1 | standalone::ocular.pupil_linear_trend.rseg_hard.rgb_nir_qc.v1 | 61 | 1857 | 0.6468 | 0.6034 | 0.6956 | estimable |
| AS.standalone::ocular.pupil_quadratic_curvature.rseg_hard.rgb_nir_qc.v1 | standalone::ocular.pupil_quadratic_curvature.rseg_hard.rgb_nir_qc.v1 | 61 | 1855 | 0.6478 | 0.6047 | 0.6967 | estimable |
| AS.standalone::ocular.pupil_variability.rseg_hard.rgb_nir_qc.v1 | standalone::ocular.pupil_variability.rseg_hard.rgb_nir_qc.v1 | 61 | 1936 | 0.6471 | 0.6035 | 0.6954 | estimable |

注：主指标为**参与者等权宏平均对数损失**。运行产物中的 `descriptive_base_rate_log_loss`（合并探针口径）与主指标不是同一口径，故未列入本表；同口径无监督基线见 `完整结果/6` §1.0。**不同分析集合分母不同，不得跨集合比较优劣。**

## F.2 全部 22 项成对比较

来源文件：`paired_increments.csv`（22 行）

| **比较类型** | **特征 / 模态** | **增量** | **95% CI 下限** | **95% CI 上限** | **参与者数** |
|---|---|---|---|---|---|
| behavior_increment | movement.body_motion_energy.median.pre30s.v1 | -0.003365 | -0.007163 | -0.000378 | 61 |
| behavior_increment | ocular.blink_rate.rgb_event_rate.pre30s.v1 | 0.001286 | -0.004866 | 0.007325 | 60 |
| behavior_increment | ocular.pupil_level.rseg_hard.rgb_nir_qc.v1 | 0.001636 | -0.00385 | 0.01124 | 60 |
| behavior_increment | ocular.pupil_linear_trend.rseg_hard.rgb_nir_qc.v1 | -0.000493 | -0.000972 | -9.8e-05 | 60 |
| behavior_increment | ocular.pupil_quadratic_curvature.rseg_hard.rgb_nir_qc.v1 | -0.000992 | -0.003152 | 0.00024 | 60 |
| behavior_increment | ocular.pupil_variability.rseg_hard.rgb_nir_qc.v1 | 0.006366 | -0.00264 | 0.01612 | 60 |
| behavior_modality_increment | modality::movement | -0.003365 | -0.007163 | -0.000378 | 61 |
| behavior_modality_increment | modality::ocular | 0.007585 | -0.007448 | 0.02799 | 60 |
| full_leave_one_modality_out | modality::behavior | 0.02883 | 0.005915 | 0.05168 | 60 |
| full_leave_one_modality_out | modality::movement | -0.002013 | -0.007523 | 0.003006 | 60 |
| full_leave_one_modality_out | modality::ocular | 0.003131 | -0.008704 | 0.01517 | 60 |
| full_leave_one_out | behavior.go_omission.raw.v1 | -0.004867 | -0.01263 | -0.000555 | 60 |
| full_leave_one_out | behavior.nogo_commission.raw.v1 | 0.03151 | 0.01197 | 0.05291 | 60 |
| full_leave_one_out | behavior.rt_level.median.v1 | -0.001591 | -0.003925 | 0.000268 | 60 |
| full_leave_one_out | behavior.rt_trend.theilsen.v1 | -0.000459 | -0.000816 | -0.000183 | 60 |
| full_leave_one_out | behavior.rt_variability.cv.v1 | -0.002971 | -0.006218 | -3.4e-05 | 60 |
| full_leave_one_out | movement.body_motion_energy.median.pre30s.v1 | -0.002013 | -0.007523 | 0.003006 | 60 |
| full_leave_one_out | ocular.blink_rate.rgb_event_rate.pre30s.v1 | 0.000875 | -0.005282 | 0.006575 | 60 |
| full_leave_one_out | ocular.pupil_level.rseg_hard.rgb_nir_qc.v1 | 0.000667 | -0.004434 | 0.005964 | 60 |
| full_leave_one_out | ocular.pupil_linear_trend.rseg_hard.rgb_nir_qc.v1 | -0.000299 | -0.000665 | 3.9e-05 | 60 |
| full_leave_one_out | ocular.pupil_quadratic_curvature.rseg_hard.rgb_nir_qc.v1 | -0.000302 | -0.006477 | 0.004859 | 60 |
| full_leave_one_out | ocular.pupil_variability.rseg_hard.rgb_nir_qc.v1 | 0.006406 | -0.003102 | 0.01645 | 60 |

注：增量为「基线损失 − 加项损失」，**负值表示加项更差**。区间为固定折外预测的参与者整簇自助（1,000 次、seed 20260830、95%、不重训），**未做多重比较校正**。22 项中 8 项区间排除 0，其中仅 2 项为正且均属行为信息。

## F.3 概率诊断（排序与校准）

来源文件：`probability_diagnostics.csv`（43 行）

| **分析集** | **模型** | **参与者宏平均 AUROC** | **AUROC CI 下限** | **AUROC CI 上限** | **Brier 分数** | **AUROC 可估人数** | **单一类别人数** | **校准斜率** |
|---|---|---|---|---|---|---|---|---|
| 设备包 M0 | M0 | 0.706 | 0.6656 | 0.7447 | 0.216 | 49 | 12 | 0.6452 |
| 设备包 M3 | M3 | 0.704 | 0.6599 | 0.7453 | 0.216 | 48 | 12 | 0.5572 |
| 设备包 M5 | M5 | 0.7069 | 0.6668 | 0.7467 | 0.2123 | 48 | 12 | 0.4812 |
| 行为 + 动作 | behavior_plus::movement.body_motion_energy.median.pre30s.v1 | 0.7024 | 0.6615 | 0.7439 | 0.2177 | 49 | 12 | 0.5726 |
| 行为 + 眼部 | behavior_plus::ocular.blink_rate.rgb_event_rate.pre30s.v1 | 0.7036 | 0.6595 | 0.7449 | 0.214 | 48 | 12 | 0.5057 |
| 行为 + 眼部 | behavior_plus::ocular.pupil_level.rseg_hard.rgb_nir_qc.v1 | 0.6954 | 0.6497 | 0.7385 | 0.2147 | 48 | 12 | 0.5295 |
| 行为 + 眼部 | behavior_plus::ocular.pupil_linear_trend.rseg_hard.rgb_nir_qc.v1 | 0.6991 | 0.6557 | 0.7394 | 0.2143 | 48 | 12 | 0.5031 |
| 行为 + 眼部 | behavior_plus::ocular.pupil_quadratic_curvature.rseg_hard.rgb_nir_qc.v1 | 0.7005 | 0.6565 | 0.7426 | 0.2143 | 48 | 12 | 0.4899 |
| 行为 + 眼部 | behavior_plus::ocular.pupil_variability.rseg_hard.rgb_nir_qc.v1 | 0.7106 | 0.6686 | 0.7504 | 0.2119 | 48 | 12 | 0.5772 |
| 行为 + 动作 | behavior_plus_modality::movement | 0.7024 | 0.6615 | 0.7439 | 0.2177 | 49 | 12 | 0.5726 |
| 行为 + 眼部 | behavior_plus_modality::ocular | 0.7111 | 0.6692 | 0.7502 | 0.2115 | 48 | 12 | 0.5468 |
| 行为 + 动作 | behavior_reference | 0.7054 | 0.6647 | 0.7441 | 0.2162 | 49 | 12 | 0.6345 |
| 行为 + 眼部 | behavior_reference | 0.7001 | 0.6563 | 0.742 | 0.2142 | 48 | 12 | 0.5082 |
| 行为参照 | behavior_reference | 0.706 | 0.6656 | 0.7447 | 0.216 | 49 | 12 | 0.6452 |
| 完整组合 | full | 0.7069 | 0.6668 | 0.7467 | 0.2123 | 48 | 12 | 0.4812 |
| 完整组合 | full_minus::behavior.go_omission.raw.v1 | 0.7127 | 0.6719 | 0.7512 | 0.2103 | 48 | 12 | 0.5495 |
| 完整组合 | full_minus::behavior.nogo_commission.raw.v1 | 0.5975 | 0.5512 | 0.6446 | 0.2273 | 48 | 12 | -0.1904 |
| 完整组合 | full_minus::behavior.rt_level.median.v1 | 0.7064 | 0.666 | 0.7466 | 0.2115 | 48 | 12 | 0.5024 |
| 完整组合 | full_minus::behavior.rt_trend.theilsen.v1 | 0.7028 | 0.6633 | 0.7421 | 0.2121 | 48 | 12 | 0.4873 |
| 完整组合 | full_minus::behavior.rt_variability.cv.v1 | 0.7098 | 0.6696 | 0.7497 | 0.2111 | 48 | 12 | 0.5338 |
| 完整组合 | full_minus::movement.body_motion_energy.median.pre30s.v1 | 0.7111 | 0.6692 | 0.7502 | 0.2115 | 48 | 12 | 0.5468 |
| 完整组合 | full_minus::ocular.blink_rate.rgb_event_rate.pre30s.v1 | 0.7063 | 0.6661 | 0.7474 | 0.2125 | 48 | 12 | 0.4869 |
| 完整组合 | full_minus::ocular.pupil_level.rseg_hard.rgb_nir_qc.v1 | 0.7039 | 0.6614 | 0.7439 | 0.2127 | 48 | 12 | 0.487 |
| 完整组合 | full_minus::ocular.pupil_linear_trend.rseg_hard.rgb_nir_qc.v1 | 0.706 | 0.6665 | 0.7453 | 0.2121 | 48 | 12 | 0.4834 |
| 完整组合 | full_minus::ocular.pupil_quadratic_curvature.rseg_hard.rgb_nir_qc.v1 | 0.7054 | 0.6656 | 0.7456 | 0.2131 | 48 | 12 | 0.4799 |
| 完整组合 | full_minus::ocular.pupil_variability.rseg_hard.rgb_nir_qc.v1 | 0.6943 | 0.6485 | 0.7379 | 0.2156 | 48 | 12 | 0.4322 |
| 完整组合 | full_minus_modality::behavior | 0.5587 | 0.5025 | 0.6116 | 0.2257 | 48 | 12 | -0.2014 |
| 完整组合 | full_minus_modality::movement | 0.7111 | 0.6692 | 0.7502 | 0.2115 | 48 | 12 | 0.5468 |
| 完整组合 | full_minus_modality::ocular | 0.6997 | 0.657 | 0.7412 | 0.2143 | 48 | 12 | 0.4995 |
| 行为 + 动作 | modality::movement | 0.4569 | 0.4008 | 0.5079 | 0.2267 | 49 | 12 | -12.78 |
| 行为 + 眼部 | modality::ocular | 0.5683 | 0.508 | 0.6257 | 0.2253 | 48 | 12 | -0.03355 |
| 仅传感信息联合 | sensor_only_joint | 0.556 | 0.5003 | 0.6081 | 0.2256 | 48 | 12 | -0.2144 |
| AS.standalone::behavior.go_omission.raw.v1 | standalone::behavior.go_omission.raw.v1 | 0.5466 | 0.5201 | 0.5755 | 0.2254 | 49 | 12 | -5.722 |
| AS.standalone::behavior.nogo_commission.raw.v1 | standalone::behavior.nogo_commission.raw.v1 | 0.7039 | 0.6639 | 0.7434 | 0.2115 | 49 | 12 | 0.8214 |
| AS.standalone::behavior.rt_level.median.v1 | standalone::behavior.rt_level.median.v1 | 0.5739 | 0.5226 | 0.623 | 0.2257 | 49 | 12 | -2.475 |
| AS.standalone::behavior.rt_trend.theilsen.v1 | standalone::behavior.rt_trend.theilsen.v1 | 0.5285 | 0.4953 | 0.5623 | 0.2251 | 49 | 12 | -17.62 |
| AS.standalone::behavior.rt_variability.cv.v1 | standalone::behavior.rt_variability.cv.v1 | 0.5517 | 0.5046 | 0.5958 | 0.2255 | 49 | 12 | -3.401 |
| AS.standalone::movement.body_motion_energy.median.pre30s.v1 | standalone::movement.body_motion_energy.median.pre30s.v1 | 0.4586 | 0.4034 | 0.5103 | 0.2265 | 49 | 12 | -13.03 |
| AS.standalone::ocular.blink_rate.rgb_event_rate.pre30s.v1 | standalone::ocular.blink_rate.rgb_event_rate.pre30s.v1 | 0.5664 | 0.5251 | 0.6096 | 0.2238 | 48 | 12 | -1.026 |
| AS.standalone::ocular.pupil_level.rseg_hard.rgb_nir_qc.v1 | standalone::ocular.pupil_level.rseg_hard.rgb_nir_qc.v1 | 0.5157 | 0.4619 | 0.576 | 0.2283 | 49 | 12 | -43.93 |
| AS.standalone::ocular.pupil_linear_trend.rseg_hard.rgb_nir_qc.v1 | standalone::ocular.pupil_linear_trend.rseg_hard.rgb_nir_qc.v1 | 0.502 | 0.4556 | 0.5481 | 0.227 | 49 | 12 | -31.4 |
| AS.standalone::ocular.pupil_quadratic_curvature.rseg_hard.rgb_nir_qc.v1 | standalone::ocular.pupil_quadratic_curvature.rseg_hard.rgb_nir_qc.v1 | 0.485 | 0.4469 | 0.5235 | 0.2273 | 49 | 12 | -41.04 |
| AS.standalone::ocular.pupil_variability.rseg_hard.rgb_nir_qc.v1 | standalone::ocular.pupil_variability.rseg_hard.rgb_nir_qc.v1 | 0.5925 | 0.5481 | 0.6441 | 0.2268 | 49 | 12 | -0.4288 |

注：AUROC 为**参与者宏平均**，只在具有两类标签的参与者上平均。校准回归按探针合并。该诊断层**不参与模型或正则化参数选择**。

---

**写作边界**：本附表内容不得改写为正文结论；正文只引用附录编号与其来源表。
