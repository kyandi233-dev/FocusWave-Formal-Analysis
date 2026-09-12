# 毫米波正式环境创建与sub-031 VMD smoke

## 总结

按正式阶段授权，新建任务专用环境`D:\CondaEnvs\focuswave-mmwave-formal`并安装锁定的`vmdpy==0.2`。环境内VMD预检通过，PR20代码路径可调用；随后使用阶段0.2修正版manifest完成`sub-031` VMD smoke。

Smoke输出的5个JSON均严格解析通过、无`NaN/Infinity`，汇总schema通过，匿名组键正确透传；但baseline和block2成功，block1因`NO_VALID_CHANNEL_BIN_SELECTION`被拒绝，整体为`n_segments_succeeded=2`、`n_segments_failed=1`。依据“smoke质量门通过后才扩大”的授权条件，本轮停止，不运行39场全量、不生成正式HR/呼吸统计、不生成重复组混合模型或参与者互斥预测基线。

## 原计划

1. 核验专用环境目标不存在，创建环境且不覆盖既有环境。
2. 安装并锁定`vmdpy==0.2`及必要运行/验证依赖，导出环境文件和explicit spec。
3. 用阶段0.2 manifest执行唯一一次`sub-031` VMD smoke。
4. 核验schema、严格JSON、质量、失败记录和匿名组键。
5. 仅当smoke整体通过后运行39场；否则记录失败并停止。

## 执行与决策过程

### 1. 环境创建和记录

目标路径初检为不存在，随后执行：

```powershell
conda create --prefix D:\CondaEnvs\focuswave-mmwave-formal python=3.13 pip -y
conda run --prefix D:\CondaEnvs\focuswave-mmwave-formal python -m pip install numpy pandas scipy matplotlib jsonschema pytest vmdpy==0.2
```

两条命令均退出码0。实测环境解释器为`D:\CondaEnvs\focuswave-mmwave-formal\python.exe`，Python 3.13.15；`vmdpy=0.2`且`VMD`符号可调用；numpy 2.5.2、scipy 1.18.1、pandas 3.0.5、matplotlib 3.11.1、jsonschema 4.26.0、pytest 9.1.1。

导出文件位于：

```text
D:\_AttentionData\mmwave_local_execution\20260829_formal39_vmd_fc682b4\environment.yml
D:\_AttentionData\mmwave_local_execution\20260829_formal39_vmd_fc682b4\conda-explicit-spec.txt
D:\_AttentionData\mmwave_local_execution\20260829_formal39_vmd_fc682b4\environment-runtime.txt
```

导出文件哈希分别为：

```text
environment.yml: 88125F9E0EEB87EDF6064F85286EE691B87C6979B415DBFAD251D6C0EB46FA30
conda-explicit-spec.txt: 38274A3A270F021DA51724BF49FEDAF247B320734AFEE22BB4CD61ACE9182183
environment-runtime.txt: 42828DEED35E09235F9744BA2D3BC62FDE0640C4F917BF903FB954ACE5540E54
```

第一次导出命令因为误用`New-Item -LiteralPath`失败，随后改用`New-Item -Path`成功；失败未改变环境和输入资产。Smoke后的第一次多行JSON检查误经`conda run ... python -c`调用，返回`NotImplementedError: Support for scripts where arguments contain newlines not implemented`；随后改用环境解释器绝对路径直接执行并成功完成门检查。

### 2. Smoke命令

使用manifest：

```text
D:\_AttentionData\mmwave_local_execution\20260829_pr20_sub031_stage0_2_manifest.csv
SHA-256: 8408C14005885AF8E6955DF43A5B2887F8C8CD3BD26362F8DD0BDDAF1B8C9B63
```

使用全新输出目录：

```text
D:\_AttentionData\mmwave_local_execution\20260829_formal39_vmd_fc682b4\smoke_sub031
```

实际命令：

```powershell
conda run --prefix D:\CondaEnvs\focuswave-mmwave-formal --no-capture-output python -u scripts/run_timeline_gated_mmwave_quality.py --roots E:\正式实验 --input-manifest D:\_AttentionData\mmwave_local_execution\20260829_pr20_sub031_stage0_2_manifest.csv --output-dir D:\_AttentionData\mmwave_local_execution\20260829_formal39_vmd_fc682b4\smoke_sub031 --run-analysis --method vmd_heart --analysis-id mmwave_formal39_sub031_vmd_smoke_v1
```

退出码为0，但程序显式报告失败段1个，不能按进程退出码判定通过。

### 3. Smoke结果

| 分段 | 结果 | 状态 |
|---|---|---|
| baseline | HR融合候选82.1 bpm，BR时域19.4 bpm，IBI候选734.7 ms | HR信号工程门通过；BR待独立工程门；IBI/HRV候选 |
| block_1 | 无HR/BR/IBI/HRV数值 | `algorithm_returned=false`、`quality_valid=false`、`selection_status=rejected`、`failure_reason=NO_VALID_CHANNEL_BIN_SELECTION` |
| block_2 | HR融合候选57.6 bpm，BR时域18.9 bpm，IBI候选1042.1 ms | HR信号工程门通过；BR待独立工程门；IBI/HRV候选 |

这些数值只是工程算法观察，不能解释为生理结果。所有分段外部验证均为`not_available`，行为关联和正式报告均阻断。

### 4. 契约核验

- JSON文件5个，严格解析通过，非有限字面量0个。
- `segment_analysis_summary.json`通过对应schema。
- 汇总为1个session、2个成功分段、1个失败分段；rows为3行、34列。
- `anonymous_participant_group_id=apg-r-B4266D433438E0E4`正确透传；未填写global `repeat_participant_id`。
- block1保留结构化拒绝，不生成伪成功结果；baseline和block2各有VMD vital JSON。
- 输出目录为25个文件、16,720,637字节；无历史目录覆盖。

Smoke关键输出哈希：

```text
crop_manifest.json: 9FC0CE02FCED81F0BB520D29464EE6107C08234B9992946C5D38FB4FE3721B52
crop_summary.json: 2683CE3B3B0AF09DECD9B5F9707A880D9A1C87C304F76EC97DBAAC031458A8A8
segment_analysis_summary.json: FB55FFFCF3F2775914CFDED1CC2B89E1C4C41CBF97FF8AB018F09DBF0E9629D0
segment_analysis_rows.csv: 5E749A3A8DA32ABF8D35AE2EE49663FA6EA961CDF8714946F38CDCAF1D491633
```

## 最终决策结果

环境门通过，smoke的schema和严格JSON门通过，但整体质量门不通过。正式39场生产不放行，原因是仍存在未解释的`NO_VALID_CHANNEL_BIN_SELECTION`失败段。必须由代码/Git任务处理或批准该失败路径后，用新空目录重新完成单场VMD验证，再决定是否扩大。

本轮不生成重复组混合模型、参与者互斥预测基线或正式分析表；这些步骤必须等待39场生产整体通过。IBI/HRV保持候选/阻断，不写成外部验证通过；BP轨道与VMD轨道不合并；RGB运动只保留future/sensitivity边界。

## 待确认事项

1. Git任务确认`fc682b4`是否为最终冻结可运行worktree，或提供新的PR20加固HEAD。
2. 代码任务解释`NO_VALID_CHANNEL_BIN_SELECTION`并完成单场整体无未解释失败的验证。
3. 重新smoke通过后，再在全新`full39`目录执行39场生产，并为036/038/040/041/047写入结构化缺失表。
