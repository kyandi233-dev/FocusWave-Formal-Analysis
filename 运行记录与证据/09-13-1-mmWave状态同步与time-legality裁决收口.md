# 09-13-1 mmWave 状态同步与 time-legality 裁决收口

## 目标与范围

本记录追溯 2026-09-13 毫米波（millimeter wave [mmWave]）状态同步与 producer-side time legality（生产侧时间合法性）方法裁决的正式收口。该轮工作只更新 `FocusWave-Formal-Analysis` 的方法与追溯层，不修改毫米波 producer、Attention-Analysis 代码、数据、算法、统一特征登记表（unified feature registry）或监督学习结果，也未重跑模型。

## Formal 收口版本

- Formal 权威分支：`kyandi233-dev/FocusWave-Formal-Analysis@codex/code-fix-ledger`。
- 状态同步：PR #10 `docs(mmwave): consolidate state sync on current canonical`，merge commit `b11d019ee94862e621d2d7a54eb0c9bf6046234a`。
- 方法裁决：PR #11 `docs(mmwave): land time-legality method decision on canonical`，merge commit `a4c5afa1ea22beef24b772e9c9cdfbc0f3eda370`。
- 当前方法落点：`分析设计/1.15.8-毫米波probe级表生成器实现问题与修复要求_20260910.md`、`1.15.9-毫米波生成链合同修复与time-legality处置_20260913.md`、`1.16-当前方法总状态与执行入口_20260912.md`、`1.16.10-监督学习模态与设备定义修订及代码迁移计划_20260912.md`、`1.16.11-监督学习特征文件接口与运行前闸门_20260913.md`。
- 被替代的 Formal PR #6、#8、#9 已关闭；旧 `codex/mmwave-formal-state-sync-v1@5f8b121` 仅保留为 provenance（来源追溯）/已核验增量来源，不再作为合入载体。
- 本轮未使用 force-push（强制推送）。

## mmWave 上游版本与 snapshot v1 lineage

- mmWave 权威仓库：`greenboo26/focuswave-multimodal-attention-analysis@main`；2026-09-13 本次追溯核验 HEAD 为 `3d3671f05b0c502e60824c9f7b9c2fa18efddbb6`。
- `MMWAVE_INTEGRATION_SNAPSHOT_V1` 的 manifest 记录 `source_commit=16729b2ef245f9304dae8674f3bac433bc02e98c`；该 corrected DLL-time replay（修正动态链接库时间回放）版本中，probe 右端排他边界、`window_effective_start_unix_ms` 切片起点和真实 usable fraction（可用窗口比例）三项均已修复。
- `16729b2` 不是当前 mmWave `main` 的祖先；当前 `main` 可见 adapter 仍保留 `1.15.8` 记录的三项旧合同问题。因此 current-main 源码链与 snapshot v1 实际执行 lineage 必须分开判断。
- replay manifest 记录的 adapter / producer / cohort-runner 源码 SHA-256 与其自记 `source_commit=16729b2` 对应文件未能一致复现，原因尚未确定。该问题定义为 source-code provenance（源码来源追溯）未闭环，不等同于已经证明 snapshot v1 的 2,320 行使用了错误时间窗口。

## 当前方法状态

| 项目 | 当前状态 | 解释边界 |
|---|---|---|
| `MMWAVE_INTEGRATION` | `READY` | snapshot v1 可继续用于接口、schema（模式）与 supporting integration（支持性集成） |
| `MAIN_ANALYSIS` | `PROCEED` | 总体分析可继续，不代表毫米波预测变量已取得正式预测资格 |
| HR / BR | `HOLD / SUPPORTING_ONLY` | 仅作为毫米波设备导出的心率/呼吸率支持性指标，不解释为已验证生理真值 |
| HRV | `BLOCKED` | 当前 snapshot 不授权心率变异性（heart rate variability [HRV]） |
| C1 / C2 | `PAUSED_PENDING_NEW_COLLECTION` | 等待满足预注册条件的新采集数据 |
| snapshot v2 | `NOT_FORMED` | 本轮不形成新快照 |
| `1.15.8` | `SUPERSEDED_BUT_TECHNICAL_ITEMS_NOT_CLOSED` | 治理角色已被当前方法入口替代；current-main 三项生成链合同技术项仍 OPEN |

## time-legality 正式裁决

`1.15.9` 新增 `blocked_upstream_contract_mismatch`：当正式时间合同明确，但上游 producer 实现、可追溯 lineage 或当前可执行主线与该合同存在已知不一致/无法无歧义复现时，采用该状态并严格 fail-closed（失败关闭）。

当前 snapshot v1 的时间语义有 corrected DLL-time replay 的生产端审计支持，且没有证据表明 2,320 行本身使用了错误窗口；但源码 provenance 尚未闭环。因此在该矛盾解决前，当前任何 Cardiopulmonary（心肺）feature 均不得取得 `verified_pre_probe_only`，全部正式预测资格保持 false。该状态是 Formal 方法合同，Attention-Analysis 的枚举、验证器和回归测试实现尚待其当前活动接口分支完成并稳定后接入，本记录不宣称代码已实现。

## 与 Attention-Analysis 的边界

本轮没有修改 `kyandi233-dev/Attention-Analysis`。当前统一监督学习接口仍由其活动的 `codex/1.16.10-modality-device-separation` / PR #68 维护；毫米波专用 ingest/audit（接入/审计）后续应基于该接口当时的最新稳定 HEAD 接续，而不在旧接口版本上平行修改。本记录不固定 PR #68 的瞬时 HEAD，以避免并行修复推进后产生伪版本权威。

## 收口状态

- `FORMAL_MMWAVE_STATE_SYNC = MERGED`
- `METHOD_DECISION = MERGED`
- `TRACEABILITY_SYNC = COMPLETE`（以本记录及 `运行记录与证据/README.md` 导航为准）
- `CARDIOPULMONARY_FORMAL_PREDICTION = FAIL_CLOSED`
- `MMWAVE_PRODUCER_CONTRACT_REPAIR = OPEN`
- `ATTENTION_IMPLEMENTATION = PENDING_CURRENT_INTERFACE_STABILIZATION`

后续如 source-code provenance 闭环、current-main producer 合同修复或 Attention-Analysis 实现状态发生变化，应新增后续记录，不回写本记录以覆盖本次历史状态。
