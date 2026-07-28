/**
 * index.js — form handler + method dispatch.
 *
 * Single POST /calculate with {date, time, city, name, method}.
 * - traditional → SVG natal wheel (12 signs) + aspect detail table
 * - hermetic    → SVG hermetic wheel (24 sectors) + hermetic detail table
 * - sephiroth   → Tree of Life (traditional Golden Dawn mapping)
 * - angels      → SVG 72-sector Shem HaMephorash wheel + angel detail table
 * - others      → raw JSON dump
 *
 * SVG/detail renderers live in natal.js (wheel, hermetic, angels) and
 * sephiroth.js (tree); this file owns fetch + layout.
 */

const METHOD_LABELS = {
    traditional:  'Astrologia Tradicional (12 Signos)',
    hermetic:     'Astrologia Hermética (24 Signos)',
    angels:       'Anjos Cabalísticos (72 Signos)',
    sephiroth:    'Astrologia Cabalística (Sephiroth)',
    agathadaimon: 'Agathadaimon (Nome do Anjo da Guarda)',
};

// Methods that get a visual SVG render instead of a raw JSON dump.
const VISUAL_METHODS = new Set(['traditional', 'hermetic', 'sephiroth', 'angels', 'agathadaimon']);

async function calculate() {
    const button = document.getElementById('calculate-button');
    const container = document.getElementById('result');

    const payload = {
        date:   document.getElementById('birthdate').value,
        time:   document.getElementById('birthtime').value,
        city:   document.getElementById('city').value,
        name:   document.getElementById('name').value || null,
        method: document.getElementById('method').value,
    };

    button.classList.add('is-loading');
    container.innerHTML = '<progress class="progress is-small is-primary" max="100">calculando…</progress>';

    try {
        const res = await fetch('/calculate', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(payload),
        });
        if (!res.ok) {
            const err = await res.json().catch(() => ({}));
            throw new Error(err.error || `HTTP ${res.status}`);
        }
        const data = await res.json();

        if (VISUAL_METHODS.has(payload.method)) {
            renderVisual(data, container, payload.method);
        } else {
            renderRawJSON(data, container, payload.method);
        }
    } catch (err) {
        container.innerHTML = `
            <div class="notification is-danger is-light">
                <strong>Erro:</strong> ${err.message}
            </div>`;
    } finally {
        button.classList.remove('is-loading');
    }
}

/* ---------- visual (SVG) render path ---------- */

function renderVisual(data, container, method) {
    const chart = data.chart;
    const label = METHOD_LABELS[method] || method;

    // Visual methods with a wheel + detail table: render inline, no toggle.
    if (method === 'traditional' || method === 'hermetic' || method === 'angels' || method === 'sephiroth') {
        container.innerHTML = `
            <div class="box">
                <h2 class="subtitle">${label}${helpIcon(method)}</h2>
                <div id="wheel-container" style="max-width: 540px; margin: 0 auto;"></div>
                <div id="details-container"></div>
                <div id="interpretation-container"></div>
                ${methodModal(method)}
            </div>`;

        const wheelContainer = document.getElementById('wheel-container');
        const detailsContainer = document.getElementById('details-container');

        if (method === 'traditional') {
            const { aspects } = renderWheel(chart, wheelContainer);
            renderDetails(chart, detailsContainer, aspects);
        } else if (method === 'hermetic') {
            renderHermeticWheel(chart, wheelContainer);
            renderHermeticDetails(chart, detailsContainer);
        } else if (method === 'angels') {
            renderAngelsWheel(chart, wheelContainer);
            renderAngelsDetails(chart, detailsContainer);
        } else if (method === 'sephiroth') {
            renderTreeOfLife(chart, wheelContainer);
            renderSephirothDetails(chart, detailsContainer);
        }
        if (data.interpretation) {
            renderInterpretation(data.interpretation, document.getElementById('interpretation-container'));
        }
        return;
    }

    if (method === 'agathadaimon') {
        renderAgathadaimonView(data, container);
        return;
    }

    container.innerHTML = `
        <div class="box">
            <h2 class="subtitle">${label}</h2>
            <div id="wheel-container" style="max-width: 540px; margin: 0 auto;"></div>
            <div id="details-container"></div>
        </div>`;

    // Stash chart + method for the details toggle.
    wheelContainer.dataset.method = method;
    wheelContainer.dataset.chart = JSON.stringify(chart);
}

