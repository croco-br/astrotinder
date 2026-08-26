/**
 * glossary.js — renders window.GLOSSARY (server-injected) into the glossary page.
 *
 * Sidebar sections + free-text filter. No backend calls after page load;
 * all data is embedded in the HTML by app/main.py -> app/glossary.py.
 */

const SIGN_PT = {
    Ari: "Áries", Tau: "Touro", Gem: "Gêmeos", Can: "Câncer",
    Leo: "Leão", Vir: "Virgem", Lib: "Libra", Sco: "Escorpião",
    Sag: "Sagitário", Cap: "Capricórnio", Aqu: "Aquário", Pis: "Peixes",
};

const POINT_PT = {
    sun: "Sol", moon: "Lua", mercury: "Mercúrio", venus: "Vênus",
    mars: "Marte", jupiter: "Júpiter", saturn: "Saturno",
    uranus: "Urano", neptune: "Netuno", pluto: "Plutão", asc: "Ascendente",
};

let CURRENT_SECTION = "planets";

/* ---------- helpers ---------- */

function card(title, glyph, body, extra = "", dataKey = "") {
    const glyphHtml = glyph ? `<span class="mr-2 text-2xl font-semibold text-amber-700">${glyph}</span>` : "";
    return `
        <div class="card glossary-item" data-key="${dataKey}">
            <h3 class="h-section">${glyphHtml}${title}</h3>
            ${extra ? `<p class="text-xs muted mt-0.5">${extra}</p>` : ""}
            <div class="prose-body mt-2">${body}</div>
        </div>`;
}

function escapeHtml(s) {
    return String(s == null ? "" : s)
        .replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
}

function formatCombination(text) {
    return escapeHtml(text).replace(/\n/g, "<br>");
}

/* ---------- section renderers ---------- */

function renderPlanets(g) {
    return Object.entries(g.planets).map(([key, p]) =>
        card(p.name, p.glyph,
            `<p><strong>${p.title}.</strong> ${p.description}</p>`,
            "", `${p.name} ${p.title}`)).join("");
}

function renderSigns(g) {
    return Object.entries(g.signs).map(([key, s]) =>
        card(s.name, s.glyph,
            `<p>${s.description}</p>`,
            `Elemento: ${s.element} · Qualidade: ${s.quality} · Regente: ${s.ruler}`,
            `${s.name} ${s.element} ${s.quality} ${s.ruler}`)).join("");
}

function renderCombinations(g) {
    const planetOptions = Object.entries(g.planets).map(([key, planet]) =>
        `<option value="${key}"${key === "sun" ? " selected" : ""}>${planet.glyph} ${planet.name}</option>`).join("");
    const signOptions = Object.entries(g.signs).map(([key, sign]) =>
        `<option value="${key}"${key === "Ari" ? " selected" : ""}>${sign.glyph} ${sign.name}</option>`).join("");
    return `
        <div class="card glossary-item" data-key="combinações planeta signo interpretação">
            <h3 class="h-section">Explore as 132 combinações planeta + signo</h3>
            <p class="prose-body mt-2">Cada planeta pode se manifestar nos 12 signos. Esta é a primeira camada da leitura; casa, aspectos e o método escolhido acrescentam contexto ao mapa natal.</p>
            <div class="combination-explorer mt-4">
                <div><label class="field-label" for="combination-planet">Planeta</label><select id="combination-planet" class="input-plain" onchange="showCombination()">${planetOptions}</select></div>
                <div><label class="field-label" for="combination-sign">Signo</label><select id="combination-sign" class="input-plain" onchange="showCombination()">${signOptions}</select></div>
            </div>
            <div id="combination-result" class="mt-4"></div>
        </div>`;
}

function showCombination() {
    const planetKey = document.getElementById("combination-planet").value;
    const signKey = document.getElementById("combination-sign").value;
    const planet = window.GLOSSARY.planets[planetKey];
    const sign = window.GLOSSARY.signs[signKey];
    const text = window.GLOSSARY.combinations[planetKey][signKey];
    document.getElementById("combination-result").innerHTML = card(
        `${planet.name} em ${sign.name}`, planet.glyph, `<p>${formatCombination(text)}</p>`,
        `${sign.element} · ${sign.quality} · Regente: ${sign.ruler}`,
        `${planet.name} ${sign.name} ${text}`,
    );
}

