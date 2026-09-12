# E 线专题调研：心率、呼吸率与毫米波非接触测量

> 调研日期：2026-09-12  
> 服务对象：FocusWave 国赛报告第 2 章“理论与技术基础”  
> 建议章节标题：**2.5 心肺自主生理活动与毫米波非接触感知**（暂定）  
> 本文件为独立文献调研记录。本轮不据此直接重写第 2 章正文。

## 0. 先行结论

本专题必须把两个证据问题分开。第一，HR（heart rate，心率）和 BR（breathing/respiratory rate，呼吸率）在心理生理学上是否可能随持续注意、警觉维持、唤醒、心理负荷、疲劳和困倦变化；第二，FocusWave 使用的 FMCW（frequency-modulated continuous-wave，调频连续波）毫米波雷达能否把这些生理变化测得足够可靠。前者成立不代表后者成立，后者成立也不代表 HR/BR 已成为持续注意的特异性指标。

心理生理证据支持把 HR 和 BR 视为**与注意状态相关的自主生理信息**。持续注意下降、低唤醒、任务脱离与心率下降在部分持续注意范式中有直接证据；心理负荷和努力增加又常伴随心率、呼吸率上升，因此不存在“HR 越高注意越好”或“BR 越低越专注”的跨任务固定方向。HRV（heart rate variability，心率变异性）与 HR 也不是同一个指标：HR 主要描述单位时间内心搏频率，而 HRV 描述相邻心搏间期的时间变异，并可在严格测量与解释条件下反映心脏自主调节，尤其部分迷走神经调节信息。FocusWave 当前若只能可靠保留 HR 和 BR，仍可研究它们与 Q1 注意内容、Q2 警觉/困倦、行为表现、任务时间进程之间的关联，以及它们在已有行为信息后的增量预测价值；但不能据此推断迷走神经张力、交感/副交感平衡、HRV、压力或单一注意机制。

毫米波技术文献充分证明“可行性”，但证明条件通常比 FocusWave 当前正式场景更受控。FMCW 雷达可定位人体反射距离门，并利用胸壁微位移引起的回波相位变化提取呼吸和心搏相关周期。呼吸位移通常大于心搏微动，因此 BR 更容易形成高信噪比周期；HR 更易受到呼吸基波/高次谐波、目标选择、峰值选择、姿态、运动和多径影响。高质量研究使用 ECG（electrocardiogram，心电图）、PPG（photoplethysmography，光电容积描记）或呼吸带作为独立参考，并报告 MAE（mean absolute error，平均绝对误差）、RMSE（root mean square error，均方根误差）、偏差和 Bland–Altman 一致性界限，而不是只证明“算法在数据集上能给出合理数字”。

对 FocusWave 当前状态，毫米波主仓库 2026-09-12 的 P2（第二阶段心率恢复失败归因）在冻结的 5 场、100 个 probe（探针）30 s 窗口中，current control 的 fused HR（融合心率）MAE 为 `10.4601 bpm`，time HR 为 `8.9695 bpm`，spectral HR 为 `15.1134 bpm`；63 个 fused absolute error（融合绝对误差）>5 bpm 的窗口中，主要错误来自 selected-target 内 peak/candidate selection（峰/候选选择）、谐波/半倍频锁定以及 target/bin/channel（目标/距离门/通道）选择。最新决策仍为 `HR/BR = HOLD / SUPPORTING_ONLY`，`HRV = BLOCKED`，没有 `FORMAL_HR_READY`。Formal 旧结果索引记录的 2026-08-31 六场扩样 BR 支持性结果为 MAE `4.17 breaths/min`、median absolute error（绝对误差中位数）`1.70 breaths/min`，但 2026-09-12 P2 没有对 BR 完成新的晋级验证，因此该数字只能作为历史 supporting evidence（支持性证据），不能覆盖最新 canonical（规范）状态。

因此，国赛报告当前最安全的表述是：**FocusWave 设计上利用毫米波感知胸壁微动，并对由此估计的 HR/BR 作为注意状态相关自主生理信息进行独立测量有效性验证；现阶段项目内 HR/BR 仍属支持性/验证中指标，IBI（inter-beat interval，心搏间期）与 HRV 不进入正式生理结论。**

---

## 1. 调研问题与检索策略

### 1.1 两个独立证据问题

**A. 心理生理问题：**HR 和 BR 为什么可能随持续注意及其相关状态变化，它们能够表达什么层面的信息？

**B. 技术测量问题：**FMCW 毫米波能否在与 FocusWave 相近的非接触条件下可靠恢复 HR/BR，当前项目自己的误差和失败机制是否已经达到正式报告所需的测量有效性？

两部分的判据不同。心理生理部分优先使用持续注意/警觉、心理负荷、疲劳、心智游移和自主神经心理生理研究；技术部分优先使用雷达生命体征教程/综述和带 ECG、PPG、呼吸带或临床参考设备的实证研究。仅识别“专注相关动作”或在某数据集上做分类的毫米波工程论文，不作为 HR/BR 与持续注意之间的心理学证据。

### 1.2 检索与核验范围

2026-09-12 以以下组合进行独立检索并逐篇核验题名、作者、年份、期刊、DOI（digital object identifier，数字对象唯一标识符）、研究设计和效标：

- `sustained attention / vigilance + heart rate / heart rate variability / respiration`；
- `arousal / mental workload / fatigue / drowsiness + heart rate / respiration`；
- `SART + ECG / cardiac / thought probe`；
- `FMCW radar + heart rate / respiration + ECG / PPG / respiration belt`；
- `mmWave + vital signs + validation / Bland-Altman / IBI / HRV`；
- `radar vital signs review / tutorial + motion / posture / multipath / harmonic`。

来源以 PubMed/PMC、Psychophysiology、Applied Ergonomics、Biological Psychology、Clinical Neurophysiology、Proceedings of the IEEE、IEEE Internet of Things Journal、IEEE Sensors Journal 等期刊/出版商页面为主。Google Drive 中 `Preparation`、`Analysis`、`Reports`、`Literature` 的历史毫米波材料仅用于追溯项目旧方案和已有文献线索；当其与 GitHub 当前 canonical/state/result 不一致时，以 GitHub 当前实现和验证为准。

