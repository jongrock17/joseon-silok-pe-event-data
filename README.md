# Joseon Annals Event–Place Dataset (Two-Model Consensus, v0.1)

**A preliminary machine-coded, article–event–place dataset from the *Veritable Records of the Joseon Dynasty* (조선왕조실록).** This repository provides a first-pass set of records matched across two LLM-based extraction outputs labeled **Codex** and **Claude**. The dataset is intended for exploratory historical political economy research, **not** as a fully validated census of historical events.

> **Release status:** v0.1 / preliminary research dataset. Human validation, coverage auditing, geocoding assessment, and reproduction documentation are pending.

## At a glance

| Measure | v0.1 |
|---|---:|
| Consensus article–event type–place records | **12,745** |
| Distinct source articles represented | **8,268** |
| Distinct normalized place-name strings | **833** |
| Event categories (major types) | **20** |
| Earliest/latest known record year | **1392–1863** |
| Distinct years with at least one dated record | **468** |
| Records missing a usable year | **25** |
| Record-key duplicates | **0** |

**Unit of observation:** one distinct `article_id × event_type × place_normalized_name` tuple. Multiple rows can refer to a single article or event. Counts below represent coded *event–place mentions*, not necessarily distinct real-world incidents or observed incidence rates.

The data cover dated consensus records from 1392 through 1863 (Taejo–Cheoljong). **This is the observed coverage of the supplied file, not an independently verified statement that all eligible source articles were successfully processed.** Neither Gojong nor Sunjong is represented in this release.

## Where to start

```text
.
├── README.md
├── DATA_DICTIONARY.md
├── METHODS_AND_LIMITATIONS.md
├── RIGHTS_AND_ATTRIBUTION.md
├── CV_ENTRY.md
├── data/
│   └── consensus_place_event_pairs_core.jsonl.gz
├── tables/
│   ├── event_types.csv
│   ├── event_subtypes_codex.csv
│   ├── event_subtypes_claude.csv
│   ├── centuries.csv
│   ├── reigns.csv
│   ├── province_joint_agreement.csv
│   ├── province_model_labels.csv
│   ├── annual_event_type_counts.csv
│   └── annual_joint_province_event_counts.csv
└── scripts/
    └── check_data.py
```

The **public-facing core file** retains event codes, article metadata, both models' place labels and geocoding status, and agreement flags. It **does not redistribute the longer verbatim source-text evidence** contained in the original research export. The core file is intentionally distinct from the original full-provenance JSONL (which is approximately 83.6 MiB uncompressed).

## Source and extraction approach

The underlying source is the *Veritable Records of the Joseon Dynasty* (朝鮮王朝實錄; 조선왕조실록), a collection of court chronicles. See the National Institute of Korean History's public reference: https://sillok.history.go.kr/ and its English overview: https://sillok.history.go.kr/intro/english.do . Individual records in this dataset are identified with `article_id` strings such as `ITKC_JT_A0_A01_12A_24A_00010`. **The precise article-ID mapping to public URLs and the exact upstream text edition should be documented by the data creator before release.**

Two coded outputs were matched according to the following key **as recorded in the source file**:

```text
same article_id + same event_type + same normalized place
```

That is a **coarse consensus key**. It does *not* require agreement on `event_subtype`, `assertion_status`, geographic reference ID, place role, or evidence span. Those model-specific labels are retained separately rather than silently reconciled.

The original file identifies the two extraction streams as `codex` and `claude`; the exact underlying model versions, prompting configuration, sampling parameters, and preprocessing steps cannot be recovered from this file alone and should be added to the methodology documentation by the dataset author.

## Event category distribution

| Event type | Description | Records | Share |
|---|---|---|---|
| NATURAL_ENVIRONMENT_EVENT | Natural environment | 6,516 | 51.13% |
| CRIME_JUSTICE_EVENT | Crime and justice | 1,567 | 12.30% |
| RELIEF_WELFARE_EVENT | Relief and welfare | 850 | 6.67% |
| MILITARY_DEFENSE_EVENT | Military and defense | 731 | 5.74% |
| AGRICULTURE_SUBSISTENCE_EVENT | Agriculture and subsistence | 716 | 5.62% |
| PUBLIC_HEALTH_MEDICINE_EVENT | Public health and medicine | 617 | 4.84% |
| FISCAL_TAXATION_EVENT | Fiscal policy and taxation | 341 | 2.68% |
| GOVERNANCE_ADMINISTRATION_EVENT | Governance and administration | 276 | 2.17% |
| DIPLOMACY_FOREIGN_RELATIONS_EVENT | Diplomacy and foreign relations | 249 | 1.95% |
| PERSONNEL_BUREAUCRACY_EVENT | Personnel and bureaucracy | 214 | 1.68% |
| COLLECTIVE_ACTION_SECURITY_EVENT | Collective action and security | 202 | 1.58% |
| LAND_POPULATION_REGISTRATION_EVENT | Land and population registration | 120 | 0.94% |
| RITUAL_ROYAL_COURT_EVENT | Ritual and royal court | 109 | 0.86% |
| CONSTRUCTION_SETTLEMENT_EVENT | Construction and settlement | 76 | 0.60% |
| COMMERCE_INDUSTRY_EVENT | Commerce and industry | 76 | 0.60% |
| TRANSPORT_INFRASTRUCTURE_EVENT | Transport and infrastructure | 56 | 0.44% |
| RELIGION_IDEOLOGY_EDUCATION_EVENT | Religion, ideology and education | 22 | 0.17% |
| SOCIAL_STATUS_FAMILY_EVENT | Social status and family | 3 | 0.02% |
| OTHER_EVENT | Other | 3 | 0.02% |
| CULTURE_KNOWLEDGE_PUBLICATION_EVENT | Culture, knowledge and publication | 1 | 0.01% |