function toggleDetails() {
    const detailsContainer = document.getElementById('details-container');
    const wheelContainer = document.getElementById('wheel-container');

    if (detailsContainer.classList.contains('is-hidden')) {
        const chart = JSON.parse(wheelContainer.dataset.chart);
        const method = wheelContainer.dataset.method;
        if (method === 'hermetic') {
            renderHermeticDetails(chart, detailsContainer);
        } else if (method === 'angels') {
            renderAngelsDetails(chart, detailsContainer);
        } else {
            const aspects = JSON.parse(wheelContainer.dataset.aspects || '[]');
            renderDetails(chart, detailsContainer, aspects);
        }
        detailsContainer.classList.remove('is-hidden');
    } else {
        detailsContainer.classList.add('is-hidden');
    }
}

/* ---------- agathadaimon view (guardian angel name) ---------- */

function renderAgathadaimonView(data, container) {
    const chart = data.chart;
    const daimon = data.daimon || {};
    const label = METHOD_LABELS.agathadaimon;
    const birth = chart.birth;
    const personName = chart.name || '—';
    const name = daimon.name || '—';
    const hebrew = daimon.hebrew_letter || '';
    const suffix = daimon.suffix || '';
    const suffixLabel = suffix === 'El' ? 'Diurno (El)' : suffix === 'Iah' ? 'Noturno (Iah)' : suffix;

    const letters = daimon.letters || [];
    const rowsHtml = letters.map(l => `
        <tr>
            <td class="has-text-centered"><strong>${escapeHtml(l.point)}</strong></td>
            <td class="has-text-centered"><span class="tag is-primary is-light is-medium">${escapeHtml(l.letter)}</span></td>
            <td class="title is-5 has-text-centered">${escapeHtml(l.hebrew || '')}</td>
            <td class="is-size-7 has-text-centered">${escapeHtml(l.description || '—')}</td>
        </tr>`).join('');

    container.innerHTML = `
        <div class="box">
            <h2 class="subtitle has-text-centered">${label}${helpIcon('agathadaimon')}</h2>

            <div class="has-text-centered my-5">
                <p class="title is-1 has-text-primary">${escapeHtml(name)}</p>
                ${hebrew ? `<p class="title is-2 has-text-grey">${escapeHtml(hebrew)}</p>` : ''}
                <p class="is-size-7 has-text-grey mt-2">Sufixo: ${escapeHtml(suffixLabel)}</p>
            </div>

            <h3 class="subtitle is-5">Letras e Correspondências</h3>
            <table class="table is-fullwidth is-narrow is-striped">
                <thead><tr><th class="has-text-centered">Ponto</th><th class="has-text-centered">Letra</th><th class="has-text-centered">Hebraico</th><th class="has-text-centered">Descrição</th></tr></thead>
                <tbody>${rowsHtml}</tbody>
            </table>
            ${methodModal('agathadaimon')}
            <div id="interpretation-container"></div>
        </div>`;
    if (data.interpretation) {
        renderInterpretation(data.interpretation, document.getElementById('interpretation-container'));
    }
}

function escapeHtml(s) {
    return String(s == null ? '' : s)
        .replace(/&/g, '&amp;')
        .replace(/</g, '&lt;')
        .replace(/>/g, '&gt;');
}

/* ---------- method help: ? icon + modal (shared by all views) ---------- */

