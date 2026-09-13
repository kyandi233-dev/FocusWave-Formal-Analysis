# 附录 C　行为完整结果附表

对应正文第 5 章。本附录只登记**聚合表**；逐探针预测、逐折审计与行级大表按仓库规则保留本地，
路径与 SHA-256 在各任务 manifest 与 `完整结果/` 中登记。

数据来源：`Behavior/formal_v3/`、`FormalScience/Behavior/tables/`
生成方式：由源表直接转换为 Markdown 表，未手工转录、未重新拟合任何模型。

---

## C.1 两个正式区块之间的行为变化（参与者聚类自助置信区间）

来源文件：`b1_b2_participant_cluster_bootstrap.csv`（15 行）

| metric | estimate_b2_minus_b1 | bootstrap_se | ci_low | ci_high | participant_group_n | session_pair_n | bootstrap_iterations | status |
|---|---|---|---|---|---|---|---|---|
| beta | 0.0678221 | 0.0575237 | -0.017982 | 0.198145 | 61 | 116 | 20000 | estimable |
| clean_go_omission_rate | 0.00181794 | 0.00412768 | -0.00682349 | 0.00987956 | 61 | 116 | 20000 | estimable |
| commission_rate | -0.0128358 | 0.0146271 | -0.0422366 | 0.0150842 | 61 | 116 | 20000 | estimable |
| criterion_c | 0.025629 | 0.0309725 | -0.0359081 | 0.0853645 | 61 | 116 | 20000 | estimable |
| dprime_loglinear | -0.0111335 | 0.0650055 | -0.139655 | 0.115518 | 61 | 116 | 20000 | estimable |
| go_correct_rt_cv | 0.0289191 | 0.0121941 | 0.00680405 | 0.0547534 | 61 | 116 | 20000 | estimable |
| go_correct_rt_iqr_ms | 6.52254 | 7.46987 | -6.76864 | 22.5323 | 61 | 116 | 20000 | estimable |
| go_correct_rt_mad_ms | 0.907826 | 1.50552 | -2.14518 | 3.79021 | 61 | 116 | 20000 | estimable |
| go_correct_rt_mean_ms | -2.12385 | 4.41818 | -10.2541 | 7.07639 | 61 | 116 | 20000 | estimable |
| go_correct_rt_median_ms | -3.96443 | 4.87955 | -12.5685 | 6.51348 | 61 | 116 | 20000 | estimable |
| go_correct_rt_sd_ms | 8.90605 | 4.00159 | 1.40959 | 17.2175 | 61 | 116 | 20000 | estimable |
| go_correct_rt_theilsen_slope_ms_per_s | -0.00373642 | 0.0164913 | -0.038078 | 0.0260886 | 61 | 116 | 20000 | estimable |
| omission_rate | 0.00479921 | 0.00441361 | -0.00410565 | 0.0133197 | 61 | 116 | 20000 | estimable |
| raw_go_omission_rate | 0.00479921 | 0.00437383 | -0.00415528 | 0.0132628 | 61 | 116 | 20000 | estimable |
| timing_ambiguous_go_omission_rate | 0.00298127 | 0.00106173 | 0.00106728 | 0.00523679 | 61 | 116 | 20000 | estimable |

注：效应为「区块 2 − 区块 1」。区间为参与者整簇自助百分位区间（20,000 次）。区间跨 0 表示没有可分辨的区块间差异。

## C.2 错误事件前后正确 Go 反应时相对参与者自身水平的变化

来源文件：`error_trajectory_summary.csv`（14 行）

| error_type | relative_trial | participant_group_n | session_n | error_event_n | participant_centered_rt_mean_ms | participant_centered_rt_sem_ms | observation_unit |
|---|---|---|---|---|---|---|---|
| go_omission | -3 | 54 | 93 | 1944 | 32.8002 | 15.1498 | participant_group_summary |
| go_omission | -2 | 54 | 93 | 1949 | 48.8361 | 12.3261 | participant_group_summary |
| go_omission | -1 | 54 | 93 | 1955 | 76.5981 | 19.2491 | participant_group_summary |
| go_omission | 0 | 54 | 93 | 1957 | — | — | participant_group_summary |
| go_omission | 1 | 54 | 93 | 1951 | -38.263 | 10.7205 | participant_group_summary |
| go_omission | 2 | 54 | 93 | 1945 | 6.70365 | 7.12399 | participant_group_summary |
| go_omission | 3 | 54 | 93 | 1941 | 10.3278 | 7.62514 | participant_group_summary |
| nogo_commission | -3 | 61 | 116 | 3724 | 4.41735 | 5.27986 | participant_group_summary |
| nogo_commission | -2 | 61 | 116 | 3724 | 8.64617 | 4.9675 | participant_group_summary |
| nogo_commission | -1 | 61 | 116 | 3724 | 9.65793 | 4.97979 | participant_group_summary |
| nogo_commission | 0 | 61 | 116 | 3724 | — | — | participant_group_summary |
| nogo_commission | 1 | 61 | 116 | 3724 | -6.13019 | 9.14123 | participant_group_summary |
| nogo_commission | 2 | 61 | 116 | 3724 | -18.2724 | 7.10737 | participant_group_summary |
| nogo_commission | 3 | 61 | 116 | 3724 | -6.60116 | 6.97993 | participant_group_summary |

