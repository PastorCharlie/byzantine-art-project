# Byzantine Art Page — Cowork Build Brief

**Project:** Discipleship Universe Scriptorium — Byzantine Art Page
**URL:** `discipleshipuniverse.com/scriptorium/byzantine-art`
**Status:** Ready to build
**Author:** Pastor Charlie + Claude
**Date:** April 28, 2026

---

## 1. Executive Summary

The Byzantine Art page is the second box in the DU Scriptorium lineup (alongside the Maps page Cowork is finishing in Phase 2). It is positioned as a **rich theological resource**, not an art-history dump — a place where pastors, teachers, and serious students of scripture can encounter sacred imagery from the most theologically-saturated era of Christian visual art and walk away spiritually fed.

**Launch scope:** 150 carefully curated artworks with full theological reflections, organized across 10 thematic collections, presented through a stunning gallery interface, anchored by an interactive timeline and a global map of where these works survive today.

**Growth path:** Architecture supports expansion to 500+ artworks, with content additions on a weekly cadence post-launch. Returning visitors should always see something new.

**Wow factor goals:**
1. The depth of theological writing (no other public Byzantine art resource does this)
2. The visual presentation (gallery experience, not database)
3. The integration of timeline + map + thematic collections (multiple ways to explore)
4. The growth velocity (page evolves, drawing visitors back)

---

## 2. Theological Framing

This is a GLM-branded resource. Voice and theology must reflect:

- **Direct, bold, scripture-grounded** (Pastor Charlie's signature voice)
- **Post-tribulation eschatological position** where Last Judgment / Second Coming imagery is discussed
- **Pastoral relevance** — every reflection should answer "why does this matter for the believer today?"
- **Reverent but not Orthodox-deferential** — we engage Byzantine theology seriously, but we are not Orthodox; we critique what conflicts with sola scriptura while honoring what teaches us about Christ
- **Sign-off where appropriate:** "Be Obedient. Be Bold."

**Important theological notes for content writers:**
- Iconography is a teaching medium for Byzantine Christians — we treat it as such, not as worship objects
- We engage with the *theological content* of icons (what they teach about Christ, the Trinity, salvation, judgment) rather than veneration practices
- For Theotokos imagery, we focus on Christological implications (her motherhood points to incarnation) rather than Marian devotion
- For Last Judgment imagery, we read post-trib (the rapture occurs at Christ's return on the Great Day of the Lord)
- We do NOT promote icon veneration but we DO recognize Byzantine art as legitimate Christian visual theology

---

## 3. Page Architecture

### 3.1 Top-level structure

```
/scriptorium/byzantine-art
│
├── /                              (Landing page — hero + collection grid)
├── /collection/[slug]             (Thematic collection view)
├── /artwork/[slug]                (Individual artwork detail page)
├── /timeline                      (Interactive timeline view)
├── /map                           (Geographic map view)
├── /search                        (Search & filter interface)
└── /about                         (Methodology, sources, theological framing)
```

### 3.2 Navigation

Persistent header should include:
- DU logo (returns to scriptorium index)
- "Byzantine Art" breadcrumb
- View toggles: **Collections / Timeline / Map / Search**
- Sub-nav for collections (when on a collection page)

### 3.3 Landing page sections

**Section 1 — Hero (above the fold)**
- Full-bleed background: Christ Pantocrator from Hagia Sophia (the deesis mosaic)
- Overlay text: large gold serif title
  - Headline: "Byzantine Art"
  - Subhead: "Eleven centuries of sacred imagery, organized for the pastor's library."
- Primary CTA button: "Begin in the Collections →"
- Secondary text below: "150 artworks · 10 collections · spanning AD 330–1453"
- Background should have subtle dark overlay (40% black) for text legibility
- GLM brand colors throughout: navy `#0d1b2e`, gold `#c9a84c`, light gold `#e8c97a`, parchment `#f5f0e8`

**Section 2 — Introduction (theological frame)**
- 2-3 paragraphs of pastoral introduction
- Key message: "Byzantine artists believed sacred image-making was theology. Every choice — color, gesture, composition — taught doctrine. This page is a guided tour through what they were teaching."
- Sets expectation that this is not Wikipedia

**Section 3 — The 10 Collections (grid of large cards)**
- Each card displays:
  - Hero image (representative artwork from that collection)
  - Collection title (gold serif)
  - One-line description
  - Artwork count ("18 artworks")
- Hover: subtle lift + gold border glow
- Click: navigates to `/collection/[slug]`

**Section 4 — Featured Artwork (rotating weekly)**
- Single artwork, full-width
- Image on left, theological reflection on right
- "Featured this week" tag
- "View full reflection →" CTA

**Section 5 — Three exploration modes**
- "Browse by era →" (Timeline view)
- "Browse by location →" (Map view)
- "Search the archive →" (Search view)
- Each as large card with iconography

**Section 6 — Footer**
- About / Methodology link
- "Maintained by Pastor Charlie Aycock at Gospel Life Ministries"
- "Be Obedient. Be Bold."

---

## 4. The Ten Collections (Content Architecture)

Each collection should have between 12-20 artworks at launch. Total = ~150.

### Collection 1 — Christ Pantocrator (15 artworks)
**The Almighty Christ — Judge, King, and Lord**

Theological frame: Pantocrator (Greek for "All-Powerful") imagery teaches Christ's divine sovereignty. He is depicted with right hand raised in blessing/judgment, left hand holding scripture. This is Christ as he appears in Revelation 1:13-16 — not the suffering servant but the returning King. Critical for end-times teaching.

Selected artworks (initial 15):
1. **Pantocrator, Hagia Sophia (deesis mosaic)** — Constantinople, c. 1261
2. **Pantocrator, Saint Catherine's Monastery** — Sinai, 6th century (oldest surviving)
3. **Pantocrator, Cefalù Cathedral** — Sicily, 1130-1240
4. **Pantocrator, Daphni Monastery** — Greece, 11th century
5. **Pantocrator, Monreale Cathedral** — Sicily, 1180s
6. **Pantocrator, Pammakaristos Church** — Constantinople, 14th century
7. **Pantocrator, Hosios Loukas** — Greece, 11th century
8. **Pantocrator, Capella Palatina** — Palermo, 1140s
9. **Pantocrator, Chora Church (Kariye)** — Constantinople, 14th century
10. **Pantocrator, Mistra (Pantanassa)** — Greece, 15th century
11. **Pantocrator, Panagia tou Arakos** — Cyprus, 1192
12. **Pantocrator, Nea Moni** — Chios, 11th century
13. **Pantocrator, Sant'Apollinare Nuovo** — Ravenna, 6th century
14. **Pantocrator from the Sinai apse** — Sinai, 6th-7th century
15. **Pantocrator, Boyana Church** — Bulgaria, 13th century

### Collection 2 — Theotokos & Incarnation (15 artworks)
**The Mother of God — Christological Implications**

Theological frame: Theotokos ("God-bearer") imagery teaches the doctrine of the incarnation. The image is not about Mary's exaltation — it is about Christ's full humanity AND full divinity meeting in her womb. Every Theotokos icon is a sermon on John 1:14 ("the Word became flesh").

Selected artworks (initial 15):
1. **Theotokos of Vladimir** — Constantinople, 12th century
2. **Virgin and Child, Saint Catherine's** — Sinai, 6th century (encaustic)
3. **Theotokos Hodegetria, original tradition** — multiple surviving copies
4. **Virgin Eleousa, various** — Tenderness icon tradition
5. **Apse mosaic, Hagia Sophia** — Constantinople, 867
6. **Annunciation, Saint Catherine's** — Sinai, 12th century
7. **Theotokos, Hosios Loukas apse** — Greece, 11th century
8. **Virgin Orans, Saint Sophia Kyiv** — Ukraine, 11th century
9. **Theotokos, Daphni** — Greece, 11th century
10. **Virgin Blachernitissa tradition**
11. **Theotokos Glykophilousa, various**
12. **Annunciation, Chora Church** — Constantinople, 14th century
13. **Nativity, Saint Catherine's** — multiple
14. **Virgin and Child enthroned, Sant'Apollinare Nuovo** — Ravenna, 6th century
15. **Theotokos Platytera, various traditions**

### Collection 3 — The Last Judgment & Second Coming (18 artworks)
**The Day of the Lord — End-Times Imagery**

Theological frame: This is the GLM-distinctive collection. Byzantine Last Judgment frescoes are among the most theologically rich surviving artworks and align directly with post-trib eschatology. The imagery shows Christ returning, the dead rising, the books opening, the separation of sheep from goats. This is not allegory to Byzantine artists — this is what is coming.

Selected artworks (initial 18):
1. **Last Judgment, Torcello Cathedral** — Italy, 12th century (one of the most complete surviving)
2. **Last Judgment, Voronet Monastery** — Romania, 16th century (post-Byz tradition, included with note)
3. **Last Judgment, Chora Church (Kariye)** — Constantinople, 14th century
4. **Last Judgment, Mistra (Brontochion)** — Greece, 14th century
5. **Last Judgment, Saint Sophia of Ohrid** — North Macedonia, 11th century
6. **Last Judgment, Cefalù Cathedral details** — Sicily, 12th century
7. **Last Judgment, Sopocani Monastery** — Serbia, 13th century
8. **Anastasis (Resurrection/Harrowing of Hades), Chora Church** — Constantinople, 14th century
9. **Anastasis, Hosios Loukas** — Greece, 11th century
10. **Anastasis, Saint Catherine's Sinai**
11. **Christ in Majesty, Cathedral of Cefalù** — Sicily, 12th century
12. **Apocalypse cycle, Patmos Monastery manuscripts**
13. **The Weighing of Souls, various** — psychostasia tradition
14. **The Heavenly Jerusalem, Sant'Apollinare in Classe** — Ravenna, 6th century
15. **The Four Living Creatures (Revelation 4), various**
16. **The 24 Elders, various apse mosaics**
17. **Christ enthroned with archangels, San Vitale** — Ravenna, 547 *(corrected from "Sant'Apollinare in Classe" — Classe's apse has a Cosmic Cross / Transfiguration program; San Vitale's apse has the Christ-on-globe-throne with archangels Michael and Gabriel composition)*
18. **Last Judgment, Studenica Monastery (King's Church narthex)** — Serbia, 1569 *(corrected from "13th century" — the Last Judgment in the King's Church narthex is post-Byzantine, painted in 1569; the 13th-c. Studenica frescoes are the famous Crucifixion of 1209 and others, which belong in Collection 5)*

### Collection 4 — The Apostles & Evangelists (12 artworks)
**The Foundation Witnesses — Those Sent**

Theological frame: Apostle imagery teaches apostolic authority and the foundation of the church on their witness (Ephesians 2:20). Byzantine artists portrayed each apostle with consistent attributes — Peter with keys, Paul as bald scholar, John as youthful theologian, Matthew with a book. This visual language helped illiterate Christians know their Bible.

Selected artworks (12 initial):
1. **The Twelve Apostles, Hosios Loukas** — Greece, 11th century
2. **Communion of the Apostles, Cefalù Cathedral**
3. **Apostles in the dome, Daphni** — Greece
4. **Saint Paul, Hagia Sophia narthex**
5. **Saint Peter, Sant'Apollinare Nuovo** — Ravenna
6. **Saint John the Theologian, various**
7. **Saint Matthew Evangelist portrait, various Gospel manuscripts**
8. **Saint Mark, Rabbula Gospels** — Syria, 586
9. **Apostles' communion mosaic, Saint Sophia Kyiv**
10. **Saint Andrew, various**
11. **Pentecost icon, Saint Catherine's**
12. **The Mission of the Apostles, Saint Mark's Venice**

### Collection 5 — The Life of Christ (20 artworks)
**Gospel Cycles in Visual Form**

Theological frame: Byzantine churches were decorated with cycles of Christ's life — from Annunciation through Ascension. These were teaching tools for catechumens and reminders for the faithful. We organize them in gospel chronology.

Selected artworks (20 initial):
1. **Annunciation, Chora Church**
2. **Nativity, Daphni**
3. **Adoration of the Magi, various**
4. **Presentation of the Theotokos in the Temple, Daphni** *(disambiguated — Daphni's mosaic depicts Mary's presentation as a child, drawn from the Protoevangelium of James, NOT Christ's Presentation per Luke 2:22–38. Note: this places the artwork primarily in Coll 2 / Theotokos rather than Coll 5; covered as `presentation-theotokos-daphni` in the corpus)*
5. **Baptism of Christ, Daphni** (note: trinitarian implications)
6. **Transfiguration, Saint Catherine's apse mosaic** — Sinai, 6th century
7. **Raising of Lazarus, Chora Church**
8. **Entry into Jerusalem, Daphni**
9. **Last Supper / Mystic Supper, various**
10. **Washing of the Feet, Hosios Loukas**
11. **Betrayal of Judas, Saint Mark's Venice**
12. **Christ before Pilate, various**
13. **Crucifixion, Daphni** (one of the great compositions)
14. **Crucifixion, Saint Catherine's** — Sinai
15. **Deposition / Lamentation, Nerezi Church** — North Macedonia, 12th century
16. **Anastasis (Harrowing of Hades), Chora Church**
17. **Doubting Thomas, Hosios Loukas**
18. **Ascension, Saint Sophia of Ohrid**
19. **Pentecost, Hosios Loukas**
20. **Christ blessing children, various**

### Collection 6 — Old Testament Typology (12 artworks)
**Reading the OT as the Byzantines Did — Christ Concealed**

Theological frame: Byzantine artists saw the Old Testament as full of types and shadows pointing to Christ. The three angels at Mamre were the Trinity. Jacob's ladder was Christ. Moses's burning bush was the Theotokos. This collection teaches typological reading — controversial in some Protestant circles but historically central to Christian interpretation.

Selected artworks (12 initial):
1. **Hospitality of Abraham (Three Angels at Mamre), Saint Mark's Venice** — Trinitarian typology
2. **Hospitality of Abraham, Andrei Rublev** — (post-Byzantine Russian, c. 1425–1427 — included with framing) *(corrected from "1411" — current scholarly consensus based on dendrochronology and restoration analysis dates the icon to 1425–1427, second decade of the 15th c.)*
3. **Moses Receiving the Law, Saint Catherine's**
4. **Moses and the Burning Bush, Saint Catherine's**
5. **Jacob's Ladder, various**
6. **Sacrifice of Isaac, San Vitale Ravenna** — sacrificial typology
7. **The Three Hebrews in the Furnace, various** — Christ-as-fourth-figure
8. **Jonah and the Whale, various** — resurrection typology
9. **King David, Paris Psalter** — Constantinople, 10th century
10. **Daniel in the Lions' Den, various**
11. **The Prophet Elijah, Saint Catherine's**
12. **Ezekiel's Vision (Wheels), various manuscript illustrations**

### Collection 7 — Saints, Martyrs & the Cloud of Witnesses (15 artworks)
**The Faithful Departed — Hebrews 12:1**

Theological frame: We engage with saints as biblical examples of faith, not as objects of veneration. Byzantine saint imagery teaches discipleship — what does it look like to follow Christ to the end? This is Hebrews 12:1's "great cloud of witnesses" made visible.

Selected artworks (15 initial):
1. **Saint Demetrios, Thessaloniki**
2. **Saint George, various warrior saint icons**
3. **Saint Theodore, various**
4. **Saint Catherine of Alexandria — icon and relic context, Saint Catherine's Monastery, Sinai** *(disambiguated: the monastery houses Catherine's relics and a distributed corpus of Catherine icons across centuries; entry should select a specific identifiable icon — the most-cited candidate is the late-Byzantine portrait icon of Saint Catherine in the monastery's icon collection. Identify specific icon at content-load time)*
5. **Saint Stephen Protomartyr, various**
6. **Saints Sergius and Bacchus, encaustic icon** — 6th-7th century
7. **Saint Nicholas, various**
8. **Saint Basil the Great, various**
9. **Saint John Chrysostom, various**
10. **Saint Gregory the Theologian, various**
11. **The Forty Martyrs of Sebaste, various**
12. **Saint Christopher (controversial dog-headed depictions)**
13. **Saint Anthony of the Desert**
14. **Saint Mary of Egypt**
15. **Saint Thecla, various**
16. **The Apostolic Flock, Sant'Apollinare in Classe** — c. 549, triumphal arch and apse base *(added post-batch-008: 12 sheep emerging from Bethlehem and Jerusalem on the triumphal arch + 12 sheep around Saint Apollinaris in the apse base. The flock-of-Christ ecclesiology — the apostolic body gathered from both covenants into one church. Theological subject: the apostolic body as the gathered church across covenant boundaries, with Apollinaris as the local successor leading the regional flock)*

### Collection 8 — Angels & the Heavenly Host (10 artworks)
**Ministering Spirits**

Theological frame: Angel imagery teaches the reality of the unseen realm. Byzantine artists distinguished the orders (cherubim, seraphim, archangels, principalities). For pastors teaching spiritual warfare and the believer's authority, this collection provides visual context for the heavenly hierarchy.

Selected artworks (10 initial):
1. **Archangel Michael, Hagia Sophia (Deesis figure)**
2. **Archangel Gabriel, Annunciation contexts** — multiple
3. **Six-winged Seraphim, Hosios Loukas**
4. **Cherubim, various dome compositions**
5. **Angel of the Annunciation, Saint Catherine's**
6. **Archangel Michael icon, Saint Mark's Venice**
7. **Angels surrounding the throne, Sant'Apollinare in Classe**
8. **Heavenly liturgy, various**
9. **Three Angels of Mamre, Saint Mark's Venice** (also in OT Typology — different reading here)
10. **Archangel weighing souls, psychostasia tradition**

### Collection 9 — Liturgical & Sacramental Imagery (10 artworks)
**The Visible Worship**

Theological frame: Byzantine art depicted worship itself — the heavenly liturgy, communion, baptism. We engage these to understand how Byzantine Christians thought about the sacraments while critiquing where their understanding diverged from biblical practice.

Selected artworks (10 initial):
1. **Communion of the Apostles, Cefalù** (also in Apostles collection)
2. **Heavenly Liturgy, Cozia Monastery** — Romania
3. **Baptism scenes, Arian Baptistery Ravenna**
4. **Baptism scenes, Orthodox Baptistery Ravenna**
5. **Empress Theodora and her court, San Vitale Ravenna**
6. **Emperor Justinian and his court, San Vitale Ravenna**
7. **The Lamb on the Throne, Santi Cosma e Damiano, Rome** — c. 526–530 *(substitution: original BRIEF entry "Christ as the Lamb, Sant'Apollinare in Classe" was iconographically inaccurate — Christ at Classe is depicted as the cosmic cross, not as a Lamb. Santi Cosma e Damiano's triumphal-arch Lamb is the cleanest available Lamb-of-God iconography: depicted in the explicit Apocalyptic context of Revelation 4–5 — the Lamb on the throne, surrounded by the seven candlesticks and the four living creatures. Pairs naturally with corpus's post-trib emphasis. Fallback: Saint Mark's Venice ceiling Lamb)*
8. **Eucharistic vessels in mosaic, various**
9. **Coronation of Roger II, Martorana Palermo**
10. **Deisis composition, multiple** (Christ flanked by John the Baptist and Mary — judgment intercession)

### Collection 10 — Iconoclasm & the Iconography Debate (10 artworks)
**The Century of Erasure (730–843)**

Theological frame: This is a uniquely interesting collection — we examine Byzantine art *through* the lens of the iconoclastic controversy. Why did Byzantines destroy their own art for over a century? What were the theological arguments? What survived? This collection helps Protestant readers understand a complex chapter and reflect on the second commandment.

Selected artworks (10 initial):
1. **Pre-iconoclasm icons at Saint Catherine's** (saved by isolation) *(specificity note: Coll 10 #1 and #6 both reference Sinai pre-iconoclasm survivors. #1 should name a specific representative work — most likely the 6th-c. Christ Pantocrator (already covered as corpus #2) or the Virgin Enthroned with Saints Theodore and George (corpus #24) — used in this collection's frame as the iconic case of survival-by-isolation, with #6 covering the broader corpus)*
2. **Iconoclastic cross at Hagia Eirene** — Constantinople, 8th century
3. **Restoration of icons, Triumph of Orthodoxy icon** — 14th century commemoration
4. **Empress Theodora restoring icons, manuscript illuminations**
5. **Khludov Psalter iconoclastic illuminations** — 9th century, post-iconoclasm
6. **Surviving 6th century encaustic icons, Saint Catherine's** (set of 3-4)
7. **Iconoclast period coin imagery, Constantine V**
8. **Pre-iconoclasm mosaic fragments, various excavated sites**
9. **Council of Nicaea II depiction (787 council that ended first iconoclasm)**
10. **The Triumph of Orthodoxy icon (843 restoration)**

### Collection Total: 137 artworks across 10 collections

Plus 13 reserved as "miscellaneous standout works" not fitting cleanly into one collection but too important to omit (the Rabbula Gospels Crucifixion miniature, the Vienna Genesis manuscript, the Joshua Roll, etc.) — for a total of **150 at launch**.

---

## 5. Individual Artwork Page Schema

Each artwork gets its own page at `/scriptorium/byzantine-art/artwork/[slug]`.

### 5.1 Page structure

**Above the fold:**
- Full-width image (high resolution, lazy-loaded)
- Image controls: zoom, fullscreen, download (where licensing allows)
- Image attribution & licensing line at bottom

**Metadata block (sidebar or below image):**
- **Title** (e.g., "Christ Pantocrator")
- **Date** (e.g., "c. 1261")
- **Location** (e.g., "Hagia Sophia, Istanbul, Turkey")
- **Medium** (e.g., "Mosaic")
- **Era** (Early / Middle / Late Byzantine / Post-Byzantine)
- **Period** (e.g., "Palaeologan Renaissance")
- **Collection(s)** (clickable tags — an artwork can belong to multiple)

**Theological reflection (the centerpiece):**
- 200-400 words
- Pastor Charlie's voice
- Structure suggestion (not rigid):
  1. **What you're seeing** — visual description, 2-3 sentences
  2. **What they meant** — Byzantine theological intent, 3-5 sentences
  3. **What scripture says** — relevant biblical passages with brief exposition, 3-5 sentences
  4. **Why this matters** — pastoral application for today, 2-4 sentences
- Scripture references should be clickable (open verse in modal or external Bible link)

**Related artworks:**
- 4-6 thumbnail cards of artworks in the same collection or with similar theological themes
- Auto-generated based on tags

**Footer:**
- "Be Obedient. Be Bold."
- Share buttons (Facebook, X, LinkedIn — repurpose your existing share component)

### 5.2 Sample reflection (for tone calibration)

**Artwork:** Christ Pantocrator, Hagia Sophia (Deesis mosaic), c. 1261

> Look at his face.
>
> The right side is calm — almost serene. The left side is severe. Byzantine artists did this on purpose. They split his expression because they wanted you to grasp something the modern church has forgotten: the same Christ who blesses also judges, and you cannot pry those two apart.
>
> This mosaic was created after the Latin Crusaders had sacked Constantinople and held it for 57 years. When the Byzantines returned, they put this image of Christ above the doors of their greatest cathedral. The message was clear: *the King is back, and he is the same King he always was.* Almighty. Sovereign. Patient with his people but not soft.
>
> Revelation 1:13–16 describes the risen Christ this way: "His head and his hairs were white like wool... and out of his mouth went a sharp two-edged sword." John saw the Pantocrator. So did the Byzantines. They tried to capture what John saw — not a tame Jesus, not a friend-of-the-family Jesus, but the Almighty One who walks among the lampstands and who is coming again.
>
> When you preach Christ, preach this Christ too. The King who is returning. The Judge who weighs every word. The Sovereign whose mercy is real but whose justice is also real. A church that only knows the soft side of his face is a church that is unprepared for his return.
>
> *Be Obedient. Be Bold.*

### 5.3 Reflection writing standards

- Voice: direct, declarative, scripture-saturated
- Length: 200-400 words (target 300)
- Always end with pastoral application — "what does this mean for the believer / the pastor / the church today?"
- Sign-off "Be Obedient. Be Bold." used selectively (not every reflection — feels diluted if every one)
- AVOID: art-history jargon without explanation, Catholic/Orthodox devotional language, sentimental tone
- INCLUDE: scripture quotes, GLM theological distinctives where relevant, post-trib framing for eschatological pieces

---

## 6. Collection Page Schema

Each collection page lives at `/scriptorium/byzantine-art/collection/[slug]`.

### 6.1 Structure

**Hero:**
- Featured image from the collection
- Collection title (gold serif)
- Collection theological framing (the 2-3 sentence frame from §4 above, expanded to 100-150 words)

**Filter bar:**
- Era filter (All / Early / Middle / Late / Post-Byzantine)
- Location filter (regional groupings)
- Medium filter (Mosaic / Fresco / Icon / Manuscript)
- Sort by (Chronological / Title / Recently added)

**Artwork grid:**
- Responsive grid of artwork cards (3-4 across on desktop, 2 on tablet, 1 on mobile)
- Each card: thumbnail, title, date, location
- Hover: subtle lift + theological theme pull-quote
- Click: artwork detail page

**Bottom:**
- "Continue exploring" — links to 2 related collections
- Footer

---

## 7. Timeline View

URL: `/scriptorium/byzantine-art/timeline`

### 7.1 Structure

**Horizontal scrollable timeline** running from AD 330 (Constantinople founded) to AD 1453 (Constantinople falls).

Major eras visually distinguished:
- **Early Byzantine (330–730)** — gold gradient
- **Iconoclasm (730–843)** — gray (visual "gap" with explanatory note)
- **Middle Byzantine (843–1204)** — gold gradient
- **Latin Occupation (1204–1261)** — gray
- **Late/Palaeologan (1261–1453)** — gold gradient
- **Post-Byzantine (1453+)** — gold fade

Key historical events anchor the timeline:
- 330 — Founding of Constantinople
- 451 — Council of Chalcedon
- 537 — Hagia Sophia consecrated
- 726 — Iconoclasm begins
- 843 — Triumph of Orthodoxy
- 1054 — Great Schism
- 1204 — Sack of Constantinople (Fourth Crusade)
- 1261 — Byzantine restoration
- 1453 — Fall of Constantinople

Artwork dots (clickable) appear on the timeline at their date. Hover shows thumbnail + title. Click navigates to the artwork page.

Filter: by collection (so you can see "all Pantocrator works on the timeline").

---

## 8. Map View

URL: `/scriptorium/byzantine-art/map`

### 8.1 Structure

**Interactive world map** with pins at locations where Byzantine art survives.

Major locations (with approximate artwork counts at launch):
- **Istanbul, Turkey** — Hagia Sophia, Chora, others (~30 artworks)
- **Sinai Peninsula, Egypt** — Saint Catherine's Monastery (~20)
- **Ravenna, Italy** — San Vitale, Sant'Apollinare in Classe, Sant'Apollinare Nuovo (~15)
- **Sicily, Italy** — Cefalù, Monreale, Capella Palatina (~10)
- **Greece (mainland)** — Hosios Loukas, Daphni, Mistra (~15)
- **Cyprus** — various churches (~5)
- **Mount Athos, Greece** — monasteries (~10)
- **Venice, Italy** — Saint Mark's Basilica (~8)
- **Serbia / North Macedonia** — Studenica, Sopocani, Nerezi, Ohrid (~10)
- **Bulgaria** — Boyana Church, others (~5)
- **Russia** — Tretyakov, Hermitage collections (~10)
- **Romania** — Voronet, Cozia, others (~5)
- **Ukraine** — Saint Sophia Kyiv (~5)

Click a pin → see all artworks in that location with thumbnails.

Filter: by era, by collection.

This view is particularly powerful because it teaches geography of surviving Christian heritage — pastors and teachers can show students "this is where the church flourished, this is what survived."

---

## 9. Search & Filter View

URL: `/scriptorium/byzantine-art/search`

Standard search interface:
- Free-text search (artwork title, location, theological theme)
- Multi-select filters: Era, Collection, Location, Medium
- Sort options: Chronological, Alphabetical, Recently Added

Results display as artwork cards.

---

## 10. Data Model

```
Artwork {
  slug: string                    // URL-safe identifier (e.g., "pantocrator-hagia-sophia")
  title: string                   // "Christ Pantocrator"
  subtitle?: string               // "Deesis Mosaic"
  date: string                    // "c. 1261" (display format)
  date_year_start: number         // 1261 (for sorting/filtering)
  date_year_end?: number          // (for ranges)
  location_name: string           // "Hagia Sophia, Istanbul, Turkey"
  location_lat: number            // for map
  location_lng: number
  medium: enum                    // "mosaic" | "fresco" | "icon" | "manuscript" | "ivory" | "metalwork" | "other"
  era: enum                       // "early" | "middle" | "late" | "post-byzantine"
  period?: string                 // "Palaeologan Renaissance"
  collections: string[]           // ["pantocrator", "second-coming"]
  image_url: string               // CDN URL of main image
  image_attribution: string       // "Photo: Wikimedia Commons / CC BY-SA 4.0"
  image_thumbnail_url: string
  reflection: markdown            // The theological reflection
  scripture_refs: string[]        // ["Revelation 1:13-16", "Matthew 28:18"]
  related_artwork_slugs?: string[]  // manual override for related
  tags: string[]                  // free-form tags for search
  featured: boolean               // for "featured this week" rotation
  added_date: ISO date            // for "recently added" sort
  updated_date: ISO date
}

Collection {
  slug: string                    // "pantocrator"
  title: string                   // "Christ Pantocrator"
  subtitle: string                // "The Almighty Christ — Judge, King, and Lord"
  framing: markdown               // The 100-150 word theological frame
  hero_image_url: string
  display_order: number           // 1-10
  artwork_count_target: number    // 15 (for tracking growth)
}
```

Storage: JSON files in repo, structured under `/data/byzantine-art/artworks/[slug].json` and `/data/byzantine-art/collections/[slug].json`. This makes content additions easy via PR / commit.

Alternatively: Sanity CMS if Cowork prefers (Pastor Charlie's existing Sanity stack supports this).

---

## 11. Image Sourcing Strategy

**This is the trickiest part of the build.** Byzantine art images are largely public domain (works are 700-1500 years old) but specific photographs of those works may have copyright held by photographers or institutions.

**Sources, in order of preference:**

1. **Wikimedia Commons** — Most photos of Byzantine art are uploaded under CC licenses. Reliable, attribution required.
2. **Met Museum Open Access** — Institution provides public-domain images of their collection. ~50 Byzantine works available.
3. **Getty Open Content** — Similar to Met. Includes manuscript illuminations.
4. **Library of Congress Public Domain** — Some older photographs.
5. **National Gallery of Art (DC) Open Access** — A few Byzantine pieces.
6. **Dumbarton Oaks** — Major Byzantine collection. Some open access, some restricted.
7. **Vatican Library Digital Collections** — Recently opened many manuscripts.
8. **St. Catherine's Monastery digital archive** — Some images available, others restricted.

**For each artwork, the data entry process is:**
1. Identify the artwork
2. Find a high-quality public-domain or CC-licensed image
3. Record the attribution exactly as required by the license
4. Download to our CDN (don't hotlink — sources can disappear)
5. Generate thumbnail
6. Store attribution in artwork record

**Cowork should NOT use stock image sites or AI-generated images for this page.** Authenticity is part of the wow factor.

---

## 12. Visual Design Direction

### 12.1 Color palette

Use existing GLM brand colors:
- **Navy primary:** `#0d1b2e`
- **Navy deep:** `#071020`
- **Gold primary:** `#c9a84c`
- **Gold light:** `#e8c97a`
- **Parchment:** `#f5f0e8`
- **Navy accent:** `#132240`

### 12.2 Typography

- **Headlines:** Serif (gold) — match existing GLM site headers
- **Body:** Sans-serif (white on navy, navy on parchment) — readability prioritized
- **Reflection text:** Slightly larger than standard body, more line-height — reading experience matters

### 12.3 Image treatment

- Subtle gold border on hover
- Lazy-loaded everywhere
- Click-to-zoom modal for full-resolution viewing
- Soft drop shadow (1-2px)
- Card hover: lift 4px + soft gold glow

### 12.4 Mobile

- Collection grid stacks single-column on mobile
- Timeline becomes vertical scroll on mobile (with collapsed era headers)
- Map fills full screen on mobile, pin tap shows bottom sheet

### 12.5 Loading & performance

- Image CDN with WebP format + JPEG fallback
- Below-fold images lazy-loaded
- Initial page load target: <2 seconds on 4G
- Routes are statically generated where possible (Next.js SSG)

---

## 13. Growth Plan

**Launch (Week 1):**
- 150 artworks live
- All 10 collections populated
- Timeline functional
- Map functional
- Featured artwork rotation set up

**Weeks 2-8 (post-launch growth):**
- Add 15-25 artworks per week (target 30-50 weekly working hours from Pastor Charlie + Claude collaboration)
- Each addition: image sourced, theological reflection written, metadata complete
- Twitter/LinkedIn announcement when collection counts cross thresholds (200, 300, 500)

**By Week 12:**
- 350+ artworks
- Every collection at 25+ artworks
- Search refined based on user behavior
- Possibly: audio reflections (Pastor Charlie reads selected reflections aloud — adds another wow layer)

**By Week 24:**
- 500+ artworks
- Possibly: scholarly contributions invited from approved theologians
- Newsletter signup tied specifically to "weekly Byzantine reflection" — drives DU membership conversions

**Key metric:** Returning visitor rate. We're building this to bring people back. Track time-on-page, pages-per-session, return frequency.

---

## 14. Integration with Scriptorium

The Scriptorium index page (`/scriptorium/`) needs a box for Byzantine Art alongside the Maps page (Phase 2). Box specs:

- **Title:** Byzantine Art
- **Subtitle:** Eleven centuries of sacred imagery, organized for the pastor's library
- **Hero image:** Christ Pantocrator (Hagia Sophia deesis)
- **Tags:** Theology, Art History, Eschatology, Visual Discipleship
- **CTA:** "Enter the archive →"
- **Box style:** Match Maps box visual treatment (consistency across Scriptorium)

---

## 15. Open Questions for Cowork

These are decisions Cowork should bring back to Pastor Charlie before building:

1. **Sanity vs. JSON files for content storage?** (Pastor Charlie has Sanity for other DU content — may be cleaner)
2. **Image CDN — Vercel built-in, or Cloudinary for advanced features?**
3. **Should the Featured Artwork rotate weekly automatically, or be manually curated?**
4. **Should reflections support comments/discussion, or stay read-only at launch?**
5. **Should there be a "Print this reflection" feature for pastors who want to use these in sermons?** (could be a future phase)
6. **Audio narration (future): record Pastor Charlie reading selected reflections — when?**

---

## 16. Build Sequence Recommendation

**Phase A — Infrastructure (3-5 days):**
1. Routing, page templates, data model
2. Scriptorium index integration
3. Artwork detail page
4. Collection page
5. Image CDN setup
6. Sample data (10 artworks across 2 collections to test)

**Phase B — Content load (2-3 weeks, in parallel with Pastor Charlie writing reflections):**
1. Source 150 images
2. Pastor Charlie + Claude write 150 reflections (working sessions of ~2 hours each, producing 8-12 reflections per session)
3. Metadata completion
4. Quality pass

**Phase C — Discovery features (1 week):**
1. Timeline view
2. Map view
3. Search
4. Filter polish

**Phase D — Launch polish (3-5 days):**
1. SEO optimization
2. OG images for sharing
3. Performance audit
4. Accessibility audit
5. Mobile testing
6. Analytics setup

**Phase E — Launch:**
1. Public announcement
2. Email to GLM list
3. Social media campaign (the social poster system can run a custom campaign)
4. Submit to Christian directories (Christianity Today digital, Christian art societies)

**Total estimated timeline: 4-6 weeks from kickoff to launch.**

---

## 17. Success Criteria

The page is a success if:
- Launch state has 150 artworks with rich theological reflections
- Returning visitor rate >40% (people come back)
- Average session duration >5 minutes (people read the reflections)
- The page becomes a referenced resource (cited in articles, used in seminary classrooms)
- DU subscribers cite it as a reason they joined / stayed

---

**Be Obedient. Be Bold.**

— Pastor Charlie Aycock + Claude
   Gospel Life Ministries
   April 28, 2026
