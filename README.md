# Byzantine Art Project

A 150-entry doctrinal corpus on Eastern Christian iconography, prepared as the source data and architecture for the **Discipleship Universe Scriptorium** — `discipleshipuniverse.com/scriptorium/byzantine-art`.

Authored by **Gospel Life Ministries**.

## What this repo contains

This is a content-and-architecture repo, not an application. The Scriptorium build (the rendered website) is a separate downstream project that consumes the data here.

```
data/artworks/     150 JSON entries — one per artwork
notes/             voice-templates.md — the doctrinal/architectural rulebook
research/          60 source-research files that fed the corpus
scripts/           audit_corpus.py, download_image.py — corpus infrastructure
public/images/     web-ready images (1600w) + thumbnails (400w), 150 each
BRIEF.md           build brief for the Scriptorium page
KICKOFF.md         project kickoff document
```

Each `data/artworks/*.json` carries: slug, title, location (with lat/lng), date range, medium, era, collection assignments, image references, an extended doctrinal **reflection**, scripture references, and tags.

## The 150 entries

The corpus covers Eastern Christian iconography from the 3rd-century catacombs through the 16th-century Cretan school, organized across ten doctrinal collections (eschatology, sacraments, anastasis, apostles, pneumatology, OT typology, saints, Christology, ecclesiology, iconoclasm). Each entry reads the iconography for the doctrinal argument it makes and weighs that argument against the apostolic text.

## The 17 numbered flagships

Seventeen entries are designated **flagship articulations** of GLM doctrinal positions — the entries where a confessional commitment first surfaced from a specific case-type and where the corpus's standing reading was locked. The flagship architecture is enumerated in `notes/voice-templates.md` (see the **Doctrinal-Position Emergence Map** and the **Cross-flagship anchor locks** sections). Future entries that touch the same doctrinal territory pattern-match to the flagship; the corpus does not improvise outside the flagship architecture without explicit review.

## The 5 architectural standing rules

Five rules govern the corpus as a whole — they hold across every entry and every collection:

1. **Anastasis-iconography standing rule** — Second-Adam Christology anchored at 1 Cor 15:22; harrowing-of-hades exegesis referenced but not adjudicated.
2. **Polemical register-restraint** — read the doctrinal argument the iconography carries; decline to amplify polemical vitriol against named historical opponents.
3. **Fresh-medium tracking** — when a medium appears for the first time, open it explicitly in the state log.
4. **Region-vs-site bucketing** — the 4-entry-per-site ceiling protects site-program coherence; regional density is properly variable.
5. **Audit-script standing rule** — corpus integrity is verified by `scripts/audit_corpus.py`, not by manual inspection.

Full statements of each rule are in `notes/voice-templates.md`. Additional collection-specific and locked-pattern rules live alongside them.

## Image licensing

Each entry's `image_attribution` field carries the source, photographer (where applicable), and license terms — predominantly CC BY-SA, CC BY, CC0, or public domain. Underlying iconography is uniformly in the public domain; the licensing applies to specific photographic reproductions. Re-users are responsible for honoring the per-image attribution as recorded in the JSON.

## Repository license

This repository is unlicensed at present. Content is © Gospel Life Ministries. Reach out before redistributing the corpus text.

---

*Be Obedient. Be Bold.*
