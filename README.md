# FocusWave 正式分析与报告证据库

更新日期：2026-09-13。

本仓库是 FocusWave 当前分析计划、研究决策、协作治理、国赛报告规范与证据映射的权威入口。可执行分析代码维护在对应代码仓库；本仓库保存方法合同、状态裁决、报告草稿、运行证据与来源追踪。历史方案继续保留，但与后出的正式决策冲突时，以当前 `codex/code-fix-ledger`、对应代码分支和真实运行输出为准。

## 先看这里

当前恢复项目上下文时，建议按以下顺序读取：

1. [`分析设计/1.16-state-snapshot-20260913.md`](分析设计/1.16-state-snapshot-20260913.md)：当前单模态科学输出、Ocular 收口、Movement P4、毫米波停放状态与停止点的快速快照。
2. [`分析设计/1.16.12-单模态科研输出绘图与特征交接计划_20260913.md`](分析设计/1.16.12-单模态科研输出绘图与特征交接计划_20260913.md)：当前 Behavior / Ocular / Movement science-output（科学输出）总合同。
3. [`分析设计/1.16.14-Ocular_G1完成后参数冻结与补充审计状态_20260913.md`](分析设计/1.16.14-Ocular_G1完成后参数冻结与补充审计状态_20260913.md)：Ocular G1 真实运行后已经冻结和仍待冻结的参数。
4. [`分析设计/1.16.15-Movement单模态科学输出实现与Ocular交叉审计状态_20260913.md`](分析设计/1.16.15-Movement单模态科学输出实现与Ocular交叉审计状态_20260913.md)：P4 Movement 与 Ocular×Movement 伪迹敏感性审计。
5. [`分析设计/1.16.16-Ocular科学特征交接接口与P4协同收口状态_20260913.md`](分析设计/1.16.16-Ocular科学特征交接接口与P4协同收口状态_20260913.md)：post-G1 Ocular handoff（特征交接）接口和当前停止边界。
6. [`分析设计/1.16-当前方法总状态与执行入口_20260912.md`](分析设计/1.16-当前方法总状态与执行入口_20260912.md)：1.16 主方法形成与监督学习协议的上位背景。该文件仍是方法总入口，但具体单模态执行状态应同时读取上面的 9 月 13 日文件。

## 当前权威仓库与代码线

| 职责 | 当前入口 |
|---|---|
| 正式实验程序 | `kyandi233-dev/FocusWave@formaltest` |
| Formal 方法、治理、报告 | `kyandi233-dev/FocusWave-Formal-Analysis@codex/code-fix-ledger` |
| Behavior / Ocular / Movement 下游分析 | `kyandi233-dev/Attention-Analysis` |
| 科学模态 / 设备命名迁移与 P4/P3 handoff | `Attention-Analysis@codex/1.16.10-modality-device-separation`，当前核验 HEAD `d4d52e8974a674ad442bf7b8fd6adc20a69106cd` |
| Ocular G1 supplemental freeze evidence（补充冻结证据） | `Attention-Analysis@codex/nir-g1-summary-hardening`，当前核验 HEAD `9b9a0ec170ab7e54198293bed181b134e492f4bc` |
| mmWave（毫米波）与多模态外部 producer | `greenboo26/focuswave-multimodal-attention-analysis` |

`Attention-Analysis@codex/formal-analysis-v2-portable` 仍是长期正式基础线，但当前代码事实不能只看基础分支；P4 Movement、post-G1 Ocular handoff 和 G1 补充汇总必须读取上表对应开发分支。

## 当前队列与分析单位

当前 governed cohort（治理队列）为 **116 sessions（场次）、61 participant groups（参与者组）**，Behavior 权威 probe（思维探针）总数为 **2,320**。`participant_group_id` 是重复测量推断、bootstrap（自助法）和 participant-disjoint prediction（参与者互斥预测）的统一参与者键。

