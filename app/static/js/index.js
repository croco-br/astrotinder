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

const METHOD_ACTIONS = {
    traditional: 'Abrir leitura',
    hermetic: 'Calcular correspondências herméticas',
    angels: 'Encontrar anjos regentes',
    sephiroth: 'Ver na Árvore da Vida',
    agathadaimon: 'Revelar nome do anjo guardião',
};

const METHOD_DESCRIPTIONS = {
    traditional: 'Mapa natal · roda, posições e aspectos.',
    hermetic: 'Tarot hermético · setores e títulos de Tarot.',
    angels: 'Anjos regentes · um anjo para cada ponto natal.',
    sephiroth: 'Árvore da Vida · planetas nas Sephiroth.',
    agathadaimon: 'Anjo guardião · nome e caminho do Agathadaimon.',
};

const EXAMPLE_PERSONALITIES = [
    { name: 'Marilyn Monroe', date: '1926-06-01', time: '09:30', city: 'Los Angeles, Estados Unidos' },
    { name: 'Michael Jackson', date: '1958-08-29', time: '19:33', city: 'Gary, Indiana, Estados Unidos' },
    { name: 'Kurt Cobain', date: '1967-02-20', time: '19:38', city: 'Aberdeen, Washington, Estados Unidos' },
    { name: 'Nelson Mandela', date: '1918-07-18', time: '14:54', city: 'Mvezo, África do Sul' },
    { name: 'Al Capone', date: '1899-01-17', time: '18:00', city: 'Brooklyn, Nova York, Estados Unidos' },
    { name: 'Mahatma Gandhi', date: '1869-10-02', time: '07:11', city: 'Porbandar, Índia' },
    { name: 'Frida Kahlo', date: '1907-07-06', time: '08:30', city: 'Coyoacán, Cidade do México, México' },
    { name: 'David Bowie', date: '1947-01-08', time: '09:15', city: 'Londres, Inglaterra' },
    { name: 'Princesa Diana', date: '1961-07-01', time: '19:45', city: 'Sandringham, Inglaterra' },
    { name: 'Albert Einstein', date: '1879-03-14', time: '11:30', city: 'Ulm, Alemanha' },
    { name: 'Barack Obama', date: '1961-08-04', time: '19:24', city: 'Honolulu, Havaí, Estados Unidos' },
    { name: 'Bill Clinton', date: '1946-08-19', time: '08:51', city: 'Hope, Arkansas, Estados Unidos' },
    { name: 'Donald Trump', date: '1946-06-14', time: '10:54', city: 'Queens, Nova York, Estados Unidos' },
    { name: 'Joe Biden', date: '1942-11-20', time: '08:30', city: 'Scranton, Pensilvânia, Estados Unidos' },
    { name: 'Luiz Inácio Lula da Silva', date: '1945-10-27', time: '05:30', city: 'Caetés, Pernambuco, Brasil' },
    { name: 'John F. Kennedy', date: '1917-05-29', time: '15:00', city: 'Brookline, Massachusetts, Estados Unidos' },
    { name: 'Franklin D. Roosevelt', date: '1882-01-30', time: '20:45', city: 'Hyde Park, Nova York, Estados Unidos' },
    { name: 'Elvis Presley', date: '1935-01-08', time: '04:35', city: 'Tupelo, Mississippi, Estados Unidos' },
    { name: 'Jair Bolsonaro', date: '1955-03-21', time: '14:45', city: 'Campinas, São Paulo, Brasil' },
    { name: 'Martin Luther King Jr.', date: '1929-01-15', time: '12:00', city: 'Atlanta, Geórgia, Estados Unidos' },
];

function selectMethod(method) {
    document.getElementById('method').value = method;
    document.getElementById('calculate-button').textContent = METHOD_ACTIONS[method];
    document.getElementById('method-description').textContent = METHOD_DESCRIPTIONS[method];
}

function fillExample() {
    const example = EXAMPLE_PERSONALITIES[Math.floor(Math.random() * EXAMPLE_PERSONALITIES.length)];
    document.getElementById('name').value = example.name;
    document.getElementById('birthdate').value = example.date;
    document.getElementById('birthtime').value = example.time;
    document.getElementById('city').value = example.city;
    document.getElementById('form-status').textContent = `Exemplo: ${example.name}. Você pode alterar os dados antes de calcular.`;
}