function renderAspects(g) {
    const out = `<div class="prose-body"><p>Aspectos são relações angulares entre planetas. Cada um tem um ângulo ideal e um orbe (tolerância) que define se está ativo.</p></div>`;
    return out + Object.entries(g.aspects).map(([key, a]) =>
        card(a.name, a.glyph,
            `<p>${a.description}</p>`,
            `Ângulo: ${a.angle}° · Orbe: ${a.orb}° · Natureza: ${a.harmony}`,
            `${a.name} ${a.description}`)).join("");
}

function renderKabbalah(g) {
    const k = g.kabbalah;
    const intro = `<div class="card glossary-item" data-key="Cabala Árvore da Vida"><h3 class="h-section">A Cabala & a Árvore da Vida</h3><div class="prose-body mt-2">${k.intro}</div></div>`;
    const seps = Object.entries(k.sephiroth).map(([name, s]) =>
        card(name, s.hebrew,
            `<p><strong>${s.title}.</strong> ${s.description}</p>`,
            `Planeta: ${s.planet} · Pilar: ${s.pillar}`,
            `${name} ${s.title} ${s.planet} ${s.description}`)).join("");
    return intro + seps;
}

function renderTarot(g) {
    const t = g.tarot;
    let out = `<div class="card glossary-item" data-key="Tarot Hermético 24"><h3 class="h-section">Astrologia Hermética (24 Signos)</h3><div class="prose-body mt-2">${t.intro}</div></div>`;

    out += `<div class="card glossary-item" data-key="Naipes"><h3 class="text-base font-semibold text-stone-800">Os Naipes & Elementos</h3>`;
    out += Object.entries(t.suits).map(([name, s]) =>
        `<p class="mt-1 text-sm"><strong>${name}</strong> (${s.element}): ${s.description}</p>`).join("") + `</div>`;

    out += `<div class="card glossary-item" data-key="Cartas de corte"><h3 class="text-base font-semibold text-stone-800">As Cartas de Corte</h3>`;
    out += Object.entries(t.court_cards).map(([name, desc]) =>
        `<p class="mt-1 text-sm"><strong>${name}:</strong> ${desc}</p>`).join("") + `</div>`;

    out += `<div class="card glossary-item" data-key="Regra cuspial"><h3 class="text-base font-semibold text-stone-800">Regra Cuspial</h3><div class="prose-body mt-2">${t.cuspal_rule}</div></div>`;

    out += `<div class="card glossary-item" data-key="24 setores tabela"><h3 class="text-base font-semibold text-stone-800">Os 24 Setores</h3>
        <div class="table-wrap"><table class="data-table mt-2 text-xs">
        <thead><tr><th>Signo</th><th>Metade</th><th>Título Hermético</th><th>Naipe</th><th>Elemento</th></tr></thead><tbody>`;
    out += t.sectors.map(sec =>
        `<tr><td>${SIGN_PT[sec.sign] || sec.sign}</td><td>${sec.half}</td><td><strong>${sec.title}</strong></td><td>${sec.suit}</td><td>${sec.element}</td></tr>`).join("");
    out += `</tbody></table></div></div>`;
    return out;
}

function renderAngels(g) {
    let out = `<div class="card glossary-item" data-key="72 Anjos Shem HaMephorash"><h3 class="h-section">Os 72 Anjos do Shem HaMephorash</h3>
        <div class="prose-body mt-2">
        <p>São as 72 expressões do Nome Divino na Cabala — 6 anjos por signo, um por cada intervalo de 5° do zodíaco
        ([0,5), [5,10), [10,15), [15,20), [20,25), [25,30]). Cada planeta cai no setor do seu anjo regente.</p></div></div>`;
    out += `<div class="card glossary-item" data-key="tabela 72 anjos"><div class="table-wrap"><table class="data-table mt-2 text-xs">
        <thead><tr><th>Anjo</th><th>Signo</th><th>Grau</th><th>Virtude</th></tr></thead><tbody>`;
    out += g.angels.map(a =>
        `<tr><td><strong>${a.angel}</strong></td><td>${SIGN_PT[a.sign] || a.sign}</td><td>${a.degrees}</td><td>${a.virtue}<br><span class="muted">${a.description}</span></td></tr>`).join("");
    out += `</tbody></table></div></div>`;
    return out;
}

