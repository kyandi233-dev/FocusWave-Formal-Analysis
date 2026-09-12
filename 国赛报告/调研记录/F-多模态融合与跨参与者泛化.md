# F-多模态融合与跨参与者泛化

> 调研日期：2026-09-12  
> 定位：国赛报告独立外部文献调研记录  
> 适用范围：解释“为什么采用多模态测量”“怎样证明多模态真正增加测评价值”“怎样评价对训练中未见参与者的泛化”  
> 独立性声明：本文件先依据外部文献建立方法学判断，再与 FocusWave 当前方案比较；不把 FocusWave 当前监督学习设计当作学界标准反向寻找支持证据。  
> FocusWave 项目状态核验基准：`FocusWave-Formal-Analysis@codex/code-fix-ledger`、`Attention-Analysis` 当前 1.16 集成审查分支、`FocusWave@formaltest` 和毫米波主仓库的 2026-09-12 当前状态。当前监督学习链仍处于集成与正式变量冻结阶段，因此本文件评价的是**研究问题和方法路线**，不是已经得到的正式预测结果。

## 结论摘要

现有文献支持 FocusWave 采用多源信息研究注意相关状态，但不支持“多模态天然优于单模态”或“完整多模态模型最高就证明每个传感器都有贡献”。在心智游移研究中，多数据流研究仍是少数：Bühler 等（2025）的系统综述纳入 134 项研究，其中 103 项（77%）仅使用一个数据流，31 项（23%）使用多个数据流；36 项使用机器学习或人工智能，其中只有 8 项采用多模态机器学习。因此更准确的学术表述是：**多模态是用于处理构念多侧面性、单通道噪声和信息歧义的一条重要发展路线，但并非注意研究已经形成的统一标准。**

多模态价值至少要区分三个层次。第一，某一信息源单独是否具有样本外预测效用；第二，在明确的参照信息已经存在后，新模态是否仍带来增量预测价值；第三，在完整组合中移除该模态后，性能是否下降，即条件预测价值或消融价值。第三层不能简单称为“不可替代信息”，因为两个高度冗余的模态都可能有真实信息，但任意删除一个都几乎不损失性能。完整多模态模型表现最高只证明该**组合**有用，不能推出组合中的每个模态均有独立作用。

对 FocusWave 而言，“单模态 → 行为条件增量 → 完整多模态 → 训练中未见参与者泛化”的总体方向具有较强方法学合理性。尤其是参与者互斥验证、训练折内完成预处理与模型选择、相同参与者和探针上的配对模型比较，以及把 Q1 明确表述为注意内容自我报告而非“真实注意真值”，均与当前较成熟的预测方法学一致。需要修订的重点包括：降低“零校准”用语强度、把 `F-x → F` 改称删一特征消融或条件预测价值、把模态级增量比较置于“证明传感器有价值”的主位置，并在概率预测之外增加校准诊断。

---

## 1. 调研问题与检索策略

### 1.1 核心问题

本轮调研围绕四个相互连接的问题展开：

1. 注意、心智游移、任务投入、认知负荷、警觉维持和疲劳/困倦等认知状态为什么采用多模态测量；
2. 多模态融合的常见技术路线分别适合什么数据条件；
3. 怎样证明一个模态具有单独价值、增量价值或条件预测价值；
4. 怎样评价模型能否推广到训练阶段完全未见的参与者，并避免同一参与者重复观测造成的数据泄漏。

### 1.2 检索范围

检索不局限于“multimodal attention detection（多模态注意检测）”，同时覆盖 mind wandering detection（心智游移检测）、sustained attention monitoring（持续注意监测）、engagement recognition（任务投入识别）、cognitive load multimodal（多模态认知负荷）、vigilance monitoring（警觉监测）、fatigue/drowsiness multimodal（多模态疲劳/困倦）、psychophysiological machine learning（心理生理机器学习）、subject-independent physiological classification（参与者独立生理分类）和 multimodal human-state recognition（多模态人类状态识别）。

证据优先级为：系统综述与方法学论文 > 明确报告训练/测试划分的代表性实证研究 > 一般工程性能论文。对工程论文特别记录其心理构念标签来源、参与者划分和能否支持心理解释，而不只记录最高准确率。

本轮属于**目的性证据综述**，不是预注册系统综述或元分析。检索通过网页学术检索、期刊/出版社页面和论文原文进行核验，并交叉复核项目 Google Drive 中既有文献池。旧项目调研只作为候选来源，不继承其中“多模态一定优于单模态”“经典范式直接等于 ground truth（真值）”等概括。

---

## 2. 多模态注意/认知状态测评的研究现状

### 2.1 多模态正在增长，但不是默认标准

Bühler 等（2025）针对心智游移测量的系统综述纳入 134 项研究。103 项（77%）只使用一个数据流，31 项（23%）使用多个数据流；36 项研究采用机器学习或人工智能，其中仅 8 项使用多模态机器学习。该结果说明，心智游移领域已经出现明显的多模态发展趋势，但目前仍不能表述为“注意研究普遍采用多模态测量”。

同一综述还显示，自我报告仍是心智游移研究中最常见的信息来源之一。大量研究使用思维探针或问卷定义当前状态，再用行为、眼动、生理或神经信号预测这些报告。由此需要严格区分：**标签来源、预测输入和用于构念验证的辅助证据并不是同一角色。** FocusWave 把 Q1 作为探针时点的自我报告预测目标，而不把行为或传感器称为“第二套注意真值”，与这一文献结构是相容的。

### 2.2 常见模态组合

注意相关状态研究中的常见信息来源大致可分为以下几类：

| 信息通道 | 常见指标 | 主要优势 | 主要解释限制 |
|---|---|---|---|
| 主观报告 | 思维探针、困倦/疲劳评分、任务投入评分 | 能直接访问参与者对内在状态的报告 | 受反应偏差、元意识和探针干扰影响 |
| 行为 | 反应时、反应时变异、遗漏、误按、任务成绩 | 与任务执行直接相关，易解释 | 同一行为变化可由注意、速度—准确权衡、策略等多种机制产生 |
| 眼部/NIR（近红外） | 瞳孔、眨眼、注视、扫视 | 对认知负荷、唤醒、疲劳和走神均可能敏感 | 光照、眼睑遮挡、个体差异和多重心理机制导致非特异性 |
| RGB（可见光视频） | 面部动作、头姿、眼睑、身体运动 | 非接触、生态性较高，可表征可见行为 | 行为可见性不等于内在注意内容，且受姿势/遮挡影响 |
| 自主生理 | 心率、心率变异性、皮电、呼吸 | 能反映自主神经系统变化 | 对压力、唤醒、负荷、运动等均敏感，状态特异性有限 |
| EEG（脑电）等神经信号 | 频谱、事件相关特征、连接特征 | 更直接反映神经活动 | 设备侵入感、运动伪迹和生态性限制较强 |

