# AI project pointer

- project_identity: FocusWave formal analysis and report evidence
- canonical_repository: https://github.com/kyandi233-dev/FocusWave-Formal-Analysis.git
- canonical_branch: `main`; task-specific refs must be verified before writes
- repository_role: analysis plans, research decisions, report specification, execution/evidence records, result indexing and report-facing provenance
- central_governance: https://github.com/greenboo26/ai-governance; read current `adapters/RUNTIME_BOOTSTRAP.md`, `rules/execution.yaml`, `rules/repository-sync.yaml`, and `rules/durable-project-record.yaml`
- workspace_registry: `greenboo26/project@august/PROJECT_INDEX.md`
- local_startup_files: `AGENTS.md`, root `README.md`, `运行记录与证据/README.md`, current module README/work record/result index
- related_repository_roles: `FocusWave@formaltest` owns formal experiment/acquisition implementation; `Attention-Analysis` owns Behavior/NIR/RGB producer and single-modality analysis; `focuswave-multimodal-attention-analysis@main` owns canonical mmWave/multimodal integration and cross-modal inference

## Branch hygiene

`main` is the current discovery and canonical evidence branch. Topic/research branches are provenance or task-specific work unless a current handoff explicitly promotes one. In particular, `codex/code-fix-ledger` is currently the head of draft PR #43 and contains one unreconciled NIR documentation/terminology correction; it is not a competing canonical branch and must not override `main` until that change is reviewed and merged or otherwise reconciled.

This file is navigation only. It does not replace current module methods, run records, result indexes or producer repositories. For scientific claims, verify the current record and the repository that owns the underlying producer/result.
