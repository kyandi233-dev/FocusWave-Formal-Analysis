# Movement 动作结果与资产

本文件记录 Movement（动作）P4 当前已经冻结的科学结果、正式源表、全部图件和证据路径。动作科学信息来自 RGB 可见光视频，但科学解释对象是**整体身体动作与姿态变化**，不是摄像设备本身；曝光、亮度和全局画面变化只作为测量质量信息。

## 1. 当前证据身份

**P4 已正式关闭。** 当前 Movement 已完成：

- 第一轮主要动作表示冻结；
- 真实数据覆盖核验；
- Block 间与 Block 内任务进程结果；
- Q1/Q2 解释性模型；
- 与近期行为的窗口级关系；
- 姿态方向敏感性分析；
- 13 张科研图生成、审计和字体可读性验证；
- 4 张报告模型源表随 final bundle 交付。

因此本模块包含**正式结果 + 敏感性结果 + QC**。

## 2. 样本与主要动作表示

正式总体：61 名参与者、116 个实验场次、2,320 个思维探针。

第一轮 Movement 正式科学特征为**整体身体动作强度中位数**。它是无量纲相对指标，用于概括探针前窗口内“整体动得多还是少”，不能解释为真实物理位移、速度或能量。

| 指标/候选 | 有限值 / 2,320 | 参与者 | 场次 | 科学角色 |
|---|---:|---:|---:|---|
| 整体身体动作强度 | 2,300 | 61 | 115 | 第一轮正式主指标 |
| 横向姿态方向 | 2,300 | 61 | 115 | 敏感性辅助 |
| 纵向姿态方向 | 2,300 | 61 | 115 | 敏感性辅助 |
| 相对径向方向分数 | 2,300 | 61 | 115 | QC / 敏感性；不解释为真实靠近/远离 |
| 曝光变化 | 2,300 | 61 | 115 | 设备 QC |
| 全局画面运动 | 2,300 | 61 | 115 | 设备 QC |
| 画面平均亮度 | 2,300 | 61 | 115 | 设备 QC |

主指标探针级覆盖率为 99.14%。唯一缺失场次没有造成参与者层面的整体丢失，全部 61 名参与者均保留至少一个有效动作场次。

## 3. 任务进程结果

每个正式 Block 包含 24 个 cycle，每个 cycle 包含 18 个连续试次。为描述 Block 内从早到晚的任务进程，每 4 个连续 cycle 合并为一个阶段，因此每个 Block 形成 6 个连续任务阶段。

正式参与者聚类 GEE 结果中：

- B1 内每向后推进一个任务阶段，整体身体动作强度平均下降：**B = −0.000164，SE = 0.000069，95% CI [−0.000298, −0.000029]**；
- B2 相对于 B1 的阶段斜率差异：**B = 0.000167，SE = 0.000092，95% CI [−0.000012, 0.000347]**。

因此当前结果支持第一个区块内部存在幅度较小的动作下降，但没有明确证据说明 B2 的任务阶段斜率稳定不同于 B1。

注意：模型中的 Block 主效应对应未观测的 `cycle_bin=0` 外推位置，因此不用于解释“B2 相对 B1 的总体水平差异”。Block 总体变化应看参与者级 B1/B2 配对图和相应汇总，而不是直接解释该模型主效应。

## 4. Movement 与 Q1 的关系

Q1 以 Q1=1“聚焦当前分类任务”为参照。整体身体动作强度标准化后进入参与者聚类稳健多项逻辑回归：

| Q1 对比 | 标准化系数 B | 95% CI | 解释 |
|---|---:|---|---|
| Q1=2 vs Q1=1 | 0.013 | [−0.211, 0.236] | 区间跨 0 |
| Q1=3 vs Q1=1 | −0.392 | [−0.888, 0.103] | 区间跨 0 |
| Q1=4 vs Q1=1 | 0.244 | [−0.318, 0.807] | 区间跨 0 |

三个区间均跨 0，因此当前数据没有显示**整体身体动作强度**与某一种 Q1 注意内容存在稳定的总体对应关系。

### 4.1 姿态方向敏感性结果

- 横向向右方向指标与 Q1=2 vs Q1=1 呈负向关系：**B = −0.119，95% CI [−0.219, −0.019]**；
- 纵向向上方向指标与 Q1=4 vs Q1=1 呈负向关系：**B = −0.220，95% CI [−0.422, −0.018]**。

这些关系属于敏感性结果。姿态方向的正负值只描述视频坐标中的相对方向，不预先等同于“更专注/更不专注”。

## 5. Movement 与 Q2 的关系

Q2 采用参与者聚类的有序 GEE。整体身体动作强度结果：

- **B = 0.054，SE = 0.088，95% CI [−0.118, 0.225]**。

区间跨 0，当前没有显示整体动作强度与主观警觉等级存在稳定总体关系。姿态辅助指标对 Q2 的区间也均跨 0。

## 6. Movement 与近期行为的关系

