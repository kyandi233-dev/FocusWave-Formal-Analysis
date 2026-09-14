# FocusWave 专利 claims-first 初筛与候选重排（2026-09-14）

状态：`PARTIAL / DIAGNOSTIC_ONLY`。

本记录承接 `09-14-1-FocusWave专利申请查新与技术点审计启动.md`。本轮不再只看摘要，而开始读取高相关专利的独立权利要求与具体实施段落，并据此重排候选保护点。

## 1. 关键新发现：P2 不能再按“明显最优先”处理

原 P2 是“RGB 眨眼事件辅助 NIR 瞳孔测量的跨模态质量控制”。本轮发现至少两组非常接近的在先技术：

### 1.1 US6090051A / WO2000054654A1

标题：Method and apparatus for eye tracking and monitoring pupil dilation to evaluate cognitive activity。

其说明书已经明确：
- 眨眼会使瞳孔测量记录出现零值；
- 眨眼前后因眼睑部分遮挡会产生异常小的瞳孔值；
- 预处理可删除眨眼本身，并删除眨眼两侧额外观测点中的极端值。

其独立权利要求 1 已覆盖“监测任务中的瞳孔反应 → 记录 → 信号分析 → 作为认知活动测量”的宽泛框架。

影响：
- “因眨眼删除瞳孔数据并在前后设置缓冲”本身不能作为 FocusWave 的核心新颖点；
- `pre200_post200` 只能视为项目实现参数，不能据此主张创造性。

公开来源：
https://patents.google.com/patent/US6090051A/en

### 1.2 US20210321876A1

标题：System and method for imaging, segmentation, temporal and spatial tracking, and analysis of visible and infrared images of ocular surface and eye adnexa。

独立权利要求 1 明确覆盖：
- 同时采集 IR 和 visible light 眼部图像；
- 监测 eye tracking 和 eye blinking；
- 识别并移除 visible frame 及其对应 IR frame 中的 artefacts；
- 通过保持同步提高测量准确性。

独立权利要求 11 给出对应的方法权利要求。

影响：
- “可见光相机 + 红外相机同步 → 用眨眼/运动信息剔除对应红外测量伪迹”已经有非常接近的 claims；
- FocusWave 的 P2 若只写“RGB 检出眨眼，然后屏蔽 NIR 瞳孔数据”，专利空间明显不足；
- P2 只有在加入其他非显而易见且有真实实现证据的限制时才值得继续，例如：特定注意测评事件锚定、严格前序窗口、独立设备来源及测量质量/覆盖输出之间的联动。但这些组合是否足够创造性仍未确认。

公开来源：
https://patents.google.com/patent/US20210321876A1/en

## 2. P1 同样受到强在先技术约束

原 P1：标准化持续注意任务 + 思维探针 + NIR/RGB/mmWave + 探针前窗口 + 跨参与者状态预测。

### 2.1 EP4552569A1 — Mind wandering detection device, system and method

其公开内容已经使用 thought probes（思维探针）作为 task focus / mind wandering 标签，并分析探针前约 15 s 的生理/神经标记；还讨论以探针前时段建立检测阈值/模型。

影响：
- “思维探针为前序生理窗口提供标签”本身不是 FocusWave 可依赖的新颖点。

公开来源：
https://patents.google.com/patent/EP4552569A1/en

### 2.2 WO2021247310A1 / EP4161387B1 — Sound-based attentive state assessment

其公开内容已经描述：
- 在体验过程中随机询问用户有多 focused / relaxed；
- 回答可作为问题出现之前一段时间的标签；
- 使用这些标签训练机器学习模型区分 attentive state / mind wandering。

影响：
- “随机探针 → 前序窗口标签 → 机器学习 attentive state”已有明确先例。

公开来源：
https://patents.google.com/patent/WO2021247310A1/en
https://patents.google.com/patent/EP4161387B1/en

### 2.3 CN116077062A/B / US20250134430A1 — 非接触多模态心理状态感知

其方案已经覆盖：
- 带时间戳的图像序列；
- 带时间戳的毫米波原始数据；
- 视觉头部/面部特征；
- 毫米波心率与呼吸；
- 非接触多模态心理状态预测。

影响：
- “RGB + mmWave + timestamp + physiological features + mental-state model”也不能作为宽泛独立权利要求。

公开来源：
https://patents.google.com/patent/CN116077062A/en

### 2.4 CN119214656B — 基于毫米波雷达的专注度检测

独立权利要求直接把毫米波得到的体动、呼吸、心率用于专注度计算/模型预测。

影响：
- FocusWave 的毫米波心肺/体动 → 专注路径不能作为主案核心。

公开来源：
https://patents.google.com/patent/CN119214656B/en

## 3. 当前候选重排

### 3.1 P1：完整多模态持续注意测评系统

状态：`KEEP_BUT_NARROW`。

理由：
- 单个组成模块几乎都有在先技术；
- 仍可能存在“特定组合及组合关系”的申请空间，但必须证明不是简单拼接。

下一步不再用“多模态 + AI + 专注”表述，而应拆成可检验的功能链：
1. 任务事件生成统一时间锚；
2. 不同设备形成可追溯的前序窗口；
3. 每个科学特征绑定实际设备来源和 QC 依赖；
4. 在某设备缺失/质量不足时，不把缺失值当零，而是改变可估计集合与可用配置；
5. 输出同时包含状态概率、数据质量和设备覆盖边界。

