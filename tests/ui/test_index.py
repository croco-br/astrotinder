"""Behavioral UI tests for the index (calculator) page.

These tests assert *behavior and structure*, not pixel style, so they must
pass identically before (Bulma) and after (Tailwind) the CSS refactor.

Strategy: load the real page, then drive the JS render functions directly
with a synthetic chart payload (no network / geocoding dependency). This
exercises the exact code paths a real calculation triggers.
"""

import pytest

# A minimal but structurally complete chart payload matching app/schema.py
# (11 canonical points, each with the fields the renderers read).
CHART = {
    "name": "John Doe",
    "birth": {"date": "1990-06-25", "time": "22:15", "city": "São Paulo", "tz": "-03:00"},
    "points": [
        {"name": n, "lon": 10.0 + i * 30, "sign": "Ari", "position": 10.0,
         "decan": 1, "quality": "Cardinal", "element": "Fire", "house": "First House",
         "retrograde": False, "sephirah_decan": "Binah", "sephirah_traditional": "Tiferet",
         "hermetic_title": "2 of Wands", "angel": "Ari (Vehuiah)"}
        for i, n in enumerate(
            ["sun", "moon", "mercury", "venus", "mars", "jupiter",
             "saturn", "uranus", "neptune", "pluto", "asc"])
    ],
    "aspects": [],
}

INTERPRETATION = {
    "method_intro": "<p>Intro</p>",
    "points": [
        {
            "name": "Sol", "glyph": "☉", "sign_name": "Áries", "sign_glyph": "♈",
            "position": 10.0, "retrograde": False, "title": "A Vontade",
            "planet_description": "planeta desc", "sign_description": "signo desc",
            "sign_element": "Fogo", "sign_quality": "Cardinal", "sign_ruler": "Marte",
            "combination": "combinação", "method_label": "Casa 1", "method_text": "texto",
        }
    ],
    "aspects": [],
}


def _inject_and_render(page, method):
    """Inject a chart + interpretation and call the app's render pipeline."""
    page.evaluate(
        """([chart, interp, method]) => {
            const container = document.getElementById('result');
            const data = { chart, interpretation: interp };
            if (method === 'agathadaimon') {
                data.daimon = {
                    name: 'Vehuiel', hebrew_letter: 'ה', suffix: 'El',
                    letters: [{ point: 'Sol', letter: 'Vav', hebrew: 'ו', description: 'x' }],
                };
            }
            renderVisual(data, container, method);
        }""",
        [CHART, INTERPRETATION, method],
    )


class TestIndexPageStructure:
    def test_form_fields_present(self, page, live_server):
        page.goto(live_server + "/")
        for fid in ["name", "birthdate", "birthtime", "city", "method"]:
            assert page.locator(f"#{fid}").count() == 1, f"missing #{fid}"
        assert page.locator("#calculate-button").count() == 1

    def test_personal_fields_start_empty(self, page, live_server):
        page.goto(live_server + "/")
        for fid in ["name", "birthdate", "birthtime", "city"]:
            assert page.locator(f"#{fid}").input_value() == ""

    def test_example_fill_is_explicit(self, page, live_server):
        page.goto(live_server + "/")
        page.get_by_role("button", name="Preencher exemplo").click()
        assert page.locator("#city").input_value() == "São Paulo, Brasil"

    def test_method_choice_updates_submit_label(self, page, live_server):
        page.goto(live_server + "/")
        page.get_by_role("radio", name="Anjo guardião").check()
        assert page.locator("#calculate-button").inner_text() == "Revelar nome do anjo guardião"

    def test_method_select_has_five_options(self, page, live_server):
        page.goto(live_server + "/")
        options = page.locator("#method option")
        assert options.count() == 5
        values = [options.nth(i).get_attribute("value") for i in range(5)]
        assert values == ["traditional", "hermetic", "angels", "sephiroth", "agathadaimon"]

    def test_tabs_link_to_glossary(self, page, live_server):
        page.goto(live_server + "/")
        href = page.locator('a:has-text("Glossário")').first.get_attribute("href")
        assert href == "/glossary"


class TestMethodRendering:
    @pytest.mark.parametrize(
        "method", ["traditional", "hermetic", "angels", "sephiroth"]
    )
    def test_wheel_methods_render(self, page, live_server, method):
        page.goto(live_server + "/")
        _inject_and_render(page, method)
        # wheel/tree SVG rendered
        assert page.locator("#wheel-container svg").count() >= 1
        # details table present
        assert page.locator("#details-container table").count() >= 1
        assert page.locator("#details-container").evaluate("el => el.hidden")
        # interpretation block present
        assert page.locator("#interpretation-container").inner_html().strip() != ""
        assert page.locator("#interpretation-container").evaluate("el => el.hidden")

    def test_agathadaimon_renders_guardian_angel_only(self, page, live_server):
        page.goto(live_server + "/")
        _inject_and_render(page, "agathadaimon")
        # daimon name appears somewhere in the result
        text = page.locator("#result").inner_text()
        assert "Vehuiel" in text
        assert "Caminho do anjo" in text
        assert "Interpretação Completa" not in text
        assert page.locator("#interpretation-container").count() == 0

    def test_result_has_method_label(self, page, live_server):
        page.goto(live_server + "/")
        _inject_and_render(page, "traditional")
        assert "Astrologia Tradicional" in page.locator("#result").inner_text()


class TestMethodHelpModal:
    def test_help_icon_opens_modal(self, page, live_server):
        page.goto(live_server + "/")
        _inject_and_render(page, "traditional")
        modal = page.locator("#modal-traditional")
        assert modal.count() == 1
        assert not modal.evaluate("el => el.classList.contains('is-active')")
        page.evaluate("openMethodModal('traditional')")
        assert modal.evaluate("el => el.classList.contains('is-active')")

    def test_close_button_closes_modal(self, page, live_server):
        page.goto(live_server + "/")
        _inject_and_render(page, "traditional")
        page.evaluate("openMethodModal('traditional')")
        page.evaluate("closeMethodModal('traditional')")
        assert not page.locator("#modal-traditional").evaluate(
            "el => el.classList.contains('is-active')"
        )

    def test_modal_has_title_and_body(self, page, live_server):
        page.goto(live_server + "/")
        _inject_and_render(page, "traditional")
        modal = page.locator("#modal-traditional")
        assert "Astrologia Tradicional" in modal.inner_text()
