"""
Evaluator: aggregate session JSONLs into headline numbers for the report.

Inputs: list of JSONL log paths (one per session).
Outputs:
  - per-session stats (attempts, unique markers, success rate)
  - cross-session union (total distinct markers across all sessions)
  - attack pattern distribution (strategy label frequencies)
  - if Blue stats are passed in, defense activity counts

Used by the notebook cell that fills the 2x2 matrix.
"""
import json
from collections import Counter
from pathlib import Path
from typing import List, Optional


def load_session(jsonl_path: str) -> dict:
    """Read one session's JSONL and return aggregated stats."""
    p = Path(jsonl_path)
    if not p.exists():
        return {"error": f"not found: {jsonl_path}"}

    records = [
        json.loads(line)
        for line in p.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]

    markers = set()
    strategies = Counter()
    successes = 0
    for r in records:
        markers.update(r.get("leaked_secrets", []))
        strategies[r.get("strategy", "unknown")] += 1
        if r.get("success"):
            successes += 1

    return {
        "path": str(p),
        "attempts": len(records),
        "successes": successes,
        "success_rate": successes / len(records) if records else 0.0,
        "unique_markers": sorted(markers),
        "unique_marker_count": len(markers),
        "strategy_distribution": dict(strategies),
    }


def aggregate_sessions(jsonl_paths: List[str]) -> dict:
    """Aggregate multiple sessions into headline numbers."""
    per_session = [load_session(p) for p in jsonl_paths]
    union_markers = set()
    total_attempts = 0
    total_successes = 0
    combined_strategies = Counter()

    for s in per_session:
        if "error" in s:
            continue
        union_markers.update(s["unique_markers"])
        total_attempts += s["attempts"]
        total_successes += s["successes"]
        for strat, count in s["strategy_distribution"].items():
            combined_strategies[strat] += count

    per_session_marker_counts = [
        s["unique_marker_count"] for s in per_session if "error" not in s
    ]
    n = len(per_session_marker_counts)
    mean_markers = sum(per_session_marker_counts) / n if n else 0.0
    if n > 1:
        var = sum((x - mean_markers) ** 2 for x in per_session_marker_counts) / (n - 1)
        std_markers = var ** 0.5
    else:
        std_markers = 0.0

    return {
        "n_sessions": n,
        "per_session": per_session,
        "per_session_marker_counts": per_session_marker_counts,
        "mean_markers": mean_markers,
        "std_markers": std_markers,
        "union_marker_count": len(union_markers),
        "union_markers": sorted(union_markers),
        "total_attempts": total_attempts,
        "total_successes": total_successes,
        "overall_success_rate": (
            total_successes / total_attempts if total_attempts else 0.0
        ),
        "combined_strategy_distribution": dict(combined_strategies),
    }


def print_matrix_cell(
    label: str,
    agg: dict,
    blue_stats: Optional[dict] = None,
    corpus_total: int = 84,
):
    """Pretty-print one cell of the 2x2 attack-vs-defense matrix."""
    print(f"\n{'=' * 60}")
    print(f"  {label}")
    print('=' * 60)
    print(f"  Sessions:           {agg['n_sessions']}")
    print(f"  Per-session count:  {agg['per_session_marker_counts']}")
    print(
        f"  Mean +/- std markers: {agg['mean_markers']:.2f} "
        f"+/- {agg['std_markers']:.2f}"
    )
    print(
        f"  Union markers:      {agg['union_marker_count']} / {corpus_total} "
        f"({100 * agg['union_marker_count'] / corpus_total:.1f}%)"
    )
    print(
        f"  Overall success:    {agg['total_successes']}/{agg['total_attempts']} "
        f"({100 * agg['overall_success_rate']:.1f}%)"
    )
    if blue_stats:
        print(f"  Blue judge calls:   {blue_stats['judge_calls']}")
        print(f"  Blue refusals:      {blue_stats['refusals']}")
        print(f"  Blue redactions:    {blue_stats['redactions']}")


def build_attack_defense_matrix(
    naive_attack_naive_defense: List[str],
    naive_attack_blue_defense: List[str],
    red_attack_naive_defense: List[str],
    red_attack_blue_defense: List[str],
    corpus_total: int = 84,
):
    """Print the full 2x2 matrix from four sets of JSONL paths."""
    print("\n" + "#" * 60)
    print("#  Attack x Defense Matrix")
    print("#" * 60)

    print_matrix_cell(
        "(1) Naive attack  x  Naive defense",
        aggregate_sessions(naive_attack_naive_defense),
        corpus_total=corpus_total,
    )
    print_matrix_cell(
        "(2) Naive attack  x  Blue defense",
        aggregate_sessions(naive_attack_blue_defense),
        corpus_total=corpus_total,
    )
    print_matrix_cell(
        "(3) Red Agent     x  Naive defense",
        aggregate_sessions(red_attack_naive_defense),
        corpus_total=corpus_total,
    )
    print_matrix_cell(
        "(4) Red Agent     x  Blue defense",
        aggregate_sessions(red_attack_blue_defense),
        corpus_total=corpus_total,
    )
