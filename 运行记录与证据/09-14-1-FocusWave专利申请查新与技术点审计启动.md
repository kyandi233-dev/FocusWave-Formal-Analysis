# FocusWave 专利申请查新与技术点审计启动（2026-09-14）

## 1. 任务与状态

状态：`PARTIAL / DIAGNOSTIC_ONLY`。

目标不是直接把比赛报告改写成专利，而是先按“仓库证据 → 发明画像 → 检索式 → 现有技术 → claims-first（以权利要求为中心）对比 → 保护点收束 → 技术交底书”的顺序建立可追溯专利申请底稿。

本记录只登记申请前查新和保护点筛选，不改变现有科研方法、正式分析结论、模型或报告口径。

当前 Formal 权威分支：`kyandi233-dev/FocusWave-Formal-Analysis@codex/code-fix-ledger`。启动时远端最近合并提交为 `4826474157adf72667227fc3f9893e3770e7ef18`（2026-09-13）。

## 2. 采用的开源工作流参考

### 2.1 handsomestWei/patent-disclosure-skill

上游 README 明确把专利工作拆为：项目扫描、专利点挖掘、查新、交底书、框图/结构图、Word 交付、自检与迭代。其 `patent-disclosure` 子技能强调优先国知局公开专利检索，并要求查新信息进入交底材料。

参考：
- https://github.com/handsomestWei/patent-disclosure-skill
- https://github.com/handsomestWei/patent-disclosure-skill/tree/main/skills/patent-disclosure

### 2.2 bb-boy/repo2patent

该仓库明确要求从代码仓库建立 `evidence.json`，再形成 `invention_profile.json`，之后生成检索词、检索 prior art（现有技术）、抓取 Top-K 专利 claims（权利要求），形成 `novelty_matrix.json`，最后才生成 disclosure（交底书）。

本项目采用其关键原则，但不直接复制脚本或结果：
1. 先锁定 FocusWave 当前权威实现和证据；
2. 每个候选技术点必须能回指真实仓库/正式结果；
3. 先比对独立权利要求，再讨论“是否值得申请”；
4. 没有完成 claims 对比前，不写“具备新颖性/创造性”。

参考：https://github.com/bb-boy/repo2patent

## 3. FocusWave 当前可作为专利证据的技术事实

### 3.1 系统与采集实现

`kyandi233-dev/FocusWave@formaltest` 当前正式实验程序同步组织：
- SART（持续性注意反应任务）行为记录；
- NIR（近红外）眼部视频；
- RGB（可见光）视频；
- mmWave（毫米波）雷达；
- 任务事件与各采集线程时间记录。

系统实际包含近红外眼部摄像头、RGB 摄像头、毫米波雷达、940 nm 补光与统一实验程序，不是仅有概念图。

### 3.2 正式数据与当前分析证据

当前 governed cohort 为 61 participant groups、116 sessions、2,320 thought probes（思维探针）。正式结果把行为、眼部、动作、心肺信息映射到共同事件/探针窗口，并在参与者互斥条件下评价预测能力。

正式冻结/纳入的信息包含：
- Behavior：正确 Go RT 中位数、RT-CV、Theil–Sen 趋势、Go omission、No-Go commission；
- Ocular：瞳孔水平、瞳孔波动、瞳孔线性趋势、瞳孔二次曲率、RGB 眨眼频率；
- Movement：body motion energy；
- Cardiopulmonary：毫米波估计心率、呼吸率（仅在当前验证边界内使用，不把纳入资格解释为独立生理效度证明）。

### 3.3 当前特别重要的跨设备依赖事实

现有正式方案已把“科学信息”和“设备来源”分开：例如瞳孔属于 Ocular，但正式瞳孔处理需要 NIR 眼部视频，同时利用 RGB 眨眼事件完成清洗/QC；因此其设备依赖是 NIR + RGB，而不是单设备。RGB 同时可提供眨眼和身体动作信息。

该设备—特征—预处理/QC 的显式依赖关系可能形成系统工程层保护点，但是否具有专利性必须经过现有技术 claims 对比。

## 4. 第一轮候选发明点

以下均为“候选”，不是已确认可授权的发明点。

### P1：非接触多模态持续注意测评系统与方法

候选组合：标准化持续注意任务 + 即时思维探针 + NIR/RGB/mmWave 同步采集 + 统一事件时间轴 + 探针前窗口特征 + 跨参与者状态概率评估。

初步判断：应用完整、证据最多，但现有“多模态认知/注意状态监测”专利较拥挤。若只写“摄像头+雷达+AI 判断专注”，保护强度很可能不足。后续必须把独立权利要求压到更具体的时间锚定、跨设备处理或质量控制机制。

### P2：RGB 眨眼事件辅助 NIR 瞳孔测量的跨模态质量控制

候选组合：
1. NIR 连续测量瞳孔/虹膜区域；
2. RGB 独立检测眨眼事件；
3. 将 RGB 事件映射到统一时间轴；
4. 对 NIR 瞳孔序列按眨眼事件施加前后时间缓冲（当前正式参数 `pre200_post200`）；
5. 在 probe 前 30 s 内按 `2 s × 15 bins` 构建轨迹，bin 内 median，空 bin 不插值；
6. 形成水平、波动与趋势表示，同时保留覆盖率/QC。

初步判断：相较于“直接用瞳孔判断专注”，这是更具体的跨设备测量技术方案，值得作为重点查新对象。但 `200 ms`、`2 s × 15` 等当前研究参数不应未经专利策略审查就写死在独立权利要求中，可放从属权利要求/实施例。

