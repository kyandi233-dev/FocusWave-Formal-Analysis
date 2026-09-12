# B｜SART 与思维探针为什么适合作为 FocusWave 的实验范式和注意状态参照

> 调研日期：2026-09-12  
> 调研线：B  
> 性质：定向证据综述，不是系统综述或元分析  
> 当前阶段：**独立文献调研，不是国赛报告正文草稿。**  
> 项目事实权威：`FocusWave-Formal-Analysis@codex/code-fix-ledger` 当前 1.16 系列；正式实验事实以 `FocusWave@formaltest` 当前程序为准；行为分析事实以 `Attention-Analysis` 当前正式/1.16 开发链为准。  
> 本轮核对基线：Formal `2556358773300058a675875e3574f6ef520149c7`；formaltest `dc05fec0c10cedbc98fede4b05a190dc224ecb0e`。  
> 研究边界：A 线已经处理“持续注意是什么、与 vigilance / alertness / arousal / mind wandering 的构念边界”；本文件专门回答 SART、思维探针、行为指标及探针前窗口能提供什么证据，以及这些证据怎样映射到 FocusWave。

---

## 1. 本调研要解决的核心问题

FocusWave 需要的并不是一个能够被称为“注意真值”的单一实验标签，而是一套能够在较长持续任务中同时保留**实际任务表现**与**离散主观体验**的实验参照，并允许这些参照与连续的瞳孔、眨眼、身体运动和后续心肺信号在同一时间轴上对应。SART（Sustained Attention to Response Task，持续性注意反应任务）与 thought probe / experience sampling（思维探针 / 经验取样）的组合之所以有价值，主要在于两者提供互补证据：SART 持续产生反应时、遗漏和误按等行为记录，思维探针则在若干时间点询问参与者自己能够报告的意识内容和清醒程度。

这套组合的解释边界同样重要。SART 并不是过程纯净的“持续注意仪器”，其表现同时受到优势反应、反应抑制、速度—准确性权衡和策略选择影响；思维探针也不是无误差的心理真值，而是受问题措辞、分类体系、自我觉察和探针频率影响的离散自我报告。FocusWave 当前把行为、Q1、Q2 和传感器视为不同证据来源，而不是相互替代的真值，这一总体方法方向与现有文献更一致。

---

## 2. FocusWave 当前真正采用的实验结构

### 2.1 当前 SART 实现

`FocusWave@formaltest` 当前正式程序采用两个正式 Block。每个 Block 为 24 个 cycle、432 个试次，单试次为 250 ms 刺激呈现加 900 ms 掩蔽，总时长 1.15 s。八类非苹果蔬果为 Go 刺激，参与者需要按空格键；苹果为 No-Go 刺激，需要抑制按键。当前正式序列中 Go 反应占明显多数，从而形成重复、优势化的按键倾向；No-Go 作为相对低频事件要求参与者在持续反应流中停止该反应。

当前每个 Block 使用 10 个思维探针，共 20 个正式探针。探针位置预先写入正式序列，但并非严格等间隔：例如 B1 位于第 31、73、117、162、204、251、293、338、380、424 试次后，B2 位于第 32、75、118、162、205、247、295、339、381、424 试次后。探针回答结束后程序显示 0.7 s 任务背景缓冲，再恢复 SART。

### 2.2 当前 Q1/Q2 原题

本轮由实验负责人确认的正式题目为：

**Q1：此画面出现前一刻，最符合您状态的是：**

1. 完全专注于分拣任务；
2. 关注实验本身，但没有聚焦于分拣任务；
3. 在想与实验无关的事情；
4. 大脑空白，没有明确想法。

**Q2：在过去的几个试次中，您的清醒程度是：**

1. 非常困倦；
2. 比较困倦；
3. 比较清醒；
4. 非常清醒。

当前 `1.16.1` 与 `1.16.8` 的正式解释是：Q1 为探针时点对刚才注意内容的自我报告；Q2 为探针时点附近的主观困倦—清醒程度；SART 行为为实际任务表现。三者可能相关，也可能分离。首轮监督学习目前预测 `Q1=1` 对 `Q1=2/3/4`，但这不把 Q1 定义为“真实注意状态”。

### 2.3 北京正式事后问卷的角色

本轮重新核对 Google Drive 中北京正式问卷原始表 `3-北京正式_111_110.xlsx`。当前版本与两个正式 Block 一致，第 7 题以“第一轮 / 第二轮 / 没有明显区别”询问最难集中阶段。问卷还包括：主观察觉 Go 遗漏次数、任务策略、整场走神比例、走神内容、走神觉察、疲劳/注意维持困难、开始吃力的时间、困倦变化、情绪、对 No-Go 规律的判断、任务与设备体验、自评专注能力、平时持续专注时长、前一晚睡眠和近 6 小时咖啡因等。

这些信息适合做**场次级回顾和背景解释**，不适合作为逐探针 Q1/Q2 的效标。其时间尺度是整场或较长阶段，且依赖事后回忆；探针则尽量采样“刚才/过去几个试次”。因此问卷可用于解释策略、疲劳、元觉察、睡眠与咖啡因等背景，也可描述整场回顾与即时探针是否一致，但不能用来计算“Q1 是否回答正确”。本文不抄录任何原始参与者答案或身份信息。

---

## 3. SART 最初为什么被提出，它实际创造了什么实验情境

Robertson 等（1997）提出 SART 的直接目标，是在实验室中诱发和捕捉日常生活中类似“动作滑误”的注意失败。经典任务让参与者对频繁出现的刺激连续反应，只在罕见且不可预测的目标出现时停止反应；原始版本的 No-Go 目标约占九分之一。作者发现，SART 表现与其他持续注意测验以及日常注意失败报告相关，并观察到错误前反应时显著缩短，由此提出一种解释：当对任务的受控监控减弱时，连续按键逐渐进入更自动化的反应模式，罕见目标出现时就容易发生误按（Robertson et al., 1997）。

Manly 等（1999）随后进一步研究了 SART，强调需要在较长任务中持续监控自身反应这一时间维度的重要性。由此，SART 的经典理论逻辑可以概括为：**高频 Go 使“按键”形成优势反应；低频 No-Go 要求持续保留任务规则并在恰当时刻阻断优势反应；长时间重复执行使任务有机会暴露注意维持、自动化反应与控制波动。**