窗口级行为对应模型以**动作指标为结果变量**、近期行为指标为标准化预测变量。系数不是因果效应，也不能反向解释为“动作增加导致行为变差”。

整体身体动作强度与主要近期行为指标的 95% CI 均跨 0：

| 行为预测变量 | B | 95% CI |
|---|---:|---|
| 正确 Go RT 中位数 | 0.00236 | [−0.00251, 0.00723] |
| Go omission | −0.00206 | [−0.00684, 0.00273] |
| No-Go commission | 0.00055 | [−0.00355, 0.00465] |

RT-CV 与 d′ 同样没有显示整体身体动作强度的稳定线性对应。

姿态敏感性中：

- Go omission 越高，横向向右方向分数越高：B = 3.04×10⁻⁵，95% CI [7.81×10⁻⁶, 5.31×10⁻⁵]；
- d′ 越高，横向向右方向分数越低：B = −4.50×10⁻⁵，95% CI [−8.26×10⁻⁵, −7.51×10⁻⁶]；
- 正确 Go RT 中位数越高，相对径向方向分数越低：B = −0.0101，95% CI [−0.0195, −0.0007]。

这些结果不改变整体身体动作强度的第一轮主指标地位。

## 7. 正式输入资产

### 7.1 RGB 5.5 根目录