### 1.3 FocusWave 当前状态核对

本次调研开始前核对：

- 报告工作区：`FocusWave-Formal-Analysis/国赛报告/`；
- 报告工作分支：`codex/code-fix-ledger`；本轮写入前 HEAD 为 `51ffefa6e90f8061c3b18ecc79065961516eade3`；
- `国赛报告/README.md`、`0-总结构与研究叙事_20260912.md`、当前 A/B/C/D/F 调研与 2.1–2.3 正文；
- `毫米波分析/README.md` 与 `毫米波分析/结果索引.md`；
- 毫米波主仓库 `greenboo26/focuswave-multimodal-attention-analysis` 当前 `main`；读取时 HEAD 为 `e4c77ceed887ea0d06f21e067914d6f8e0f8aba4`；
- 当前 canonical interface（规范接口）、2026-09-12 HR recovery（心率恢复）P0/P1/P2 决策与 P2 真实验证报告；
- 当前 HRV beat-level gate（逐搏层门控）结果。

Drive 旧文件 `044-毫米波HR与HRV分析指南.md` 仍保留了“平均 HR/BR、逐搏 IBI、HRV 必须分级验证”的正确方法学框架，但其“尚无正式外部参考验证”等状态已经被后续 GitHub 结果更新；旧 `2.4-现有测评技术与毫米波感知.md` 的技术文献可作为历史线索，不能替代本轮独立核验。

---

## 2. 心率的心理生理证据

### 2.1 HR 是自主生理反应，不是持续注意的直接读数

HR 由窦房结自发节律和自主神经、体液、呼吸、姿态、运动及代谢需求共同调节。现代 Psychophysiology（心理生理学）方法指南强调，HR/HRV 的解释需要结合采集方法、参与者特征和实验条件；不能把单个 HR 数值直接映射到某个心理构念（Quigley et al., 2024）。

对持续注意而言，Oken、Salinsky 与 Elsas（2006）指出 vigilance（警觉维持）、tonic alertness（紧张性警觉）与 sustained attention（持续注意）在文献中高度重叠，但同时包含睡眠—觉醒轴上的 arousal（唤醒）与认知表现成分。自主神经指标可反映这一状态系统的一部分，却不能取代行为测量。这一点与 FocusWave 当前第 2.1 的构念边界一致：唤醒影响持续注意，但不等于持续注意。

### 2.2 持续注意下降与低唤醒时，HR 可下降，但方向依赖任务机制

Pattyn 等（2008）在 90 min 持续警觉任务中同步记录 ECG 和呼吸。随 time-on-task（任务持续时间）增加，行为反应变慢，heart period（心搏周期，即 HR 的倒数）和 RSA（respiratory sinus arrhythmia，呼吸性窦性心律不齐）增加，作者将其解释为支持 underload/underarousal（低负荷/低唤醒）路线。换言之，该范式中注意维持恶化伴随总体心率下降和更高的部分迷走调节表现。

更直接贴近 FocusWave 的证据来自 Corcoran 等（2025）。65 名成人完成 SART（sustained attention to response task，持续性注意反应任务），同时记录 ECG、EEG（electroencephalography，脑电）和瞳孔，并使用 thought probe（思维探针）区分 on-task（任务内）、mind-wandering（心智游移）、mind-blanking（思维空白）及 alertness/sleepiness（警觉/困倦）。研究发现：更低 HR 预测更低 vigilance（警觉）、更小瞳孔和更慢反应；mind-blanking 伴随更明显的 HR 下降，而 mind-wandering 的突出心脏特征则更多体现在 HRV 增大。该结果说明 HR 能携带与探针前唤醒/任务脱离有关的信息，但不同形式的“注意不在任务上”并不共享同一种心脏模式。

这也解释了为什么不能设定“HR 越高越专注”的普遍规则。当任务本身需要更高努力、压力或心理负荷时，HR 可因能量动员和自主激活上升；当长时单调任务进入低唤醒、无聊或困倦时，HR 又可能下降。Charles 与 Nixon（2019）对 58 篇心理负荷研究的系统综述指出，多种心血管和呼吸指标能区分任务负荷，但不存在一种生理指标可在所有环境中清晰、唯一地区分心理负荷。

### 2.3 HR 与 mental workload（心理负荷）和 effort（努力）的关系

心理负荷不是持续注意本身。Tao 等（2019）系统综述 91 项研究后发现，心血管指标是最常使用的心理负荷生理测量之一，且多数研究报告与负荷变化存在显著关系，但有效性明显依赖任务领域和具体指标。Charles 与 Nixon（2019）同样强调 task type（任务类型）、task load（任务负荷）和 task difficulty（任务难度）都可改变生理反应。

因此在 SART 中，如果某个时期 HR 升高，至少存在多种可能解释：更高警觉、更大努力投入、任务困难/冲突、压力、情绪激活、姿态/动作变化等。HR 的优势在于连续、客观地提供一个自主激活通道，而不是具有构念特异性。

### 2.4 fatigue（疲劳）、drowsiness（困倦）与 HR

疲劳同样不是单一机制。长时认知任务可出现 mental fatigue（心理疲劳）、低唤醒、无聊、动机下降和策略改变。Pattyn 等（2008）显示，在单调警觉任务中 HR 下降与低唤醒路线一致；Corcoran 等（2025）又在 SART 中直接观察到低 HR 与低警觉/困倦相关。

但更丰富的疲劳信息往往出现在 HRV 而非平均 HR。Csathó、Van der Linden 与 Matuz（2024）系统回顾 19 项 time-on-task 诱发心理疲劳研究，17 项观察到 HRV 随任务持续时间显著变化，较一致的变化集中在低频成分和时域指标，尤其 RMSSD（root mean square of successive differences，相邻正常心搏间期差值均方根）。这说明如果科学问题是“自主调节如何随疲劳发展”，HRV 理论上比单纯平均 HR 提供更多信息；同时也意味着 FocusWave 当前 HRV 被技术验证门挡住后，不能用 HR 去替代 HRV 的生理含义。