function editDetails() {
    document.querySelector('form').scrollIntoView({ behavior: 'smooth', block: 'start' });
    document.getElementById('birthdate').focus();
}

async function calculate() {
    const button = document.getElementById('calculate-button');
    const container = document.getElementById('result');
    const status = document.getElementById('form-status');

    const payload = {
        date:   document.getElementById('birthdate').value,
        time:   document.getElementById('birthtime').value,
        city:   document.getElementById('city').value,
        name:   document.getElementById('name').value || null,
        method: document.getElementById('method').value,
    };

    button.disabled = true;
    status.textContent = 'A localizar a cidade e a calcular o resultado…';
    container.innerHTML = '<div class="result-loading"><div class="spinner" role="status" aria-label="calculando…"></div><span>A localizar a cidade e a compor a leitura…</span></div>';

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
        status.textContent = 'Resultado calculado.';
        const heading = container.querySelector('[data-result-heading]');
        if (heading) {
            heading.scrollIntoView({ behavior: 'smooth', block: 'start' });
            heading.focus({ preventScroll: true });
        }
    } catch (err) {
        container.innerHTML = `
            <div class="alert-error">
                <strong>Erro:</strong> ${escapeHtml(err.message)}
            </div>`;
        status.textContent = 'Não foi possível calcular o resultado. Reveja os dados e tente novamente.';
    } finally {
        button.disabled = false;
    }
}

/* ---------- visual (SVG) render path ---------- */

function renderVisual(data, container, method) {
    const chart = data.chart;
    const label = METHOD_LABELS[method] || method;

    // Visual methods with a wheel + detail table: render inline, no toggle.
    if (method === 'traditional' || method === 'hermetic' || method === 'angels' || method === 'sephiroth') {
        container.innerHTML = `
            <div class="result-toolbar">
                <button type="button" class="btn-ghost" onclick="editDetails()">Editar dados</button>
                <button type="button" class="btn-ghost" onclick="editDetails()">Mudar lente</button>
            </div>
            <section class="result-heading">
                <p class="kicker">Leitura calculada</p>
                <h2 data-result-heading tabindex="-1">${label}${helpIcon(method)}</h2>
                <p class="result-meta">${birthLine(chart.birth)}${chart.name ? ` · ${escapeHtml(chart.name)}` : ''}</p>
            </section>
            <div class="reading-desk">
                <div class="diagram-panel"><div id="wheel-container"></div></div>
                <div class="reading-panel">
                    <h3>Primeiras leituras</h3>
                    <div id="highlights-container"></div>
                    <button type="button" class="details-toggle" aria-expanded="false" aria-controls="interpretation-container" onclick="toggleSection('interpretation-container', this, 'Ler interpretação completa', 'Ocultar interpretação completa')">Ler interpretação completa</button>
                    <div id="interpretation-container" class="interpretation-container"></div>
                    <button type="button" class="details-toggle" aria-expanded="false" aria-controls="details-container" onclick="toggleSection('details-container', this, 'Ver detalhes técnicos', 'Ocultar detalhes técnicos')">Ver detalhes técnicos</button>
                    <div id="details-container" class="details-container"></div>
                </div>
            </div>
            ${methodModal(method)}`;

        const wheelContainer = document.getElementById('wheel-container');
        const detailsContainer = document.getElementById('details-container');

        if (method === 'traditional') {
            const { aspects } = renderWheel(chart, wheelContainer);
            renderDetails(chart, detailsContainer, aspects, data.interpretation?.aspects);
            renderHighlights(chart, method, document.getElementById('highlights-container'), aspects);
        } else if (method === 'hermetic') {
            renderHermeticWheel(chart, wheelContainer);
            renderHermeticDetails(chart, detailsContainer);
            renderHighlights(chart, method, document.getElementById('highlights-container'));
        } else if (method === 'angels') {
            renderAngelsWheel(chart, wheelContainer);
            renderAngelsDetails(chart, detailsContainer);
            renderHighlights(chart, method, document.getElementById('highlights-container'));
        } else if (method === 'sephiroth') {
            renderTreeOfLife(chart, wheelContainer);
            renderSephirothDetails(chart, detailsContainer);
            renderHighlights(chart, method, document.getElementById('highlights-container'));
        }
        detailsContainer.hidden = true;
        if (data.interpretation) {
            renderInterpretation(data.interpretation, document.getElementById('interpretation-container'));
        }
        document.getElementById('interpretation-container').hidden = true;
        return;
    }

    if (method === 'agathadaimon') {
        renderAgathadaimonView(data, container);
        return;
    }

    container.innerHTML = `
        <div class="card">
            <h2 class="h-subtitle">${label}</h2>
            <div id="wheel-container" class="mx-auto max-w-[540px]"></div>
            <div id="details-container"></div>
        </div>`;

    // Stash chart + method for the details toggle.
    wheelContainer.dataset.method = method;
    wheelContainer.dataset.chart = JSON.stringify(chart);
}