这也是 SART 与普通一次性 Go/No-Go 抑制任务的重要差别：研究关心的不只是“能不能抑制”，还关心在持续重复、较低事件新颖性和长时间任务中，表现怎样随时间和当前状态波动。Seli 等（2012）比较视觉和听觉 SART 后发现，错误率、反应时和反应时变异在两种感觉模态间具有较强个体内一致性，说明这些指标并不只是某一种视觉刺激材料的特例。

但经典提出者的解释不能被当作已经排除其他机制的结论。后续方法学研究证明，SART 的误按高度受反应速度、Go 比例和任务指令影响。因此，更准确的表述是：**SART 提供一个要求长期维持任务集、持续执行优势反应并间歇抑制该反应的标准化持续任务情境。它对持续注意变化敏感，但行为表现不是持续注意这一单一过程的纯指标。**

---

## 4. Go/No-Go 结构、优势反应和低频 No-Go 的心理意义

高频 Go 的核心作用，是让“看到刺激就按键”逐渐成为占优势的反应集合。No-Go 相对稀少时，正确表现要求参与者一方面维持连续反应节律，另一方面保留对罕见停止条件的监控。因此，一个 No-Go 误按至少可能来自三类过程的组合：当前任务监控不足、优势按键过强或过快、以及抑制过程失败。它不能只凭错误本身区分这些机制。

这一点已经被实验操纵直接证明。Seli、Jonker、Solman 等（2013）延迟参与者反应后发现，约 800 ms 的反应延迟可以显著降低 commission error（No-Go 误按），说明误按率会系统地随速度—准确性权衡变化。Wilson 等（2016）直接改变 Go 刺激比例，发现 Go 比例越高，反应越快、No-Go 误按越多，同时 task-related thoughts（任务相关思维）也增加，而 task-unrelated thoughts（任务无关思维）并未同步改变。Dang、Figueroa 和 Helton（2018）进一步从人内速度—准确性权衡角度批评把 SART 单纯视作持续注意测验。

这些争议并没有使 SART 对 FocusWave 失去价值，反而说明为什么当前分析必须同时保留**反应时、反应时波动、Go 遗漏和 No-Go 误按**，并把任务策略问卷作为解释背景。FocusWave 不依赖“一个 commission rate 就代表注意”，因此比把单一误按率直接作为注意分数的做法更稳妥。

---

## 5. SART 各行为指标分别能解释什么

| 指标 | 能直接描述什么 | 与注意/思维状态的文献关系 | 主要解释边界 | 对 FocusWave 的建议 |
|---|---|---|---|---|
| 正确 Go 反应时水平 | 当前正确反应总体快慢 | 经典研究观察到错误前加速；部分心智游移研究也观察到探针前更快反应 | 强烈受速度—准确性策略影响；低唤醒或 mind blanking（思维空白）又可能表现为变慢 | 保留为“反应速度”，不直接命名为注意水平 |
| 反应时波动 | 反应节律稳定性 | Cheyne 等（2009）、Bastian 与 Sackur（2013）等支持较高 RT variability（反应时变异）与任务脱离/心智游移相关；Seli 等（2012）显示跨感觉模态一致性 | 波动不是主观状态真值，也可能受运动、策略和异常试次影响 | 当前 CV 作为主要行为维度有较强文献基础；报告称“反应稳定性/波动”最合适 |
| 反应时局部趋势 | 探针前窗口内反应逐渐变快或变慢 | 错误前加速和不同低唤醒状态提示局部趋势有解释价值 | “斜率”本身不是一个已有统一心理学构念；方向可能随状态类型变化 | 可作为动态描述量，避免写成公认的“注意下降指标” |
| Go omission（Go 遗漏） | 应反应试次没有产生有效反应 | Cheyne 等（2009）把遗漏与更深的 response disengagement（反应脱离）联系；Andrillon 等（2021）发现 MW 与 MB 均增加遗漏，MB 更明显 | 可能由反应过慢、时序错位、暂时无反应等形成；不能自动判定为某类主观思维 | 当前将 raw Go omission 独立于 commission 是正确的；更细 timing 分类留 QC/敏感性 |
| No-Go commission（No-Go 误按） | 应抑制试次发生按键 | 多项研究发现 off-task / MW 附近误按增加；经典 SART 最常用该指标 | 同时受抑制、优势反应、Go 比例、反应速度和策略影响 | 报告称“No-Go 误按/抑制失败表现”，不能直接称“走神次数” |
| d′（辨别力） | 将 Go 命中与 No-Go 错误共同形成的敏感性总结 | Corcoran 等（2025）在探针前 10 s 发现 off-task 报告前 d′ 较低 | 是综合性能指标，不能告诉下降来自 Go 命中降低还是 No-Go 误按增加 | 适合作为行为综合/敏感性指标，不替代 omission 与 commission 的机制分解 |
| criterion c / β | 反应偏向 | 信号检测论可区分敏感性与“更愿意按/更愿意不按”的偏向 | 强依赖编码与任务结构；心理含义不是“注意好坏” | 当前留作补充分析合理 |

### 5.1 哪些指标与心智游移关系相对更稳定

现有 SART 文献中，**反应时变异增大**是较反复出现的行为关联之一。Bastian 与 Sackur（2013）基于 SART 构建连续 RT 变异指标，发现局部变异增大能够预测随后报告的心智游移。Cheyne 等（2009）的任务投入/脱离模型同样把反应变异视为从稳定投入向任务脱离过渡的行为表现。McVay 与 Kane（2009）则发现任务无关思维与较差 SART 表现和更不稳定反应有关。

No-Go 误按也经常在任务无关思维附近升高，但由于它受速度—准确性权衡影响更明显，其心理解释需要同时看反应速度。Go 遗漏在较低唤醒、思维空白或更深任务脱离状态中可能更突出。Andrillon 等（2021）的结果尤其重要：MW 与 MB 都增加错误，但 MB 相比 MW 表现出更多遗漏和更慢反应；MW 则相对更接近“冲动/快速”的错误模式。因而，“注意不好 = 反应变快”或“注意不好 = 反应变慢”都过于简单。

### 5.2 行为错误不能自动推出主观注意内容