---

## 3. 呼吸率的心理生理证据

### 3.1 BR 对认知负荷敏感，但并非注意特异性指标

Grassmann 等（2016）系统回顾 54 个实验，发现 cognitive load（认知负荷）总体伴随更快的呼吸和更高 minute ventilation（分钟通气量）；更高任务难度还可进一步提高 respiratory rate（呼吸率）。在可计算效应量的研究中，约一半关于基线到任务的显著 RR 增加达到中到大效应。相比之下，tidal volume（潮气量）对心理负荷的变化更不一致。

这一证据支持 BR 作为“任务相关生理激活”通道，但不支持 BR 直接作为持续注意水平。Grassmann 等明确区分 mental load（心理负荷）与 mental stress（心理压力）：两者都可能引起自主/呼吸变化，但情绪评价和应对机制不同。反馈、焦虑等情绪因素也可改变呼吸模式。

### 3.2 持续注意/警觉中的呼吸证据较 HR 更间接

呼吸研究的主体集中在认知负荷、压力和情绪，而不是 SART 探针状态。Grassmann 等的综述指出 vigilance（警觉维持）可能有特定呼吸模式，但直接数据库仍不足。Wientjes（1992）的经典综述也指出，呼吸同时反映代谢、心理负荷、压力、情绪和主观不适；呼吸率只是呼吸系统多个维度之一。

因此 FocusWave 若使用 BR，最合理的问题是：**在同一实验、同一人的探针前窗口中，BR 是否随 Q2 警觉/困倦、Q1 注意内容、time-on-task 和行为表现发生稳定变化？** 不能预先规定“更专注 = 呼吸更快”或“更困 = 呼吸更慢”。

### 3.3 BR 的解释应保留呼吸本身的行为性质

呼吸既受自主调节，也可被说话、吞咽、叹气、主动深呼吸、姿势改变和运动直接改变。人在认知任务中还可能出现短暂屏息、呼吸变浅、加快或周期不规则。只保留“每分钟呼吸次数”会丢失深度、变异性、叹气和吸呼比例等信息。

所以当前只有 BR 时，报告应将它称为**呼吸频率/呼吸节律的低维摘要**，而非“呼吸系统唤醒指数”。

---

## 4. HR/BR 与注意、唤醒、疲劳等构念的边界

### 4.1 HR 与 HRV 的理论区别

HR 和 HRV 来源于同一心搏序列，但回答不同问题：

| 指标 | 基本定义 | 主要信息层级 | 不能自动推出 |
| --- | --- | --- | --- |
| HR（心率） | 单位时间心搏数，或平均 IBI 的倒数 | 总体心脏节律快慢、整体自主/代谢反应 | 交感/副交感成分、迷走神经张力、逐搏调节质量 |
| IBI（心搏间期） | 相邻心搏时点之间的间隔 | 逐搏时间结构，是 HRV 的原始基础 | 仅平均 IBI 正确不代表每个 beat（心搏）时点正确 |
| HRV（心率变异性） | IBI 序列的时间/频率/非线性变异 | 心脏自主调节动态；特定指标在严格条件下可联系迷走调节 | 简单“交感/副交感平衡”；LF/HF（低频/高频比）等也不应被粗糙解释 |

Quigley 等（2024）的 Society for Psychophysiological Research（心理生理研究学会）委员会指南明确强调 HR/HRV 的测量、派生和解释边界，并反对把 LF（low frequency，低频）或 LF/HF 简单解释为心脏交感活动。Laborde、Mosley 与 Thayer（2017）则指出，以迷走调节为研究目的时，RMSSD、pNN50（相邻正常心搏间期差值超过 50 ms 的比例）和 HF（high frequency，高频）HRV 等需要足够精确的逐搏间期、合适记录长度、运动控制和呼吸信息。

因此，FocusWave 当前即使 HR 平均值未来通过验证，也不能据此开放 IBI/HRV；逐搏时点是一个更严格的技术门。

### 4.2 如果只可靠保留 HR 和 BR，可以回答什么

可以回答：

1. 探针前 HR/BR 的水平和时间变化是否与 Q1 注意内容、Q2 警觉/困倦相关；
2. 同一参与者内部，HR/BR 是否随行为波动、time-on-task 或主观状态共同变化；
3. 在控制 task/block/order（任务/区块/顺序）、运动、覆盖率等因素后，这些关系是否仍存在；
4. HR/BR 在已有行为信息之后是否提供可重复的增量预测信息；
5. 在未参与训练的新参与者上，这些信息是否具有泛化价值。

不能回答：

- “自主神经系统处于某种确定的交感/副交感状态”；
- “HR 下降就是注意下降”或“BR 上升就是高注意”；
- “HR/BR 是持续注意的特异性生物标志物”；
- 真实 IBI、RMSSD、SDNN（standard deviation of NN intervals，正常心搏间期标准差）、LF/HF 或其他 HRV；
- 临床级心脏或呼吸监测精度；
- 压力、情绪、疲劳、困倦、心理负荷与注意之间的单一因果归属。

### 4.3 主要混杂因素的重要性

运动、姿态、压力/情绪、年龄和体能不是次要噪声，而是 HR/BR 解释的核心边界。

- **运动与身体微动：**既真实提高心率/呼吸，又直接污染毫米波胸壁微动信号，因此同时是生理混杂和测量伪迹来源。
- **姿态：**改变心血管调节、呼吸机械和雷达散射几何。HRV 方法指南要求固定/报告姿态；毫米波研究也显示胸部朝向会改变误差。
- **压力与情绪：**可独立改变 HR 和呼吸。认知负荷与心理压力在实验上经常混淆，呼吸尤其受焦虑、紧张和主动应对影响。
- **年龄与体能：**会影响静息 HR、最大心率、自主调节和恢复速度；跨参与者绝对水平比较若不控制这些差异，容易把个体生理基线误认为注意差异。
- **呼吸—心脏耦合：**呼吸本身会调节心搏间期，HRV 的部分指标高度依赖呼吸；即使只分析 HR，也应避免把明显呼吸/运动改变解释成注意特异效应。

