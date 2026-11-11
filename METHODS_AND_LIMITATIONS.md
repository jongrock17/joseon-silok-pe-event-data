# Methods and limitations (documented vs pending)

## Observed structure and confirmed transformations

The input to this repository is a 12,745-row UTF-8 JSONL research export with version key `joseon_place_event_model_consensus_v1` and one fixed rule:

> `same article_id + same event_type + same normalized place`

We verified: **8,268** distinct article identifiers; **833** distinct normalized place-name strings; **20** event categories; no duplicated coarse keys; dated records between **1392 and 1863**; **25** records without usable years. Those statements are based on the file, not on an external corpus inventory.

The released `core.jsonl.gz` file removes verbatim source-evidence blocks, detailed record notes, and aliases, while adding four deterministic, row-level agreement flags. All other retained fields are direct copies of original values. Table CSVs are derived mechanically from those rows.

## Multi-model consensus is not validation

Two outputs with labels `codex` and `claude` must agree on an article identifier, broad event class, and normalized place **string** for a row to appear. The rule can reduce uncorroborated candidates but cannot validate the event, location, classification, source linkage, or true positive rate. Both models can agree on an incorrect extraction, and both can miss the same event. **No full-corpus agreement rate can be inferred** without unmatched outputs and candidate denominators.

Within these retained rows, agreement rates are: subtype **10,534/12,745 (82.65%)**, assertion status **10,360/12,745 (81.29%)**, shared non-null place reference ID **8,653/12,745 (67.89%)**, and shared non-null province label **8,689/12,745 (68.18%)**. These rates are conditional on already being in the coarse-consensus dataset.

**The units can be non-independent:** a single article may generate multiple province/event-type rows, and a `article_id × event_type × place` key might stand for more than one passage or incident. The count should not be labeled "12,745 distinct historical events" without adjudication.

## Event timing and assertion modality

An article may record an official **order** or **proposal**, a later report about an event, or an event that actually happened. The model-generated `assertion_status` fields are not always equal. Event-time offsets (e.g., a past disaster reported months later) may also be relevant. Treat year in `article_metadata` as the **article record's year**, not a verified onset date; calendar conventions and leap months require checking before finer time-series analysis.

## Geographic uncertainty

`place_normalized_name` is a surface/normalized label. It is not necessarily a stable county identifier across centuries. The two streams can assign different historical reference IDs, administrative levels, provinces, or place roles. The file has no trustworthy coordinates or finished spatial crosswalk. The `JHG_...` identifiers cannot be assumed to resolve to modern administrative units without documentation of the reference gazetteer and its historical validity.

## Source and sampling selection

The visible observed years are 1392–1863. Neither the number of articles supplied to the models nor input/article selection criteria can be inferred from the consensus output. The dataset may represent **only a selected portion** of the Annals, despite spanning many reigns. Reporting rates over time requires a source article denominator and potentially correction for changing chroniclers' attention, record survival, and genre conventions.

## Before describing as reproducible or validated

- [ ] Identify exact model/provider versions; inference settings; date(s) of extraction.
- [ ] Publish or document prompts, event-type codebook, and place-reference database version (subject to rights and privacy/contract restrictions).
- [ ] State total number of input articles, full historical coverage, exclusions, preprocessing, and failed/missing model outputs.
- [ ] Preserve both original candidate lists for calculating overall pairwise agreement, selection, and attrition at each filtering stage.
- [ ] Human-audit a stratified sample for event class, event time/status, place, and false-positive rates; ideally estimate precision with intervals.
- [ ] Validate historical to modern administrative crosswalk and exact place references.
- [ ] Document original edition and redistribution terms for quotations and database metadata.
- [ ] Add versioned release notes and author information.