`D:\Project\厚粲杯\11_数据\_FormalAnalysis\RGB\21_analysis_tables_5.5\`

核心探针表：

`D:\Project\厚粲杯\11_数据\_FormalAnalysis\RGB\21_analysis_tables_5.5\tables\rgb_probe_pre30s_strict_features.csv`

该表提供 2,320 个探针前严格窗口的 RGB 动作/姿态/曝光等特征。

### 7.2 既有模型源表

Movement P4 不重新拟合 RGB producer 模型，而是把既有 RGB 5.5 结果按 Movement 科学角色重新物化。主要源表：

| RGB 5.5 源表 | 原始行数 | Movement 使用行数 | 用途 |
|---|---:|---:|---|
| `models/rgb_block_cycle_gee.csv` | 24 | 16 | 任务进程 |
| `models/rgb_q1_mnlogit.csv` | 18 | 12 | Q1 关系 |
| `models/rgb_q2_ordinal_gee.csv` | 6 | 4 | Q2 关系 |
| `models/rgb_behavior_window_gee.csv` | 30 | 20 | 动作与近期行为关系 |
| `models/rgb_probe_within_between.csv` | 13,920 | 9,280 | 人内/人间分解支持表 |

### 7.3 Ocular 交叉伪迹输入

Movement P4 还读取：

`D:\Project\厚粲杯\11_数据\_FormalAnalysis\NIR_G1\NIR_G1_20260912_fixed\probe_measurement_candidates.csv`

仅用于生成 Ocular × Movement 交叉伪迹敏感性审计，不用于选择 Movement 主科学指标。

## 8. Movement 正式输出根目录

`D:\Project\厚粲杯\11_数据\_FormalAnalysis\FormalScience\Movement\`

### 8.1 正式/报告源表

| 文件 | 行数/规模 | 用途 | 报告地位 |
|---|---:|---|---|
| `tables/movement_task_progression.csv` | 16 行 | Block × task-stage GEE 的 estimate、SE、95% CI | 正式结果源表 |
| `tables/movement_q1_models.csv` | 12 行 | Q1 多项逻辑回归标准化系数、SE、CI | 正式结果源表 |
| `tables/movement_q2_models.csv` | 4 行 | Q2 有序 GEE 标准化系数、SE、CI | 正式结果源表 |
| `tables/movement_behavior_links.csv` | 20 行 | 动作结果变量与近期行为标准化预测变量的 GEE | 正式/敏感性结果源表 |
| `tables/movement_feature_handoff.csv` | 候选清单 | 特征角色、单位、设备依赖、时间合法性 | 后续 registry 输入 |
| `tables/movement_feature_coverage.csv` | 覆盖摘要 | 每个候选 finite probe / participant / session | 5.1 / QC |
| `tables/movement_probe_descriptive_source.csv` | 探针级 | 正式图件的探针级描述数据源 | 图件源表 |
| `tables/ocular_cross_artifact_audit.csv` | 240 行 | Ocular × Movement 伪迹敏感性 | sensitivity only |

另有 local-only 较大源表：

- `movement_within_between.csv`，约 1.4 MB；
- `rgb_block_cycle_source.csv`，约 524 KB；
- `rgb_session_coverage_source.csv`；
- 各图件源表。

它们保留在本地，不在 GitHub 重复复制全文。

### 8.2 manifests

| 文件 | 用途 |
|---|---|
| `manifests/figure_manifest.csv` | 13 张图的路径、科学问题、图件角色与源表 |
| `manifests/figure_audit.csv` | 图件 generated/not_estimable、标题、格式等审计 |
| `movement_science_output_manifest.json` | Movement 输出状态、主候选角色和停止线 |

## 9. 全部 13 张 Movement 图件

所有 13 张图均：

- `generated`；
- PNG 300 dpi；
- 同时存在 SVG；
- 图内无完整标题；
- 中文字体可读；
- 没有 glyph missing 警告。

| figure_id / 文件 | 分区 | 用途 | 是否建议正文主图 |
|---|---|---|---|
| `movement_primary_distribution` | qualification | 主动作指标总体分布 | 可选，通常补充 |
| `movement_block_pair_task_progression` | main | B1/B2 配对 + 6 阶段任务进程 | **是；5.4 已使用** |
| `movement_exposure_qc` | qc | 曝光变化与测量条件 | 否，QC |
| `movement_pose_direction_distribution` | sensitivity | 姿态方向分布 | 否，补充 |
| `movement_source_coverage` | qc | Movement 输入覆盖率 | 5.1 可用表代替 |
| `movement_task_progression_coefficients` | main | 主动作指标任务进程系数 | 可选；与主轨迹图二选一或组合 |
| `movement_task_progression_coefficients_pose_sensitivity` | sensitivity | 姿态任务进程敏感性 | 否，补充 |
| `movement_q1_relationships` | main | 主动作指标与 Q1 | 可选；正文目前用紧凑表 |
| `movement_q1_relationships_pose_sensitivity` | sensitivity | 姿态与 Q1 | 否，补充 |
| `movement_q2_relationships` | main | 主动作指标与 Q2 | 可选；正文目前用紧凑表 |
| `movement_q2_relationships_pose_sensitivity` | sensitivity | 姿态与 Q2 | 否，补充 |
| `movement_behavior_relationships` | sensitivity | 动作主指标与近期行为 | 可放补充 |
| `movement_behavior_relationships_pose_sensitivity` | sensitivity | 姿态与近期行为 | 否，补充 |

本地图片目录：

- `D:\Project\厚粲杯\11_数据\_FormalAnalysis\FormalScience\Movement\figures\main\`
- `...\figures\qualification\`
- `...\figures\sensitivity\`
- `...\figures\qc\`

对应 SVG 与 PNG 同名存放。

## 10. Google Drive 最终证据

当前 Movement 权威 bundle：

**`_AI_HANDOFF/2026-09-13_p4-movement-final-6955ad9/`**  
https://drive.google.com/drive/folders/1RhP38Im0kKDFv2g-q7e4_nzIP8QpGrpM

HANDOFF：  
https://drive.google.com/file/d/1W_AJ1znSzOF2XmqsftkTFOtv6W5a-KWO/view

运行/manifest 日志：  
https://drive.google.com/file/d/16fpl0mIRDVujSCDcWGzj8Aw5ZpC6s_NN/view

bundle 当前包含：

- `HANDOFF.md`；
- `movement_science_output_manifest.json`；
- `figure_manifest.csv`、`figure_audit.csv`；
- `movement_feature_handoff.csv`、`movement_feature_coverage.csv`；
- 五张核心 PNG：
  - `movement_primary_distribution.png`
  - `movement_block_pair_task_progression.png`
  - `movement_q1_relationships.png`
  - `movement_q2_relationships.png`
  - `movement_exposure_qc.png`
- 四张正式报告源表：
  - `movement_task_progression.csv`
  - `movement_q1_models.csv`
  - `movement_q2_models.csv`
  - `movement_behavior_links.csv`
- `movement_font_patch_final.diff`；
- CJK rendering regression test；
- `movement_build_final.log`；
- `bundle_manifest.csv`。

其余 8 张 PNG、13 张 SVG、较大源表和图件源表保留在本地；Drive bundle 通过 `rclone check --checksum` 校验。

历史证据仍保留：

- `2026-09-13_p4-movement-real-materialization-ed2e9dc/`
- `2026-09-13_p4-movement-font-patch-ed2e9dc/`

它们分别记录字体缺陷发现和字体修补过程，不再作为最终 P4 科学证据入口。

## 11. GitHub 方法与代码来源

- 分析仓库：`kyandi233-dev/Attention-Analysis`
- Movement final evidence：`codex/1.16.10-modality-device-separation @ 6955ad9c91929a9c991847e5d057e03ff1002ecc`
- 当前正式结果方法：`国赛报告/章节草稿/4.4-科学变量形成、窗口化与质量控制.md`、`4.5-解释性统计与主观信息关联分析.md`
- 当前结果正文：`国赛报告/章节草稿/5.4-动作与注意相关状态_20260913.md`

## 12. 已知边界

1. `body_motion_energy_median` 的**研究决策已经冻结**，但 unified feature registry 尚未在本 P4 bundle 中物化；不能把 `registry_ready=false` 的历史字段误解为科学决策仍未完成。
2. pose direction 的少量非零关系是敏感性结果，不用于按显著性事后选特征。
3. exposure、global motion、gray mean 均为设备/成像 QC，不作为注意相关科学指标。
4. 当前 Movement 结果是解释性科学结果，不等于跨参与者预测性能；正式监督学习必须在后续独立模块报告。
