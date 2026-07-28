"""Interpretation composer — turns a calculated Chart + method into a full
narrative interpretation using the glossary data (app.glossary.py).

This is the single consumer of the glossary on the calculation path: the
frontend never needs to fetch /api/glossary, keeping the glossary as the
backend's single source of truth.

Composition per point:
  - planet meaning (title + description)
  - sign meaning (element/quality/ruler + description)
  - the specific planet+sign combination paragraph
  - a method-specific layer (hermetic title / angel / sephirah / house)

Aspects are computed here (the canonical Chart carries an empty aspects list;
natal.js detects them client-side for the wheel). We mirror that logic so the
interpretation is self-contained.

Returned structure is JSON-serialisable and embedded in the /calculate
response under the ``interpretation`` key.
"""

from __future__ import annotations

from app.glossary import (
    AGATHADAIMON,
    ANGELS,
    ASPECTS,
    COMBINATIONS,
    KABBALAH,
    PLANETS,
    SIGNS,
    TAROT,
)

# Mirror of ASPECTS in natal.js (the frontend wheel detector).
_ASPECT_DEFS = [
    {"key": "conjunction", "angle": 0, "orb": 8},
    {"key": "sextile", "angle": 60, "orb": 5},
    {"key": "square", "angle": 90, "orb": 6},
    {"key": "trine", "angle": 120, "orb": 7},
    {"key": "opposition", "angle": 180, "orb": 8},
]
_HARMONIOUS = {"sextile", "trine"}

# Sign key -> display name (PT). Kept local to avoid importing natal.js maps.
_SIGN_PT = {
    "Ari": "Áries", "Tau": "Touro", "Gem": "Gêmeos", "Can": "Câncer",
    "Leo": "Leão", "Vir": "Virgem", "Lib": "Libra", "Sco": "Escorpião",
    "Sag": "Sagitário", "Cap": "Capricórnio", "Aqu": "Aquário", "Pis": "Peixes",
}


def _circular_separation(a: float, b: float) -> float:
    d = abs(((a - b) % 360 + 360) % 360)
    return min(d, 360 - d)


def _compute_aspects(points: dict) -> list:
    names = list(points.keys())
    out = []
    for i in range(len(names)):
        for j in range(i + 1, len(names)):
            pa, pb = points[names[i]], points[names[j]]
            sep = _circular_separation(pa["lon"], pb["lon"])
            for asp in _ASPECT_DEFS:
                d = abs(sep - asp["angle"])
                if d <= asp["orb"]:
                    info = ASPECTS[asp["key"]]
                    out.append({
                        "a": names[i],
                        "b": names[j],
                        "aspect": asp["key"],
                        "aspect_name": info["name"],
                        "aspect_glyph": info["glyph"],
                        "harmony": info["harmony"],
                        "orb": round(d, 2),
                        "description": info["description"],
                    })
                    break
    return out