Charles 与 Nixon（2019）及 Tao 等（2019）关于心理负荷生理测量的系统综述均指出，没有单一生理指标在所有任务与环境中普遍最优，不同指标对任务要求、环境和个体差异的敏感性不同。Nazari 等（2025）对心智游移测量方法的系统综述同样强调，不同方法观察的是心智游移的不同侧面，没有一种方法可以被简单视为普遍最佳。

### 2.3 多模态采集不等于多模态融合

Chen 等（2022）的 MM-SART（多模态持续性注意反应任务数据库）同步采集了 EEG（脑电）、PPG（光电容积描记）、GSR（皮肤电反应）、眼动和问卷等多种信息，但论文提出的自动心智游移检测器实际主要使用 EEG（脑电）信号。该例说明：

**多模态采集 → 不等于多模态模型 → 更不等于已经证明多模态带来增量价值。**

因此 FocusWave 报告中应分别说明“系统采集了哪些通道”“哪些通道进入当前模型”“加入这些通道是否相对于明确基准产生样本外改善”。

---

## 3. 多模态为什么可能有价值

现有文献支持的多模态价值主要有四类。

### 3.1 覆盖同一心理构念的不同表现层面

注意和心智游移不是可以被某一个传感器直接完整读取的物理量。主观报告反映参与者对当前心理内容的报告，行为反映任务执行，眼部指标反映视觉与唤醒相关过程，心率/呼吸反映自主生理，视频反映可见动作。多方法同时测量可形成更完整的证据结构。

这一逻辑更接近心理测量中的 triangulation（证据三角互证），而不是把多个传感器简单相加形成一个“更真实的注意分数”。如果多个通道对同一状态出现一致变化，可以增加收敛证据；如果出现分离，也可能揭示不同心理过程或测量噪声。

### 3.2 降低单通道噪声和暂时失效的影响

Bühler 等（2025）指出，多数据流可以在某一通道暂时噪声较大时提供补偿，并利用跨模态相关结构帮助消除歧义。实际场景中，瞳孔可能受遮挡影响，视频可能受姿态影响，毫米波生理信号可能受运动或目标选择影响。多个通道的价值因此可以体现为稳健性，而不一定总表现为平均准确率的大幅提高。

### 3.3 区分共享信息与补充信息

Brishtel 等（2020）将眼动与 EDA（皮电活动）用于用户独立的心智游移识别。随机森林中 EDA（皮电活动）单独的 F1 分数约为 0.78，眼动约为 0.80，组合约为 0.83，说明多模态增益存在但幅度有限；加入行为后并未在所有模型中进一步提升。该结果恰好说明，模态之间可能既有互补，也有大量重叠。

因此“某模态没有明显增量”不能直接解释为“该模态没有心理意义”；它可能只是与已有行为或其他模态携带相似信息。

### 3.4 应对个体差异

生理和眼动信号往往存在明显稳定个体差异。跨参与者模型需要学习在不同个体中仍可复现的关系，而不是记住个人基线。多模态有可能通过组合多个相对独立的信息来源提高稳健性，但也可能因为每个模态都带有个体身份特征而放大过拟合。因此，多模态是否真正帮助跨个体泛化必须由参与者独立验证检验，不能由训练集拟合或同人随机划分证明。

---

## 4. 主流融合方法及其适用范围

Baltrušaitis、Ahuja 与 Morency（2019）以及 Sleeman、Kapoor 与 Ghosh（2022）将多模态机器学习中的融合大致区分为早期/特征级融合、后期/决策级融合，以及通过共同中间表征学习跨模态关系的深度路线。不同术语在不同领域并不完全统一，以下按 FocusWave 最相关的功能差异整理。

| 融合路线 | 基本做法 | 优点 | 局限 | 对 FocusWave 的适用性 |
|---|---|---|---|---|
| feature-level/early fusion（特征级/早期融合） | 先分别提取各模态特征，再拼接进入同一模型 | 简单、可直接比较具体特征、便于统一监督学习 | 维度增加后易过拟合，要求时间窗和样本对齐 | **最适合作为当前主线**：已有 30 s 探针级摘要，独立参与者数有限，强调可解释性 |
| decision-level/late fusion（决策级/后期融合） | 各模态单独建模，再融合概率或分数 | 模块化、各模态可用不同模型，对不同采样率更友好 | 可能损失细粒度跨模态交互；概率需要具有可比性 | 可作为缺失模态或设备模块化部署的扩展路线 |
| intermediate representation learning（中间表征学习） | 模态专属编码器学习表示，再通过共享潜变量、注意力或交叉注意力联合学习 | 能捕获复杂非线性交互和原始时序结构 | 参数量大、调参复杂、需要更多独立参与者、解释难 | 当前不宜作为主要证据链，可作为未来扩展 |
| hybrid fusion（混合融合） | 同时结合特征级、中间表征和决策级信息 | 灵活 | 设计复杂、比较和解释困难 | 当前样本与报告目标下优先级较低 |

Bixler 等（2015）在阅读心智游移检测中比较眼动和生理数据的融合，特征级融合相对最佳单模态获得约 11% 的分类准确率提升，而决策级融合没有获得同等程度的提升。这说明“采用多模态”本身还不够，融合位置也会决定能否真正利用跨模态信息。

对 FocusWave 当前样本结构而言，独立信息量主要由参与者数量决定，而不是由同一参与者产生了多少探针决定。Bühler 等（2024）的多模态心智游移研究在约 87 名参与者条件下将眼动、视频和生理信息进行早期融合后得到超过千维的特征空间，并明确面对过拟合风险，随后缩减特征。该例进一步支持 FocusWave 现阶段优先使用预定义科学特征与正则化简单模型，而不是直接进入高维深度融合。

简单模型的合理性应表述为“更符合当前有效独立样本量、预定义特征和解释目标”，而不是声称简单模型普遍优于深度模型。若未来拥有大规模、跨场景、参与者独立的原始时序数据，representation learning（表征学习）可以成为新的研究路线。

---

## 5. 个体差异与跨参与者泛化

### 5.1 为什么个体差异是核心挑战

心智游移、工作负荷、困倦等研究中，同一信号在不同人之间可能有不同基线、变异范围和状态关系。Dong 等（2021）直接比较 EEG（脑电）心智游移识别的个体内与跨个体性能：支持向量机个体内 AUROC（受试者工作特征曲线下面积）约为 0.715，而 LOSO（留一参与者交叉验证）的跨个体 AUROC（受试者工作特征曲线下面积）约为 0.613；逻辑回归也呈现类似下降。研究者明确把 LOSO（留一参与者交叉验证）解释为模拟对训练中未见参与者的部署。