因此，FocusWave 更应利用 repeated measures（重复测量）结构做 participant-level（参与者层）控制、人内中心化和任务进程控制，而不是依赖跨人的绝对 HR/BR 阈值。

### 4.4 报告术语建议

建议正式使用：

> **“与注意状态相关的自主生理信息”**

或更具体：

> **“探针前心率与呼吸率提供的心肺自主生理状态信息”**。

不建议在理论章节把 HR/BR 单独称为“注意指标”“专注度指标”或“注意生物标志物”。只有在本项目内部完成测量有效性和效标关系验证后，才可以写“对注意状态预测具有信息”。

---

## 5. FMCW 毫米波生命体征测量原理

### 5.1 从 chirp（线性调频脉冲）到胸壁微位移

FMCW 雷达连续发射频率随时间线性变化的 chirp。接收人体反射回波后，发射与接收信号混频形成 beat signal（拍频信号）；beat frequency（拍频）主要编码目标距离。对连续 chirp 做 range FFT（距离向快速傅里叶变换）后，可获得不同 range bin（距离门）的反射复数值。

对于相对静止的被试，胸壁因呼吸和心脏机械活动产生亚厘米到亚毫米级周期位移。位移会改变传播路径长度，从而调制选定距离门复数回波的 phase（相位）。相位展开、去趋势和带通/分解后，可以分别搜索呼吸与心搏频带中的周期成分，估计 BR 和 HR。Paterniani 等（2023）的 Proceedings of the IEEE 教程系统总结了这一路径，并强调雷达体制、目标选择、相位处理、运动抑制和算法假设共同决定结果。

### 5.2 为什么 HR 通常比 BR 更难

这里的“通常”指信号物理和算法难度，不代表每篇研究的最终误差都必然 HR > BR。

1. 呼吸造成的胸壁位移通常显著大于心搏微动，心搏信号 SNR（signal-to-noise ratio，信噪比）更低；
2. 呼吸的基波及高次谐波可能落入 HR 频带，造成错误 peak（峰值）或 half/double-frequency lock（半倍频/倍频锁定）；
3. 小幅姿态改变、手臂/躯干运动和多径反射的位移幅度可远大于心搏；
4. HR 常需要在多个 target/bin/channel 候选之间做更精细的选择和融合；
5. 若要进一步得到 IBI，问题从“找一个窗口平均主频”升级为“逐个定位每次心搏时点”，误差要求更严。

Yao 等（2024）在 IEEE Internet of Things Journal 中明确指出，呼吸估计主要受噪声限制，而 HR 的主要困难是强呼吸信号及其高次谐波干扰。Sacco 等（2020）的姿态实验也观察到 HR 数据离散度高于呼吸，并将其归因于心搏引起的胸壁位移更小。

---

## 6. 毫米波 HR/BR 的外部验证证据

### 6.1 高质量验证应验证“测量”，而不只是“算法输出”

真正的生理测量验证至少需要：

- 同步独立参考：HR 使用 ECG/高质量 PPG，BR 使用呼吸带、呼吸感应体积描记或临床呼吸参考；
- 同一时间窗配对；
- 报告误差而不仅是 correlation（相关）；
- 报告 bias（偏差）、Bland–Altman limits of agreement（一致性界限）、coverage（覆盖率）和失败率；
- 覆盖与目标场景相符的距离、姿态、运动和参与者差异；
- 参数/算法选择不能借助测试集参考真值反向调优。

只在公开数据集上优化 RMSE、只报告雷达内部 time/frequency（时域/频域）一致性、或只看输出是否落在“正常人体范围”，均不能替代外部生理效标。

### 6.2 代表性实证

**Sacco et al. (2020)**：5 名参与者，胸前、左侧、背部、右侧四种朝向；用 PPG 作为 HR 参考、呼吸带作为 BR 参考。两类速率的回归斜率均接近 1，但 HR 离散更大。该研究支持“姿态改变下仍有可测性”，同时显示朝向和心搏微动幅度会影响质量。

**Turppa et al. (2020)**：10 名参与者、不同卧姿和模拟不同心肺状态，以 Embla Titanium 临床设备为参考。总体 relative MAE（相对平均绝对误差）为 HR 3.6%、BR 9.1%；BR 的 overall MAE 约 `1.414 breaths/min`。它说明同一雷达系统在特定睡眠样场景中可实现较好速率估计，但也提醒“BR 一定比 HR 数值误差更小”并非每项实验都成立。

**Wang et al. (2021), mmHRV**：商用毫米波系统、11 名参与者，进一步验证逐搏 IBI；报告 median IBI error（心搏间期误差中位数）`28 ms`，非视距条件 RMSE `31.71 ms`，并考察距离、朝向、入射角、遮挡和多用户。该研究证明毫米波在专门设计和验证条件下可以达到逐搏分析级别，但它不构成 FocusWave 当前设备/算法的外推证据。

**Yao et al. (2024)**：77 GHz FMCW，8 名参与者，与可靠参考传感器比较；BR RMSE <`1 breath/min`、HR RMSE <`1.5 bpm`，并报告 Bland–Altman 高一致性。论文同时把 HR 难点定位到呼吸及其高次谐波干扰。该研究说明先进估计器在受控条件下可把 HR/BR 做到很低误差，但不能用于替代项目自身外部验证。

这些论文共同说明：毫米波 HR/BR 的“技术上可测”已有充分先例；精度是**系统—算法—场景联合属性**，不是“毫米波”这个传感器类别天然拥有的属性。

---

## 7. 主要技术限制

### 7.1 距离与 target/bin/channel 选择

FMCW 能提供距离分辨率，但“人体反射最强点”并不总等于“心肺微动最优点”。衣物、桌面、椅背、手臂、身体不同部位和静态强反射可形成多个候选。若 target/bin/channel 选择不稳定，后面的频谱峰值可能来自错误散射点。

### 7.2 姿态与朝向

胸壁朝向天线时通常更容易获得明显微动；侧向、背向或身体倾斜会改变径向位移分量和反射强度。Sacco 等（2020）直接将胸前/左右/背向作为验证因素。毫米波结果因此必须报告实验几何，而不能把不同姿态混成无条件的“设备精度”。