需要查：是否已有“sensor availability / quality-aware configuration + cognitive state assessment”同构专利。

### 3.2 P2：RGB blink → NIR pupil 跨模态 QC

状态：`DOWNGRADED`。

不能再把“眨眼缓冲剔除 NIR 瞳孔伪迹”作为主独立发明点。US20210321876A1 的独立权利要求已经非常接近双相机同步 + blink/artefact removal。

仅在它与 FocusWave 独有的任务事件时间语义、严格前序窗口、质量/覆盖输出组合后，才继续考察。

### 3.3 P3：统一事件时间轴 + strict pre-probe legality

状态：`PROMOTED_FOR_COMBINATION`。

“时间对齐”单独仍可能普通，但 FocusWave 的正式实现强调：
- probe/event 是共同端点；
- 只消费端点之前的数据；
- 不同设备都形成相同时间语义；
- 时间合法性作为 feature handoff / registry 的显式字段；
- 不允许 probe 后信息或不明时间来源进入模型。

这不是单纯数据科学规范，而是实际决定连续传感流如何切片、哪些数据能进入测评输出。后续查新应围绕“event-anchored pre-event legal window + multimodal cognitive assessment”展开。

### 3.4 P4：科学信息—设备—预处理/QC—覆盖联动配置

状态：`PROMOTED_FOR_DEEP_SEARCH`。

这是目前相对更可能形成工程型技术差异的候选：
- scientific modality 不等于 device；
- 一个特征可依赖多个设备；
- 一个设备可产生多个科学信息；
- 设备组合不是静态枚举，而由冻结特征的真实 required devices 和 QC/preprocessing dependency 决定；
- 某必要设备不可用时，相应特征/模型配置不可估计，而不是补零或继续输出；
- 输出同时报告预测结果与数据覆盖/失效条件。

但风险仍高：如果最终只表现为“数据库字段管理”，会偏抽象。必须把权利要求锚定到具体传感器数据获取、预处理、特征形成和测评输出控制。

### 3.5 P5：毫米波心肺专注

状态：`DROP_AS_CORE`。

保留为 P1/P4 从属实施例，不作为核心发明点。

## 4. 第二轮候选优先级

1. **P4 + P3 组合**：基于实际传感器依赖、质量状态与严格事件前窗口的多模态持续注意测评配置/输出控制方法。
2. **收窄 P1**：把 P3/P4 作为独立权利要求中的必要结构，而不是泛化“多模态专注 AI”。
3. **P2**：仅作为一个跨设备 QC 实施例/从属方案继续保留。
4. **P5**：只作为心肺来源的从属设备路线。

## 5. 初步 claims-first 特征矩阵

| 特征 | FocusWave | US6090051A | US20210321876A1 | EP4552569A1 / EP4161387B1 | CN116077062A/B | CN119214656B |
|---|---|---|---|---|---|---|
| 注意/认知任务期间连续测量 | 是 | 是 | 否（眼病/眼表测量） | 是 | 心理状态 | 专注 |
| 思维/主观探针标注前序窗口 | 是 | 否 | 否 | 是 | 否 | 可请求用户确认但不同 |
| RGB/visible + NIR/IR 双视觉来源 | 是 | 否 | 是 | 否 | 图像 + radar | 否 |
| 眨眼相关伪迹剔除 | 是 | 是 | 是 | 非核心 | 未确认 | 否 |
| 可见光事件用于对应 IR/NIR 伪迹处理 | 是 | 否 | **是（非常接近）** | 否 | 未确认 | 否 |
| mmWave HR/BR | 是 | 否 | 否 | 否 | 是 | 是 |
| 时间戳同步多源数据 | 是 | 单眼动记录 | 是（同步图像） | 前序窗口 | 是 | 时间段 |
| 严格 probe/event 前数据合法性 | 是 | 未见 | 未见 | 有探针前窗口但未见同样治理语义 | 未见 | 未见 |
| feature→required devices→QC dependency 显式联动 | 是 | 未见 | 未见 | 未见 | 未见 | 未见 |
| 设备/质量不足时改变可估计配置并报告覆盖 | 是 | 未见 | 未见 | 未见 | 未见 | 未见 |

说明：`未见`仅表示本轮读取范围内未看到，绝不等于现有技术不存在。

## 6. 目前最重要的专利策略变化

上一轮曾把 P2 排在第一。本轮 claims-first 阅读后，该判断被**取代**：

- `P2 优先深挖` → **SUPERSEDED**；
- 当前第一优先级改为 **P4 + P3 组合**；
- P1 只保留为承载该组合的系统级主案候选；
- P2 降为从属/QC 实施例；
- P5 不作为核心。

## 7. 下一步唯一优先级

检索并比对以下主题的独立权利要求：

1. `quality-aware multimodal cognitive state assessment sensor availability`；
2. `sensor dependency feature availability configuration cognitive assessment`；
3. `event anchored pre-event window multimodal physiological cognitive state`；
4. `data quality coverage device configuration attention monitoring`；
5. 中文对应：`多模态 心理/注意 测评 设备依赖 质量控制 覆盖率 时间窗口`、`传感器缺失 可估计 配置 注意状态`。

验收门：至少形成 Top-K 高相关专利的独立权利要求对比后，才进入正式交底书重写。当前已有 Word 草案不得视为定稿。