跨参与者生理分类中的类似现象更加普遍。Zhou 等（2023）指出 EEG（脑电）的非平稳性与被试间变异是跨被试工作负荷识别的重要障碍；Cui 等（2022）也将 calibration-free（免个体校准）的跨参与者困倦识别视为具有实际价值但更困难的任务。

### 5.2 为什么随机试次划分可能严重高估泛化

如果同一参与者的多个时间窗或探针同时进入训练集和测试集，模型可以利用稳定的个体特征、设备特征或 session（场次）特征，而不是学习真正可推广的状态关系。此时测试集回答的是“对训练阶段已经见过的人，能否预测他的新时间窗”，而不是“能否预测新参与者”。

Brookshire 等（2024）针对转化 EEG（脑电）深度学习研究给出非常直接的演示：在一个阿尔茨海默病分类例子中，忽略参与者身份、随机划分时间片时准确率达到约 99.8%，改为参与者互斥划分后约为 53.0%，接近机会水平。该论文对 63 项转化 EEG（脑电）深度学习研究作非穷尽审查，只有 17 项（27.0%）能够明确确认避免了参与者特异的数据泄漏。这个 27.0% **不能直接解释为注意研究中的比例**，但能说明重复测量数据中参与者级泄漏可能造成数量级很大的性能夸大。

Kapoor 与 Narayanan（2023）从更广泛的机器学习科学研究角度也指出，训练集和测试集不独立、特征选择或预处理使用测试信息，是高性能却不可复现的重要来源。

### 5.3 当前注意研究中随机 trial split（试次随机划分）到底有多少

本轮**没有找到能够代表整个注意/心智游移领域、系统编码训练—测试划分层级的综述**，因此不能严谨给出“整个领域有多少百分比使用随机试次划分”的数字。Bühler 等（2025）的 134 项研究系统综述详细编码了数据源和分析类型，但没有提供足以计算参与者级与试次级划分比例的统一字段。

本轮另对 9 篇具有代表性的自动注意/心智游移研究进行目的性验证协议审计：Bixler 与 D’Mello（2016）、Hutt 等（2019）、Brishtel 等（2020）、Dong 等（2021）、Chen 等（2022）、Bixler 与 D’Mello（2021）、Bühler 等（2024）和 Daza 等（2024）均明确采用 user-independent/subject-independent（用户/参与者独立）、LOSO（留一参与者交叉验证）或 leave-one-person-out（留一参与者）路线；Hu 等（2023）报告的是样本级五折/十折交叉验证，公开方法中未说明按 participant（参与者）分组。这个 9 篇样本是为比较方法路线而有目的选择的，**不能把“8/9”当作领域比例**。

### 5.4 LOSO（留一参与者交叉验证）和 grouped cross-validation（参与者分组交叉验证）的依据

当研究目标是对训练阶段完全未见的参与者进行预测时，最核心的原则不是某一种固定交叉验证名称，而是：**所有属于同一参与者的重复观测必须始终位于同一侧。**

LOSO（留一参与者交叉验证）每次把一个完整参与者作为测试集，优点是每名参与者都得到一次纯样本外预测，适合参与者数量不大的研究；grouped cross-validation（参与者分组交叉验证）一次留出多个参与者，计算成本较低，在参与者较多时也很常见。两者都可以回答新参与者泛化，只要所有数据驱动预处理、特征选择和超参数选择均限制在当前训练参与者内部。

Vabalas 等（2019）关于小样本机器学习验证的模拟研究进一步表明，在有限样本中需要特别控制特征选择和模型开发导致的乐观偏差；nested cross-validation（嵌套交叉验证）将模型开发限制在内层训练数据，是更稳妥的方案。

### 5.5 participant-independent（参与者独立）不等于真实世界全面泛化

即使参与者完全互斥，训练和测试仍可能来自相同任务、设备、实验室、文化和招募总体。Bixler 与 D’Mello（2021）发现跨阅读领域迁移仍然困难；Bühler 等（2025）的实验室到自然场景研究也显示，实验室内得到的心智游移模型转移到真实场景后性能下降。

因此 FocusWave 的 LOSO（留一参与者交叉验证）结果应表述为：

> **对本研究采样总体中、训练阶段未见参与者的内部跨参与者泛化。**

除非另有外部数据集或独立场景验证，不能直接写成“适用于真实世界所有用户”或“跨场景泛化”。

### 5.6 calibration-free（免个体校准）/zero-calibration（零校准）的实际意义

相关生理机器学习文献中的 calibration-free（免个体校准）强调减少部署时为每个新用户重新采集有标签状态数据、重新训练或重新设阈值的成本，其产品意义是更接近 plug-and-play（即插即用）。Bhosale 等（2022）等跨被试研究把训练只依赖其他参与者、目标参与者不提供标签的情况作为免校准目标。

FocusWave 当前更稳妥的学术表述是：**participant-independent prediction without label-based individual calibration（参与者独立、无标签个体校准预测）**。如果实际系统仍需要摄像头几何校准、静息生理基线或其他目标参与者数据，应把这些设备/测量校准与“无需目标参与者注意标签进行模型校准”区分，不宜笼统宣称“完全零校准”。

---

## 6. 多模态“互补性/增量价值”应该怎样评价

### 6.1 三类不同的价值问题

对某个传感器或具体特征，至少应区分以下三类问题：

| 问题 | 推荐学术表达 | 模型比较 | 能支持的解释 |
|---|---|---|---|
| 单独有没有信息 | standalone predictive utility（单独预测效用） | `M → Q1` | 只使用该信息时，对新参与者 Q1 报告有多少可推广预测信息 |
| 在基准之后还能增加什么 | incremental/added predictive value（增量/新增预测价值） | `B` vs `B+M` | 在基准信息已知后，该模态是否提供额外样本外预测信息 |
| 在其他信息都存在时删除它有何影响 | conditional predictive value / leave-one-modality-out ablation（条件预测价值/删一模态消融） | `F-M` vs `F` | 给定其余信息后，该模态是否仍改善完整模型 |

Xanthakis 等（2014）关于新生物标志物的统计方法论文强调，新增预测指标的价值取决于它相对于什么基准模型进行比较；与结果变量显著关联，并不等价于能够改善已有预测模型。

### 6.2 为什么“完整多模态模型最高”不能证明所有模态有贡献

假设行为、瞳孔和眨眼均进入完整模型，而完整模型优于行为模型，只能说明“加入这一整组信息后组合表现更好”。其中可能存在多种情况：