### 7.3 运动

random body movement（随机身体运动）是雷达生命体征长期公认的主要瓶颈。身体位移的幅度通常远高于心搏和呼吸微动，可改变距离门、相位和多普勒。运动既可制造假峰，也可让真实峰消失。对于 FocusWave，D 线所研究的身体运动不能只被当成另一个心理特征，它同时是 E 线的生理测量质量变量。

### 7.4 多径与环境反射

桌面、墙壁、屏幕、人体其他部位会产生 multipath（多径）和静态/动态 clutter（杂波）。多径可使同一胸壁运动在多个 bin/channel 出现，或与其他反射叠加。算法若在测试数据上从大量候选中挑到“恰好接近参考值”的频率，会产生 oracle-like（近似预知真值式）选择偏差，因此 candidate pool（候选池）“包含真值”不等于 production selector（正式选择器）已验证。

### 7.5 呼吸谐波与心搏峰选择

这是 HR 的关键困难。呼吸基频通常低于 HR，但二、三、四次谐波可进入心搏频带；同时机械运动也可产生窄频峰。仅用“最高峰”或在结果后做倍/半频修正，容易过拟合。需要冻结候选生成、峰选择、融合和质量门，并在独立参与者上验证。

### 7.6 外部参考与时间对齐

参考信号必须与 radar window（雷达窗口）共享可靠时间轴。ECG 适合逐搏 R peak（R 波峰）与 HR；PPG 可用于平均 HR，但脉搏传播延迟会影响逐搏时间对齐；BR 参考宜使用呼吸带/呼吸感应体积描记。FocusWave 已完成 DLL timestamp（动态链接库时间戳）主线修复，但任何新的算法比较仍需保持相同 frame identity（帧身份）、window identity（窗口身份）和 reference identity（参考身份）。

---

## 8. 当前 FocusWave 毫米波状态与外部证据对照

### 8.1 当前正式角色

毫米波主仓库当前 canonical interface 明确：

- HR：`HOLD / SUPPORTING_ONLY`；
- BR：`HOLD / SUPPORTING_ONLY`；
- IBI/HRV：`BLOCKED / EXCLUDE`；
- target/bin/channel、phase stability（相位稳定性）、motion-like proxy（运动类代理）等主要作为 diagnostic（诊断）信息；
- 当前正式窗口为 `pre_30s`，30 s、60 s 等不同时间合同不能混用；
- 历史 60 s fixed-target（固定目标）HR MAE ≈`3.777 bpm` 是旧校准 comparator（比较基线），不能写成当前 30 s 正式链精度。

### 8.2 2026-09-12 P2：当前 HR 最关键的新证据

P2 固定 5 场、100 个探针窗口，ECG 只在雷达 target/candidate（目标/候选）生成后用于 retrospective failure attribution（回顾性失败归因），没有进入调参。current control：

- fused HR MAE = `10.460107 bpm`；
- time HR MAE = `8.969469 bpm`；
- spectral HR MAE = `15.113444 bpm`；
- 37/100 为 `CORRECT_OR_NEAR_CORRECT`；
- 28/100 为 `SELECTED_TARGET_WRONG_PEAK`；
- 18/100 为 `HARMONIC_OR_HALF_DOUBLE_LOCK`；
- 17/100 为 `TARGET_BIN_CHANNEL_MISS`。

在 63 个 fused AE >5 bpm 的失败窗中，44.4% 归于 selected-target peak/candidate error，28.6% 为谐波/半倍频锁定，27.0% 为 target/bin/channel miss。Fusion（融合）相对 time HR 改善/恶化/不变为 31/47/22；time HR 当前反而优于 fused HR。P2 因而将主要剩余机制定位为 `SELECTED_TARGET_ESTIMATOR_PEAK_AND_FUSION_PATH`，并继续保持 HR/BR `HOLD`、HRV `BLOCKED`。

这个结果与外部文献高度一致：外部研究反复指出 HR 的主要困难是较弱心搏微动、呼吸谐波、目标选择与峰选择；FocusWave 当前的真实失败也集中在这些环节，而不是“毫米波原理不可行”。

### 8.3 BR：已有支持性外部验证，但没有完成最新晋级

Formal `毫米波分析/结果索引.md` 登记 2026-08-31 pre_30s 六场扩样：100 个 ECG 有效 probe 窗中，BR MAE `4.17 breaths/min`、medianAE `1.70`、half-frequency lock（半频锁定）`12/100`。同一旧阶段 HR 30 s fused MAE 为 `10.83 bpm`。

这表明 FocusWave 自身 BR 当前明显具备“可提取、与外部 RSP（respiration reference signal，呼吸参考信号）有一定一致性”的支持证据；但 2026-09-12 HR recovery P2 没有执行新的 BR estimator repair（呼吸率估计器修复）或晋级验证，canonical 仍明确保持 `BR = HOLD / SUPPORTING_ONLY`。因此新报告不应把 4.17 写成“最终准确度”，更不应把 BR 称为已验证正式指标。

### 8.4 IBI/HRV：当前仍应排除

项目当前 beat-level validation（逐搏验证）比平均 HR 更直接决定 HRV 可否使用。5 场、16 个 block（区块）的扩样结果在 ±75 ms 一对一匹配下：

- ECG R peaks（R 波峰）matched：`198/1364`；
- radar peaks（雷达心搏峰）=`1089`；
- sensitivity（灵敏度）=`0.145161`；
- precision（精确率）=`0.181818`。

该门控明确给出 `HRV_BLOCKED`，且没有计算正式 RMSSD/SDNN/LF/HF。平均 HR 即使未来达到低误差，也可能由漏峰和多检相互抵消而“平均正确”；HRV 需要连续、准确的逐搏时点，所以这是独立且更严格的验证层。

外部 mmHRV 文献证明“毫米波逐搏 IBI 可以被做准”，但恰恰因为 Wang 等（2021）使用专门 heartbeat extractor（心搏提取器）并针对 IBI 误差验证，它不能成为 FocusWave 当前低 beat-match rate（逐搏匹配率）的豁免证据。因此当前 IBI/HRV 继续排除是项目状态和外部方法学共同支持的结论。

