# 科研绘图 Prompt 模板

本模板只在 Figure Specification 已确认后使用。不要让图像模型重新解释或改写科学关系。

## A. Prompt 主体结构

### 1. Communication goal

Create a publication-quality scientific figure that clearly communicates:

> [用一句话写这张图最核心的科学信息]

### 2. Composition

- Overall layout: [horizontal / vertical / multi-panel]
- Number of major regions: [N]
- Region A on the [left/top]: [具体放什么]
- Region B in the [center]: [具体放什么]
- Region C on the [right/bottom]: [具体放什么]
- Maintain generous whitespace between major regions.

### 3. Scientific objects

Describe each object concretely rather than naming only its category.

- [Object 1]: [外观、位置、必须体现的科研特征]
- [Object 2]: [外观、位置、必须体现的科研特征]
- [Object 3]: [外观、位置、必须体现的科研特征]

### 4. Relationships and arrows

Write every important connection explicitly.

- Draw an arrow from [A] to [B], representing [含义].
- Draw parallel arrows from [A/B/C] toward [D], representing [并行采集/汇聚/时间顺序].
- Do not use arrows between [X] and [Y] because their relationship is associative rather than causal.

### 5. Labels

Use exactly these short labels:

- [label 1]
- [label 2]
- [label 3]

Do not invent additional scientific claims or long text inside the figure.

### 6. Visual hierarchy

- Primary visual emphasis: [核心对象/流程]
- Secondary emphasis: [辅助模态/时间轴]
- Supporting elements: [必要背景]
- Keep implementation details visually subordinate.

### 7. Style constraints

Publication-quality flat vector scientific schematic; white background; restrained scientific palette; thin consistent outlines; large readable typography; minimal shadows; no 3D rendering; no decorative background; no excessive gradients; no unnecessary icons; no dense paragraphs; preserve clear spacing and alignment.

### 8. Hard constraints

- Do not change the scientific topology described above.
- Do not add sensors, variables, causal arrows, outcomes, or performance claims not listed in the specification.
- Do not create a generic “attention score” unless explicitly requested by the specification.
- Do not include identifiable faces or specific experimental locations.
- Keep all text short and legible.

## B. 两阶段使用方式

第一轮只输出 Figure Specification，不生图：

> 根据提供的研究方法，先充当 scientific figure designer。只输出 Figure Specification：沟通目标、构图、主要区域、对象、箭头、并行/时间/汇聚关系、应省略内容和全部图内标签。暂时不要讨论配色，也不要生成图片。

第二轮在规格确认后生成最终 Prompt：

> 根据已经确认的 Figure Specification 生成完整英文 image-generation prompt。不得改变任何科学关系。详细描述空间布局、对象位置、箭头方向、视觉层级、图内标签和 hard constraints，再加入期刊级科研示意图风格要求。

## C. 结构图的额外规则

如果图的核心是流程、时间轴、分析管线或统计结构，优先先生成 Mermaid/SVG 草图检查结构。只有在需要人体、仪器、眼睛或复杂视觉对象时，才让生成式图像模型参与视觉化。最终图中的文字、框和箭头优先用 SVG/PPTX 重建为可编辑对象。
