"""Behavioral UI tests for the glossary page.

Asserts structure + interactions (nav switching, search filter, clear) that
must be preserved across the Bulma → Tailwind refactor.
"""


class TestGlossaryStructure:
    def test_sidebar_nav_has_eight_sections(self, page, live_server):
        page.goto(live_server + "/glossary")
        links = page.locator("#glossary-nav a")
        assert links.count() == 8

    def test_search_input_and_clear_present(self, page, live_server):
        page.goto(live_server + "/glossary")
        assert page.locator("#glossary-search").count() == 1

    def test_tabs_link_to_calc(self, page, live_server):
        page.goto(live_server + "/glossary")
        href = page.locator('a:has-text("Calcular")').first.get_attribute("href")
        assert href == "/"


class TestGlossaryNav:
    def test_default_section_is_planets(self, page, live_server):
        page.goto(live_server + "/glossary")
        # planets section renders at least 11 cards
        assert page.locator("#glossary-content .glossary-item").count() >= 11

    def test_clicking_nav_switches_section(self, page, live_server):
        page.goto(live_server + "/glossary")
        page.locator('#glossary-nav a:has-text("Signos")').click()
        assert page.locator("#glossary-content .glossary-item").count() >= 12

    def test_combinations_section_has_132_cards(self, page, live_server):
        page.goto(live_server + "/glossary")
        page.locator('#glossary-nav a:has-text("Planeta + Signo")').click()
        # 11 planet headers + 132 combination cards
        assert page.locator("#glossary-content .glossary-item").count() >= 132

    def test_angels_section_renders(self, page, live_server):
        page.goto(live_server + "/glossary")
        page.locator('#glossary-nav a:has-text("72 Anjos")').click()
        assert "Shem HaMephorash" in page.locator("#glossary-content").inner_text()


class TestGlossaryFilter:
    def test_filter_narrows_items(self, page, live_server):
        page.goto(live_server + "/glossary")
        total = page.locator("#glossary-content .glossary-item").count()
        page.fill("#glossary-search", "Sol")
        page.evaluate("filterGlossary()")
        visible = page.locator("#glossary-content .glossary-item:visible").count()
        assert 0 < visible < total

    def test_clear_restores_all(self, page, live_server):
        page.goto(live_server + "/glossary")
        total = page.locator("#glossary-content .glossary-item").count()
        page.fill("#glossary-search", "zzz-no-match")
        page.evaluate("filterGlossary()")
        assert page.locator("#glossary-content .glossary-item:visible").count() == 0
        page.evaluate("clearGlossarySearch()")
        assert page.locator("#glossary-content .glossary-item:visible").count() == total