---

## 9. 文献证据矩阵

| 证据问题 | 来源 | 设计/效标 | 关键结果 | 对 FocusWave 的支持 | 主要边界 |
| --- | --- | --- | --- | --- | --- |
| 持续注意与自主生理 | Oken et al., 2006 | vigilance/alertness 综述 | 持续注意与唤醒系统相关；自主指标可测其部分生理状态 | HR/BR 可作为辅助生理通道 | 唤醒不等于注意构念 |
| vigilance decrement（警觉下降）与心脏 | Pattyn et al., 2008 | 90 min 注意任务；ECG+呼吸 | time-on-task 后 heart period、RSA 增大，行为变慢 | 低唤醒/长时任务中 HR 可下降 | 具体范式，不能固定方向 |
| SART 探针状态与心脏 | Corcoran et al., 2025 | n=65；SART+thought probe+ECG+EEG+瞳孔 | 低 HR 预测低警觉；mind-blanking HR 更低；mind-wandering HRV 更高 | 与 FocusWave 范式最接近；支持 probe-aligned cardiac features（探针对齐心脏特征） | HR 与 HRV 对不同脱离状态含义不同 |
| 心理负荷与呼吸 | Grassmann et al., 2016 | 54 个实验系统综述 | 负荷通常伴随更快 RR；任务难度可进一步提高 RR | BR 对任务相关激活敏感 | 压力、情绪、任务类型均可改变呼吸 |
| 心理负荷多指标 | Charles & Nixon, 2019 | 58 篇系统综述 | 多种生理指标可区分负荷，但无单一指标普遍有效 | 支持多模态而非单变量指数 | 不直接证明持续注意 |
| mental fatigue（心理疲劳）与 HRV | Csathó et al., 2024 | 19 项系统综述 | 多数研究 HRV 随 time-on-task 改变，RMSSD 等较一致 | 说明 HRV 理论价值高于仅 HR | 当前项目 HRV 技术上未通过 |
| HR/HRV 方法学 | Quigley et al., 2024 | Psychophysiology 委员会指南 | 强调测量、参与者、姿态、呼吸和解释边界 | 支持 HR≠HRV、控制混杂 | 不是注意效标研究 |
| 雷达生命体征总体原理 | Paterniani et al., 2023 | Proceedings IEEE 教程综述 | 雷达相位微动可估计心肺；设备/姿态/运动/算法决定性能 | 支持 FMCW 技术基础 | 不证明 FocusWave 自身精度 |
| 不同胸部朝向验证 | Sacco et al., 2020 | 5 人；PPG+呼吸带 | 四种朝向均可测；HR 离散高于 BR | 支持姿态是验证维度；心搏更难 | 样本小、设备不同 |
| 睡眠样场景验证 | Turppa et al., 2020 | 10 人；临床参考设备 | HR relative MAE 3.6%，BR 9.1%；BR MAE 1.414/min | 证明受控条件下速率可达较好一致性 | 误差排序依任务/算法，不可外推 |
| 逐搏 HRV 可行性 | Wang et al., 2021 | 11 人；毫米波 HRV；多距离/朝向/NLOS | median IBI error 28 ms；NLOS RMSE 31.71 ms | 证明逐搏毫米波可行 | 专门系统结果不能转移到 FocusWave |
| HR/BR 高精度估计 | Yao et al., 2024 | 8 人；77 GHz FMCW+外部参考 | BR RMSE <1/min，HR <1.5 bpm；Bland–Altman 高一致性 | 给出测量验证范式与技术上限示例 | 受控环境、不同算法/硬件 |
| FocusWave 当前 HR | P2, 2026-09-12 | 5 场100 probe；ECG retrospective attribution | fused/time/spectral MAE 10.46/8.97/15.11 bpm | 真实项目当前边界 | 尚未达到 formal promotion |
| FocusWave 当前 BR | Formal 结果索引, 2026-08-31 | 6 场100 probe；RSP reference | MAE 4.17/min，medianAE 1.70；半频锁定12% | 有 supporting evidence | 尚无 09-12 新晋级验证 |
| FocusWave 当前 IBI/HRV | beat-level gate, 2026-08-31 | 5 场16 blocks；ECG beat match | sensitivity .145，precision .182 | 直接支持继续排除 HRV | 逐搏检测器/选择链未过门 |

---

## 10. 当前能写进国赛报告的内容

### 10.1 理论与技术基础可以写

1. HR/BR 会随自主生理激活、心理负荷、唤醒和疲劳等过程变化，因此可能携带与持续注意状态相关但非特异的信息。
2. 在持续注意任务中已有直接心脏证据：低警觉/某些任务脱离状态可伴随较低 HR；不同心智状态可能表现不同的 HR/HRV 特征。
3. 认知负荷常伴随 RR 加快，但 RR 同时受压力、情绪、代谢和行为影响。
4. FMCW 雷达可通过目标距离定位和胸壁微动相位调制，非接触估计呼吸和心搏相关周期。
5. 外部研究使用 ECG、PPG 和呼吸带已证明，在特定硬件、距离、姿态和算法条件下，毫米波 HR/BR 可以达到较低误差。
6. 心搏微动通常弱于呼吸，HR 更容易受到呼吸谐波、峰值选择和运动干扰；因此 HR/BR 必须分别验证。
7. FocusWave 当前正在用同步 ECG/RSP 对毫米波 HR/BR 做独立外部效标验证，当前 role 仍为 supporting-only（仅支持性）。
8. FocusWave 当前不把 IBI/HRV 作为正式生理指标。

### 10.2 方法/结果部分当前可以安全声称

可以写到的最高强度为：

> “项目已建立毫米波胸壁微动到 HR/BR 候选估计的完整处理链，并完成小规模同步 ECG/RSP 外部效标审计。现有结果证明信号链能够恢复部分心肺频率信息，同时揭示 HR 的峰值选择、呼吸谐波和 target/bin/channel 选择仍是主要误差来源，因此 HR/BR 当前仅作为支持性候选生理信息，不将其视为已完成测量验证的正式注意指标。”