同一个 No-Go 误按可能出现在快速、自动化反应状态，也可能由其他控制失败形成；同一个 Go 遗漏也可能来自困倦、思维空白、按键时序问题或其他暂时脱离。行为与探针的科学价值恰恰在于可以检验二者何时一致、何时分离，而不是用行为错误替代主观报告。

---

## 6. SART 的主要测量争议

### 6.1 速度—准确性权衡不是次要技术问题

SART 要求频繁按键，因此反应策略能够显著改变误按率。Seli、Jonker、Solman 等（2013）实验操纵反应延迟后发现，单纯把反应放慢就能显著减少 commission errors；Seli、Jonker、Cheyne 和 Smilek（2013）随后提出应在 SART 评价中显式控制速度—准确性权衡。Dang 等（2018）甚至据此提出强烈批评，认为相当一部分 SART 表现可以被“决定得更快”而非持续注意解释。

因此，国赛报告不应写“误按率直接衡量注意维持能力”。更稳妥的是：“SART 误按反映持续任务中优势反应未被成功抑制的表现，其变化可能同时受到注意监控、反应速度和策略影响。”

### 6.2 SART 同时混合持续注意与反应抑制

No-Go 的核心操作就是 withholding（停止/抑制），因此反应抑制不可能从任务中被完全剥离。经典研究强调长时间持续监控，后续研究则强调反应抑制和策略。当前文献更支持把两类过程都承认为任务的一部分，而不是把争论写成“到底谁完全正确”。

### 6.3 Go 比例和目标可预测性会改变任务策略

Wilson 等（2016）表明，改变 Go 比例可以系统地改变 RT 和 commission rate，却不必同步改变任务无关思维。这说明高 Go 比例的意义不仅是“更能诱发走神”，还在于它建立更强的优势反应和不同决策策略。FocusWave 的正式序列固定了较高 Go 比例，因此跨研究比较时不能忽视任务参数差异。

### 6.4 FocusWave 因而应把 SART 称为什么

建议在国赛报告中使用以下层级：

**SART 是一个用于研究持续任务表现的 Go/No-Go 范式，在高频 Go、低频 No-Go 的连续反应背景下，同时对任务维持、反应稳定性、优势反应和反应抑制敏感。**

这个表述既保留其经典持续注意来源，也承认后续构念争议。不要写成“专门、纯粹测量持续注意”，也不要因为争议就反过来说 SART 与持续注意无关。

---

## 7. 为什么思维探针适合测量任务中的即时注意内容

### 7.1 探针提供行为无法直接得到的“意识内容”信息

行为记录能告诉我们参与者做了什么，却不能直接告诉我们当时在想什么。thought probe / experience sampling（思维探针 / 经验取样）的基本做法，是在正在进行的任务中偶尔暂停并询问刚才意识内容，从而获得与明确时间点绑定的自我报告。Weinstein（2018）回顾 2005—2015 年 105 篇文章中的 145 项研究，指出 probe-caught（探针捕获）已经成为实验室心智游移研究最广泛使用的方法，同时也发现至少 69 种不同探针实现，说明题目措辞和反应选项本身就是测量设计的一部分。

Kane 等（2021）在超过 1000 名大学生中比较不同探针形式，发现部分结论会随测量方式变化，并据此暂时更推荐 content-report probe（内容报告式探针），而不是只问意图或深度。FocusWave 当前 Q1 正是内容分类，而不是要求参与者把“注意程度”压缩成一条连续强度评分，这一点具有方法学优势。

### 7.2 probe-caught 与 self-caught 各测到什么

| 方法 | 操作 | 优势 | 主要局限 |
|---|---|---|---|
| probe-caught（探针捕获） | 实验在预定/随机时点主动询问当前或刚才状态 | 不要求参与者始终监控自己；能捕捉参与者尚未自觉的 off-task 状态；探针时间可与连续信号精确对齐 | 会中断任务；频率、措辞和分类可能影响报告；只能离散采样 |
| self-caught（自我捕获） | 参与者一旦发现自己走神就主动报告 | 能研究 meta-awareness（元觉察）和“何时意识到自己走神” | 只能捕捉已经被自己察觉的事件；不同人的自我监控能力不同；要求持续监控可能额外占用认知资源 |

Schooler 等（2011）指出，心智游移本身与对心智游移的 meta-awareness（元觉察）可以分离，因此 self-caught 和 probe-caught 不应被视为可互换。Chu 等（2023）对 39 项 self-caught 研究的系统综述也指出该方法存在较大方法异质性，且很少有研究同时报告可靠性与效度。更近期的 Safati、Seli 与 Smilek（2026）甚至发现，要求参与者持续 self-catch 会增加主任务反应时变异，提示“持续自我监控”本身可能有性能成本。

对 FocusWave 而言，使用 probe-caught 更符合目标：需要在不要求参与者持续自我监控的情况下取得若干统一时间锚点，再把这些锚点与连续传感信息对应。事后问卷第 6 题关于“走神后很快发现 / 过一会发现 / 只有状态检查时才发现”的回答，则可以作为元觉察背景，而不是替代探针。

---

## 8. 思维探针会不会打断任务、改变随后状态

不能笼统地写“探针完全无干扰”。现有证据更适合支持一个有条件的结论。

Wiemers 与 Redick（2019）让 149 名参与者分别完成含探针和不含探针的 SART，没有发现总体 SART 表现因探针而系统改变，支持在这一类任务中 probe-caught 测量具有较低的整体性能反应性。Robison、Miller 与 Unsworth（2019）在三项实验中操纵探针频率、反应选项和 framing（框架），也没有发现探针频率或框架改变主任务表现。

但其他研究显示 probe rate（探针频率）可能影响报告出的心智游移率，而且这种影响可能随任务负荷而变化。在线探针的方法学文献也长期提醒：探针会让参与者知道研究者在关注他们的内部状态，从而可能改变元认知取向或响应标准。因此更准确的表述是：**在部分持续注意任务中，思维探针对总体行为表现的反应性可以较小，但探针并非理论上完全无干扰，探针频率和问题形式仍可能影响自我报告。**

FocusWave 当前使用每 Block 10 次离散探针，并把正式传感/行为关联锁定在**探针之前**的窗口。这一做法有一个明显优势：探针本身的中断和随后 0.7 s 恢复过程不会反向污染已经结束的 pre-probe（探针前）窗口。若未来分析探针后的状态，则必须单独处理探针反应性和恢复期。

