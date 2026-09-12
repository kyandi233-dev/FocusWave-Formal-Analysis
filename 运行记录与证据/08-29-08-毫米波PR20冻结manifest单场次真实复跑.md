# 毫米波PR20冻结manifest单场次真实复跑

## 总结

本次作为本地毫米波数据执行任务，在PR20隔离工作树`D:\AAAWORK\07-竞赛\厚璨杯\验证工作树\毫米波-PR20-fc682b4`（`fc682b491fcbeeb9bd1b030c8af9da33282d2846`，detached、干净）上完成指定解释器核验、VMD/BP方法预检、冻结`sub-031` manifest单场次真实复跑和输出契约验收。VMD因缺少`vmdpy==0.2`保持`blocked`，未安装依赖、未静默降级；显式`bp_heart`工程冒烟完成，但三段中block1被严格拒绝，因此**不通过扩大门**。

本轮未运行39场/33组正式生产，未进行正式统计，未形成HR/RR/IBI/HRV生理结论。新增正式证据文档为`毫米波分析/1.4-PR20冻结manifest单场次真实复跑与扩大量门.md`，本记录保留未提交。

## 原计划

1. 完整读取PR20工作树入口、已有毫米波1、1.1、1.2、1.3文档和`08-29-07`记录。
2. 核验工作树HEAD、状态、冻结manifest和`D:\Code\python\python.exe`。
3. 从冻结当前队列身份映射中使用仅含`sub-031`的单场次manifest，在全新空目录显式运行`bp_heart`。
4. 核验VMD阻断、严格JSON、HR/RR质量同源、状态字段、匿名组键、分段表、manifest、哈希和非空输出保护。
5. 写入后续毫米波证据文档和本工作记录，判断是否允许扩大。

## 执行与决策过程

### 1. 入口和治理

已完整读取PR20工作树的`AGENTS.md`、`README.md`、`pipelines/mmwave/README.md`、`docs/mmwave_reanalysis_v2/README.md`和`configs/mmwave_reanalysis_v2/manifest.json`，以及正式证据库毫米波分析`1`、`1.1`、`1.2`、`1.3`和`运行记录与证据/08-29-07`。

入口约束确认：global身份、global cohort和跨站点推断只能中央冻结；HRV保持阻断；正式cohort HR/BR在ECG/RSP外部参考门冻结前不得运行；本地派生只写Git-safe provenance和外部数据区产物。

### 2. 冻结manifest和输入事实

冻结源为：

```text
D:\_AttentionData\anonymous_participant_mapping_phase0_1_20260829\anonymous_session_participant_mapping.csv
```

从源文件抽取`sub-031`一行生成：

```text
D:\_AttentionData\mmwave_local_execution\20260829_pr20_sub031_frozen_manifest.csv
SHA-256: 875464A7D5D2610559AB88D2E988FC701EEC992269AFF32D4AD582C5B7224DA9
anonymous_participant_group_id: 具体值仅保留在数据区 manifest，不写入 Git 记录
```

只读复核当前身份/输入口径：当前队列44场、38个匿名分析组，其中6个双场重复组；毫米波可加载39场、33个当前队列匿名分析组；`global`跨队列身份尚未冻结。036/038/040/041为32字节`.bin`和0字节timestamps无效占位，047目录为空。未来+72场次必须重新生成全量映射和全量合并键。

### 3. 解释器和预检

`D:\Code\python\python.exe`实测为Python 3.13.0，`vmdpy_spec=None`。

VMD命令：

```powershell
D:\Code\python\python.exe -u scripts/run_timeline_gated_mmwave_quality.py --preflight-only --method vmd_heart
```

结果：`blocked`、`MISSING_VMDPY_DEPENDENCY`、`selected_method=null`、退出码2。保持阻断，未安装新依赖。

BP命令：

```powershell
D:\Code\python\python.exe -u scripts/run_timeline_gated_mmwave_quality.py --preflight-only --method bp_heart
```

结果：`pass`、`selected_method=bp_heart`、`backend=scipy_bandpass`、退出码0。

### 4. 真实复跑

输出目录在运行前不存在：

```text
D:\_AttentionData\mmwave_local_execution\20260829_pr20_sub031_bpheart_fc682b4
```

实际命令：