- 真正的改善全部来自瞳孔，眨眼几乎不增加信息；
- 瞳孔与眨眼高度冗余，两者任一都足以表达同一信息；
- 两个单模态都弱，但组合后产生互补；
- 高维模型偶然获得性能提升，但在新参与者上不稳定。

因此完整模型最高不是逐模态贡献证明。至少还需要预先指定的增量比较或删一模态消融，并在相同参与者、相同探针、相同外层预测和相同训练规则上进行配对比较。

### 6.3 模态互补与模态冗余怎样报告

推荐把结果解释成“预测信息关系”，而不是“贡献率”。例如：

- 单模态较好，加入行为后仍改善：该模态具有单独预测效用，并包含行为之外的补充预测信息；
- 单模态较好，但加入行为后几乎不改善：该模态与行为共享较多 Q1 相关预测信息；
- 单模态较弱，但加入行为后改善：该模态单独信息有限，但可能提供条件互补信息；
- 完整模型删去该模态几乎不变：在当前其余信息存在时，该模态具有较强冗余性；不能据此断言该模态本身“没有价值”。

只有在明确检验非加性或交互增益时，才建议使用 synergy（协同）一词。一般的多模态性能提升不应自动称为“协同效应”。

### 6.4 公平比较的必要条件

直接把两个使用不同参与者或不同探针集合训练的模型分数相减，差异可能同时包含“特征变化”和“样本变化”。因此任何增量或消融比较均应尽量满足：同一批测试参与者、同一批探针、同一外层折、同一预处理与模型选择规则，只改变所比较的信息集合。FocusWave 当前 `analysis_set_id`（分析集合标识）和 comparison-specific（按比较特异）共同样本设计在这一点上是方法学合理的。

### 6.5 推荐的统计报告单位

如果每名参与者探针数不完全相同，直接把所有探针混在一起计算总体损失会让探针更多的参与者拥有更高权重。FocusWave 当前先在参与者内对探针损失求平均，再对参与者等权平均，本质上估计的是“平均参与者的样本外表现”，是合理的 estimand（估计目标）选择，但并不是机器学习领域唯一标准。

增量比较建议在参与者层面形成配对差值，再进行 participant-cluster bootstrap（参与者聚类自助法）或等价的参与者层面不确定性估计。这样得到的置信区间直接对应“在参与者层面的增量是否稳定”。

---

## 7. 可解释性问题

### 7.1 可解释多模态建模的成熟做法

对 FocusWave 这类以科学解释为目标的项目，可解释性不应依赖一个统一“重要性权重”，而应由多个层次共同构成：

1. 使用有心理和测量意义、预先定义的科学特征；
2. 用简单正则化模型作为主要预测器，使变量进入方式清楚；
3. 用单独预测、基准后增量和删一模态/删一特征消融解释不同层面的价值；
4. 报告标准化模型系数的方向和跨折稳定性，但只解释为“模型在给定其他特征后如何使用该变量”；
5. 如使用 SHAP（沙普利加性解释）或 permutation importance（置换重要性），把它们作为模型行为的补充描述，不解释成心理构念组成比例。

### 7.2 为什么不能写“模态贡献率”或“权重占比”

Kumar 等（2020）指出，基于 Shapley value（沙普利值）的特征重要性具有明确的解释假设和局限，并不能自动获得因果含义。在高度相关特征条件下，不同重要性方法还可能在冗余变量之间重新分配或掩盖重要性。

因此以下表述应避免：

- “瞳孔贡献 35%，眨眼贡献 20%”；
- “模型权重证明瞳孔是注意的主要组成”；
- “SHAP（沙普利加性解释）值最大说明该生理过程最重要”。

更稳妥的表述是“加入该指标后样本外预测损失降低多少”“删去该指标后模型性能是否下降”“系数方向在多少参与者折中保持一致”。

### 7.3 深度多模态模型的角色

深度表示学习并非不适合认知状态识别。其优势主要出现在高维原始时序、非线性交互和大型数据集。但 FocusWave 当前独立参与者数量是有限的，重复探针不能等价增加独立训练样本数；项目同时要求解释具体心理/生理指标。因此深度多模态网络更适合作为未来或探索性扩展，而不应成为当前证明多模态价值的必要条件。

---

## 8. 预测评价指标分别回答什么问题

| 指标 | 主要回答的问题 | 优点 | 主要限制 | FocusWave 建议角色 |
|---|---|---|---|---|
| log loss（对数损失） | 预测概率是否给真实类别较高概率 | strictly proper scoring rule（严格适当评分规则），对过度自信的错误惩罚大 | 数值受任务难度和类别数影响，不是“纯校准指标” | **二分类主要指标合理**；参与者内平均后再参与者等权 |
| AUROC（受试者工作特征曲线下面积） | 正例通常是否排在负例前面 | 与固定分类阈值无关，易比较区分能力 | 不反映概率校准；严重不平衡时可能掩盖正类精确率问题 | 主要补充区分指标 |
| AUPRC（精确率—召回率曲线下面积） | 对较稀少正类的识别质量 | 类别不平衡时更敏感 | 强烈依赖正类流行率 | 若 Q1=1 比例明显不平衡，建议补充 |
| balanced accuracy（平衡准确率） | 固定阈值后两类召回率是否均衡 | 对类别不平衡比普通准确率稳健 | 丢失概率置信度信息，依赖阈值 | 易解释的补充分类指标 |
| F1（F1 分数） | 精确率与召回率的折中 | 适合关心正类检出 | 依赖阈值与正类比例，忽略真负类 | 次要补充 |
| Brier score（布里尔分数） | 概率预测的总体平方误差 | 同时反映概率质量 | 区分与校准混合在一个分数中 | 若报告“概率可信度”，建议补充 |
| calibration plot/slope/intercept（校准图/校准斜率/截距） | 预测 0.7 的事件是否约 70% 发生 | 直接检查概率校准 | 小样本时不稳定 | 建议作为概率解释的诊断 |

Gneiting 与 Raftery（2007）为 log score（对数评分）作为严格适当概率评分提供理论基础；Steyerberg 等（2010）强调区分能力、总体预测误差和概率校准是不同评价维度；Silva Filho 等（2023）系统总结了分类概率校准的评价与修正方法。因此 FocusWave 当前以参与者宏平均 log loss（对数损失）作为主要概率预测指标是合理的，但如果报告中需要解释“预测概率本身是否可信”，应再报告 Brier score（布里尔分数）或校准图，而不能把 log loss（对数损失）直接称为“校准指标”。

---

## 9. 文献证据矩阵

