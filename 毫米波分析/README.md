# 毫米波分析

本模块先完成本机当前 44-session 的 HR、RR/BR、质量覆盖和行为对齐，输出 schema 固定、可与后续约 72-session 直接纵向拼接的 merge-ready 行级表和 manifest。HR、RR、IBI/HRV 的“能计算”“通过工程 QC”“通过外部生理验证”“可进入报告”是不同状态。RGB motion gate 只生成附加标记和敏感性副本，不覆盖原始毫米波输出。