function toggleSection(id, button, showLabel, hideLabel) {
    const section = document.getElementById(id);
    const isHidden = section.hidden;
    section.hidden = !isHidden;
    button.setAttribute('aria-expanded', String(isHidden));
    button.textContent = isHidden ? hideLabel : showLabel;
}

function renderHighlights(chart, method, target, aspects = []) {
    const points = chart.points || {};
    if (method === 'traditional') {
        const featured = ['sun', 'moon', 'asc'].filter(key => points[key]).map(key =>
            `<span class="tag tag-primary">${POINT_GLYPH[key] || ''} ${POINT_PT[key] || key}: ${points[key].sign}</span>`).join('');
        const aspectText = aspects.length ? `${aspects.length} aspectos detectados` : 'Sem aspectos detectados';
        target.innerHTML = `<div class="highlights-panel"><h3 class="reading-section-title">Destaques do mapa</h3><p class="highlight-tags">${featured}</p><p class="field-help">${aspectText}</p></div>`;
    } else if (method === 'angels') {
        const angels = [...new Set(Object.values(points).map(p => p.angel).filter(Boolean))];
        target.innerHTML = `<div class="highlights-panel"><h3 class="reading-section-title">Anjos em destaque</h3><p class="field-help">${angels.slice(0, 4).join(' · ') || 'Consulte a roda para os anjos regentes.'}</p></div>`;
    } else if (method === 'sephiroth') {
        const nodes = [...new Set(Object.values(points).map(p => p.sephirah_traditional).filter(Boolean))];
        target.innerHTML = `<div class="highlights-panel"><h3 class="reading-section-title">Centros mais ativados</h3><p class="field-help">${nodes.join(' · ')}</p></div>`;
    } else {
        target.innerHTML = `<div class="highlights-panel"><h3 class="reading-section-title">Correspondências principais</h3><p class="field-help">Consulte os títulos e posições para explorar as relações herméticas.</p></div>`;
    }
}

function toggleDetails() {
    const detailsContainer = document.getElementById('details-container');
    const wheelContainer = document.getElementById('wheel-container');

    if (detailsContainer.classList.contains('hidden')) {
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
        detailsContainer.classList.remove('hidden');
    } else {
        detailsContainer.classList.add('hidden');
    }
}

/* ---------- agathadaimon view (guardian angel name) ---------- */