function renderAgathadaimon(g) {
    const a = g.agathadaimon;
    let out = `<div class="card glossary-item" data-key="Agathadaimon"><h3 class="h-section">Agathadaimon</h3><div class="prose-body mt-2">${a.intro}</div></div>`;

    out += `<div class="card glossary-item" data-key="Sufixos"><h3 class="text-base font-semibold text-stone-800">Sufixos (Dia/Noite)</h3>`;
    out += Object.entries(a.suffixes).map(([name, desc]) =>
        `<p class="mt-1 text-sm"><strong>${name}:</strong> ${desc}</p>`).join("") + `</div>`;

    out += `<div class="card glossary-item" data-key="Letras hebraicas"><h3 class="text-base font-semibold text-stone-800">As 22 Letras Hebraicas & Correspondências</h3>
        <div class="table-wrap"><table class="data-table mt-2 text-xs">
        <thead><tr><th>Letra</th><th>Hebraico</th><th>Correspondência</th></tr></thead><tbody>`;
    out += Object.entries(a.hebrew_letters).map(([name, desc]) => {
        const uni = a.hebrew_unicode[name] || "";
        return `<tr><td><strong>${name}</strong></td><td class="text-xl font-semibold">${uni}</td><td>${desc}</td></tr>`;
    }).join("");
    out += `</tbody></table></div></div>`;
    return out;
}

const RENDERERS = {
    planets: renderPlanets,
    signs: renderSigns,
    combinations: renderCombinations,
    aspects: renderAspects,
    kabbalah: renderKabbalah,
    tarot: renderTarot,
    angels: renderAngels,
    agathadaimon: renderAgathadaimon,
};

/* ---------- nav + filter ---------- */

function showSection(name, navLink) {
    CURRENT_SECTION = name;
    document.getElementById("glossary-content").innerHTML = RENDERERS[name](window.GLOSSARY);
    if (name === "combinations") showCombination();
    const picker = document.getElementById("glossary-section-picker");
    if (picker) picker.value = name;
    // nav active state
    document.querySelectorAll("#glossary-nav button").forEach(a => {
        a.classList.remove("glossary-nav-active");
        a.removeAttribute("aria-current");
    });
    if (navLink) {
        navLink.classList.add("glossary-nav-active");
        navLink.setAttribute("aria-current", "page");
    }
    else {
        // activate the matching link (after a re-render/filter)
        const links = document.querySelectorAll("#glossary-nav button");
        links.forEach(a => { if (a.textContent.trim().toLowerCase().includes(name) ||
            (name === "combinations" && a.textContent.includes("Planeta + Signo")) ||
            (name === "kabbalah" && a.textContent.includes("Cabala")) ||
            (name === "tarot" && a.textContent.includes("Tarot")) ||
            (name === "angels" && a.textContent.includes("72")) ) {
            a.classList.add("glossary-nav-active");
            a.setAttribute("aria-current", "page");
        }});
    }
    filterGlossary();
}

function filterGlossary() {
    const q = (document.getElementById("glossary-search").value || "").toLocaleLowerCase().trim();
    const items = document.querySelectorAll("#glossary-content .glossary-item");
    let visible = 0;
    items.forEach(el => {
        const matches = !q || el.textContent.toLocaleLowerCase().includes(q);
        el.style.display = matches ? "" : "none";
        if (matches) visible++;
    });
    document.getElementById("glossary-search-status").textContent = q
        ? `${visible} resultados nesta seção.` : "";
}

function clearGlossarySearch() {
    document.getElementById("glossary-search").value = "";
    filterGlossary();
}

window.addEventListener("DOMContentLoaded", () => {
    showSection("planets", document.querySelector("#glossary-nav button"));
});
