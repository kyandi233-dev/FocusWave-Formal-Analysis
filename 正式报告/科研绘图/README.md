# 科研绘图工作区

本目录用于 FocusWave 正式报告中的科研流程图、实验范式图、采集示意图、方法框架图和图形摘要。这里保存图形规划、Figure Specification（图形规格）、外部工具参考、结构草图和最终可编辑图；统计结果图仍应由正式分析代码从真实数据生成，不以生成式图片替代。

## 当前绘图原则

科研图优先保证科学关系正确，再处理视觉风格。每张图先固定沟通目标、panel 数量、每个 panel 的对象、箭头关系、图内文字和省略项，再交给外部绘图工具或设计者制作。避免直接把长篇方法文字交给生图模型，也不使用仅包含“Nature style”“clean”“professional”等表面风格词的提示词。

用户给出的论文示例表明，本报告更适合采用 **人工可控的多面板矢量科研图**，而不是自动流程图。因此当前正式路线为：

1. **Figure Specification**：在本仓库固定科学逻辑和 panel 结构。
2. **外部制作**：根据图类型选择 Figma、Adobe Illustrator、Inkscape、BioRender 或其他专业科研绘图工具。
3. **矢量重建与校对**：确保文字、箭头、框、设备和 panel 标签保持可编辑，并检查科学关系、字体、对齐、留白和颜色。
4. **结果图分离**：真实统计结果图由分析代码生成，不由生成式工具伪造或美化不存在的结果。

## 工具分工

- **Figma**：推荐作为主要排版与结构绘图工具。适合实验范式、方法框架、多模态数据流和复杂 panel 布局。
- **Adobe Illustrator**：适合最终精修、矢量线条、复杂箭头、出版级版式和 PDF/SVG 输出。
- **Inkscape**：开源替代方案，适合可编辑 SVG 与矢量科研图。
- **BioRender**：适合参与者、摄像头、眼睛、雷达、电脑等科研图标和设备示意；建议作为素材/场景起稿工具，再到 Figma/Illustrator 统一版式。
- **PowerPoint**：可快速搭建范式图和 panel 草稿，但复杂终稿建议转入矢量软件。
- **sci-plot / PaperVizAgent / academic-figures / scientific-figure 等公开仓库**：主要作为 Figure Specification、科研图组织方式、SVG 规范和提示词设计参考，不再要求必须在 GitHub Actions 中直接生成终稿。

## Mermaid 的当前定位

F02 曾建立 `mgranberry/mermaid-diagram-skill` 的 GitHub Actions 实际调用链，并成功得到渲染 PNG。这一试验验证了自动流程图的结构正确性，但最终视觉效果不符合当前报告所需的专业多面板学术插图风格。

因此：

- `F02-正式实验范式与时间轴/f02-timeline.mmd` 与 `rendered/f02-timeline.png` 保留为结构验证记录；
- Mermaid 不再作为正式报告插图的终稿路线；
- 正式 F02 改为 4-panel 实验范式图，并由 Figma/Illustrator/Inkscape 等精确排版。

## 目录索引

- `01-图形总计划.md`：当前正式建议绘制的图及工具分工。
- `02-Figure-Specification模板.md`：通用图形规格模板。
- `03-科研绘图Prompt模板.md`：需要外部 AI 绘图时使用的提示词结构。
- `04-六张正式科研图详细规格_20260830.md`：F01～F06 的完整科学逻辑、panel 布局、标签、箭头和边界，可直接交给外部绘图工具或设计者。
- `05-正文图三分类清单_20260831.md`：正文图的统一分类（科研示意图/统计结果图/补充图）与去向清单。
- `F02-正式实验范式与时间轴/figure-spec.md`：已经按专业 4-panel 范式重新设计的 F02 单图规格。
- `视觉AI重绘/`：2026-08-31 移入的视觉 AI 重绘图目录（路线图、管线与时间轴等）。

## 输出要求

最终方法图优先保存 SVG、PDF、AI 或 Figma 源文件；插入 Word 时可额外导出 300 dpi 以上 PNG。中文建议使用思源黑体/Noto Sans CJK SC，英文与数字可用 Arial/Helvetica。正式图中尽量不用长段文字，完整解释放在图题和正文。