const METHOD_INFO = {
    traditional: {
        title: 'O que é a Astrologia Tradicional?',
        body: `
            <p>A <strong>Astrologia Tradicional</strong> divide o zodíaco em
            <strong>12 signos</strong> de 30° cada, começando em Áries (0°). Cada
            planeta é colocado na roda pela sua longitude eclíptica absoluta.</p>
            <p>Este método apresenta a <strong>roda natal clássica</strong> com os
            signos, os glifos planetários e as linhas de aspecto
            (conjunção, oposição, trígono, quadratura, sextil). A tabela de
            detalhes mostra o signo, grau, sephiroth e casa de cada ponto.</p>
            <p>As casas (1–12) indicam em que área de vida cada planeta atua;
            o Ascendente define a casa 1.</p>`,
    },
    hermetic: {
        title: 'O que é a Astrologia Hermética?',
        body: `
            <p>A <strong>Astrologia Hermética</strong> subdivide cada signo em
            duas metades de 15° — primeira [0,15) e segunda [15,30] — regidas
            por cartas de corte do tarô (Rei, Rainha, Príncipe) e associadas a
            um naipe: <strong>Bastões</strong> (Fogo), <strong>Moedas</strong>
            (Terra), <strong>Espadas</strong> (Ar) e <strong>Taças</strong>
            (Água).</p>
            <p>Os <strong>24 signos</strong> resultantes formam o sistema
            hermético. Planetas cujo grau cai nas bordas cuspais
            (≤5° ou ≥25°) recebem um <strong>título hermético</strong> e são
            destacados na roda.</p>`,
    },
    angels: {
        title: 'O que são os Anjos Cabalísticos?',
        body: `
            <p>Os <strong>72 Anjos do Shem HaMephorash</strong> são as
            expressões do Nome Divino na Cabala. São <strong>6 anjos por
            signo</strong>, um por cada bin de 5°: [0,5), [5,10), [10,15),
            [15,20), [20,25), [25,30]. Cada anjo rege um sector de 5° do
            zodíaco.</p>
            <p>Os planetas natais são colocados pelo grau e caem no sector do
            seu <strong>anjo regente</strong> — esses sectors são destacados na
            roda. A tabela de detalhes mostra qual anjo rege cada ponto.</p>`,
    },
    agathadaimon: {
        title: 'O que é o Agathadaimon?',
        body: `
            <p>O <strong>Agathadaimon</strong> (ou <em>Agathos Daimon</em>) é o
            "Bom Demónio" da tradição hermética e helenística — o espírito
            guardião pessoal, equivalente ao <em>nous</em> ou génio de cada
            indivíduo.</p>
            <p>Este método constrói o <strong>nome do anjo da guarda</strong> a
            partir de três letras hebraicas derivadas dos graus do <strong>Sol</strong>,
            da <strong>Lua</strong> e do <strong>Ascendente</strong> no mapa natal.
            Cada letra é atribuída segundo uma correspondência entre as 22 letras
            do alfabeto hebraico e os 360° do zodíaco (12 signos × 30°).</p>
            <p>Uma quarta letra, o <strong>sufixo</strong>, é adicionada ao nome:
            <em>El</em> para nascimentos diurnos (06h–18h) e <em>Iah</em> para
            nascimentos noturnos.</p>
            <p>Cada letra hebraica possui um conjunto de correspondências
            tradicionais (género, forma e caráter) que ajudam a interpretar a
            natureza do espírito guardião.</p>`,
    },
    sephiroth: {
        title: 'O que é a Astrologia Cabalística?',
        body: `
            <p>A <strong>Astrologia Cabalística</strong> coloca cada planeta na
            <strong>Árvore da Vida</strong> — o diagrama das 10 sephiroth
            (Kether → Malkuth) mais a sephirah oculta <em>Da'ath</em>, ligadas
            por 22 caminhos correspondentes às 22 letras hebraicas.</p>
            <p>Este método usa a correspondência fixa da <strong>Aurora Dourada
            (Golden Dawn)</strong>: cada planeta está associado a uma sephirah
            — Sol→Tiferet, Lua→Yesod, Saturno→Binah, etc. Os planetas natais
            são colocados na sua sephirah; as sephiroth ocupadas crescem e as
            vagas ficam esvaídas.</p>
            <p>A Árvore da Vida é a visão completa — não há roda natal neste
            método.</p>`,
    },
};