---

## 9. FocusWave Q1 四类与文献中的心理状态如何对应

当前 Q1 的最大优点，是没有把所有非完全专注状态压成一个“走神”选项。Robison 等（2019）基于方法实验明确主张，thought probe 至少应区分 on-task（任务中）、off-task（任务外）和 task-related interference, TRI（任务相关干扰）；若研究心智游移，还应进一步区分 mind-wandering（心智游移）、external distraction（外部干扰）和 mind-blanking（思维空白）。Van den Driessche 等（2025）提出并验证的五类 mental-state 分类同样包括 focus、task-related interference、external distraction、daydream 和 blank。

| FocusWave Q1 | 最接近的文献概念 | 文献对应程度 | 需要保留的边界 |
|---|---|---|---|
| 1 完全专注于分拣任务 | on-task / focus | 高 | 是任务聚焦自报，不是客观“高注意真值” |
| 2 关注实验本身，但没有聚焦分拣任务 | task-related interference（TRI，任务相关干扰/任务评价性思维） | 高 | 与真正执行分拣规则不同，但也不是与实验无关的心智游移 |
| 3 在想与实验无关的事情 | task-unrelated thought（TUT，任务无关思维）；与 mind-wandering 高度接近 | 中—高 | 当前选项没有单独区分内部自发思维、外部环境分心和身体感觉，因此不宜严格等同于狭义 stimulus-independent mind wandering |
| 4 大脑空白，没有明确想法 | mind blanking（思维空白） | 高 | 不能并入普通 MW 作为同一种心理状态；已有行为和生理证据显示二者可分离 |

### 9.1 当前二分类 `Q1=1` 对 `Q1=2/3/4` 应怎样命名

这个二分类在工程上和首轮跨参与者预测上是清楚的，但心理学语言必须精确。`2/3/4` 包含 TRI、任务无关思维和思维空白，三者没有一个共同的“走神内容”。因此首轮标签最合适的报告语言是：

**“完全任务聚焦报告” vs “其他非完全任务聚焦报告状态”**，或简写为**“完全任务聚焦 vs 其他报告状态”**。

不建议把它写成：

- “专注 vs 走神”；
- “高注意 vs 低注意”；
- “正常注意 vs 注意涣散”；
- “清醒 vs 困倦”。

Q1 四分类后续如果进入正式分析，也必须按 nominal categories（无序类别）解释，不应把 1→4 当作连续注意下降等级。

### 9.2 Q1 当前仍缺少哪一类常见状态

较新的多类别探针通常会把 external distraction（外部干扰，例如环境声音、身体感觉）单独列出。FocusWave Q1 没有这个独立类别，因此 Q1=3 很可能承担了一部分广义“实验无关”内容。北京正式事后问卷第 5 题确实另外询问了“被周围环境吸引（声音、光线、身体感觉等）”，说明项目已经在场次回顾层面记录了这类内容，但逐探针层面没有把它单列。

这不是必须补做实验的错误，因为正式数据已经采集完成；报告只需承认 Q1 是项目自己的四分类操作化，而不是声称完整覆盖了所有心智状态分类。

---

## 10. Q2 应解释为主观困倦—清醒程度，而不是另一个“注意等级”

Q2 的文献对应非常直接。Corcoran 等（2025）在 SART 中除了询问 on-task、mind-wandering 和 mind-blanking，还要求参与者评价“过去几个试次”的 vigilance，使用四点量表从 “Extremely Sleepy” 到 “Extremely Alert”。这与 FocusWave 当前 Q2“过去几个试次中，非常困倦—非常清醒”的题干和时间范围高度同构。该研究还把探针前 10 s 的行为、瞳孔和心脏活动与随后主观状态对应，说明“注意内容 + 清醒程度 + 探针前连续信号”的整体设计在近期文献中已有直接先例。

但文献同样清楚表明 Q1 类注意内容与 Q2 类困倦/清醒不能互换。Stawarczyk 与 D’Argembeau（2016）在 SART 中同时在线采样 mind-wandering 和 subjective sleepiness（主观困倦），发现二者虽经常共现，却在参与者内和参与者间都能独立、叠加地预测任务表现。Andrillon 等（2021）也发现 MW 与 MB 均伴随较低主观 vigilance，但两种状态的行为模式不同；MB 更偏向慢反应和遗漏，MW 则更偏向相对冲动模式。Corcoran 等（2025）同样观察到 MW 和 MB 都与较低清醒度相关，但二者具有不同的心脏、瞳孔和行为特征。

因此 FocusWave 当前把 Q2 作为解释性关联变量，而不把它作为 Q1 的定义成分或首轮 Q1 预测输入，是合理的。报告应优先称 Q2 为**“主观困倦—清醒程度”**或**“主观清醒程度”**；若使用 vigilance 一词，应同时说明这里是探针自报的 alertness/sleepiness，而不是把 Q2 等同于客观 vigilance decrement（警觉递减）。

---

## 11. mind wandering、低清醒和 vigilance decrement 不能直接等同

三者可以随 time-on-task（任务持续时间）共同变化，但并不因此是同一个过程。

Martínez-Pérez 等（2023）在带 thought probes 的 SART 中同时操纵任务要求和经颅直流刺激，观察到双重分离：任务要求影响 vigilance decrement，而刺激影响 mind-wandering rate；二者的个体指标也不相关。这直接反驳“只要任务表现随时间下降，就等于心智游移增加”的简单等同。

同样，Stawarczyk 与 D’Argembeau（2016）的结果说明 sleepiness（困倦）与 mind-wandering 可以共同出现，但各自仍有独立行为关联。因此，FocusWave 结果中如果出现“后半程 Q2 更困、RT 波动更大、Q1 非完全聚焦更多”，最多说明这些现象在任务过程中共变；若要说其中一个“导致”另一个，需要额外设计和分析证据。

---

## 12. 为什么“持续任务 + 离散探针 + 探针前窗口”适合连续传感信号

这套设计的逻辑不是把离散探针伪装成连续真值，而是用探针建立**时间锚点**。连续行为和传感信号在整个任务中一直存在，探针只在有限时点提供主观报告；研究可以围绕每个探针向前截取一个近端时间窗，回答“在参与者随后报告某一状态之前，行为/生理信号呈现什么特征”。

