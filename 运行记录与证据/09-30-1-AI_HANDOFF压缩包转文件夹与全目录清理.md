# AI_HANDOFF 压缩包转文件夹与全目录清理

状态：进行中。任务范围仅为交接文件组织与完整性核验，不修改报告、分析代码、模型参数或科学结果。

上次整理只转换了 v13 的压缩包，遗漏了根目录中的 v9 及若干子目录中的归档 ZIP。本轮从正式 `_AI_HANDOFF`（folder id `1wZ6fHAyz4JMBwQ7LxL2fYZ9DdhO4XAfL`）递归核查，发现 8 个 ZIP；已完成 v9 的 7 个原始文件展开，加上交接说明与清单共 9 项，逐文件云端完整下载 SHA-256 全部匹配，并已删除旧云端 ZIP。根目录回读为零压缩包。

其余 7 包包含 v7 图表与报告核验、补充二分类分析、历史行为结果及预测与逐折记录。保留全部原始文件字节和目录关系，补充独立可读清单；待逐项核验全部通过后删除各原 ZIP。

进展更新：v7 的 108 项及 archive_predictions 的 21 项已逐文件完整下载 SHA-256 核验通过，原 ZIP 均已删除并回读确认不再列出。连同 v9，云端已完成 3/8 包转换。对本机剩余 14 份 ZIP 及回读副本逐一检查，所有成员均在展开目录中保留原始字节；已删除这些压缩包，本机交接目录当前无 ZIP。其余云端归档继续传输和核验，原 ZIP 保留至通过验证。

## 文件夹对应

| 原 ZIP | 替代文件夹 | 原始文件数 |
| --- | --- | ---: |
| v9 研究主线衔接交接包 | [2026-09-29_国赛报告v9研究主线衔接-33d9d8f](https://drive.google.com/drive/folders/1JvXqkuLcNm8Rgdw07XTYKolzcnvYTXqa) | 7 |
| 问题1选项1–2对3–4完整分析 | [完整分析文件](https://drive.google.com/drive/folders/11tzvnJRZBEOLCvQwXY1lLy3DhHE-2hkD)，位于原任务目录 | 420 |
| v7 图表与全文核验 | [图表与全文核验文件](https://drive.google.com/drive/folders/1knB2Ie00wsKrj7pUQxuAo_UyssxVhItk)，位于原任务目录 | 106 |
| formal_v3_20260912 | [formal_v3_20260912](https://drive.google.com/drive/folders/1CuAL5lNvW84Ozb2dj7SCkISiZm2NjdBO)，位于行为核验目录 | 167 |
| archive_predictions | [archive_predictions](https://drive.google.com/drive/folders/11-NGGDMDVOOSWuXpxsKmNwr4WMYUpL73)，位于原 predictions 目录 | 19 |
| probe_trajectory | [probe_trajectory](https://drive.google.com/drive/folders/1KWMC-F_lWEYMssb578wdP-hq4okulMIS)，位于原 predictions 目录 | 19 |
| probe_predictions | [probe_predictions](https://drive.google.com/drive/folders/1r1GbbGnu68wyJUd6GxM0UEIa37mr0pKD)，位于原 predictions 目录 | 19 |
| fold_audits | [fold_audits](https://drive.google.com/drive/folders/1l1RKj08RI-XbdIn6v5HV4ng9LAiXyYOl)，位于原 fold_audits 目录 | 19 |

本机解包及验证入口：`D:\Project\厚粲杯\11_数据\_FormalAnalysis\_handoff\2026-09-30_archive-conversion\`。`extract_and_manifest.py` 为解包、路径安全检查和清单生成脚本；`extracted_manifest.json` 记录原 ZIP 身份及每个展开文件的字节数和 SHA-256；`upload_receipts.jsonl`、`cloud_verified.jsonl` 记录云端文件身份和逐项完整下载校验。文件内容与明细留在本机和原有私有云盘，Git 仅登记记录与索引。

批量同步工具现场探测为授权失效；实际使用 Google Drive 连接器展开上传和完整回读，不宣称批量同步校验成功。研究方案、分析结果与报告版本决策均保持原状态。
