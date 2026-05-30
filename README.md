# RAG Privacy Agent

This repository contains the code and saved experiment artifacts for a
synthetic RAG privacy-leakage study. The corpus uses fake `_DECOY_<8-char>`
markers; no real credentials are included.

## Reproduce Saved Results Without API Calls

The reported figures and summaries can be checked without spending API
credits:

1. Open `notebooks/phaseC_experiment.ipynb`.
2. Start from the cells that load `logs/phaseC_*.jsonl`.
3. Rerun the aggregation and plotting cells.

The notebook recomputes statistics from JSONL logs and writes summaries under
`reports/`.

## Rerun Experiments With API Calls

To rerun the attack sessions, create a local `.env` file from the template:

```bash
cp .env.example .env
```

Then edit `.env`:

```env
ANTHROPIC_API_KEY=your_anthropic_api_key_here
```

The real `.env` file is intentionally ignored by git.

## Key Files

- `src/`: RAG system, Red Agent, Blue Agent, and evaluation helpers
- `data/fake_docs/`: synthetic IoT-company documents with planted markers
- `logs/phaseC_*.jsonl`: raw saved experiment logs
- `reports/`: saved summaries and figures
- `notebooks/phaseC_experiment.ipynb`: completed experiment notebook