function helpIcon(method) {
    return ` <a class="method-help" title="O que é isto?" onclick="openMethodModal('${method}')">
        <span class="icon has-text-info is-small"><i class="fa fa-question-circle"></i></span></a>`;
}

function methodModal(method) {
    const info = METHOD_INFO[method];
    if (!info) return '';
    return `
        <div class="modal" id="modal-${method}">
            <div class="modal-background" onclick="closeMethodModal('${method}')"></div>
            <div class="modal-card">
                <header class="modal-card-head">
                    <p class="modal-card-title">${info.title}</p>
                    <button class="delete" aria-label="close" onclick="closeMethodModal('${method}')"></button>
                </header>
                <section class="modal-card-body">
                    <div class="content">${info.body}</div>
                </section>
                <footer class="modal-card-foot">
                    <button class="button" onclick="closeMethodModal('${method}')">Fechar</button>
                </footer>
            </div>
        </div>`;
}

function openMethodModal(method) {
    const m = document.getElementById('modal-' + method);
    if (m) m.classList.add('is-active');
}

function closeMethodModal(method) {
    const m = document.getElementById('modal-' + method);
    if (m) m.classList.remove('is-active');
}

/* ---------- raw JSON render path ---------- */

function renderRawJSON(data, container, method) {
    const label = METHOD_LABELS[method] || method;
    // Escape so the JSON is safe inside <pre>.
    const pretty = JSON.stringify(data, null, 2)
        .replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
    container.innerHTML = `
        <div class="box">
            <h2 class="subtitle">${label}</h2>
            <pre style="background:#f5f5f5;padding:1rem;border-radius:4px;overflow-x:auto;max-height:600px;font-size:0.8rem;">${pretty}</pre>
        </div>`;
}

/* ============================================================
 *  Interpretação completa (composta no backend a partir do glossário)
 * ============================================================ */

function degreeLabelInterp(pos) {
    if (pos == null) return '';
    const d = Math.floor(pos);
    const m = Math.round((pos % 1) * 60);
    return `${d}° ${m}'`;
}

function retroTagInterp(p) {
    return p.retrograde ? ' <span class="tag is-light" title="Retrógrado">R</span>' : '';
}

function pointInterpCard(p) {
    const glyph = p.glyph ? `<span style="font-size:26px;margin-right:.4rem">${p.glyph}</span>` : '';
    const header = `${glyph}<strong>${escapeHtml(p.name)}</strong> em ` +
        `<span style="font-size:20px;margin:0 .2rem">${p.sign_glyph || ''}</span>` +
        `<strong>${escapeHtml(p.sign_name)}</strong> ` +
        `<small class="has-text-grey">(${degreeLabelInterp(p.position)})</small>` +
        retroTagInterp(p);

    const signMeta = [p.sign_element, p.sign_quality, 'Regente: ' + p.sign_ruler]
        .filter(Boolean).join(' · ');

    let methodBlock = '';
    if (p.method_label) {
        methodBlock = `
            <div class="has-text-centered">
                <span class="tag is-primary is-light">${escapeHtml(p.method_label)}</span>
                <p class="is-size-7" style="margin-top:.3rem">${p.method_text}</p>
            </div>`;
    }

    return `
        <div class="box">
            <h3 class="title is-5 has-text-centered">${header}</h3>
            <hr>
            <div class="columns is-multiline has-text-centered">
                <div class="column">
                    <p class="subtitle is-7 has-text-grey">O Planeta</p>
                    <p class="title is-6">${escapeHtml(p.title)}</p>
                    <p class="is-size-7">${p.planet_description}</p>
                </div>
                <div class="column">
                    <p class="subtitle is-7 has-text-grey">O Signo</p>
                    <p class="title is-6">${escapeHtml(p.sign_name)}</p>
                    <p class="is-size-7 has-text-grey" style="margin-bottom:.3rem">${escapeHtml(signMeta)}</p>
                    <p class="is-size-7">${p.sign_description}</p>
                </div>
            </div>
            <div class="content has-text-centered">
                <p class="tag is-warning is-light">Combinação ${escapeHtml(p.name)} + ${escapeHtml(p.sign_name)}</p>
                <p class="is-size-6" style="margin-top:.4rem">${p.combination}</p>
            </div>
            ${methodBlock ? '<hr>' + methodBlock : ''}
        </div>`;
}