模态 availability（可用性）与 cohort membership（队列成员资格）必须分开。NIR、RGB 或 mmWave 缺失不得反向改变 Behavior 总体队列。历史 `44/38/6` 与更早 `115/61/11` 不再作为当前总体样本口径；旧数字只在对应历史工程审计中保留 provenance（来源追踪）意义。

## 当前研究阶段

当前已经不是继续扩大 A/B/C/D 并行开发或直接跑真实多模态模型的阶段。当前主任务是：

`single-modal producer（单模态生产端）`
→ `measurement/QC + scientific analysis（测量审计、质量控制与单模态科学分析）`
→ `Behavior / Ocular / Movement feature handoff`
→ `研究者冻结少量剩余表示`
→ **STOP**。

只有完成研究者最终冻结后，才能继续物化真实 feature registry（特征登记表）、运行参与者互斥 LOSO（留一参与者）监督学习和多模态增量比较。

Q1/Q2 与单模态指标的关系可以作为正式科学结果；Q1/Q2 显著性、outer-test（外层测试）表现或全样本预测结果不能作为“看到效果就选特征”的冻结规则。

## Behavior 当前状态

Behavior producer 不重跑。当前本地 `FormalScience/Behavior/` 已有正式科学输出，覆盖 **61 名参与者、116 场、2,320 probes**。

当前核心科学维度为：

- RT level（反应时水平）；
- RT variability（反应时波动）；
- RT trend（反应时趋势）；
- Go omission（Go 遗漏）；
- No-Go commission（No-Go 抑制错误）。

RT-CV、Theil–Sen slope、raw Go omission 和 commission 已有明确科学角色；RT mean/median 的最终统一表示仍保留研究者冻结边界。当前 Behavior handoff 已存在，但 handoff 接口存在不等于最终 feature registry 已经冻结。

## Ocular 当前状态

G1 权威真实运行 `NIR_G1_20260912_fixed` 已完成：**109 / 109 / 0**。唯一 RGB blink source unavailable（RGB 眨眼来源不可用）为 `sub-041`，其 NIR-only（仅近红外）测量继续保留；缺失 RGB 保持 missing，不能解释为 zero blink（零眨眼）。

当前已经冻结：

- blink buffer（眨眼缓冲）：`pre200_post200`；
- fixed bin（固定时间箱）：`2 s × 15 bins`，主窗口为 probe 前 30 s；
- bin 内 median（中位数），空 bin 不插值；
- `nir_qc_only` 与 `rgb_plus_nir_qc + pre200_post200` 的 cleaning-track（清洗轨道）角色。

仍待研究者冻结：geometry（几何瞳孔）与 hard `R_seg`（硬分割瞳孔/虹膜比例）的最终角色、SD（标准差）与 MAD（中位数绝对偏差）的波动表示角色、trend temporal span（趋势最低真实时间跨度）。

`FormalScience/Ocular/` 和 `ocular_feature_handoff.csv` 的代码接口已经实现，但真实物化仍必须读取本机权威 G1 大表；云盘没有大表不是重跑 G1 的理由。

## Movement 当前状态

RGB 是 source/device namespace（来源/设备命名空间），不是科学模态。P4 Movement 当前第一轮组织为：

- `body_motion_energy_median`：Movement 主候选；
- pose lateral / vertical（横向 / 纵向姿态）：辅助或 sensitivity（敏感性）；
- radial proximity proxy（径向接近代理）：QC / sensitivity，仅为无量纲代理，不解释为真实物理位移；
- blink（眨眼）：归入 Ocular；
- exposure / coverage（曝光 / 覆盖率）：device-support / QC。

既有 RGB 5.5 真实运行已有 **116 场治理骨架、115 场视频、2,320 个严格 probe 前 30 s 窗口**。P4 science-output builder（科学输出构建器）不重跑视频 producer，而消费已有表和参与者聚类统计。