### P3：统一事件时间轴上的严格前序窗口多模态测评

候选组合：由任务事件/探针时刻定义公共端点，各传感器只消费端点之前的合法数据窗口，形成统一的时间语义与可追溯窗口输出，避免探针后信息或不同传感器时间范围混入。

初步判断：这是 FocusWave 的关键工程基础，但“事件对齐+滑动窗口”本身通常较常见。单独申请风险较高，更适合作为 P1/P2 的必要限定特征。

### P4：科学信息与设备依赖解耦的测评配置生成

候选组合：每个预测特征同时登记 scientific modality、source/device namespace、preprocessing dependency、measurement/QC status、temporal legality、coverage；按实际依赖生成可用设备配置和对应模型，不把“某模态”错误等同于“某单设备”。

初步判断：项目治理和可部署性价值高，但容易落入抽象信息组织/软件规则，需要证明其直接作用于实际传感采集、质量控制和可执行设备配置。暂列次级候选。

### P5：毫米波心肺信息参与持续注意评估

候选组合：毫米波非接触估计 HR/BR，与行为/视觉信息在统一探针前窗口内联合形成持续注意状态预测。

初步判断：毫米波 HR/BR 本身已有大量先例；把 HR/BR 加到“注意/疲劳”检测也存在大量先例。当前项目内心肺增量证据也弱，暂不建议把它作为主独立发明点，只作为系统从属组成。

## 5. 第一轮现有技术命中（仅摘要/页面级预检）

以下检索来自公开 Google Patents 页面，当前只完成摘要/页面级预检，不等于正式 claims-first 查新。

### A. 眼部/认知与注意检测

1. `CN117056793A` — Attention level monitoring and predicting method, device, equipment and storage medium
   - 主要点：瞳孔直径预处理、异常值处理、注意/分心预测。
   - 对 FocusWave 的影响：会直接压缩“根据瞳孔预测注意”这类宽泛权利要求空间。

2. `US20240164677A1` — Attention detection
   - 主要点：blink rate、gaze、saccade、pupil radius 等眼部特征用于 focused / mind wandering attentive state。
   - 对 FocusWave 的影响：宽泛“眼部特征→专注/走神状态”的独立权利要求风险高。

3. `US11723568B2` — Mental state monitoring system
   - 主要点：blink rate/variability、pupil size、breathing 等生理信息推断 attention、stress、arousal 等状态。
   - 对 FocusWave 的影响：多生理指标联合推断心理状态也存在较强先例。

4. `CN119625837A` — online learning concentration evaluation combined with formative assessment
   - 主要点：红外眼动/瞳孔/眨眼等多维数据 + 学习过程评价，估计持续/瞬时注意。
   - 对 FocusWave 的影响：教育/专注应用本身不是可依赖的主要新颖点。

### B. 毫米波心肺

1. `CN115736854A` — 毫米波雷达呼吸和心跳监测系统。
2. `CN116602634A/B` — 基于多样性机制的毫米波人体生命体征监测。
3. `CN118592921B` — CNN 融合特征毫米波心率/呼吸率检测。
4. `CN119924797A/B` — 毫米波 HR/BR + 驾驶员图像状态联合监测。

对 FocusWave 的影响：毫米波 HR/BR 的采集、常规滤波/频谱估计、与视觉信息联合用于状态监测都不能假定为新颖。P5 暂不作为主保护点。

## 6. 当前新颖性风险排序（第一轮）

| 候选 | 当前建议 | 主要原因 |
|---|---|---|
| P2 RGB blink → NIR pupil 跨模态 QC | **优先深挖** | 技术链具体，直接解决 NIR 瞳孔受眨眼遮挡/异常影响的问题；目前第一轮未发现完全同构方案 |
| P1 完整非接触多模态持续注意系统 | **保留，但必须收窄** | 项目整体最完整，但宽泛多模态注意检测现有技术密集 |
| P3 严格前序窗口/统一时间轴 | **作为组合限定** | 工程价值高，单独新颖性/创造性可能不足 |
| P4 feature-device-QC dependency 配置机制 | **次级探索** | 可部署性强，但存在抽象规则风险 |
| P5 mmWave HR/BR → 注意 | **不作为主案** | prior art 密集，且当前科研增量证据弱 |

## 7. 当前禁止写入正式交底书的结论

在 claims-first 对比完成前，禁止写：
- “本发明具有新颖性/创造性”；
- “现有技术没有……”；
- “首次……”；
- “独有……”；
- 把科研统计显著性或模型性能直接当成专利创造性依据；
- 把当前具体研究参数（30 s、2 s、200 ms 等）全部硬编码进独立权利要求。

## 8. 下一步唯一优先级

围绕 P2 与收窄后的 P1 建立正式 `invention profile` 和检索式，优先检索：

- `RGB blink event` + `near infrared pupil` + artifact / masking / cleaning / quality control；
- `visible camera blink` + `infrared pupil` + synchronized / timestamp；
- `multimodal sustained attention` + thought probe / self report + pupil / blink / radar；
- `pre-event window` / `pre-probe window` + cognitive state / attention + multimodal sensor。

对 Top-K 结果逐件读取独立权利要求，建立特征矩阵：F1 传感器组合、F2 跨设备事件映射、F3 眨眼缓冲清洗、F4 固定时间轨迹、F5 质量/覆盖输出、F6 注意任务/探针锚点、F7 非接触多模态状态估计。

只有该矩阵完成后，才决定是否拆成一件主案 + 一件分案/第二申请，或只保留一件收窄主案。