| 文献 | 构念/任务 | 数据来源 | 验证结构 | 关键发现 | 对 FocusWave 的意义 |
|---|---|---|---|---|---|
| Bühler et al., 2025，系统综述 | 心智游移 | 134 项研究，多类数据流 | 综述 | 77% 单数据流，23% 多数据流；多模态机器学习仍较少 | 不能宣称多模态已是注意研究标准 |
| Charles & Nixon, 2019 | 心理负荷 | 多类生理信号 | 系统综述 | 没有单一指标满足所有场景需求，推荐多指标三角互证 | 支持多通道测量的理论动机 |
| Tao et al., 2019 | 心理负荷 | 多类生理信号 | 系统综述 | 指标效果依赖任务和情境，没有普遍最佳生理指标 | 支持“多方法而非单一生物标志物”叙事 |
| Bixler et al., 2015 | 阅读心智游移 | 眼动+生理 | 多种融合比较 | 特征级融合优于最佳单模态，决策级融合未同等改善 | 说明融合方式本身需要验证 |
| Bixler & D’Mello, 2016 | 阅读心智游移 | 眼动 | user-independent（用户独立） | 建立用户独立的眼动心智游移检测 | 新用户泛化可独立成为研究问题 |
| Hutt et al., 2019 | 课堂学习心智游移 | 眼动+视频 | student-independent（学生独立），含新样本测试 | 多模态只在有限条件下改善，真实场景性能低于离线估计 | 反对“多模态必然改善”和“实验室性能=真实部署” |
| Brishtel et al., 2020 | 阅读心智游移 | 眼动+EDA（皮电活动）+行为 | user-independent（用户独立） | 多模态有小幅改善；行为加入后不总是继续提升 | 很适合解释互补与冗余 |
| Dong et al., 2021 | 心智游移 | EEG（脑电） | 个体内 vs LOSO（留一参与者交叉验证） | 跨个体性能明显低于个体内 | 直接支持参与者独立验证的重要性 |
| Chen et al., 2022 | SART（持续性注意反应任务）心智游移 | 多模态采集；模型主要用 EEG（脑电） | LOSO（留一参与者交叉验证） | 多模态数据库并不等于多模态模型 | 区分采集、融合和增量价值 |
| Bixler & D’Mello, 2021 | 心智游移跨领域迁移 | 眼动 | 5-fold user-independent（五折用户独立） | 跨领域迁移仍受 domain shift（领域漂移）限制 | 参与者独立不等于跨任务泛化 |
| Bühler et al., 2024 | aware/unaware mind wandering（有觉察/无觉察心智游移） | 眼动+面部视频+生理 | leave-one-person-out（留一参与者） | 多模态高维特征面临过拟合与特征筛选问题 | 支持简单预定义特征主线 |
| Bühler et al., 2025，实验室到自然场景 | 心智游移 | 视频等 | 跨数据集/场景 | 实验室模型转移到自然场景后性能下降 | 明确 FocusWave 泛化结论的边界 |
| Daza et al., 2024 | e-learning（电子学习）注意/认知负荷代理 | 眨眼、HR（心率）、面部动作、头姿等 | leave-one-user-out（留一用户） | 多种脸部/生理信息融合，表示方式和窗口影响性能 | 代表非接触多模态工程路线，但构念与 Q1 不同 |
| Hu et al., 2023 | VR（虚拟现实）学习专注 | 交互+视觉，EEG（脑电）设备标签 | 样本级 K-fold（K 折），未报告参与者分组 | 多模态性能较高，但跨参与者推广证据有限 | 说明高性能不能替代合理划分和标签效度审查 |
| Brookshire et al., 2024 | 转化 EEG（脑电） | EEG（脑电） | 时间片随机 vs 参与者互斥 | 随机时间片划分可产生极端性能夸大 | 强方法学证据：同人重复观测不能跨折 |
| Vabalas et al., 2019 | 小样本机器学习 | 模拟/多算法 | 多种验证方案 | 特征选择和模型开发若泄漏会产生乐观偏差 | 支持嵌套、训练折内预处理 |
| Xanthakis et al., 2014 | 新预测指标 | 统计方法 | 基准模型 vs 扩展模型 | 增量价值取决于明确基准，显著关联不等于预测改善 | 为 `B` vs `B+M` 提供成熟统计语言 |
| Kumar et al., 2020 | 模型解释 | Shapley value（沙普利值）方法 | 方法学 | 特征重要性不能自动解释为因果贡献 | 反对“贡献率/权重占比”叙事 |

---

## 10. 对 FocusWave 当前监督学习思路的独立方法学评价

### 10.1 与外部文献高度一致的部分

**第一，明确 Q1 是预测目标而非真实注意真值。** 当前 `1.16.1` 把首轮任务定义为用探针前合法信息预测 Q1 注意内容自我报告，并明确行为和传感器都不是注意真值。这比很多工程论文直接把任务难度、设备评分或行为结果当“注意真值”的做法更谨慎，也更符合心理测量边界。

**第二，先报告单模态，再报告增量。** 文献中的增量预测方法要求先定义参照模型，再检验新增信息是否真正改善样本外预测。当前 `x → Q1` 和 `B` vs `B+x` 正好对应单独预测效用与行为条件增量价值，是合理且成熟的研究问题。

**第三，参与者互斥外层评价。** 当前 outer participant-disjoint LOSO（外层参与者互斥留一验证）直接匹配“推广到训练中未见参与者”的研究目标，也避免了重复探针跨折造成的个体身份泄漏。

**第四，内层按参与者分组，并将插补、标准化、候选方案和超参数选择限制在训练参与者内部。** 这一点符合嵌套机器学习验证的基本要求，对防止小样本乐观偏差尤其重要。

**第五，直接性能比较要求相同分析集合。** 当前按 comparison-specific analysis set（特定比较分析集合）构造共同测试参与者/探针，能把“信息包变化”与“样本变化”分开，这是增量评价的关键。

**第六，简单正则化逻辑回归作为主模型是合理的。** 这里的理由不是“逻辑回归最先进”，而是当前独立参与者规模有限、已有预定义心理/生理摘要特征、研究目标要求变量级解释。复杂深度融合可以保留为后续路线，但不应成为证明多模态价值的前置条件。

### 10.2 与主流做法不同、但合理的部分

**参与者等权训练和评价。** 大量机器学习论文直接让每个样本/时间窗等权，FocusWave 进一步让每个参与者获得相同总训练权重，并以参与者宏平均损失作为主要总体。这不是领域统一标准，但如果研究目标定义为“平均新参与者的预测性能”，该 estimand（估计目标）是清晰且合理的。报告中应明确它是本研究的评价目标选择，而不是“标准机器学习规定”。

**把行为作为主要增量基准。** 文献并没有规定传感器一定要相对行为模型比较，但对于 FocusWave，“已经知道近期任务表现后，传感器是否还能增加 Q1 预测信息”具有直接科学意义和产品意义。它应被描述为本研究选择的 scientifically meaningful baseline（科学上有意义的基准），而非学界唯一标准。