function renderAgathadaimonView(data, container) {
    const daimon = data.daimon || {};
    const name = daimon.name || '—';
    const hebrew = daimon.hebrew_letter || '';
    const suffix = daimon.suffix || '';
    const suffixLabel = suffix === 'El' ? 'Diurno (El)' : suffix === 'Iah' ? 'Noturno (Iah)' : suffix;

    const letters = daimon.letters || [];
    const rowsHtml = letters.map(l => `
        <tr>
            <td><strong>${escapeHtml(l.point)}</strong></td>
            <td><span class="tag tag-primary text-sm">${escapeHtml(l.letter)}</span></td>
            <td class="text-xl font-semibold">${escapeHtml(l.hebrew || '')}</td>
            <td class="text-xs">${escapeHtml(l.description || '—')}</td>
        </tr>`).join('');

    container.innerHTML = `
        <div class="result-toolbar">
            <button type="button" class="btn-ghost" onclick="editDetails()">Editar dados</button>
            <button type="button" class="btn-ghost" onclick="editDetails()">Ver outro método</button>
        </div>
        <section class="result-heading">
            <p class="kicker">Leitura calculada</p>
            <h2 data-result-heading tabindex="-1">O seu nome de anjo guardião${helpIcon('agathadaimon')}</h2>
        </section>
        <div class="reading-desk">
        <div class="diagram-panel">

            <div>
                <p class="guardian-name">${escapeHtml(name)}</p>
                ${hebrew ? `<p class="reading-section-title">${escapeHtml(hebrew)}</p>` : ''}
                <p class="field-help">Sufixo: ${escapeHtml(suffixLabel)}</p>
            </div>

            <p class="field-help">Formado pelas correspondências do Sol, Lua e Ascendente, com sufixo diurno ou noturno.</p>
        </div><div class="reading-panel"><h3>Caminho do anjo</h3>
            <div class="table-wrap"><table class="data-table">
                <thead><tr><th>Ponto</th><th>Letra</th><th>Hebraico</th><th>Descrição</th></tr></thead>
                <tbody>${rowsHtml}</tbody>
            </table></div>
        </div></div>${methodModal('agathadaimon')}`;
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
            [15,20), [20,25), [25,30]. Cada anjo rege um setor de 5° do
            zodíaco.</p>
            <p>Os planetas natais são colocados pelo grau e caem no setor do
            seu <strong>anjo regente</strong> — esses setores são destacados na
            roda. A tabela de detalhes mostra qual anjo rege cada ponto.</p>`,
    },
    agathadaimon: {
        title: 'O que é o Agathadaimon?',
        body: `
            <p>O <strong>Agathadaimon</strong> (ou <em>Agathos Daimon</em>) é o
            "Bom Demônio" da tradição hermética e helenística — o espírito
            guardião pessoal, equivalente ao <em>nous</em> ou gênio de cada
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
            tradicionais (gênero, forma e caráter) que ajudam a interpretar a
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
    return ` <button type="button" class="method-help" title="O que é isto?" aria-label="Saber mais sobre este método" onclick="openMethodModal('${method}', this)">
        <span class="ml-1 inline-flex text-sky-600"><i class="fa fa-question-circle"></i></span></button>`;
}

function methodModal(method) {
    const info = METHOD_INFO[method];
    if (!info) return '';
    return `
        <div class="modal" id="modal-${method}" role="dialog" aria-modal="true" aria-labelledby="modal-title-${method}" onkeydown="handleModalKey(event, '${method}')">
            <div class="modal-backdrop" onclick="closeMethodModal('${method}')"></div>
            <div class="modal-card">
                <header class="modal-head">
                    <p class="modal-title" id="modal-title-${method}">${info.title}</p>
                    <button class="modal-close text-2xl leading-none" aria-label="close" onclick="closeMethodModal('${method}')">&times;</button>
                </header>
                <section class="modal-body">
                    ${info.body}
                </section>
                <footer class="modal-foot">
                    <button class="btn-ghost" onclick="closeMethodModal('${method}')">Fechar</button>
                </footer>
            </div>
        </div>`;
}

let modalTrigger = null;

function openMethodModal(method, trigger) {
    const m = document.getElementById('modal-' + method);
    if (m) {
        modalTrigger = trigger || document.activeElement;
        m.classList.add('is-active');
        m.querySelector('.modal-close').focus();
    }
}

function closeMethodModal(method) {
    const m = document.getElementById('modal-' + method);
    if (m) m.classList.remove('is-active');
    if (modalTrigger) modalTrigger.focus();
}

function handleModalKey(event, method) {
    if (event.key === 'Escape') closeMethodModal(method);
}

/* ---------- raw JSON render path ---------- */