如果国赛报告需要呈现最新数字，应明确写成**验证样本上的当前算法性能**，同时给出分母、窗口、参考设备、MAE/medianAE/bias/coverage，并标注 `supporting-only`，不得只展示表现较好的历史 60 s `3.777 bpm`。

---

## 11. 当前不能写的内容

当前不应出现以下表述：

- “毫米波准确测得了所有被试的心率/呼吸率”；
- “FocusWave 的毫米波 HR 已达到医疗级/临床级精度”；
- “HR 或 BR 是注意力指标/专注度指数”；
- “HR 越高注意越好”“BR 越低越专注”等固定方向；
- “毫米波 HRV 已验证”“可以测真实 IBI/RMSSD/SDNN/LF/HF”；
- 用 `3.777 bpm` 历史 60 s fixed-target 结果代表当前 30 s dynamic-target 正式链；
- 用 mmHRV、Yao 等外部系统的高精度替代 FocusWave 自己的测量误差；
- 用 Ge 等“concentration monitoring（专注监测）”动作分类论文证明 HR/BR 与持续注意构念的心理学关系；
- 仅凭雷达 HR/BR 与 Q1/Q2 显著相关，就宣称雷达完成了生理测量验证。若底层量测有系统误差或状态相关伪迹，统计关联本身不能证明量测准确。

---

## 12. 对 2.5 结构和标题的建议

当前暂定标题“**2.5 心肺活动、唤醒与非接触生理感知**”容易让读者把“心肺活动 → 唤醒 → 注意”理解为单一路径，也容易把毫米波技术可测性和心理构念有效性写在一起。建议修改为：

> **2.5 心肺自主生理活动与毫米波非接触感知**

正文按两个层次组织：

**第一段/小层次：心率与呼吸率作为注意相关自主生理信息。** 说明 HR/BR 与唤醒、心理负荷、疲劳、任务投入均有关，方向受任务和个体影响，因此它们提供的是辅助生理通道，不是持续注意的特异性指标；HR 与 HRV 分开解释。

**第二段/小层次：毫米波非接触心肺微动感知及测量边界。** 简述 FMCW 距离定位—相位微动—呼吸/心搏频率提取，随后立即说明运动、姿态、多径和呼吸谐波限制，并用外部 ECG/PPG/呼吸带验证研究说明“技术上可行但必须本项目验证”。

如果第 2 章篇幅允许，可在段末加一句项目定位：FocusWave 将毫米波 HR/BR 作为待外部效标验证的自主生理通道，与行为、眼部和外显运动信息互补；正式效度由后续方法与结果章节单独给出。

不建议在 2.5 中展开当前 P2 的所有误差数字；理论章只保留“当前项目需独立验证”的边界，P2 数字放方法/结果或附录更合适。

---

## 13. 需要回到毫米波代码/验证线解决的问题

1. **HR estimator path（心率估计路径）修复优先于新增心理分析。** P2 已将主要故障定位到 selected-target 内 peak/candidate selection 和 fusion；在这条链冻结前不应继续扩大 HR 与 Q1/Q2 的正式统计解释。
2. **BR 需要基于当前 canonical 30 s 链重做/确认独立外部验证。** 08-31 的 BR 结果可以保留为 supporting comparator（支持性比较），但当前报告若要给“最新 BR 性能”，需要与 09-12 当前 window/selector/timestamp 合同完全一致的结果。
3. **验证集必须扩大并保持 participant-disjoint（参与者互斥）。** 当前 HR P2 为 5 场100 probe，足以做机制定位，不足以证明跨参与者稳定测量性能。后续应预先冻结参与者/场次分母和 held-out（留出）验证方案。
4. **预注册 acceptance gate（接受门槛）。** 不能跑完结果后再决定“多少 bpm 算可用”。门槛应根据用途决定：如果用于检测探针前细微人内状态差异，测量误差必须明显小于预期生理变化尺度；并同时考虑 bias、limits of agreement、coverage 和 failure rate，而非只看 MAE。
5. **把运动/姿态作为双重变量处理。** 它们既是心理相关外显状态，也是毫米波生理测量质量因素。验证输出应分层报告高/低运动、不同坐姿/朝向、target stability（目标稳定性）下的误差，而不是仅做总体平均。
6. **不要通过 outcome-derived quality cutoff（由结果反推质量阈值）“清掉坏结果”。** P2 当前正确地没有根据 ECG 误差新建 confidence/motion cutoff；后续 QC 阈值必须先于最终 held-out 验证冻结。
7. **IBI/HRV 单独立项，继续阻断下游。** 只有逐搏 sensitivity/precision、timing error（时间误差）、paired IBI error（配对心搏间期误差）通过预先规定门槛后，才讨论 RMSSD/SDNN 等；平均 HR 晋级不能自动开放 HRV。
8. **正式报告需要 measurement-validation manifest（测量验证清单）。** 至少固定 algorithm commit、reference device、timestamp mapping、window、target/selector/fusion 版本、样本分母、排除原因、MAE/medianAE/bias/RMSE/Bland–Altman/coverage/failure，并保持结果可追溯。

---

## 14. 推荐优先阅读的 8 篇核心文献

1. **Corcoran et al. (2025)**：与 FocusWave 最接近的 SART + thought probe + ECG + pupil/EEG 直接证据，说明 HR/HRV 与不同任务脱离和警觉状态的关系并不相同。
2. **Grassmann et al. (2016)**：呼吸与认知负荷系统综述，最适合界定 BR 能支持什么、不能支持什么。
3. **Quigley et al. (2024)**：Society for Psychophysiological Research 的 HR/HRV 方法学与解释指南，用于限制 HR→HRV/自主神经推断。
4. **Csathó et al. (2024)**：time-on-task 心理疲劳与 HRV 系统综述，说明 HRV 的理论价值及其与平均 HR 的区别。
5. **Paterniani et al. (2023)**：Proceedings of the IEEE 雷达生命体征教程综述，作为 FMCW 原理和工程限制的核心技术依据。
6. **Wang et al. (2021)**：mmHRV 逐搏 IBI 外部验证，说明雷达 HRV 真正需要达到什么验证层级。
7. **Yao et al. (2024)**：77 GHz FMCW HR/BR 外部参考验证，直接说明呼吸谐波为何使 HR 更难，并提供严格的误差/一致性范式。
8. **Sacco et al. (2020)**：PPG+呼吸带、不同胸部朝向，直接支持姿态/朝向对毫米波心肺测量的重要性。