function aspectInterpRow(a) {
    const pa = POINT_PT[a.a] || a.a;
    const pb = POINT_PT[a.b] || a.b;
    const ga = POINT_GLYPH[a.a] || '·';
    const gb = POINT_GLYPH[a.b] || '·';
    const tag = a.harmony === 'harmónico'
        ? `<span class="tag is-link is-light">${a.aspect_glyph} ${escapeHtml(a.aspect_name)}</span>`
        : `<span class="tag is-warning is-light">${a.aspect_glyph} ${escapeHtml(a.aspect_name)}</span>`;
    return `
        <div class="box">
            <div class="columns is-vcentered has-text-centered is-mobile">
                <div class="column is-3"><strong>${ga} ${escapeHtml(pa)}</strong></div>
                <div class="column is-3">${tag}<br><small class="has-text-grey">${a.aspect_name} · orbe ${a.orb}°</small></div>
                <div class="column is-3"><strong>${gb} ${escapeHtml(pb)}</strong></div>
                <div class="column is-3"><p class="is-size-7">${a.description}</p></div>
            </div>
        </div>`;
}

function agathadaimonInterpBlock(sec) {
    const rows = sec.letters.map(l => `
        <tr>
            <td class="has-text-centered"><strong>${escapeHtml(l.point)}</strong></td>
            <td class="has-text-centered"><span class="tag is-primary is-light">${escapeHtml(l.letter)}</span></td>
            <td class="title is-5 has-text-centered">${escapeHtml(l.hebrew || '')}</td>
            <td class="is-size-7 has-text-centered">${escapeHtml(l.description || '—')}</td>
        </tr>`).join('');
    return `
        <div class="box">
            <h3 class="title is-5 has-text-centered">Nome do Anjo da Guarda</h3>
            <div class="has-text-centered my-4">
                <p class="title is-2 has-text-primary">${escapeHtml(sec.name)}</p>
                ${sec.hebrew_letter ? `<p class="title is-3 has-text-grey">${escapeHtml(sec.hebrew_letter)}</p>` : ''}
                ${sec.suffix ? `<p class="is-size-7 has-text-grey">Sufixo: <strong>${escapeHtml(sec.suffix)}</strong> — ${escapeHtml(sec.suffix_meaning || '')}</p>` : ''}
            </div>
            <table class="table is-fullwidth is-narrow is-striped">
                <thead><tr><th class="has-text-centered">Ponto</th><th class="has-text-centered">Letra</th><th class="has-text-centered">Hebraico</th><th class="has-text-centered">Descrição</th></tr></thead>
                <tbody>${rows}</tbody>
            </table>
        </div>`;
}

function renderInterpretation(interp, target) {
    if (!interp) { target.innerHTML = ''; return; }

    const pointsHtml = (interp.points || []).map(pointInterpCard).join('');

    const aspectsHtml = (interp.aspects && interp.aspects.length)
        ? `<h3 class="title is-5 has-text-centered">Aspectos do Mapa</h3>` +
          interp.aspects.map(aspectInterpRow).join('')
        : '<p class="has-text-centered has-text-grey">Nenhum aspecto detetado.</p>';

    let daimonHtml = '';
    if (interp.agathadaimon) {
        daimonHtml = agathadaimonInterpBlock(interp.agathadaimon);
    }

    target.innerHTML = `
        <div class="mt-6">
            <h2 class="title is-4 has-text-centered">Interpretação Completa</h2>
            <div class="box">
                <div class="content has-text-justified">${interp.method_intro}</div>
            </div>
            <h3 class="title is-5 has-text-centered">Os Pontos do Mapa</h3>
            ${pointsHtml}
            ${daimonHtml}
            ${aspectsHtml}
        </div>`;
}