这种 probe-locked pre-probe window（探针锁定的探针前窗口）在相关研究中很常见，但窗口长度没有唯一标准。Andrillon 等（2021）主要分析探针前 20 s，并说明 20 s 的选择既保证每个窗口大致包含两个 No-Go 试次，又保持与主观报告的时间接近；他们还用 10 s 做敏感性检查。Corcoran 等（2025）使用探针前 10 s 计算 d′、反应偏向、反应速度、瞳孔和心脏指标。Bastian 与 Sackur（2013）则从探针附近的局部 RT 变异出发建立连续状态指标。

因此，文献可以直接支持的是：

1. 把探针出现前的近端行为和生理活动与随后状态报告对应；
2. 窗口需要在“心理时间局部性”和“有足够试次/信号支持稳定统计”之间权衡；
3. 应通过不同窗口长度检查结论是否依赖某个任意时间尺度。

文献**不能**直接证明 FocusWave 的 30 s 是统一标准。FocusWave 当前 30 s 主窗口更适合表述为项目正式权衡：相较 10 s/20 s，它增加 Go RT、No-Go 机会和连续传感数据量，有利于估计水平、波动与趋势；代价是离探针更远的信息也会进入摘要。因此当前保留 10/20 s 敏感性窗口具有重要方法学意义。如果 30 s 与较短窗口结果方向一致，可以增强时间尺度稳健性；若不同，应如实解释，不应只保留最显著窗口。

---

## 13. SART + 思维探针组合的优势与限制

### 13.1 优势

第一，**行为和主观体验互补**。SART 连续记录“做得怎么样”，探针记录“参与者报告自己刚才处于什么意识内容/清醒状态”。两者能够检验一致与分离，而不是彼此替代。

第二，**具有自然的时间结构**。SART 的持续反应流让 RT、遗漏、误按和时间趋势可以在多个尺度上描述；探针则给这些连续数据提供若干有心理含义的时间锚点。

第三，**适合多模态同步研究**。瞳孔、眨眼、身体运动、心脏等信号是连续记录，探针前窗口可以把不同采样率的传感器转成同一 probe-level（探针级）比较单位。Corcoran 等（2025）和 Andrillon 等（2021）已经展示了 SART + probe + pupil / cardiac / EEG 的直接先例。

第四，**能够区分内容和唤醒维度**。FocusWave 分开 Q1 与 Q2，与当前文献把 attentional content（注意内容）和 alertness/sleepiness（清醒/困倦）分别测量的做法一致。

### 13.2 限制

第一，SART 行为不具过程纯净性。误按同时涉及持续监控、反应抑制和速度策略，遗漏也可能有多种形成机制。

第二，探针是自我报告。参与者可能没有完全觉察当前状态，分类会受题目定义和响应框架影响。

第三，探针是离散采样。两个探针之间发生了什么不能由探针本身直接知道，连续传感模型只能在验证后推断，不应把 probe labels 插值成连续真值。

第四，探针可能有反应性。已有 SART 研究显示总体行为反应性可以较小，但不能声称完全没有干扰；尤其探针后的短时行为和持续自我监控需要谨慎。

第五，Q1 的分类体系是有理论依据的项目操作化，但不是领域唯一分类。当前没有逐探针 external distraction 独立选项。

---

## 14. 北京正式事后问卷可以怎样与 B 线配合

| 问卷内容 | 在研究中的合适角色 | 不应怎样解释 |
|---|---|---|
| 主观察觉 Go 遗漏次数 | metacognitive awareness（元认知觉察）及行为回顾 | 不能替代实际行为日志中的 Go omission |
| 任务策略 | 解释速度—准确性权衡、反应抑制策略和个体差异 | 不能作为事后“修正”行为结果的依据 |
| 整场走神比例、内容 | session-level（场次级）主观回顾，与 Q1 分布做描述性对应 | 不能用来判断每一个 Q1 是否“正确” |
| 走神觉察 | 补充 self-caught / probe-caught 与 meta-awareness 解释 | 不能把“只有探针时发现”简单等同于更差注意 |
| 第一/第二轮最难集中、开始吃力时间 | 描述 time-on-task 和主观疲劳进程 | 不能替代试次级/探针级时间趋势统计 |
| 困倦变化 | 与 Q2 的场次级回顾对应 | 不能把整场回顾当成逐探针 Q2 |
| 对苹果规律的判断 | 很重要的策略/目标可预测性感知背景 | 不能据此认定程序真的具有该规律 |
| 自评专注能力、日常持续专注时长 | trait-like（类特质）背景 | 不是标准化持续注意量表或临床诊断 |
| 睡眠、咖啡因 | arousal（唤醒）相关背景变量 | 不能自动作为 Q1 的原因或首轮预测特征 |

总体上，当前 `1.16.1` 把问卷定位为“整场回顾和背景解释”是合适的。

---

## 15. 文献证据矩阵

