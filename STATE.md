# Astrology Matcher — State Document

**Date:** 2026-07-24  
**Project:** natal-chart (Astrology Calculator + Compatibility Matcher)  
**Current Phase:** Phase 2 complete + Phase 2.5 (Glossary & Interpretations) — ready for Phase 3  
**Language:** Python 3.14 (FastAPI) + vanilla JS + hand-built SVG

---

## Project Overview

Build an astrology compatibility matcher that:
1. Calculates natal charts from birth data (date, time, city)
2. Cross-references charts with Kabbalah (Sephirotic Tree of Life)
3. Matches one chart against N others using **classical synastry**
4. Scales to millions of comparisons in milliseconds

**Core insight:** Astrological aspects are harmonics of the circle. Encode planet longitudes as Fourier features (sin/cos for k=1,2,3,4,6) to get a 110-float vector where cosine similarity ≈ aspect resonance. Use this for fast recall (FAISS), then exact synastry scoring on candidates.

---

## Architecture Decisions (Locked)

| Aspect | Decision |
|--------|----------|
| **Match algorithm** | Classical synastry (aspects weighted by planet pairs), NOT Levenshtein/hash |
| **Speed strategy** | Two-stage: harmonic embedding → FAISS recall → exact synastry on candidates |
| **Data model** | Absolute longitudes [0-360°] as source of truth; all else derived |
| **Planet set** | 10 classical planets + Ascendant (11 points total) |
| **Match profiles** | Romance, Friendship, Business (weighted differently) |
| **Birth time** | Required (for Ascendant/house positions) |
| **Sephirotic mapping** | Traditional Golden Dawn only (decan-based scheme removed from UI) |
| **Frontend** | Server-rendered Jinja2 + Bulma + vanilla JS + hand-built SVG (no React/SPA) |
| **Scale** | Design for millions (NumPy → FAISS), but start simple |

---

## Completed Work

### Phase 0: Schema & Engine Refactor ✅

**Goal:** Establish canonical data model where longitude is the source of truth.

**Key files:**
- `app/schema.py` — Framework-free dataclasses for `Chart`, `Birth`, `PointData`, `Aspect`
- `app/engine.py` — `calculate_chart()` dispatcher + `build_chart_from_subject()` extractor
- `app/models.py` — Pydantic `ChartRequest` request model (pydantic-v1 compatible)
- `app/geocoder.py` — City → (lat, lon, tz) via `geopy` + `timezonefinder`
- `app/sephiroth.py` — Dual mapping (decan + traditional) — both still computed server-side
- `app/extensions.py` — **deleted** (no longer needed)

**What changed:**
- **Longitude-first:** `PointData.lon` (0-360°) is the source of truth; `sign`, `position`,
  `decan`, `quality`, `element` all derived from it via kerykeion attrs.
- **Timezone auto:** `geocoder.py` derives IANA tz from lat/lon via `timezonefinder`, so the
  user only supplies a city.
- **Dual sephiroth** both still populated per point (`sephirah_decan` + `sephirah_traditional`),
  but the **UI only shows the traditional** scheme now (decan scheme dropped in Phase 2).
- **Single endpoint:** `POST /calculate` dispatches on `req.method` and returns method-specific
  dict. There is **no** `/charts/calculate` endpoint (the HANDOFF that mentioned it was stale).
- Birth time is hard-required (`_require_time` raises `ValueError`).

**Schema shape** (`app/schema.py`):
```python
@dataclass
class PointData:
    name: str
    lon: float                      # source of truth (absolute, 0-360°)
    sign: str                       # "Ari", "Tau", ...
    position: float                 # degrees within sign (0-30)
    decan: int                      # 1, 2, or 3
    quality: Optional[str]          # Cardinal / Fixed / Mutable
    element: Optional[str]          # Fire / Earth / Air / Water
    house: Optional[str]
    retrograde: bool
    sephirah_decan: str             # scheme A: (quality × decan) — computed, not shown in UI
    sephirah_traditional: str       # scheme B: Golden Dawn fixed planet→sephirah — shown in UI
    hermetic_title: Optional[str]   # populated only by enrich_hermetic
    angel: Optional[str]            # populated only by enrich_angels
```

