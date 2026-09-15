# 分析设计｜当前正式方法入口

> **状态：CURRENT（当前方法导航）**  
> 最后核验：2026-09-15  
> 当前权威分支：`FocusWave-Formal-Analysis@main`  
> 当前可执行分析权威：`Attention-Analysis@codex/formal-analysis-v2-portable`

本目录保存 FocusWave 方法从早期方案到正式分析的完整演变。阅读时必须区分：**当前实际实现、已经冻结的方法合同、历史方案与中间计划**。旧文件不删除，但文件编号较早、篇幅较长或曾经写成“执行计划”，都不自动获得当前优先级。

旧 README 中关于 `codex/code-fix-ledger`、#40–#44 active issues（活动问题）、“冻结后才能启动真实监督学习”等状态已经过期。当前 Formal 长期权威只有 `main`，监督学习和正式结果已经实际运行。

## 1. 当前研究问题

FocusWave 当前正式分析围绕三个连续问题：

1. Behavior（行为）、Ocular（眼部）、Movement（动作）和 Cardiopulmonary（心肺）测量怎样随 Q1 注意内容报告、Q2 困倦/清醒报告和任务进程变化；
2. Ocular、Movement、Cardiopulmonary 等传感信息在已有 Behavior 信息基础上是否提供稳定的额外预测信息；
3. 这些关系和模型能否推广到训练中完全未见的 participant（参与者）。

Q1 是 attention-content self-report（注意内容自我报告），不是潜在注意状态“真值”。Q1 二分类是主要监督学习任务；四分类是扩展分析。Q2 用于解释性分析，不作为首轮 Q1 预测输入。

## 2. 当前样本、身份与缺失合同

当前 governed cohort（治理队列）为 **116 sessions（场次）、61 participant groups（参与者组）、2,320 个 Behavior 权威 probes（思维探针）**。`participant_group_id` 是重复测量推断、participant-cluster bootstrap（参与者簇自助法）和 participant-disjoint prediction（参与者互斥预测）的统一统计键。

模态 availability（可用性）与 cohort membership（队列成员资格）分开。NIR（近红外）、RGB（可见光视频）、mmWave（毫米波）的缺失不得反向删除 Behavior 场次或重写参与者身份；比较模型只在对应特征真正需要的分析集合中评价。

## 3. 科学模态与设备来源的正式区分

| 科学模态 | 主要设备/记录来源 | 主要分析角色 |
|---|---|---|
| Behavior（行为） | SART / 思维探针 | RT 水平、RT 变异、趋势、遗漏、误按等 |
| Ocular（眼部） | NIR 瞳孔 + RGB 眨眼 | 瞳孔水平/波动/动态、眨眼、联合伪迹处理 |
| Movement（动作） | RGB | 整体身体动作与姿态变化 |
| Cardiopulmonary（心肺） | mmWave | 毫米波估计心率与呼吸率；当前支持性使用 |

RGB/NIR/mmWave 属于 device/source namespace（设备/来源命名空间）。跨设备辅助处理不改变科学模态归属，但 feature provenance（特征来源）必须记录真实设备依赖，以支持设备组合评价。

## 4. 当前方法链

当前正式流程已经从单模态测量一路执行到监督学习与报告：

```text
治理队列与身份冻结
→ 单模态 measurement/QC（测量与质量控制）
→ Behavior / Ocular / Movement 科学输出与 handoff（交接）
→ Cardiopulmonary producer provenance + time-legality
→ 冻结 feature registry（特征登记表）
→ comparison-specific analysis sets（比较特异分析集合）
→ Q1 二分类 participant-disjoint LOSO
→ OOF probability diagnostics（折外概率诊断）
→ 模态增量 / Full-x 条件价值 / 设备组合
→ Q1 四分类扩展与多分类诊断
→ 完整结果总账与国赛报告
```

因此，本目录中任何仍写“STOP，等待研究者冻结后不得进入监督学习”的阶段性文件，都应作为当时的治理快照阅读，而不是当前状态。

## 5. 当前监督学习合同

### 5.1 外层泛化

外层验证按 `participant_group_id` 做 participant-disjoint LOSO（参与者互斥留一参与者验证）。同一参与者的多场数据不得跨训练/测试边界。

### 5.2 内层开发与预处理

inner validation（内层验证）采用 participant-grouped cross-validation（参与者分组交叉验证）。插补、标准化、模型选择和任何数据依赖变换只能在外层训练数据内部拟合，再应用于测试参与者。

### 5.3 参与者等权

训练与主要评价强调 participant-equal（参与者等权）原则，避免参加次数较多的参与者仅因 probe 更多而支配整体结果。主要不确定性使用固定 OOF（折外）预测上的 participant-cluster bootstrap（参与者簇自助法）。