---

## 15. 参考文献（APA 第 7 版）

Charles, R. L., & Nixon, J. (2019). Measuring mental workload using physiological measures: A systematic review. *Applied Ergonomics, 74*, 221–232. https://doi.org/10.1016/j.apergo.2018.08.028

Corcoran, A. W., Le Coz, A., Hohwy, J., & Andrillon, T. (2025). When your heart isn’t in it anymore: Cardiac correlates of task disengagement. *Communications Biology, 8*, Article 1646. https://doi.org/10.1038/s42003-025-09026-3

Csathó, Á., Van der Linden, D., & Matuz, A. (2024). Change in heart rate variability with increasing time-on-task as a marker for mental fatigue: A systematic review. *Biological Psychology, 185*, 108727. https://doi.org/10.1016/j.biopsycho.2023.108727

Grassmann, M., Vlemincx, E., von Leupoldt, A., Mittelstädt, J. M., & Van den Bergh, O. (2016). Respiratory changes in response to cognitive load: A systematic review. *Neural Plasticity, 2016*, 8146809. https://doi.org/10.1155/2016/8146809

Laborde, S., Mosley, E., & Thayer, J. F. (2017). Heart rate variability and cardiac vagal tone in psychophysiological research: Recommendations for experiment planning, data analysis, and data reporting. *Frontiers in Psychology, 8*, 213. https://doi.org/10.3389/fpsyg.2017.00213

Oken, B. S., Salinsky, M. C., & Elsas, S. M. (2006). Vigilance, alertness, or sustained attention: Physiological basis and measurement. *Clinical Neurophysiology, 117*(9), 1885–1901. https://doi.org/10.1016/j.clinph.2006.01.017

Paterniani, G., Sgreccia, D., Davoli, A., Guerzoni, G., Di Viesti, P., Valenti, A. C., Vitolo, M., Vitetta, G. M., & Boriani, G. (2023). Radar-based monitoring of vital signs: A tutorial overview. *Proceedings of the IEEE, 111*(3), 277–317. https://doi.org/10.1109/JPROC.2023.3244362

Pattyn, N., Neyt, X., Henderickx, D., & Soetens, E. (2008). Psychophysiological investigation of vigilance decrement: Boredom or cognitive fatigue? *Physiology & Behavior, 93*(1–2), 369–378. https://doi.org/10.1016/j.physbeh.2007.09.016

Quigley, K. S., Gianaros, P. J., Norman, G. J., Jennings, J. R., Berntson, G. G., & de Geus, E. J. C. (2024). Publication guidelines for human heart rate and heart rate variability studies in psychophysiology—Part 1: Physiological underpinnings and foundations of measurement. *Psychophysiology, 61*(9), e14604. https://doi.org/10.1111/psyp.14604

Sacco, G., Piuzzi, E., Pittella, E., & Pisa, S. (2020). An FMCW radar for localization and vital signs measurement for different chest orientations. *Sensors, 20*(12), 3489. https://doi.org/10.3390/s20123489

Tao, D., Tan, H., Wang, H., Zhang, X., Qu, X., & Zhang, T. (2019). A systematic review of physiological measures of mental workload. *International Journal of Environmental Research and Public Health, 16*(15), 2716. https://doi.org/10.3390/ijerph16152716

Turppa, E., Kortelainen, J. M., Antropov, O., & Kiuru, T. (2020). Vital sign monitoring using FMCW radar in various sleeping scenarios. *Sensors, 20*(22), 6505. https://doi.org/10.3390/s20226505

Wang, F., Zeng, X., Wu, C., Wang, B., & Liu, K. J. R. (2021). mmHRV: Contactless heart rate variability monitoring using millimeter-wave radio. *IEEE Internet of Things Journal, 8*(22), 16623–16636. https://doi.org/10.1109/JIOT.2021.3075167

Wientjes, C. J. E. (1992). Respiration in psychophysiology: Methods and applications. *Biological Psychology, 34*(2–3), 179–203. https://doi.org/10.1016/0301-0511(92)90015-M

Yao, S., Cong, J., Li, D., & Deng, Z. (2024). Noncontact vital sign monitoring with FMCW radar via maximum likelihood estimation. *IEEE Internet of Things Journal, 11*(23), 38686–38703. https://doi.org/10.1109/JIOT.2024.3449408

---

## 项目内部证据定位（不作为外部文献）

- `FocusWave-Formal-Analysis/国赛报告/README.md`
- `FocusWave-Formal-Analysis/国赛报告/0-总结构与研究叙事_20260912.md`
- `FocusWave-Formal-Analysis/国赛报告/章节草稿/2-理论与技术基础_章节框架_20260912.md`
- `FocusWave-Formal-Analysis/毫米波分析/结果索引.md`
- `focuswave-multimodal-attention-analysis/docs/canonical/MMWAVE_CANONICAL_STATE_AND_INTERFACE_V1.md`
- `focuswave-multimodal-attention-analysis/docs/canonical/2026-09-12_MMWAVE_HR_RECOVERY_AND_BASELINE_INTEGRATION_DECISION.md`
- `focuswave-multimodal-attention-analysis/docs/results/2026-09-12_MMWAVE_HR_RECOVERY_P2/MMWAVE_HR_RECOVERY_P2_REPORT.md`
- `focuswave-multimodal-attention-analysis/docs/results/2026-08-30_MMWAVE_HRV_BEAT_LEVEL_GATE/MMWAVE_BEAT_LEVEL_VALIDATION_REPORT_EXPANDED_5SUBJECTS_2026-08-31.md`

本文件不把历史 Drive 报告或旧国赛正文作为当前方法事实；当内部材料版本不一致时，以以上当前 GitHub canonical/result 为准。