def _angel_for(sign: str, position: float):
    """Find the glossary angel entry for a sign+position (5° bins)."""
    bin_idx = min(int(position // 5), 5)
    for a in ANGELS:
        if a["sign"] == sign and a["bin"] == bin_idx:
            return a
    return None


def _court_card_info(title: str):
    """Given a hermetic title like 'Rei de Bastões', return (card, suit info)."""
    if not title:
        return None
    parts = title.split(" de ")
    if len(parts) != 2:
        return None
    card, suit = parts[0], parts[1]
    suit_info = TAROT["suits"].get(suit, {})
    court_desc = TAROT["court_cards"].get(card, "")
    return {
        "card": card,
        "suit": suit,
        "suit_element": suit_info.get("element", ""),
        "suit_description": suit_info.get("description", ""),
        "court_description": court_desc,
    }


def _method_intro(method: str) -> str:
    """A short intro for the interpretation, per method (from glossary)."""
    if method == "kabbalah" or method == "sephiroth":
        return KABBALAH["intro"]
    if method == "hermetic":
        return TAROT["intro"]
    if method == "angels":
        return (
            "Os <strong>72 Anjos do Shem HaMephorash</strong> são as expressões "
            "do Nome Divino na Cabala — 6 anjos por signo, um por cada intervalo "
            "de 5° do zodíaco. Cada ponto do mapa cai no sector do seu anjo "
            "regente, que influência a expressão daquele planeta."
        )
    if method == "agathadaimon":
        return AGATHADAIMON["intro"]
    # traditional
    return (
        "A <strong>Astrologia Tradicional</strong> divide o zodíaco em 12 signos "
        "de 30°. Cada planeta manifesta-se segundo o signo em que se encontra, "
        "a casa em que cai e os aspectos que forma com os outros pontos. A "
        "interpretação abaixo combina o significado do planeta, do signo e da "
        "combinação específica planeta+signo para cada ponto do mapa."
    )


def _point_method_layer(method: str, point: dict) -> dict:
    """Method-specific extra text for a point."""
    layer = {"label": "", "text": ""}
    if method == "traditional":
        house = point.get("house")
        if house and house != "None":
            layer["label"] = "Casa"
            layer["text"] = str(house)
        else:
            layer["label"] = ""
            layer["text"] = ""
    elif method == "hermetic":
        title = point.get("hermetic_title")
        info = _court_card_info(title) if title else None
        if info:
            layer["label"] = "Título Hermético"
            layer["text"] = (
                f"<strong>{title}</strong>. {info['court_description']} "
                f"{info['suit_description']}"
            )
        else:
            layer["label"] = "Título Hermético"
            layer["text"] = (
                "Sem título hermético (grau não cuspal, entre 6° e 24°)."
            )
    elif method == "angels":
        angel = _angel_for(point["sign"], point["position"])
        if angel:
            layer["label"] = "Anjo Regente"
            layer["text"] = (
                f"<strong>{angel['angel']}</strong> "
                f"({angel['degrees']} de {_SIGN_PT.get(angel['sign'], angel['sign'])}). "
                f"<em>Virtude:</em> {angel['virtue']}. {angel['description']}"
            )
        else:
            layer["label"] = "Anjo Regente"
            layer["text"] = "—"
    elif method == "sephiroth":
        sep_name = point.get("sephirah_traditional")
        sep = KABBALAH["sephiroth"].get(sep_name, {})
        if sep:
            layer["label"] = "Sephirah"
            layer["text"] = (
                f"<strong>{sep_name}</strong> ({sep.get('hebrew', '')} — "
                f"{sep.get('title', '')}). {sep.get('description', '')} "
                f"<em>Pilar:</em> {sep.get('pillar', '')}. "
                f"<em>Planeta:</em> {sep.get('planet', '')}."
            )
        else:
            layer["label"] = "Sephirah"
            layer["text"] = "—"
    # agathadaimon handled in its own section
    return layer


def compose(chart: dict, method: str, daimon: dict | None = None) -> dict:
    """Build the full interpretation for a calculated chart.

    Args:
        chart: Chart.to_dict() output (with method-specific fields already
               enriched, e.g. hermetic_title / angel).
        method: one of traditional/hermetic/angels/sephiroth/agathadaimon.
        daimon: the agathadaimon result dict (only for that method).

    Returns a JSON-serialisable dict.
    """
    points = chart.get("points", {})

    point_interps = []
    for key, p in points.items():
        planet = PLANETS.get(key, {})
        sign = SIGNS.get(p.get("sign"), {})
        combination = COMBINATIONS.get(key, {}).get(p.get("sign"), "")
        layer = _point_method_layer(method, p)
        point_interps.append({
            "key": key,
            "name": planet.get("name", key),
            "glyph": planet.get("glyph", ""),
            "title": planet.get("title", ""),
            "planet_description": planet.get("description", ""),
            "sign_name": sign.get("name", p.get("sign", "")),
            "sign_glyph": sign.get("glyph", ""),
            "sign_description": sign.get("description", ""),
            "sign_element": sign.get("element", ""),
            "sign_quality": sign.get("quality", ""),
            "sign_ruler": sign.get("ruler", ""),
            "position": p.get("position"),
            "lon": p.get("lon"),
            "retrograde": p.get("retrograde", False),
            "combination": combination,
            "method_label": layer["label"],
            "method_text": layer["text"],
        })

    aspects = _compute_aspects(points)

    agathadaimon_section = None
    if method == "agathadaimon" and daimon is not None:
        suffix = daimon.get("suffix", "")
        suffix_meaning = AGATHADAIMON["suffixes"].get(suffix, "")
        letters = []
        for l in daimon.get("letters", []):
            letters.append({
                "point": l.get("point", ""),
                "letter": l.get("letter", ""),
                "hebrew": l.get("hebrew", ""),
                "description": l.get("description", ""),
            })
        agathadaimon_section = {
            "name": daimon.get("name", ""),
            "hebrew_letter": daimon.get("hebrew_letter", ""),
            "suffix": suffix,
            "suffix_meaning": suffix_meaning,
            "letters": letters,
        }

    return {
        "method": method,
        "method_intro": _method_intro(method),
        "points": point_interps,
        "aspects": aspects,
        "agathadaimon": agathadaimon_section,
    }
