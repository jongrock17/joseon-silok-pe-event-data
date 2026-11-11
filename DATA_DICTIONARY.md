# Data dictionary — v0.1

**File:** `data/consensus_place_event_pairs_core.jsonl.gz`. Each newline-delimited object represents one coarse-consensus `article_id × event_type × place_normalized_name` key. `12,745` records. The public core file is derived from the supplied research export and omits source quotes, model decision notes, and other detailed raw-record fields.

| Field | Type | Interpretation |
|---|---|---|
| `schema_version` | string | Original coding schema identifier (`joseon_place_event_model_consensus_v1`). |
| `agreement_rule` | string | Literal consensus key: article ID + major event type + normalized place name. |
| `article_id` | string | Identifier of an article or passage in the upstream research corpus. |
| `article_metadata` | object | Chronological / reign metadata; see nested fields below. |
| `event_type` | string | Major event category agreed by coarse matching rule. |
| `event_subtype_codex` | string | Codex extraction stream's subtype code. |
| `event_subtype_claude` | string | Claude extraction stream's subtype code. |
| `assertion_status_codex` | string | Codex stream's status code (e.g., `OCCURRED`, `ORDERED`, `REPORTED`). |
| `assertion_status_claude` | string | Claude stream's status code. |
| `place_normalized_name` | string | The normalized place label used as part of the consensus key; this is a string, not necessarily a unique geospatial entity. |
| `place_record_id_codex` | string/null | Codex stream's matched historical reference ID; may be null. |
| `place_record_id_claude` | string/null | Claude stream's matched historical reference ID; may be null. |
| `place_codex` | object | Codex stream's place attributes; see nested fields below. |
| `place_claude` | object | Claude stream's place attributes; see nested fields below. |
| `subtype_agreement` | bool | Both subtype codes exactly match. |
| `assertion_agreement` | bool | Both assertion-status codes exactly match. |
| `place_id_agreement_nonnull` | bool | Both historical place reference IDs match and neither is null. |
| `province_agreement_nonnull` | bool | Both province labels match and neither is null. |

### `article_metadata`

| Subfield | Type | Interpretation |
|---|---|---|
| `king` | string/null | Reign label for the article. |
| `reign_year` | integer/null | Reported reign year; may be missing. |
| `year` | integer/null | Reported article year (not necessarily event occurrence year). |
| `month`, `day` | integer/null | Reported date fields; calendar conversion not verified. |
| `title` | string/null | Article title; missing for 12,722 of 12,745 records. |

### `place_codex` and `place_claude`

| Subfield | Type | Interpretation |
|---|---|---|
| `normalized_name` | string/null | Model-specific normalized place label. |
| `admin_level` | string/null | Source-coded historical administrative hierarchy (e.g., `lv2`); mapping documentation needs verification. |
| `province_group` | string/null | Source-coded provincial grouping (historical, not yet modern GIS). |
| `local_group` | string/null | Source-coded local grouping. |
| `valid_from_year`, `valid_to_year` | integer/null | Claimed temporal validity of the historical place reference; not independent validation. |
| `place_role` | string/null | Relation of place to reported event (e.g., `EVENT_LOCATION`, `DESTINATION`, `ADMIN_JURISDICTION`). |
| `reference_match_status` | string/null | Whether stream could match its place to a reference (`MATCHED`, `NOT_IN_REFERENCE`, `AMBIGUOUS`). |

### Fields retained only in the original full research export

- `evidence_codex`, `evidence_claude`: source quotation spans for evidence, location, event, and relation.
- `record_codex`, `record_claude`: nested model records, decision notes, uncertainty flags, and alternative interpretations.
- `place_codex.mention` / `place_claude.mention`: exact model-extracted place mentions and aliases.
- `place_codex.alternative_place_ids` / `place_claude.alternative_place_ids`: alternative reference IDs.

**Why omitted from the public core?** These fields include source-text excerpts or can be redundant. They should remain in the private audit/provenance copy until redistribution rights and use cases are reviewed. The core is not a lossless archive of the original file.

### Suggested analytical conventions

- Maintain both subtype and assertion fields if no adjudication has been carried out.
- Use `place_id_agreement_nonnull` rather than comparing the two place IDs with an unqualified equality operator; `null == null` is not evidence of a successful geocoding match.
- When aggregating events to years, report that values are record counts, not directly observed real-world event rates.
- When aggregating over province labels, describe whether you used the Codex label, Claude label, or their non-null intersection; do not silently fill missing province values.