| 证据主题 | 关键来源 | 研究类型/对象 | 主要发现 | 对 FocusWave 的直接意义 | 证据边界 |
|---|---|---|---|---|---|
| SART 原始目的 | Robertson et al., 1997 | TBI + 正常对照；原始 SART | 罕见 No-Go 误按与日常注意失败/持续注意测验相关；错误前 RT 加速 | 支持在持续优势反应中观察动作滑误与注意失败 | 早期效度证据不能证明过程纯净 |
| 持续时间维度 | Manly et al., 1999 | SART 后续实验 | 支持持续监控自身反应的重要性 | 支持用较长任务研究任务维持 | 同时仍包含抑制需求 |
| 跨刺激模态一致性 | Seli et al., 2012 | 听觉 vs 视觉 SART | error、RT、RT variability 跨模态高度相关 | 支持这些指标不是单一视觉素材特例 | 仍是任务表现指标，不等于主观状态 |
| RT 变异与 MW | Bastian & Sackur, 2013 | SART + 主观报告 | 局部 RT variability 增大预测 MW | 支持 FocusWave 保留 RT 波动 | 不能把 CV 当连续真值 |
| 行为脱离模型 | Cheyne et al., 2009 | SART 行为建模 | variability、anticipation、omission 对应不同任务投入/脱离阶段 | 支持分开速度、波动、遗漏 | 模型是一种解释框架，不是唯一机制 |
| SART 与 TUT | McVay & Kane, 2009 | SART + thought probes | TUT 与目标忽略、较差/不稳定表现相关 | 支持探针前行为与 Q1 对应分析 | TUT 不是所有非 Q1=1 状态 |
| 速度—准确性争议 | Seli et al., 2013a, 2013b | 操纵反应延迟；方法研究 | 改变反应速度即可显著改变 commission | 要求 RT 与误按联合解释 | 不能用 commission 单独命名“持续注意” |
| Go 比例与策略 | Wilson et al., 2016 | 操纵 Go 比例 | Go 越多，RT 越快、commission 越多；TUT 不同步变化 | 说明正式 Go/No-Go 比例本身塑造反应策略 | 跨 SART 版本不能直接比错误率 |
| SART 强批评 | Dang et al., 2018 | 人内 SATO | 强调 strategy / SATO 对 SART 的影响 | 报告必须承认构念混合 | 该文的“does not measure”是争议一端，不代表领域唯一结论 |
| Probe 方法异质性 | Weinstein, 2018 | 145 studies / 105 articles review | probe-caught 广泛使用，但有大量措辞/选项变体 | Q1 题目本身必须作为测量设计报告 | 不存在唯一“标准问题” |
| 探针分类设计 | Robison et al., 2019 | 3 experiments | 建议至少区分 on-task、off-task、TRI；MW 研究再区分 external distraction / blank | 强支持 Q1 1/2/3/4 的多类别思路 | FocusWave 未单列 external distraction |
| Probe 构念效度 | Kane et al., 2021 | >1000 undergraduates | 不同 probe 形式部分结果不同；较支持内容报告式探针 | 支持 Q1 使用内容类别而非单一注意强度 | 自我报告仍有测量误差 |
| Probe 反应性 | Wiemers & Redick, 2019 | N=149 SART | 含/不含 probes 的总体 SART 表现无差异 | 支持探针在该类任务中总体性能反应性较低 | 不证明所有频率/任务都无反应性 |
| Self-caught 局限 | Chu et al., 2023; Safati et al., 2026 | 系统综述；实验 | self-caught 强依赖 meta-awareness；持续自我监控可能损害主任务 | 支持 FocusWave 采用 probe-caught 而非持续自我监控 | probe-caught 也并非无偏 |
| MW 与困倦区分 | Stawarczyk & D’Argembeau, 2016 | SART + 在线 MW + sleepiness | 二者共现但独立、叠加预测表现 | 强支持 Q1/Q2 分开 | 相关不代表因果 |
| MW 与 vigilance decrement 区分 | Martínez-Pérez et al., 2023 | SART + probes + experimental manipulations | 双重分离，vigilance decrement 与 MW rate 不相关 | 禁止把任务随时间下降等同走神 | 特定任务与操纵下证据 |
| MW vs MB 行为模式 | Andrillon et al., 2021 | SART + probe + pupil + EEG | 20 s pre-probe：MW/MB 均更多错误；MB 更多 miss 和更慢 RT；10 s 敏感性一致 | 支持 Q1=3 与 Q1=4 分开；支持 pre-probe window | 样本与任务版本不同于 FocusWave |
| Q2 与多模态直接先例 | Corcoran et al., 2025 | N=65，SART + probe + EEG/ECG/pupil | attention content + 4-point sleepy-alert；10 s pre-probe d′/RT/pupil/cardio | 与 FocusWave Q1/Q2 + 连续传感设计高度接近 | 不是对 FocusWave 30 s 的直接验证 |
| 多状态分类 | Van den Driessche et al., 2025 | 构念/效标验证 | focus、TRI、external distraction、daydream、blank 五类可区分 | 强化 Q1 多类别的构念依据 | FocusWave 四类是简化版本 |

---

## 16. 可以直接支撑国赛报告的关键论点

1. **SART 适合提供标准化、连续的持续任务情境。** 高频 Go 与低频 No-Go 使参与者形成优势反应，并要求在较长时间内持续维持任务规则与间歇抑制反应，因此能够产生反应速度、反应稳定性、遗漏和误按等互补行为信息（Robertson et al., 1997; Manly et al., 1999）。

2. **SART 应作为多维行为参照，而不是单一误按率的“注意分数”。** RT、RT variability、Go omission、No-Go commission 和 d′分别保留速度、稳定性、反应脱离、抑制失败与综合敏感性信息；速度—准确性研究证明这些指标必须联合解释（Seli et al., 2013a, 2013b）。

3. **思维探针弥补行为记录无法直接识别意识内容的缺口。** probe-caught experience sampling 能在持续任务中建立时间明确的主观状态样本，是心智游移研究的主流方法，但其分类和措辞属于正式测量设计的一部分（Weinstein, 2018; Kane et al., 2021）。

4. **FocusWave Q1 四分类具有清楚的现代文献对应。** Q1=1 对应 focus/on-task，Q1=2 接近 TRI，Q1=3 接近广义 TUT/MW，Q1=4 对应 mind blanking；多类别方案比把所有非任务聚焦状态直接称为“走神”更符合当前研究（Robison et al., 2019; Van den Driessche et al., 2025）。

5. **Q1 与 Q2 必须分开。** 注意内容和主观困倦/清醒常共变，却能独立关联任务表现；近期 SART 多模态研究直接采用了注意内容 + 四级 sleepy-alert 探针（Stawarczyk & D’Argembeau, 2016; Corcoran et al., 2025）。

6. **探针前连续窗口有直接方法学先例。** 已有研究在 SART 中使用 10 s 或 20 s pre-probe windows 汇总行为、瞳孔、心脏和 EEG 信息；其核心思想是围绕随后主观报告提取近端连续信号，而非规定某个唯一秒数（Andrillon et al., 2021; Corcoran et al., 2025）。

7. **持续任务 + 离散探针适合多模态系统验证。** 行为和传感器保持连续记录，探针提供稀疏但有心理意义的时间锚点，使不同模态可以被转换到共同的 probe-level 单位，同时保留行为与主观体验可能分离这一科学问题。

---

## 17. 国赛报告中不能过度声称的内容