**Endpoints:**
```
GET  /              — serves index.html (form UI, Calc/Glossário tabs)
GET  /glossary      — dedicated glossary page (server-injected data)
GET  /api/glossary  — raw glossary JSON for programmatic access
POST /calculate     — {date, time, city, name, method} → method-specific response
                       methods: traditional | hermetic | angels | sephiroth | agathadaimon
                       ALL methods now also return "interpretation" (see Phase 2.5)
```

---

### Phase 1: Natal Chart UI ✅

**Goal:** Render natal charts as interactive SVG wheels with aspect lines.

**Key files:**
- `app/static/js/natal.js` — SVG wheel builder (natal + hermetic) + aspect calculator + detail tables
- `app/static/js/index.js` — `calculate()` form handler → `/calculate` → dispatches render by method

**What was built:**
- **SVG natal wheel:** 360° zodiac ring (Aries on the left, counter-clockwise), sign sectors,
  planet glyphs, intra-chart aspect lines (trine/sextile/square/opposition/conjunction).
- **Hermetic wheel:** 24 sectors of 15° (early/late halves per sign), suit-coloured
  (Wands=Fire, Coins=Earth, Swords=Air, Cups=Water); planets in cuspal bands (≤5° or ≥25°)
  highlighted. Mirrors `app/hermetic.py`.
- **Aspect detection (JS):** for each planet pair, compute angular distance [0-180°], check
  against aspect orbs (first match wins). Harmony lines drawn under tension lines.
- **Detail tables:** collapsible — point positions (+ intra-chart aspects for traditional;
  + hermetic titles for hermetic).

**Aspect orbs (degrees):** conjunction 8, opposition 8, trine 7, square 6, sextile 5.

