#!/usr/bin/env python3
"""Read and sanity-check the compact, shared-core dataset (stdlib only)."""
import gzip
import json
from collections import Counter
from pathlib import Path

PATH = Path(__file__).resolve().parents[1] / "data" / "consensus_place_event_pairs_core.jsonl.gz"

with gzip.open(PATH, "rt", encoding="utf-8") as handle:
    rows = [json.loads(line) for line in handle]

keys = {(r["article_id"], r["event_type"], r["place_normalized_name"]) for r in rows}
print("records:", len(rows))
print("distinct_articles:", len({r["article_id"] for r in rows}))
print("distinct_places:", len({r["place_normalized_name"] for r in rows}))
print("duplicate_coarse_keys:", len(rows) - len(keys))
print("distinct_categories:", len({r["event_type"] for r in rows}))
print("event type counts:")
for event_type, count in Counter(r["event_type"] for r in rows).most_common():
    print(f"  {event_type}: {count}")
print("agreement counts:")
for field in ("subtype_agreement", "assertion_agreement", "place_id_agreement_nonnull", "province_agreement_nonnull"):
    n = sum(r[field] for r in rows)
    print(f"  {field}: {n}/{len(rows)} = {n/len(rows):.2%}")