1. 不能写“**SART 专门/纯粹测量持续注意**”。它同时涉及反应抑制、优势反应和速度策略。
2. 不能写“**No-Go 误按就是走神**”或“**Go 遗漏就是困倦**”。错误类型与主观状态只有概率关系。
3. 不能写“**反应越快/越慢就一定代表注意越差**”。不同 MW、MB、低唤醒和策略状态可能产生不同方向。
4. 不能把 `d′` 写成“**纯注意力指数**”。它是任务敏感性的综合行为量。
5. 不能把 Q1 写成“**attention ground truth（注意真值）**”。它是探针时点的注意内容自我报告。
6. 不能把 Q1=2/3/4 统称“**走神**”。其中至少包含 TRI、任务无关思维和思维空白。
7. 不能把 Q1 四类解释成从 1 到 4 连续变差的注意等级。
8. 不能把 Q2 写成“**客观警觉水平**”或“另一种注意真值”。它是主观困倦—清醒报告。
9. 不能把 mind wandering、sleepiness 和 vigilance decrement 直接等同。
10. 不能写“**思维探针完全不会干扰任务**”。更准确的是在部分 SART 研究中总体行为反应性较小，但探针频率和形式仍可能影响报告。
11. 不能把两个探针之间的连续时间段直接赋予最近一次 Q1 标签。
12. 不能写“**30 s 是 SART + probe 文献的标准窗口**”。文献支持近端 pre-probe 窗口，具体长度需要任务内权衡和敏感性检查。
13. 不能用事后问卷去“验证”每个 Q1/Q2 是否正确。问卷是场次级回顾和背景信息。

---

## 18. 对 FocusWave 当前项目叙事的具体修改建议

### 18.1 “SART 为什么适合作为范式”的表述

当前 `国赛报告/0-总结构与研究叙事_20260912.md` 中“通过较长时间任务形成自然的注意波动”建议在正式写作时稍作收紧。更严谨的版本应强调：

**SART 在持续、重复的 Go/No-Go 情境中提供较长的任务维持过程，使反应速度、稳定性、遗漏和抑制失败能够随时间变化，并为任务脱离、困倦和其他注意状态波动提供出现和被采样的机会。**

这样避免把所有时间变化都预先解释为“被 SART 诱发的注意下降”。

### 18.2 行为的角色

报告中应统一写成“任务表现参照/行为证据”，而不是“客观注意真值”。尤其 No-Go commission 的名称尽量保留“误按/抑制失败表现”，Go omission 保留“遗漏”，RT CV 保留“反应稳定性/波动”。

### 18.3 Q1 首轮二分类语言

正式监督学习的 `Q1=1` vs `Q1=2/3/4` 推荐统一写为：

**完全任务聚焦报告 vs 其他非完全任务聚焦报告状态。**

这是本轮最需要修正的叙事边界之一。任何“专注 vs 走神”的简称都会把 Q1=2 的任务相关干扰和 Q1=4 的思维空白错误归入 mind wandering。

### 18.4 Q2 的语言

Q2 推荐统一称“主观困倦—清醒程度”或“主观清醒程度”。如果英文使用 vigilance，正文应同时给出实际量表含义，防止与 vigilance decrement 混同。

### 18.5 30 s 探针前窗口

报告可说明已有研究采用 10 s、20 s 等近端探针前窗口把行为/生理信号与随后状态报告对应；FocusWave 将 30 s 作为主窗口，是为了在保持时间接近性的同时获得更多行为和传感数据支持，并以 10/20 s 作为敏感性尺度。不要把 30 s 写成外部文献规定的标准参数。

### 18.6 事后问卷

事后问卷应作为“即时探针之外的整场回顾与背景解释”：尤其任务策略、走神觉察、困倦变化、睡眠和咖啡因有助于解释个体差异与任务进程。它与 probe data 的不一致本身也有研究意义，不应被处理成谁“答错了”。

---

## 19. 5–8 篇核心推荐文献

若国赛正文篇幅有限，优先保留下列 8 篇：

1. **Robertson et al. (1997)**：SART 原始论文；回答范式为什么被提出、优势反应与错误前加速的经典解释。
2. **Manly et al. (1999)**：SART 经典后续研究；支持持续监控/任务时间维度。
3. **Seli, Jonker, Solman, et al. (2013)**：SART 速度—准确性权衡的关键方法学证据，防止把 commission 直接当注意指标。
4. **Weinstein (2018)**：thought-probe 方法综述，说明 probe-caught 的领域地位和方法异质性。
5. **Robison et al. (2019)**：直接研究探针频率、响应选项与 framing，并支持 on-task / off-task / TRI 以及进一步区分 blank 等状态。
6. **Stawarczyk & D’Argembeau (2016)**：SART 中同时测量 mind wandering 与 sleepiness，直接证明两者相关但可分离。
7. **Andrillon et al. (2021)**：SART + probe + pupil + EEG；20 s/10 s 探针前窗口，并区分 MW 与 MB 的不同行为模式。
8. **Corcoran et al. (2025)**：与 FocusWave 设计最接近的近期多模态先例；SART + 注意内容 + 四级 sleepy-alert + 10 s 行为/瞳孔/心脏窗口。

Wiemers 与 Redick（2019）、Kane 等（2021）、Van den Driessche 等（2025）适合在方法限制和 Q1 分类依据处作为补充核心证据。

---

## 20. 完整参考文献（APA 第七版）

Andrillon, T., Burns, A., Mackay, T., Windt, J., & Tsuchiya, N. (2021). Predicting lapses of attention with sleep-like slow waves. *Nature Communications, 12*, 3657. https://doi.org/10.1038/s41467-021-23890-7

Bastian, M., & Sackur, J. (2013). Mind wandering at the fingertips: Automatic parsing of subjective states based on response time variability. *Frontiers in Psychology, 4*, 573. https://doi.org/10.3389/fpsyg.2013.00573

Cheyne, J. A., Solman, G. J. F., Carriere, J. S. A., & Smilek, D. (2009). Anatomy of an error: A bidirectional state model of task engagement/disengagement and attention-related errors. *Cognition, 111*(1), 98–113. https://doi.org/10.1016/j.cognition.2008.12.009

Chu, M. T., Marks, E., Smith, C. L., & Chadwick, P. (2023). Self-caught methodologies for measuring mind wandering with meta-awareness: A systematic review. *Consciousness and Cognition, 108*, 103463. https://doi.org/10.1016/j.concog.2022.103463

Corcoran, A. W., Le Coz, A., Hohwy, J., & Andrillon, T. (2025). When your heart isn’t in it anymore: Cardiac correlates of task disengagement. *Communications Biology, 8*, 1646. https://doi.org/10.1038/s42003-025-09026-3