**使用 LOSO（留一参与者交叉验证）而非普通 grouped K-fold（参与者分组 K 折）作为外层。** 两种方法都可以实现参与者独立验证。当前参与者数量有限时，LOSO（留一参与者交叉验证）能够为每名参与者形成独立样本外预测，便于参与者级不确定性分析，因此无需因为文献中也常见 grouped K-fold（参与者分组 K 折）而修改。

### 10.3 建议修改的地方

**1. `F-x → F` 不建议再称“不可替代信息”。** 推荐改成 conditional predictive value（条件预测价值）或 leave-one-feature-out ablation（删一特征消融）。高度冗余的两个特征可能都很有信息，但删除任一都不降低性能；“不可替代”会把冗余误写成无价值。

**2. “传感器有价值”的主证据应优先使用模态级行为条件增量。** 例如 Behavior（行为） vs Behavior+NIR（行为+近红外）、Behavior（行为） vs Behavior+RGB（行为+可见光视频）、Behavior（行为） vs Behavior+mmWave（行为+毫米波）。具体特征 `B+x` 和 `F-x → F` 更适合作为解释层。这样国赛叙事会更清楚地回答“多装一套传感器值不值得”。

**3. “零校准”需要限定。** 建议正文使用“对训练中未见参与者、无需其注意标签进行个体校准的预测”。如果设备本身仍需摄像头几何校准、毫米波静息基线或其他目标参与者数据，不宜直接写成“完全零校准”。

**4. 增加概率校准诊断。** 当前参与者宏平均 log loss（对数损失）作为主指标合理，但如果报告展示概率轨迹或把预测概率解释为风险/注意概率，应至少补充 Brier score（布里尔分数）或 calibration plot（校准图）。

**5. 泛化表述要限制在参与者层面。** LOSO（留一参与者交叉验证）支持“训练未见参与者”的内部泛化，不支持直接宣称跨任务、跨设备、跨学校、跨环境泛化。

**6. 模型解释不要换算为“模态贡献率”。** 系数、SHAP（沙普利加性解释）或置换重要性可以辅助说明模型如何使用变量，但真正的增量价值仍应由配对样本外模型比较给出。

**7. 毫米波必须继续遵守测量资格边界。** 当前项目仓库中 HR（心率）测量链仍在独立恢复与验证，HRV（心率变异性）仍受 beat/IBI（心搏/搏间期）有效性门控。外部文献证明“心率/呼吸可能与认知状态相关”不能替代 FocusWave 自己的传感器测量有效性验证。

---

## 11. 建议国赛报告采用的学术语言和论证方式

建议按以下逻辑形成报告叙事：

> 持续注意及相关认知状态不能由单一外显指标完整观测。行为表现、自我报告、眼部活动、身体动作和自主生理反映不同且部分重叠的状态表现，并受到不同噪声与个体差异影响。因此，本研究采用多源测量，以获得互补的状态证据，而不预设任一传感器是“注意真值”。
>
> 多模态是否真正增加测评价值进一步通过样本外预测检验。首先评价各信息来源单独对训练中未见参与者 Q1 注意内容报告的预测效用；随后以近期行为表现为参照，检验加入 NIR（近红外）、RGB（可见光视频）和通过独立测量验证的毫米波信息后是否进一步改善预测；最后通过完整组合及删一模态/删一特征消融考察信息冗余和条件预测价值。
>
> 所有直接性能比较在相同参与者、相同探针和相同外层验证条件下完成。参与者独立验证用于评价模型对训练阶段完全未见参与者的内部泛化能力；该结果不等同于跨任务、跨设备或跨应用场景的外部泛化。

建议国赛正文优先使用以下术语：

| 不够稳妥的说法 | 建议说法 |
|---|---|
| 多模态注意识别 | 多源信息预测 Q1 注意内容自我报告 / 多模态注意状态测评 |
| 注意真值 | Q1 探针时点注意内容自我报告 |
| 某模态贡献率 | 某模态的增量预测价值 / 条件预测价值 |
| 不可替代信息 | 给定其余信息后的条件预测价值 |
| 完全零校准 | 无需目标参与者注意标签进行个体校准的参与者独立预测 |
| 多模态一定更准确 | 检验多模态是否在样本外产生稳定增量 |
| 泛化到真实用户 | 对本研究总体中训练未见参与者的内部泛化 |
| SHAP（沙普利加性解释）证明特征重要 | SHAP（沙普利加性解释）描述当前模型如何使用特征 |

---

## 12. 不能由现有文献支持的宣传性结论

以下表述不建议出现在国赛报告的科学结论中：

1. **“多模态已经成为注意力测评的主流标准。”** 心智游移系统综述显示，多数据流研究仍占少数。
2. **“传感器越多，注意识别准确率越高。”** 多项研究只得到有限增益，部分融合策略甚至不优于最佳单模态。
3. **“完整多模态模型最好，所以每个传感器都有独立贡献。”** 完整模型只证明组合价值，不能定位单个模态。
4. **“Q1 是真实注意状态。”** Q1 是当前注意内容自我报告，本身也受到报告与元意识过程影响。
5. **“跨参与者验证证明系统已经能够真实世界泛化。”** 它只控制参与者身份重叠，仍未检验任务、设备、场景和总体漂移。
6. **“模型权重或 SHAP（沙普利加性解释）百分比就是心理贡献率。”** 相关预测特征下重要性依赖模型和条件分布，不具有这种直接心理解释。
7. **“无需任何校准。”** 若系统仍有设备校准、静息基线或目标参与者数据需求，必须限定“无需标签个体校准”的具体范围。
8. **“毫米波心率/心率变异性已证明能够提高 FocusWave 的注意预测。”** 当前项目自己的毫米波测量资格和正式增量结果尚未完成，外部论文不能替代项目内验证。

---

## 13. 最值得进入正式报告的 8 篇核心文献

1. **Bühler et al. (2025), Educational Psychology Review**：最直接的心智游移测量系统综述，可支持“多模态正在增长但尚非默认标准”“多方法的必要性和当前研究格局”。
2. **Charles & Nixon (2019), Applied Ergonomics**：系统综述心理负荷生理测量，可支持“没有单一生理指标普遍最佳”和多指标三角互证。
3. **Baltrušaitis et al. (2019), IEEE TPAMI**：多模态机器学习经典综述，适合定义特征级、决策级及表征学习的技术位置。
4. **Brishtel et al. (2020), Sensors**：眼动+皮电的用户独立心智游移研究，能直观展示“多模态增益可以存在但有限，行为与传感器可能冗余”。
5. **Hutt et al. (2019), User Modeling and User-Adapted Interaction**：课堂真实场景、学生独立验证和多模态有限增益，适合限制工程宣传。
6. **Dong et al. (2021), PLOS ONE**：直接比较个体内与跨个体心智游移识别，强力支持参与者独立验证。
7. **Brookshire et al. (2024), Frontiers in Neuroscience**：重复时间片随机划分导致参与者特异泄漏的直观数量证据，可作为验证设计的方法学依据。
8. **Xanthakis et al. (2014), Statistics in Medicine**：提供“增量预测价值”相对于明确基准模型的成熟统计表述，直接支持 Behavior（行为） vs Behavior+Sensor（行为+传感器）的研究逻辑。