```powershell
$env:PYTHONIOENCODING='utf-8'; $env:PYTHONUTF8='1'
& 'D:\Code\python\python.exe' -u scripts/run_timeline_gated_mmwave_quality.py --roots 'E:\正式实验' --input-manifest 'D:\_AttentionData\mmwave_local_execution\20260829_pr20_sub031_frozen_manifest.csv' --output-dir 'D:\_AttentionData\mmwave_local_execution\20260829_pr20_sub031_bpheart_fc682b4' --run-analysis --method bp_heart --analysis-id mmwave_pr20_sub031_smoke_v1
```

程序退出码为0，但结果为`completed_with_failures`：baseline成功、block1失败、block2成功。block1的精确拒绝为：

```text
algorithm_returned=false
quality_valid=false
selection_status=rejected
failure_reason=NO_VALID_CHANNEL_BIN_SELECTION
```

PR20没有回退到`ch0/bin10`，失败段保留8个候选摘要。

## 最终决策结果

### 1. 契约核验

- 5个JSON全部严格解析通过；原始JSON无`NaN`、`Infinity`、`-Infinity`。
- baseline和block2的`breath_rate`、`heart_rate.time_course.signal_quality`、`heart_rate.time_course.metrics`均与对应生产JSON同源且完全一致。
- `algorithm_returned`、`quality_valid`、`selection_status`、`failure_reason`及三类工程状态均写入segment结果和34列的`segment_analysis_rows.csv`。
- 冻结匿名组键透传至crop manifest、summary、segment和rows；具体值仅保留在数据区产物中，`repeat_participant_id`保持空值。
- `crop_summary.json`和`segment_analysis_summary.json`保留输入manifest路径、哈希和`n_sessions=1`；rows为3行，对应3个分段。
- 已有输出目录再次调用入口时返回`OUTPUT_DIRECTORY_NOT_EMPTY`、退出码1，未覆盖已有产物。

### 2. 运行产物

完整输出目录为：

```text
D:\_AttentionData\mmwave_local_execution\20260829_pr20_sub031_bpheart_fc682b4
```

关键文件SHA-256：

| 文件 | SHA-256 |
|---|---|
| `crop_manifest.json` | `1FB4AFF58265281C0C82370969DB6CCC3BBEA3A2828002407C1A8812551E984E` |
| `crop_summary.json` | `6CFF924EA93C799E4D7A6AF27BF02A9C8B9718904CF115F1B0971A83F612966F` |
| `segment_analysis_summary.json` | `F0809B8AE3F194400A3E666178DE4B689C5BC2302EF09F837CD586A00D9F9FC5` |
| `segment_analysis_rows.csv` | `3AE6E2F382A06B7BA919721436CD78F60DFD90B09F840438E849870066F97D0A` |

### 3. 定向测试

```powershell
D:\Code\python\python.exe -m pytest -q tests/test_mmwave_production_contract_v1.py tests/test_mmwave_benchmark_contract_v1.py
```

结果：`18 passed in 1.55s`。requests产生依赖版本提示，但不影响退出码。中央PR20工作树仍干净，本轮没有代码、配置或测试变更。

## 已完成事项

- 完整读取PR20入口和指定正式证据文档。
- 核验`fc682b4` detached干净工作树和`D:\Code\python\python.exe`。
- 以冻结`sub-031` manifest完成一次真实、隔离、显式`bp_heart`复跑。
- 复核VMD依赖阻断、严格JSON、同源HR/RR质量、状态字段、匿名组键、manifest和输出哈希。
- 实际验证非空输出保护。
- 只读复核39场/33组可加载队列及5个无效/空输入。
- 写入毫米波`1.4`后续文档。

## 未完成与待确认事项

- VMD `vmdpy==0.2`仍未安装，VMD正式方法未能真实复跑。
- `sub-031`的block1被`NO_VALID_CHANNEL_BIN_SELECTION`拒绝，单场次整体未通过扩大门。
- HR/RR/IBI/HRV均未完成外部ECG/RSP验证；HRV仍为候选/阻断，不作生理解释。
- 未运行39场正式生产、未进行正式统计、未形成行为关联或报告结论。

## 正式扩大门判断

**不通过。** 在VMD依赖、单场次失败段处理和完整三段重跑均通过前，不得扩大到39场/33组。后续+72场次必须重新生成全量匿名映射和合并键；任何需要安装依赖、修复代码或改变字段契约的动作交回对应治理任务，本地任务不自行处理。
