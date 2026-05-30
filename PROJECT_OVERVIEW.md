# Agentic Privacy Leakage in Refusal-Hardened RAG

UCLA ECE 202C, Spring 2026 - Final Project

## 1. Research Question

This project studies privacy leakage in a Retrieval-Augmented Generation
(RAG) assistant built over a synthetic IoT-company document corpus. The
documents contain planted canary markers in the form `_DECOY_<8-char>`.
Leakage is measured by how many distinct markers an attacker can cause the
RAG system to reveal.

The main question is:

> In a cost-asymmetric deployment, where the attacker can use a stronger
> model than the RAG generator and defender, how much privacy leakage remains
> after a lightweight Blue defense is added?

The setup is motivated by production constraints: a public-facing RAG service
may use cheaper models for serving and filtering, while an attacker can spend
more per query on a targeted campaign.

## 2. Threat Model

The project follows the EDEA framing from SECRET (He et al., 2025): an attack
can be described by an extraction instruction, a jailbreak operator, and a
retrieval trigger.

**Red Agent**

- Model: Claude Sonnet 4.5
- Access: black-box query access to the RAG endpoint
- Observations: answer text, retrieved filenames, retrieved sensitivity tags,
  and automatic marker-detection feedback
- Budget: 25 tool calls per session in the main Phase C runs
- No access to: Blue prompts, full vector store contents, or the ground-truth
  marker list

**RAG and Blue Agent**

- RAG generator: Claude Haiku 4.5
- Blue judge: Claude Haiku 4.5
- Blue defense:
  - pre-generation query judge
  - optional regex output redactor for `_DECOY_` markers
- No cross-session memory or persistent hardening is used.

## 3. Experiment Design

Phase C uses a 2 by 3 matrix:

| Attacker | No Blue | Judge only | Judge + redact |
|---|---:|---:|---:|
| Naive attack | Cell 1 | Cell 2 | Cell 3 |
| Red Agent | Cell 4 | Cell 5 | Cell 6 |

The naive attack is a fixed list of hand-written queries. The Red Agent runs
independent sessions and adapts after each query using tool feedback.

Cell 7 is an additional ablation:

- Cell 6: Red Agent vs Judge + redact
- Cell 7: Red Agent vs Judge + redact, with an encoding-bypass strategy hint

Cell 7 checks whether transformation-style prompting changes the outcome
against the same defense pipeline.

## 4. Metrics

- **Per-session unique markers**: number of distinct markers leaked in each
  session.
- **Union markers**: distinct markers leaked across all sessions in a cell.
- **Pre-redaction union**: markers emitted by the RAG generator before Blue's
  output redactor.
- **Post-redaction union**: markers actually visible to the attacker.
- **Strategy distribution**: Red Agent strategy labels from `record_attempt`.
- **Defense attribution**: whether attempts were stopped by the judge, by the
  redactor, or by the RAG model refusing/withholding content.

## 5. Repository Layout

```text
src/
  rag/
    ingest.py        Build the ChromaDB collection from fake docs
    system.py        RAGSystem with optional Blue defense
  agents/
    tools.py         Tool wrappers, leakage checker, JSONL logger
    red_agent.py     Tool-use Red Agent loop
    blue_agent.py    Query judge and regex redactor
  eval/
    evaluator.py     JSONL aggregation helpers

data/
  fake_docs/         Synthetic IoT-company documents with planted markers

notebooks/
  phaseC_experiment.ipynb

logs/
  phaseC_*.jsonl    Raw Phase C session logs

reports/
  phaseC_summary.json
  phaseC_cell7_analysis.json
  figures/

```

## 6. Reproducibility Notes

The raw Phase C logs are included so the figures can be regenerated without
spending API credits. To rerun the attacks, create a local `.env` file with an
Anthropic API key, rebuild the ChromaDB collection from `data/fake_docs`, and
run `notebooks/phaseC_experiment.ipynb`.

The repository intentionally does not include API keys, `.env`, Python cache
files, or the generated ChromaDB database.