如果报告参考文献数量严格受限，优先保留 Bühler 等（2025）、Baltrušaitis 等（2019）、Dong 等（2021）、Brookshire 等（2024）、Xanthakis 等（2014）五篇；Brishtel 等（2020）、Hutt 等（2019）和 Charles 与 Nixon（2019）用于补充实证和理论论证。

---

## 14. APA 第七版参考文献

Azevedo, R., & Gašević, D. (2019). Analyzing multimodal multichannel data about self-regulated learning with advanced learning technologies: Issues and challenges. *Computers in Human Behavior, 96*, 207–210. https://doi.org/10.1016/j.chb.2019.03.025

Baltrušaitis, T., Ahuja, C., & Morency, L.-P. (2019). Multimodal machine learning: A survey and taxonomy. *IEEE Transactions on Pattern Analysis and Machine Intelligence, 41*(2), 423–443. https://doi.org/10.1109/TPAMI.2018.2798607

Bhosale, S., Chakraborty, R., & Kopparapu, S. K. (2022). Calibration free meta learning based approach for subject independent EEG emotion recognition. *Biomedical Signal Processing and Control, 72*, 103289. https://doi.org/10.1016/j.bspc.2021.103289

Bixler, R., Blanchard, N., Garrison, L., & D’Mello, S. (2015). Automatic detection of mind wandering during reading using gaze and physiology. In *Proceedings of the 2015 ACM International Conference on Multimodal Interaction* (pp. 299–306). ACM. https://doi.org/10.1145/2818346.2820742

Bixler, R., & D’Mello, S. (2016). Automatic gaze-based user-independent detection of mind wandering during computerized reading. *User Modeling and User-Adapted Interaction, 26*(1), 33–68. https://doi.org/10.1007/s11257-015-9167-1

Bixler, R. E., & D’Mello, S. K. (2021). Crossed eyes: Domain adaptation for gaze-based mind wandering models. In *2021 Symposium on Eye Tracking Research and Applications*. ACM. https://doi.org/10.1145/3448017.3457386

Brishtel, I., Khan, A. A., Schmidt, T., Dingler, T., Ishimaru, S., & Dengel, A. (2020). Mind wandering in a multimodal reading setting: Behavior analysis & automatic detection using eye-tracking and an EDA sensor. *Sensors, 20*(9), 2546. https://doi.org/10.3390/s20092546

Brookshire, G., Kasper, J., Blauch, N. M., Wu, Y. C., Glatt, R., Merrill, D. A., Gerrol, S., Yoder, K. J., Quirk, C., & Lucero, C. (2024). Data leakage in deep learning studies of translational EEG. *Frontiers in Neuroscience, 18*, 1373515. https://doi.org/10.3389/fnins.2024.1373515

Brodersen, K. H., Ong, C. S., Stephan, K. E., & Buhmann, J. M. (2010). The balanced accuracy and its posterior distribution. In *2010 20th International Conference on Pattern Recognition* (pp. 3121–3124). IEEE. https://doi.org/10.1109/ICPR.2010.764

Bühler, B., Bozkir, E., Deininger, H., Goldberg, P., Gerjets, P., Trautwein, U., & Kasneci, E. (2024). Detecting aware and unaware mind wandering during lecture viewing: A multimodal machine learning approach using eye tracking, facial videos and physiological data. In *Proceedings of the 26th International Conference on Multimodal Interaction* (pp. 244–253). ACM. https://doi.org/10.1145/3678957.3685710

Bühler, B., Bozkir, E., Goldberg, P., Sümer, Ö., D’Mello, S. K., Gerjets, P., Trautwein, U., & Kasneci, E. (2025). From the lab to the wild: Examining generalizability of video-based mind wandering detection. *International Journal of Artificial Intelligence in Education, 35*, 823–857. https://doi.org/10.1007/s40593-024-00412-2

Bühler, B., Fütterer, T., von Keyserlingk, L., Bozkir, E., Kasneci, E., Gerjets, P., & Trautwein, U. (2025). Mapping mind wandering to the “self-regulated learning process, multimodal data, and analysis grid”: A systematic review. *Educational Psychology Review, 37*, 76. https://doi.org/10.1007/s10648-025-10041-3

Charles, R. L., & Nixon, J. (2019). Measuring mental workload using physiological measures: A systematic review. *Applied Ergonomics, 74*, 221–232. https://doi.org/10.1016/j.apergo.2018.08.028

Chen, Y.-T., Lee, H.-H., Shih, C.-Y., Chen, Z.-L., Beh, W.-K., Yeh, S.-L., & Wu, A.-Y. (2022). An effective entropy-assisted mind-wandering detection system using EEG signals of MM-SART database. *IEEE Journal of Biomedical and Health Informatics, 26*(8), 3649–3660. https://doi.org/10.1109/JBHI.2022.3187346

Cui, J., Lan, Z., Liu, Y., Li, R., Li, F., Sourina, O., & Müller-Wittig, W. (2022). A compact and interpretable convolutional neural network for cross-subject driver drowsiness detection from single-channel EEG. *Methods, 202*, 173–184. https://doi.org/10.1016/j.ymeth.2021.04.017

Daza, R., Gomez-Gomez, L. F., Fierrez, J., Morales, A., Tolosana, R., & Ortega-Garcia, J. (2024). DeepFace-Attention: Multimodal face biometrics for attention estimation with application to e-learning. *IEEE Access, 12*, 111343–111359. https://doi.org/10.1109/ACCESS.2024.3437291

Dong, H. W., Mills, C., Knight, R. T., & Kam, J. W. Y. (2021). Detection of mind wandering using EEG: Within and across individuals. *PLOS ONE, 16*(5), e0251490. https://doi.org/10.1371/journal.pone.0251490

Gneiting, T., & Raftery, A. E. (2007). Strictly proper scoring rules, prediction, and estimation. *Journal of the American Statistical Association, 102*(477), 359–378. https://doi.org/10.1198/016214506000001437

Hu, R., Hui, Z., Li, Y., & Guan, J. (2023). Research on learning concentration recognition with multi-modal features in virtual reality environments. *Sustainability, 15*(15), 11606. https://doi.org/10.3390/su151511606