function renderRawJSON(data, container, method) {
    const label = METHOD_LABELS[method] || method;
    // Escape so the JSON is safe inside <pre>.
    const pretty = JSON.stringify(data, null, 2)
        .replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
    container.innerHTML = `
        <div class="card">
            <h2 class="h-subtitle">${label}</h2>
            <pre class="max-h-[600px] overflow-x-auto rounded-md bg-stone-100 p-4 text-xs">${pretty}</pre>
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
    return p.retrograde ? ' <span class="tag tag-neutral" title="Retrógrado">R</span>' : '';
}

function formatCombination(text) {
    return escapeHtml(text).replace(/\n/g, '<br>');
}

function pointInterpCard(p) {
    const glyph = p.glyph ? `<span class="mr-2 text-2xl">${p.glyph}</span>` : '';
    const header = `${glyph}<strong>${escapeHtml(p.name)}</strong> em ` +
        `<span class="mx-1 text-xl">${p.sign_glyph || ''}</span>` +
        `<strong>${escapeHtml(p.sign_name)}</strong> ` +
        `<small class="muted">(${degreeLabelInterp(p.position)})</small>` +
        retroTagInterp(p);

    const signMeta = [p.sign_element, p.sign_quality, 'Regente: ' + p.sign_ruler]
        .filter(Boolean).join(' · ');

    const readingLayer = (label, text) => text ? `
        <div class="reading-layer">
            <p class="reading-layer-name">${label}</p>
            <p>${escapeHtml(text)}</p>
        </div>` : '';

    let methodBlock = '';
    if (p.method_label) {
        methodBlock = `
            <div class="reading-layer">
                <p class="reading-layer-name">${escapeHtml(p.method_label)}</p>
                <p>${p.method_text}</p>
            </div>`;
    }

    return `
        <div class="interpretation-card">
            <h3>${header}</h3>
            <p class="mt-1 muted" style="font-size:.86rem">${escapeHtml(p.title)} — ${escapeHtml(signMeta)}</p>
            <hr class="divider">
            <div class="prose-body">${p.planet_description ? `<p>${escapeHtml(p.planet_description)}</p>` : ''}${p.sign_description ? `<p class="mt-2">${escapeHtml(p.sign_description)}</p>` : ''}</div>
            <div class="interp-layers">
                ${readingLayer('Luz do planeta', p.planet_light)}
                ${readingLayer('Sombra do planeta', p.planet_shadow)}
                ${readingLayer('Integração do planeta', p.planet_integration)}
                ${readingLayer('Luz do signo', p.sign_light)}
                ${readingLayer('Sombra do signo', p.sign_shadow)}
                ${readingLayer('Integração do signo', p.sign_integration)}
            </div>
            <div class="interp-combination">
                <p class="reading-layer-name">Combinação ${escapeHtml(p.name)} + ${escapeHtml(p.sign_name)}</p>
                <p>${formatCombination(p.combination)}</p>
            </div>
            ${methodBlock}
        </div>`;
}

let interpretationPoints = [];

function selectInterpretationPoint(index) {
    const point = interpretationPoints[index];
    const target = document.getElementById('selected-combination');
    if (!point || !target) return;
    target.innerHTML = pointInterpCard(point);
    document.querySelectorAll('#combination-picker button').forEach((button, buttonIndex) => {
        button.setAttribute('aria-pressed', String(buttonIndex === index));
    });
}

function combinationLayers(method) {
    const fourthLayer = method === 'traditional' ? 'Casa' :
        method === 'hermetic' ? 'Tarot' : method === 'angels' ? 'Anjo regente' : 'Sephirah';
    return `
        <div class="combination-card">
            <h3>Uma leitura nasce do encontro de camadas</h3>
            <p class="field-help">Nenhum elemento do mapa é lido isoladamente. Escolha um ponto abaixo para explorar a combinação que ele forma neste mapa.</p>
            <div class="combination-layers">
                <div class="combination-layer"><strong>Planeta</strong>o que se expressa</div>
                <div class="combination-layer"><strong>Signo</strong>como se expressa</div>
                <div class="combination-layer"><strong>${fourthLayer}</strong>onde ou por qual lente se expressa</div>
                <div class="combination-layer"><strong>Aspectos</strong>como dialoga com os demais pontos</div>
            </div>
        </div>`;
}

function renderInterpretation(interp, target) {
    if (!interp) { target.innerHTML = ''; return; }

    interpretationPoints = interp.points || [];
    const pickerHtml = interpretationPoints.map((point, index) =>
        `<button type="button" aria-pressed="${index === 0}" onclick="selectInterpretationPoint(${index})">${point.glyph || ''} ${escapeHtml(point.name)} em ${escapeHtml(point.sign_name)}</button>`).join('');

    target.innerHTML = `
        <div class="mt-6">
            <h2 class="reading-section-title">Interpretação completa</h2>
            <div class="interpretation-card"><div class="prose-body">${interp.method_intro}</div></div>
            ${combinationLayers(interp.method)}
            <h3 class="reading-section-title">Explore as combinações deste mapa</h3>
            <div id="combination-picker" class="combination-picker">${pickerHtml}</div>
            <div id="selected-combination">${interpretationPoints[0] ? pointInterpCard(interpretationPoints[0]) : ''}</div>
        </div>`;
}