`FormalScience/Movement/`、`movement_feature_handoff.csv` 和 Ocular×Movement artifact-sensitivity audit（伪迹敏感性审计）代码已经实现；真实本地 materialization（物化）仍待用既有 RGB 5.5 大表和 G1 `probe_measurement_candidates.csv` 完成。

## 毫米波当前状态

毫米波相关历史 `44 场 / 39 场可加载` 仅代表早期工程输入审计，不再代表当前 governed cohort。当前分析设计中的 integration snapshot（集成快照）保留 116 场 / 2,320 probes 的总体骨架，心肺候选特征仍处于 physiology-limited（生理验证受限）状态。

另有隔离 Formal 状态同步分支：

`codex/mmwave-formal-state-sync-v1`  
远端 HEAD：`8f9bb62593b440e88b42ffd0d047bfd12c4b90e9`

该分支当前**尚未合入** `codex/code-fix-ledger`，只修改 3 份 `分析设计/` 文档，没有代码、数据或 `01_管理/` 改动。当前停放状态：

- `FORMAL_MMWAVE_STATE_SYNC = PARTIAL`；
- `BRANCH_ISOLATION = DONE`；
- `MERGE = NOT_YET`；
- `TRACEABILITY_SYNC = PENDING`。

其中的重要待合并边界是：`MAIN_ANALYSIS = PROCEED` 不等于正式毫米波 predictor 已通过 producer-side time-legality（生产端时间合法性）；`MMWAVE_INTEGRATION = READY` 也不能单独视为 `verified_pre_probe_only`。1.15.8 的治理角色已被后续方法 superseded（取代），但其中技术问题仍是 `NOT_VERIFIED_CLOSED`，不能写成 resolved（已解决）。

在该隔离分支完成 rebase / PR / merge 前，上述内容属于待合并状态同步，不得反向改写当前权威正文。

## 当前真实执行顺序

1. 不重跑 Behavior producer、RGB producer 或 NIR G1；
2. 用本机现有 RGB 5.5 + G1 权威大表物化 `FormalScience/Movement`；
3. 完成 Ocular×Movement 交叉伪迹审计；
4. 物化 `FormalScience/Ocular` 并结合 G1 supplemental summary（补充汇总）冻结 trend temporal span；
5. 研究者冻结 Behavior / Ocular / Movement 的少量剩余表示；
6. 到此停止，不自动生成 final feature registry，不启动真实多模态 fit；
7. 毫米波状态同步分支独立等待 `codex/code-fix-ledger` 稳定后再 rebase / PR，`TRACEABILITY_SYNC` 在其合入后另做。

## 目录导航

- [`分析设计/README.md`](分析设计/README.md)：方法设计与历史演变。
- [`协作治理/`](协作治理/)：分支、issue、PR 和修复任务治理。
- [`行为分析/`](行为分析/)：Behavior 方法、结果与证据。
- [`NIR分析/`](NIR分析/)：NIR/Ocular producer、测量与 G1 证据。
- [`RGB分析/`](RGB分析/)：RGB producer、动作/眨眼来源与技术证据。
- [`毫米波分析/README.md`](毫米波分析/README.md)：毫米波历史工程审计与当前状态边界。
- [`跨模态融合/`](跨模态融合/)：统一键、共同集合与后续多模态接口。
- [`国赛报告/`](国赛报告/)：当前新版报告工作区。
- [`正式报告/`](正式报告/)：历史报告与写作/统计/版式规范来源。
- [`运行记录与证据/`](运行记录与证据/)：真实运行命令、环境、失败和验收证据。

## 证据边界

代码存在、接口实现、CI（持续集成）通过、配置声明和文档计划都不等于真实科学结果已经产生。正式结果必须基于当前 governed cohort、当前代码/配置、真实运行输出及对应 QC 分母形成。任何仍待本地 materialization、研究者冻结、PR 合并或 traceability sync（追溯同步）的内容，都必须保持为 pending（待完成）状态。