Hutt, S., Krasich, K., Mills, C., Bosch, N., White, S., Brockmole, J. R., & D’Mello, S. K. (2019). Automated gaze-based mind wandering detection during computerized learning in classrooms. *User Modeling and User-Adapted Interaction, 29*(4), 821–867. https://doi.org/10.1007/s11257-019-09228-5

Kapoor, S., & Narayanan, A. (2023). Leakage and the reproducibility crisis in machine-learning-based science. *Patterns, 4*(9), 100804. https://doi.org/10.1016/j.patter.2023.100804

Kumar, I. E., Venkatasubramanian, S., Scheidegger, C., & Friedler, S. A. (2020). Problems with Shapley-value-based explanations as feature importance measures. In *Proceedings of the 37th International Conference on Machine Learning* (Vol. 119, pp. 5491–5500). PMLR.

Nazari, S., Fitzgerald, P., & Kazemi, R. (2025). The relative accuracy of different methods for measuring mind wandering subtypes: A systematic review. *Brain and Behavior, 15*(8), e70764. https://doi.org/10.1002/brb3.70764

Silva Filho, T., Song, H., Perello-Nieto, M., Santos-Rodriguez, R., Kull, M., & Flach, P. (2023). Classifier calibration: A survey on how to assess and improve predicted class probabilities. *Machine Learning, 112*, 3211–3260. https://doi.org/10.1007/s10994-023-06336-7

Sleeman, W. C., IV, Kapoor, R., & Ghosh, P. (2022). Multimodal classification: Current landscape, taxonomy and future directions. *ACM Computing Surveys, 55*(7), Article 150, 1–31. https://doi.org/10.1145/3543848

Steyerberg, E. W., Vickers, A. J., Cook, N. R., Gerds, T., Gonen, M., Obuchowski, N., Pencina, M. J., & Kattan, M. W. (2010). Assessing the performance of prediction models: A framework for traditional and novel measures. *Epidemiology, 21*(1), 128–138. https://doi.org/10.1097/EDE.0b013e3181c30fb2

Tao, D., Tan, H., Wang, H., Zhang, X., Qu, X., & Zhang, T. (2019). A systematic review of physiological measures of mental workload. *International Journal of Environmental Research and Public Health, 16*(15), 2716. https://doi.org/10.3390/ijerph16152716

Vabalas, A., Gowen, E., Poliakoff, E., & Casson, A. J. (2019). Machine learning algorithm validation with a limited sample size. *PLOS ONE, 14*(11), e0224365. https://doi.org/10.1371/journal.pone.0224365

Xanthakis, V., Sullivan, L. M., Vasan, R. S., Benjamin, E. J., Massaro, J. M., D’Agostino, R. B., Sr., & Pencina, M. J. (2014). Assessing the incremental predictive performance of novel biomarkers over standard predictors. *Statistics in Medicine, 33*(15), 2577–2584. https://doi.org/10.1002/sim.6165

Zhou, Y., Wang, P., Gong, P., Wei, F., Wen, X., Wu, X., & Zhang, D. (2023). Cross-subject cognitive workload recognition based on EEG and deep domain adaptation. *IEEE Transactions on Instrumentation and Measurement, 72*, 1–12, Article 2518912. https://doi.org/10.1109/TIM.2023.3276515

---

## 15. 对当前国赛报告的最终建议

FocusWave 不需要把自己包装成“提出一种复杂多模态深度融合算法”才能证明项目价值。现阶段更有说服力的科研叙事是：

**多源测量首先用于避免把任何单一指标当作注意的完整代理；随后用严格的参与者独立样本外预测，分别检验各通道单独包含多少 Q1 相关信息，以及传感器在行为信息已经存在后还能增加多少信息。**

在这个框架中，系统价值由三类证据共同构成：单模态本身是否稳定、行为条件增量是否存在、完整组合在新参与者上是否进一步改善；具体特征再通过删一特征消融和系数稳定性解释其条件作用。这样的论证比“多模态最高准确率”更严格，也更符合 FocusWave 当前强调心理学解释、非接触测量和新参与者推广的研究定位。

当前最需要防止的叙事偏差有两个：其一，把多模态当作先验优势；其二，把参与者独立预测写成对“真实注意”的完全识别。外部文献更支持一种克制但更有方法学力量的表述：**多模态是否有价值不是由传感器数量决定，而由它在严格样本外条件下是否提供稳定、可解释、相对于已有信息仍然新增的预测信息决定。**

---

## 16. 后续监督学习执行标记：概率校准诊断

> **状态：FOLLOW-UP / SUPERVISED-ANALYSIS（后续监督学习阶段执行）**  
> **当前不是已实现结果，也不要求为此重新训练模型。** 该项应在正式 participant-disjoint（参与者互斥）外层预测完成、OOF（out-of-fold，折外）预测概率归档后追加。

### 16.1 建议追加的诊断

首轮二分类正式监督学习继续以 participant-macro log loss（参与者宏平均对数损失）作为主要概率预测指标；在此基础上追加：

1. **Brier score（布里尔分数）**：直接使用每个外层留出参与者的 OOF（折外）预测概率计算，不重新拟合模型。为保持与当前总体 estimand（估计目标）一致，建议先在每名参与者内对合法 probe（探针）的 Brier loss 求平均，再在参与者之间等权汇总；如报告置信区间，可继续使用参与者层面的重抽样。
2. **calibration plot（校准图）**：使用正式 OOF（折外）概率检查“预测概率与实际 Q1=1 发生频率是否一致”。图形汇总时应避免探针较多的参与者获得不成比例的权重，优先采用参与者等权的样本权重或等价的参与者层面汇总方案。
3. 如样本量和概率分布支持，可补充 **calibration slope / calibration intercept（校准斜率 / 校准截距）**；若估计不稳定，则保留 Brier score（布里尔分数）与 calibration plot（校准图）即可，不为了凑指标强行报告。

### 16.2 解释边界

这组指标回答的是**模型给出的概率本身是否具有合理的概率意义**，不是新的多模态研究问题，也不替代以下当前主分析：

- standalone predictive utility（单独预测效用）；
- Behavior（行为） vs Behavior+Sensor（行为+传感器）的增量预测价值；
- Full（完整模型）及删一模态/删一特征消融；
- AUROC（受试者工作特征曲线下面积）、balanced accuracy（平衡准确率）等区分/分类表现。

因此后续代码实施时，应把概率校准作为**正式 OOF 预测产生后的评价层诊断**，而不是另起一套训练流程。只有当未来需要主动 recalibration（再校准）预测概率时，才需要把校准模型本身纳入训练折内部重新设计；本标记当前只要求**评价校准情况，不进行后处理校准**。