## Distribution by century

Centuries follow the conventional **1–100, 101–200, ...** calendar convention; the 14th-century group covers the available years 1392–1400.

| Period | Records | Share |
|---|---|---|
| 14th century | 120 | 0.94% |
| 15th century | 2,173 | 17.05% |
| 16th century | 4,390 | 34.44% |
| 17th century | 3,054 | 23.96% |
| 18th century | 2,226 | 17.47% |
| 19th century | 757 | 5.94% |
| Year unavailable | 25 | 0.20% |


## Conditional model-label consistency

These diagnostics are computed **only among the 12,745 already-retained consensus rows**; they are *not* estimates of full-corpus inter-model agreement, precision, or recall.

| Within-consensus diagnostic | Records | Share |
|---|---:|---:|
| Same event subtype | 10,534 | 82.65% |
| Same assertion status (e.g., occurred / ordered / reported) | 10,360 | 81.29% |
| Same non-null historical place reference ID | 8,653 | 67.89% |
| Same non-null province label | 8,689 | 68.18% |
| Same subtype **and** assertion status | 8,693 | 68.21% |

A record can be in the coarse matched dataset while the models disagree on whether the passage describes an event as **ordered** versus **occurred**. Treating every row as an actual, completed government intervention would therefore be inappropriate.

### Geographic assignment (shared, non-null province labels only)

| Shared historical province label | Records | Share of all rows |
|---|---|---|
| (no shared nonmissing label) | 4,056 | 31.82% |
| 전라 | 1,448 | 11.36% |
| 평안 | 1,328 | 10.42% |
| 경기 | 1,191 | 9.34% |
| 경상 | 1,187 | 9.31% |
| 충청 | 1,040 | 8.16% |
| 함경 | 1,001 | 7.85% |
| 황해 | 774 | 6.07% |
| 강원 | 676 | 5.30% |
| 경도 | 32 | 0.25% |
| 개성 | 12 | 0.09% |


`(no shared nonmissing label)` includes null and conflicting provincial assignments. The place names and historical administrative classifications have **not** been harmonized to a modern GIS boundary layer. Province frequencies are not shares of true event incidence.

## Reading the dataset

```python
import gzip
import json
from collections import Counter

path = "data/consensus_place_event_pairs_core.jsonl.gz"
with gzip.open(path, "rt", encoding="utf-8") as f:
    records = [json.loads(line) for line in f]

print(len(records))  # 12,745
print(Counter(row["event_type"] for row in records).most_common(5))

# Optional, more restrictive analytical subset; NOT an accuracy guarantee.
stricter = [
    row for row in records
    if row["subtype_agreement"]
    and row["assertion_agreement"]
    and row["place_id_agreement_nonnull"]
]
print(len(stricter))  # 5,819
```

The more restrictive subset has **selection effects**: it may disproportionately retain easier-to-classify events and place names. Use the agreement flags to report robustness rather than assuming that the strict subset is a human-validated gold standard.

## Potential research applications

- Spatial and temporal measurement of recorded natural shocks, epidemics, and subsistence crises.
- Descriptive mapping of relief and fiscal-action mentions, including contrasts with disaster-related mentions.
- Study of historical administrative, military, and personnel events in relation to institutional development.
- Evaluation of disagreement patterns in LLM-based historical-event extraction.

Research using annual or location-level counts should incorporate the number of underlying articles or other source-coverage measures where possible. This release does **not** supply population denominators, unique physical incident identifiers, confirmed action dates, or geocoded coordinates.

## Limitations

1. **Selection and recall are unknown:** only records retained by the specified cross-model matching rule are present; unmatched candidate outputs and the number of all processed input articles are unavailable here.
2. **Not human-validated:** machine agreement reduces certain forms of disagreement but does not establish historical or semantic correctness.
3. **Unresolved ambiguity:** subtype, assertion status, historic place-reference IDs, and administrative geography can disagree.
4. **Time measurement:** the metadata `year` marks a record year; event timing can differ from publication/article timing, and `month`/`day` have not been verified as Gregorian dates.
5. **Multiplicity:** a document may contain multiple event types or locations, and the match key can collapse same-category episodes mentioned in one article and place.
6. **Sources and rights:** the full research export contains quoted evidence text; determine the correct source edition and applicable redistribution conditions before putting it online.

More detail appears in [METHODS_AND_LIMITATIONS.md](METHODS_AND_LIMITATIONS.md).

## Citation

**Suggested preliminary citation (edit author and URL before publication):**

> [Dataset author]. (2026). *Joseon Annals Event–Place Dataset: Two-Model Consensus (Version 0.1)* [Dataset]. GitHub. [Repository URL].

A DOI can be added if a fixed release is deposited in an archival service. This version should not be described as a peer-reviewed publication or validated benchmark.

## Licensing and attribution

See [RIGHTS_AND_ATTRIBUTION.md](RIGHTS_AND_ATTRIBUTION.md). **No third-party source-text license or unrestricted redistribution right is asserted by this repository.** Any final open license should cover only the components the dataset author can lawfully release. Add the author name, source-edition attribution, model versions, prompting details, and appropriate license terms before publication.