### 5.4 增量与条件价值

科学解释优先使用同一分析集合内的成对比较：

```text
Behavior → Behavior + x
Full - x → Full
```

不同模态单独模型若使用不同可用样本，其原始 log loss（对数损失）或 AUROC（受试者工作特征曲线下面积）不能直接横向排名。

### 5.5 四分类扩展

Q1 四分类沿用既定参与者互斥与分析集合合同，但评价必须同时查看 multiclass log loss（多分类对数损失）、macro AUROC（宏平均曲线下面积）、balanced accuracy（平衡准确率）、macro F1（宏平均 F1）、Brier（布里尔分数）、类别概率和预测类别分布。概率损失改善不等于已经形成可用的四类别判别。

## 6. 当前单模态方法要点

### Behavior

当前正式行为分析围绕 probe 前窗口和任务进程组织 RT 水平、RT-CV（反应时变异系数）、Theil–Sen slope（Theil–Sen 斜率）、Go omission（Go 遗漏）、No-Go commission（No-Go 误按）等变量。RT-CV 当前唯一口径为 30 s 窗口内至少 **2 次**有效正确 Go 反应；历史 `rt_cv_min_n = 20` 已作废。

### Ocular

正式 Ocular 把 NIR 瞳孔与 RGB 眨眼作为同一科学模态下的不同特征家族。第一轮瞳孔主表示为 hard `R_seg = pupil/(pupil+iris)`（硬分割瞳孔面积比例），几何直径保留为跨表示敏感性；波动主表示为 MAD（中位数绝对偏差）。probe 前 30 s 使用 15 个 2 s fixed bins（固定时间箱），bin 内中位数，空 bin 不插值；线性斜率/二次曲率要求至少 20 s 真实时间支持。RGB 眨眼同时提供独立 blink rate（眨眼频率）和瞳孔伪迹辅助清洗。

### Movement

第一轮 Movement 主指标为整体身体动作强度中位数；横向/纵向姿态作为敏感性，径向方向代理与曝光/全局画面变化作为 QC 或辅助指标。动作值是相对无量纲表示，不解释为真实物理位移或能量。

### Cardiopulmonary

mmWave producer 的 provenance（来源追踪）和 pre-probe time-legality（探针前时间合法性）已经闭环，毫米波估计心率和呼吸率进入正式 feature registry 与监督学习比较。该资格**不等于独立生理效度验证**；HR/BR 当前为支持性指标，HRV（心率变异性）继续阻塞。

## 7. 1.16 系列怎样读

1.16 系列仍是当前方法形成的核心证据，但要按“合同”与“阶段状态”区分：

| 主题 | 推荐用途 |
|---|---|
| `1.16.1` | Q1 预测心理意义、参与者等权、分层验证和评价原则 |
| `1.16.2–1.16.6` | Ocular 瞳孔×眨眼测量、审计和特征治理 |
| `1.16.7–1.16.10` | RGB/Movement、报告变量、预测扩展、模态/设备区分 |
| `1.16.11–1.16.12` | 监督学习特征接口、运行闸门、科学输出与 handoff |
| `1.16.13–1.16.19` | Behavior/Ocular/Movement 的真实运行、冻结、P3/P4/P5 收口与结果汇报角色 |
| `1.16.20–1.16.23` | RT 水平冻结、sensor-only（仅传感）预注册、概率诊断、RT-CV 口径统一 |

其中部分文件标题仍含“计划”“停止点”“待运行”，因为它们保存当时决策时点。判断**现在是否已经完成**必须再读当前结果总账、Attention 当前代码和后出的运行证据。

更早 1.15.x 及 1.1–1.14 文件主要用于方案演变和历史解释；与后出 1.16 或当前实现冲突时，不覆盖当前正式路线。

## 8. 当前结果与方法的分工

本目录不应重复保存最终结果数字。正式结果进入：

```text
国赛报告/完整结果/
```

面向评审者的压缩表达进入：

```text
国赛报告/章节草稿/5.*
```

运行版本、输入哈希、producer commit（生产端提交）和异常处置进入：

```text
运行记录与证据/
```

如果方法文件仍描述一个旧待办，而完整结果与运行记录已经证明该步骤完成，应更新 README/状态索引，不应修改历史方法文件来伪造当时已经完成。

## 9. 当前代码入口

正式科学代码统一查看：

```text
kyandi233-dev/Attention-Analysis
└─ codex/formal-analysis-v2-portable
```

NIR、RGB 的硬件 producer 分支只负责生产来源：

```text
amd-DirectML
nvidia-cuda-v8
rgb-amd
rgb-nvidia
```

当前不要再从已经删除的临时 `codex/*` 分支恢复任务。如果需要追溯其独有历史，使用 commit、PR、Issue 或 archive tag（归档标签）。