Dang, J. S., Figueroa, I. J., & Helton, W. S. (2018). You are measuring the decision to be fast, not inattention: The Sustained Attention to Response Task does not measure sustained attention. *Experimental Brain Research, 236*(8), 2255–2262. https://doi.org/10.1007/s00221-018-5291-6

Kane, M. J., Smeekens, B. A., Meier, M. E., Welhaf, M. S., & Phillips, N. E. (2021). Testing the construct validity of competing measurement approaches to probed mind-wandering reports. *Behavior Research Methods, 53*(6), 2372–2411. https://doi.org/10.3758/s13428-021-01557-x

Manly, T., Robertson, I. H., Galloway, M., & Hawkins, K. (1999). The absent mind: Further investigations of sustained attention to response. *Neuropsychologia, 37*(6), 661–670. https://doi.org/10.1016/S0028-3932(98)00127-4

Martínez-Pérez, V., Andreu, A., Sandoval-Lentisco, A., Tortajada, M., Palmero, L. B., Castillo, A., Campoy, G., & Fuentes, L. J. (2023). Vigilance decrement and mind-wandering in sustained attention tasks: Two sides of the same coin? *Frontiers in Neuroscience, 17*, 1122406. https://doi.org/10.3389/fnins.2023.1122406

McVay, J. C., & Kane, M. J. (2009). Conducting the train of thought: Working memory capacity, goal neglect, and mind wandering in an executive-control task. *Journal of Experimental Psychology: Learning, Memory, and Cognition, 35*(1), 196–204. https://doi.org/10.1037/a0014104

Robertson, I. H., Manly, T., Andrade, J., Baddeley, B. T., & Yiend, J. (1997). ‘Oops!’: Performance correlates of everyday attentional failures in traumatic brain injured and normal subjects. *Neuropsychologia, 35*(6), 747–758. https://doi.org/10.1016/S0028-3932(97)00015-8

Robison, M. K., Miller, A. L., & Unsworth, N. (2019). Examining the effects of probe frequency, response options, and framing within the thought-probe method. *Behavior Research Methods, 51*(1), 398–408. https://doi.org/10.3758/s13428-019-01212-6

Safati, A. B., Seli, P., & Smilek, D. (2026). The costs of monitoring: Does self-catching the wandering mind influence task performance and/or residual probe-caught mind-wandering? *Consciousness and Cognition, 144*, 104112. https://doi.org/10.1016/j.concog.2026.104112

Schooler, J. W., Smallwood, J., Christoff, K., Handy, T. C., Reichle, E. D., & Sayette, M. A. (2011). Meta-awareness, perceptual decoupling and the wandering mind. *Trends in Cognitive Sciences, 15*(7), 319–326. https://doi.org/10.1016/j.tics.2011.05.006

Seli, P., Cheyne, J. A., Barton, K. R., & Smilek, D. (2012). Consistency of sustained attention across modalities: Comparing visual and auditory versions of the SART. *Canadian Journal of Experimental Psychology, 66*(1), 44–50. https://doi.org/10.1037/a0025111

Seli, P., Jonker, T. R., Cheyne, J. A., & Smilek, D. (2013). Enhancing SART validity by statistically controlling speed-accuracy trade-offs. *Frontiers in Psychology, 4*, 265. https://doi.org/10.3389/fpsyg.2013.00265

Seli, P., Jonker, T. R., Solman, G. J. F., Cheyne, J. A., & Smilek, D. (2013). A methodological note on evaluating performance in a sustained-attention-to-response task. *Behavior Research Methods, 45*(2), 355–363. https://doi.org/10.3758/s13428-012-0266-1

Stawarczyk, D., & D’Argembeau, A. (2016). Conjoint influence of mind-wandering and sleepiness on task performance. *Journal of Experimental Psychology: Human Perception and Performance, 42*(10), 1587–1600. https://doi.org/10.1037/xhp0000254

Stawarczyk, D., Majerus, S., Maj, M., Van der Linden, M., & D’Argembeau, A. (2011). Mind-wandering: Phenomenology and function as assessed with a novel experience sampling method. *Acta Psychologica, 136*(3), 370–381. https://doi.org/10.1016/j.actpsy.2011.01.002

Van den Driessche, C., Chappé, C., Konishi, M., Cleeremans, A., & Sackur, J. (2025). States of mind: Towards a common classification of mental states. *Consciousness and Cognition, 129*, 103828. https://doi.org/10.1016/j.concog.2025.103828

Weinstein, Y. (2018). Mind-wandering, how do I measure thee with probes? Let me count the ways. *Behavior Research Methods, 50*(2), 642–661. https://doi.org/10.3758/s13428-017-0891-9

Wiemers, E. A., & Redick, T. S. (2019). The influence of thought probes on performance: Does the mind wander more if you ask it? *Psychonomic Bulletin & Review, 26*(1), 367–373. https://doi.org/10.3758/s13423-018-1529-3

Wilson, K. M., Finkbeiner, K. M., de Joux, N. R., Russell, P. N., & Helton, W. S. (2016). Go-stimuli proportion influences response strategy in a sustained attention to response task. *Experimental Brain Research, 234*(10), 2989–2998. https://doi.org/10.1007/s00221-016-4701-x

---

## 21. 本轮结论

SART + 思维探针适合作为 FocusWave 的实验参照，不是因为它们共同产生了一个无误差“注意标签”，而是因为它们在同一持续任务时间轴上提供了两个互补观察层：**SART 连续描述任务执行，probe 离散采样参与者能够报告的意识内容和困倦—清醒状态。** 高时间分辨率传感信号再围绕 probe 前窗口汇总，就可以检验不同生理/行为变量与这些观察层的一致、分离及额外预测信息。

当前 FocusWave 的总体方法方向与文献基本一致：行为不等同 Q1，Q1 不等同注意真值，Q2 与 Q1 分开，Go omission 与 No-Go commission 分开，并使用探针前窗口避免把探针后反应性混入状态参照。最需要在国赛叙事上进一步收紧的是三个语言边界：**SART 不是过程纯净的持续注意测验；Q1=2/3/4 不能统称走神；30 s 是项目正式时间尺度选择而不是领域标准窗口。**