**Conditional rendering:** `traditional` + `hermetic` + `sephiroth` → SVG views; `angels` +
`agathadaimon` → raw JSON dump (visuals pending — see task #4 for angels).

---

### Phase 2: Sephirotic Tree of Life ✅

**Goal:** SVG Tree of Life with planets placed on sephiroth via the fixed Golden Dawn attribution.

**Key files:**
- `app/static/js/sephiroth.js` — Tree of Life SVG builder + planet placement
- `app/static/js/index.js` — `renderSephiroticView()` (tree only)
- `app/templates/index.html` — loads `sephiroth.js` (cache-busted to v6)

**What was built:**
- **11 fixed nodes** at Kircher three-pillar coordinates (Kether..Malkuth + hidden Da'ath),
  each with Hebrew name, Portuguese title, and Golden Dawn colour.
- **22 connecting paths** with Hebrew letters (Aleph..Tav) on path midpoints.
- **Planet placement** reads `point.sephirah_traditional` only (fixed Golden Dawn mapping:
  Sun→Tiferet, Saturn→Binah, Uranus→**Chockmah**, Neptune→Kether, Pluto→Da'ath, etc.).
- **Node scaling** — occupied sephiroth grow with planet count; unoccupied render faded; Da'ath
  renders dashed and only fills when Pluto lands there.
- **Hover tooltips** — each planet glyph has an SVG `<title>` (name + sign + degree).
- **View is tree-only** — no natal wheel shown (removed per request). A hidden `wheel-container`
  still stashes the chart JSON so the details toggle can find it.

**Critical spelling note:** sephirah names in JS must match `app/sephiroth.py` exactly (it is the
source of truth). Python emits **`Chockmah`** (two c's) for Uranus — NOT `Chokmah`. A JS key
mismatch here silently drops the node. This was the original "missing Chockmah" bug.

**Decan scheme removed:** the original decan-based mapping (quality × decan → sephirah) is no
longer shown in the UI. `sephirah_decan` is still computed server-side in `PointData` but the
tree and the detail table only use `sephirah_traditional`. The detail table's `Decanato` /
`Sephiroth (dec.)` columns were removed; only a single `Sephiroth` column (traditional) remains.

**Bugs fixed during this work:**
- `natal.js` had its entire hermetic block **duplicated three times** → `const` redeclaration
  `SyntaxError` killed the whole file (no wheel rendered). Collapsed to one copy.
- `sephiroth.js` redeclared `const POINT_GLYPH` (already global from `natal.js`) → "Identifier
  already declared" aborted the file. Now reuses the global with a fallback.
- `Chockmah` misspelled `Chokmah` in JS → Uranus's node silently failed to render. Fixed.

**Verified:**
- ✅ All 5 Python tests pass; network probe reads `result["chart"]` (returns a dict, not a Chart)
- ✅ All 3 JS files parse (`node --check`) and load together cleanly in a shared global scope
- ✅ `renderTreeOfLife` lands on `window`; all 11 nodes render incl. Chockmah with Uranus
- ✅ Pluto→Da'ath renders the hidden node

---

### Phase 2.5: Esoteric Glossary & Narrative Interpretations ✅ (uncommitted)

**Goal:** Turn raw chart data into full narrative interpretations, powered by a single
backend glossary as the source of truth (Portuguese UI).

**New files:**
- `app/glossary.py` (~825 lines) — the single source of truth for all esoteric content:
  - `PLANETS` (11: name, glyph, title, description)
  - `SIGNS` (12: element, quality, ruler, description)
  - `COMBINATIONS` (11×12 = **132 hand-written planet+sign paragraphs**)
  - `ASPECTS` (5: angle, orb, harmony, description)
  - `KABBALAH` (intro + all 11 sephiroth incl. Da'ath — spelling matches `sephiroth.py`, `Chockmah`)
  - `TAROT` (intro, 4 suits, 3 court cards, cuspal rule, 24 sectors table)
  - `ANGELS` (72 entries: sign, 5°-bin, degrees, virtue, description — mirrors `angels.py`)
  - `AGATHADAIMON` (intro, El/Iah suffixes, 22 Hebrew letters + unicode)
  - `as_dict()` — JSON-serialisable dump of everything
- `app/interpretation.py` — `compose(chart_dict, method, daimon=None)` builds a full
  interpretation dict per `/calculate`:
  - per point: planet meaning + sign meaning (element/quality/ruler) + the specific
    planet+sign combination paragraph + a method-specific layer (house for traditional,
    hermetic court-card for hermetic, ruling angel for angels, sephirah for sephiroth)
  - `_compute_aspects()` — Python re-implementation of the JS aspect detector
    (same orbs: conj 8, opp 8, trine 7, square 6, sextile 5), so interpretations
    include intra-chart aspects even though `Chart.aspects` stays `[]` server-side
  - agathadaimon section (letters + suffix meanings) when method == "agathadaimon"
- `app/templates/glossary.html` — dedicated `/glossary` page: sidebar nav (Planetas,
  Signos, Planeta+Signo, Aspectos, Cabala, Tarot Hermético, 72 Anjos, Agathadaimon)
  + free-text filter; data injected server-side via `window.GLOSSARY`
- `app/static/js/glossary.js` — renders `window.GLOSSARY` into the 8 sections,
  no backend calls after page load

**Modified files:**
- `app/engine.py` — every `/calculate` method now returns
  `{"chart": ..., "interpretation": compose(...)}` (agathadaimon also keeps `daimon`)
- `app/main.py` — added `GET /glossary` (server-rendered) and `GET /api/glossary` (raw JSON)
- `app/static/js/index.js` — `renderInterpretation()` + per-point cards (planet/sign/
  combination/method-layer), aspect rows, agathadaimon name block; rendered below
  every visual method (traditional, hermetic, sephiroth, agathadaimon). `angels` is
  no longer raw-JSON — it renders the interpretation block (the wheel is still pending,
  see task #4)
- `app/templates/index.html` — Calc/Glossário tabs; `index.js` cache-busted to v23

**Design note:** the glossary is backend-only; the frontend never fetches it
(`/api/glossary` exists only for programmatic consumers). This keeps one source of
truth and zero JS/Python duplication.

**Verified working:** server runs, all 5 methods return interpretation blocks,
`/glossary` renders all 8 sections with filter.

---

## Current State

**Running:** `python -m uvicorn app.main:app --reload --port 8000`, form at `/`.

**Methods:**
- `traditional` → natal wheel + aspect detail table + interpretation
- `hermetic` → 24-sector wheel + hermetic detail table + interpretation
- `sephiroth` → Tree of Life only + detail table (Sephiroth column = traditional) + interpretation
- `angels` → interpretation block (72-angels wheel still pending — task #4)
- `agathadaimon` → daimon name block + interpretation (wheel/visual TBD)

---

## Technical Context

**Python environment:**
- Python 3.14 (pyenv), `.venv` active, all deps installed
- Key deps: `kerykeion==4.2.4`, `fastapi`, `uvicorn`, `geopy`, `timezonefinder`, `numpy`

**Kerykeion version quirk:**
- v4.2.4 provides `sun.abs_pos`, `moon.abs_pos`, etc. as absolute longitudes.
- v5+ changed the API; we're pinned to 4.2.4.
- Kerykeion pulls `pydantic<2`; `schema.py` uses pure dataclasses to stay framework-free,
  `models.py` keeps the request model pydantic-v1-compatible.

**Load-order gotcha (frontend):** all three JS files use classic `<script defer>`, which share
one global scope. Do **not** redeclare a top-level `const`/`let` that another file already
declares — it throws "Identifier already declared" and aborts the whole file. (`POINT_GLYPH` is
declared in `natal.js`; `sephiroth.js` reuses it.) `node --check` per-file will NOT catch this —
load both files in a `vm` sandbox together to verify.

**File structure:**
```
natal-chart/
├── app/
│   ├── __init__.py
│   ├── main.py              — FastAPI app, GET / + POST /calculate
│   ├── engine.py            — calculate_chart() dispatcher + build_chart_from_subject()
│   ├── schema.py            — Chart, Birth, PointData, Aspect dataclasses + CANONICAL_POINTS
│   ├── models.py            — ChartRequest pydantic model
│   ├── sephiroth.py         — decan + traditional sephirah mappings
│   ├── hermetic.py          — hermetic tarot titles (enrich_hermetic)
│   ├── angels.py            — 72 Shem HaMephorash angels (enrich_angels)
│   ├── agathadaimon.py      — Agathadaemon name (enrich_agathadaimon)
│   ├── geocoder.py          — resolve_location(): city → (lat, lon, tz)
│   ├── glossary.py          — esoteric glossary: single source of truth (as_dict)
│   ├── interpretation.py    — compose(): chart dict → narrative interpretation
│   ├── templates/index.html — form UI (Calc/Glossário tabs)
│   ├── templates/glossary.html — glossary page (server-injected window.GLOSSARY)
│   └── static/js/
│       ├── natal.js         — natal + hermetic wheels, aspect detection, detail tables
│       ├── sephiroth.js     — Tree of Life renderer (renderTreeOfLife)
│       ├── glossary.js      — glossary page renderer (8 sections + filter)
│       └── index.js         — form handler, method dispatch, renderVisual, renderInterpretation
├── tests/test_phase0.py     — 5 core tests + network probe
├── requirements.txt
├── PLAN.md                  — original spec / architecture
├── STATE.md                 — THIS FILE
└── .venv/
```

---

## What's Next: Phase 3 (Matcher — NumPy Synastry)

**Goal:** Two-stage compatibility search — harmonic embedding recall → exact synastry re-rank.

**Key design points (from PLAN.md §3):**
- Each chart → 110-float harmonic embedding (11 points × 5 harmonics × 2),
  `cos kλ, sin kλ` for k ∈ {1,2,3,4,6}. Stage 1 = recall filter (millions → ~1k).
- Stage 2 (source of truth): 11×11 cross-chart aspects, vectorized with NumPy
  broadcasting over all candidates at once. Report harmony + tension subscores.
- Three weight profiles (planet weights `wₚ`): Romance (Venus/Mars/Moon/Sun/ASC),
  Friendship (Moon/Mercury/Sun/Jupiter/ASC), Business (Saturn/Mercury/Mars/Sun/Jupiter).
- Orbs/weights in a config file (the primary "does it feel right" tuning lever).
- Brute-force NumPy now (thousands, <100ms); FAISS pre-filter only at Phase 5.

**Implementation plan:**
1. `app/matcher.py` — synastry scorer + harmonic embedding (`Chart.embedding`).
2. `app/config/aspects.py` (or YAML) — aspect definitions, orbs, weights, profiles.
3. `POST /match` — `{chart_id | inline chart, type, limit}` → ranked matches with
   per-match shared-aspect breakdown.
4. `app/seeder.py` + `POST /admin/seed` (or CLI) — synthetic charts → embedding matrix.
5. SQLite chart store (`/charts/{id}`) — persist chart + embedding.

**Frontend (Phase 4, after engine lands):** match view (new Jinja2 template + route) with
match-type selector, ranked list, and a bi-wheel highlighting shared aspects.

---

## Pending Frontend Work

- **Task #4 (queued): 72 Angels of Shem HaMephorash diagram.** The `angels` method
  now renders the narrative interpretation block, but no wheel yet. Each chart point
  already carries `p.angel = "Sign (AngelName)"` via `enrich_angels`, and
  `glossary.ANGELS` has all 72 sectors. Build a 72-sector ring (12 signs × 6
  five-degree bins) showing the Shem HaMephorash names, with natal planets placed on
  their angel's sector. Add to `natal.js` or a new `angels.js`; wire into `index.js`
  `VISUAL_METHODS` + `renderVisual`.
- `agathadaimon` method → daimon block + interpretation shown; dedicated visual TBD.

---

## Known Issues & Notes

1. **Timezone cache:** `requests_cache` was removed during the refactor — geocoding hits
   Nominatim directly each call. Re-add caching if geocoding latency matters (offline tests
   skip network).
2. **Aspect detection is duplicated:** `Chart.aspects` is always `[]` server-side, but
   `interpretation.py._compute_aspects()` now mirrors the JS detector (same orbs) for
   narrative output. Phase 3 should unify on the Python scorer as the source of truth.
3. **Sephirotic mapping:** both schemes still computed server-side; UI shows traditional only.
   If Phase 3 needs a single sephirah value per point, use `sephirah_traditional`.
4. **Scale:** no FAISS yet; current engine does brute-force NumPy (sufficient until Phase 5).
5. **Match profiles:** weights not yet defined; placeholder land in Phase 3.
6. **Phase 2.5 uncommitted:** glossary + interpretation work (4 new files, 4 modified)
   is on the working tree, not yet committed.

---

## Quick Start (for Next Session)

```bash
cd /Users/nsx001146/Documents/source/natal-chart
source .venv/bin/activate
python tests/test_phase0.py          # 5/5 core tests + network probe
node --check app/static/js/natal.js
node --check app/static/js/sephiroth.js
node --check app/static/js/index.js
node --check app/static/js/glossary.js
python -m uvicorn app.main:app --reload --port 8000
```

Then navigate to http://127.0.0.1:8000 — all 5 methods respond; 3 render as SVG views
(traditional, hermetic, sephiroth) and every method shows a narrative interpretation
block; `angels` is interpretation-only until task #4. The `/glossary` page lists all
esoteric content (planetas, signos, 132 combinações, aspectos, Cabala, Tarot, 72 anjos,
Agathadaimon) with a text filter.

**Next task:** task #4 (72 Angels diagram) is queued; Phase 3 (NumPy synastry matcher)
follows per PLAN.md §3. Consider committing Phase 2.5 (glossary + interpretations)
first — it's a self-contained feature.

---

## References

- `PLAN.md` — original requirements / architecture document
- `tests/test_phase0.py` — schema verification tests (5 core + network probe)
- `app/static/js/natal.js` — natal + hermetic wheel renderers, detail tables
- `app/static/js/sephiroth.js` — Tree of Life renderer (`renderTreeOfLife`)
- `app/static/js/index.js` — form handler + method dispatch + `renderInterpretation`
- `app/static/js/glossary.js` — glossary page renderer
- `app/glossary.py` — esoteric content, single source of truth (`as_dict()`)
- `app/interpretation.py` — `compose()`: narrative interpretation per method
- `app/schema.py` — canonical data model (source of truth for the chart shape)
- `app/sephiroth.py` — source of truth for sephirah spelling (note: `Chockmah`, two c's)
