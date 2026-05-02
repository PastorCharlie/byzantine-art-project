# Claude Code Kickoff — Byzantine Art Project

## Read first
Read `BRIEF.md` in this directory. The full project specification is there.
You are working on Phase B (content load) — researching artworks, sourcing 
images, writing theological reflections.

## Your first task: 5 artworks from Collection 1 (Pantocrator)

Do NOT attempt to build all 150 artworks at once. Your first task is exactly
5 artworks so Pastor Charlie can review the quality before you scale up.

Build entries for these 5 artworks from Collection 1 (Christ Pantocrator):

1. Pantocrator, Hagia Sophia (deesis mosaic) — Constantinople, c. 1261
2. Pantocrator, Saint Catherine's Monastery — Sinai, 6th century
3. Pantocrator, Cefalù Cathedral — Sicily, 1130-1240
4. Pantocrator, Daphni Monastery — Greece, 11th century
5. Pantocrator, Hosios Loukas — Greece, 11th century

## For each artwork, produce:

### A JSON file at `data/artworks/[slug].json`
Match the schema in BRIEF.md §10. Include all required fields. The reflection
field should be the full theological reflection (markdown).

### A research note at `research/[slug]-research.md`
Document your research: what sources you consulted, where the image came from,
what the licensing is, key historical/theological references. This makes the
work reviewable and citable.

### A downloaded image at `images/full/[slug].jpg` or `.png`
Public domain or CC-licensed only. Wikimedia Commons preferred. DO NOT use 
stock images, AI-generated images, or hot-link external URLs.

## Voice and theology requirements

Read BRIEF.md §2 (Theological Framing) and §5.2 (Sample Reflection) carefully.
The reflection in §5.2 is the tone calibration target. Match that voice:
- Direct, declarative
- Scripture-saturated  
- Pastoral application at the end
- 200-400 words (target 300)
- Post-tribulation eschatology where relevant
- "Be Obedient. Be Bold." sign-off used selectively

GLM is post-trib. Do not write reflections that imply pre-trib rapture or
dispensational framings.

## Before writing reflections

Verify scripture references. If you cite Revelation 1:13-16, make sure the
verses actually say what you claim. Pastor Charlie will catch errors.

## When you finish the 5

Stop. Write a summary at `notes/batch-001-summary.md` covering:
- What you produced
- Image sources used (with licensing)
- Any artworks where you struggled to find good images
- Any theological calls you'd like Pastor Charlie to review
- Estimated time per artwork (so we can plan the remaining 145)

Do not proceed to artwork 6 until Pastor Charlie has reviewed the first batch.

## Working environment notes

You're on Pastor-Ubuntu-Claude (Ubuntu, Python 3.14, requests library available).
Project root: ~/byzantine-art-project/
The terminal is Ptyxis — file paths display with link styling but underlying 
text is clean. Trust the actual file contents, not the visual rendering.

## Be honest about uncertainty

If you can't find a properly licensed high-resolution image of a specific 
artwork, say so. Don't substitute with something close. Pastor Charlie would 
rather have 4 well-sourced artworks than 5 with a fabricated one.