注：相对位置 0 为错误事件本身，该试次没有正确 Go 反应时，因此无估计值。「参与者/场次」为该错误类型至少出现一次事件的组级计数，不等于每个位置的估计分母；「事件数」为该相对位置上的事件行数，也不等于可用反应时数。标准误为正式输出；**本节不提供正式置信区间**，正文的近似区间按 估计 ± 1.96 × 标准误 计算。

## C.3 行为指标的有效覆盖

来源文件：`behavior_feature_coverage.csv`（12 行）

| predictor_column | display_name | report_role | coverage_summary |
|---|---|---|---|
| go_correct_rt_mean_ms | RT level (mean) | primary_candidate | {"finite_fraction": 0.9991379310344828, "finite_probe_n": 2318, "participant_group_n": 61, "probe_total_n": 2320, "session_n": 116} |
| go_correct_rt_median_ms | RT level (median) | primary_candidate | {"finite_fraction": 0.9991379310344828, "finite_probe_n": 2318, "participant_group_n": 61, "probe_total_n": 2320, "session_n": 116} |
| go_correct_rt_cv | RT variability (CV) | primary | {"finite_fraction": 0.9991379310344828, "finite_probe_n": 2318, "participant_group_n": 61, "probe_total_n": 2320, "session_n": 116} |
| go_correct_rt_theilsen_slope_ms_per_s | RT trend (Theil-Sen slope) | primary | {"finite_fraction": 0.9982758620689656, "finite_probe_n": 2316, "participant_group_n": 61, "probe_total_n": 2320, "session_n": 116} |
| raw_go_omission_rate | Go omission rate | primary | {"finite_fraction": 1.0, "finite_probe_n": 2320, "participant_group_n": 61, "probe_total_n": 2320, "session_n": 116} |
| commission_rate | No-Go commission rate | primary | {"finite_fraction": 1.0, "finite_probe_n": 2320, "participant_group_n": 61, "probe_total_n": 2320, "session_n": 116} |
| go_correct_rt_sd_ms | RT variability (SD) | sensitivity | {"finite_fraction": 0.9991379310344828, "finite_probe_n": 2318, "participant_group_n": 61, "probe_total_n": 2320, "session_n": 116} |
| go_correct_rt_mad_ms | RT variability (MAD) | sensitivity | {"finite_fraction": 0.9991379310344828, "finite_probe_n": 2318, "participant_group_n": 61, "probe_total_n": 2320, "session_n": 116} |
| go_correct_rt_iqr_ms | RT variability (IQR) | sensitivity | {"finite_fraction": 0.9991379310344828, "finite_probe_n": 2318, "participant_group_n": 61, "probe_total_n": 2320, "session_n": 116} |
| dprime_loglinear | Loglinear d-prime | sensitivity | {"finite_fraction": 1.0, "finite_probe_n": 2320, "participant_group_n": 61, "probe_total_n": 2320, "session_n": 116} |
| clean_go_omission_rate | Go omission without detected timing ambiguity | qc_sensitivity | {"finite_fraction": 1.0, "finite_probe_n": 2320, "participant_group_n": 61, "probe_total_n": 2320, "session_n": 116} |
| timing_ambiguous_go_omission_rate | Timing-ambiguous Go omission | qc_sensitivity | {"finite_fraction": 1.0, "finite_probe_n": 2320, "participant_group_n": 61, "probe_total_n": 2320, "session_n": 116} |

注：`coverage_summary` 为 JSON，含 `finite_probe_n`、`finite_fraction`、`participant_group_n`、`session_n`、`probe_total_n`。

---

**写作边界**：本附表内容不得改写为正文结论；正文只引用附录编号与其来源表。不同分析集合的分母不同，**不得跨集合比较优劣**。
