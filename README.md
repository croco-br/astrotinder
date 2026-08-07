# Natal Chart Calculator

Calculadora de mapas astrais com cinco métodos de análise: Tradicional (12 signos), Hermético (24 signos), Anjos Cabalísticos (72 signos), Astrologia Cabalística (Sephiroth) e Agathadaimon (Nome do Anjo da Guarda).

## Arquitetura

Aplicação FastAPI stateless com pipeline unificado baseado em dataclasses. Cada método enriquece o esquema `Chart` com seus próprios campos específicos. O glossário esotérico (`app/glossary.py`) é a fonte única de verdade para todo o conteúdo narrativo; `app/interpretation.py` compõe uma interpretação completa por mapa.

Os dados de nascimento só existem no formulário e no pedido de cálculo atual. A aplicação não guarda contas, histórico, mapas, preferências ou resultados partilháveis.

### Métodos de Cálculo

- **Tradicional**: Roda natal SVG, destaques (Sol, Lua, Ascendente), detalhes e interpretação expansíveis.
- **Hermético**: 24 setores com títulos de Tarot. Adiciona `hermetic_title`; roda, resumo e detalhes expansíveis.
- **Anjos Cabalísticos**: 72 anjos mapeados por bins de 5°. Adiciona `angel`; roda, anjos em destaque e detalhes expansíveis.
- **Sephiroth**: Árvore da Vida cabalística (Golden Dawn), centros ativados e detalhes expansíveis.
- **Agathadaimon**: Nome baseado em Sol, Lua, Ascendente e sufixo dia/noite. A interface mostra apenas o nome e o caminho do anjo, sem mapa natal completo.

Todos os métodos retornam também um bloco `interpretation` (narrativa composta a partir do glossário).

### API

**Endpoint único**: `POST /calculate`

```json
{
  "date": "1990-06-25",
  "time": "22:15",
  "city": "São Paulo",
  "method": "traditional"
}
```

Resposta: `{ "chart": {...}, "interpretation": {...} }` (o método `agathadaimon` inclui também `daimon`).

**Outros endpoints**:
- `GET /` — interface web (formulário, tabs Calc/Glossário)
- `GET /glossary` — página do glossário esotérico (dados injetados server-side)
- `GET /api/glossary` — glossário em JSON puro (acesso programático)

## Estrutura do Projeto

```
app/
├── main.py              # FastAPI endpoints (/ , /glossary, /api/glossary, /calculate)
├── engine.py            # Pipeline unificado de cálculo
├── schema.py            # Dataclasses: Birth, PointData, Aspect, Chart
├── models.py            # ChartRequest (Pydantic)
├── geocoder.py          # Geocoding e timezone automático
├── hermetic.py          # Método hermético (24 setores)
├── angels.py            # 72 anjos cabalísticos
├── agathadaimon.py      # Agathos Daimon
├── sephiroth.py         # Mapeamento Sephiroth
├── glossary.py          # Glossário esotérico (fonte única de verdade)
├── interpretation.py    # compose(): mapa → interpretação narrativa
├── static/
│   ├── css/
│   │   ├── input.css    # Fonte Tailwind v4 (@import + design system em @layer components)
│   │   └── app.css      # Compilado (gerado por `npm run css:build`, não versionado)
│   └── js/
│       ├── natal.js     # Rodas SVG (natal, hermética, anjos) + tabelas de detalhes
│       ├── sephiroth.js # Árvore da Vida SVG
│       ├── glossary.js  # Renderizador da página do glossário
│       └── index.js     # Fluxo stateless, dispatch por método, resultados progressivos e modal
└── templates/
    ├── index.html       # Interface web (formulário)
    └── glossary.html    # Página do glossário

tests/
└── ui/                  # Testes de comportamento da UI (Playwright + pytest)
    ├── conftest.py      # Fixture live_server (uvicorn em processo, porta aleatória)
    ├── test_index.py    # Formulário, render dos 5 métodos, modal, tabs
    └── test_glossary.py # Navegação por seções, filtro de busca, limpar
```

## Tecnologias

- **Backend**: Python 3.14, FastAPI, Kerykeion 4.2.4, geopy, timezonefinder
- **Frontend**: Vanilla JS, SVG puro, **Tailwind CSS v4** (compilado em build-time)
- **Build CSS**: Node 22 + `@tailwindcss/cli`
- **Testes de UI**: Playwright + pytest (Chromium headless)

## Instalação

```bash
git clone https://github.com/croco-br/natal-chart.git
cd natal-chart

# Python deps
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

# Frontend deps + CSS (necessário para gerar app/static/css/app.css)
npm install
npm run css:build

# Rodar
uvicorn app.main:app --reload --port 8000
```

Acesse: http://127.0.0.1:8000

## Desenvolvimento

### CSS (Tailwind)

O CSS é compilado a partir de `app/static/css/input.css` (Tailwind v4 auto-detecta as classes
nos templates Jinja e nos template literals do JS). Recompile após qualquer mudança de classe:

```bash
npm run css:build   # build único (minificado) → app/static/css/app.css
npm run css:watch   # rebuild automático durante o desenvolvimento
```

As referências a arquivos estáticos são geradas por `static_url()` em `app/main.py`, que acrescenta
um hash do conteúdo ao URL. Não use versões manuais como `?v=25`: qualquer alteração a CSS ou JS
gera automaticamente um URL novo e evita cache desatualizada.

### UX Stateless

- O formulário começa vazio; `Preencher exemplo` é a única forma de inserir dados de demonstração.
- O seletor descreve o resultado de cada método e o botão de cálculo se adapta ao método escolhido.
- Durante o cálculo, a página fornece estado acessível; depois, move o foco para o resultado.
- Resultados técnicos e interpretações extensas começam recolhidos, com resumos no topo.
- `Editar dados` e `Ver outro método` retornam ao formulário atual; não persistem dados.
- Tabelas têm scroll horizontal em telas pequenas; o glossário usa um seletor de seção compacto
  no celular. Os diálogos de ajuda suportam teclado e Escape.

### Testes de UI

Os testes de UI são testes de **comportamento**: sobem o app FastAPI real em uma porta aleatória
(fixture `live_server`) e dirigem as funções de render do próprio frontend com um payload
sintético — sem depender de geocoding ao vivo nem de snapshots de pixel. Verificam estrutura
(SVG/tabela/interpretação presentes) e interações (modal, seleção de método, preenchimento de
exemplo, divulgação progressiva, navegação e filtro).

```bash
# Primeira vez: instalar o Chromium do Playwright
python -m playwright install chromium

# Rodar a suíte (24 testes)
python -m pytest tests/ui
```

`pytest.ini` já aponta `testpaths` para `tests/ui`, então `pytest` sem argumentos também funciona.

## Refatoração (Julho 2026)

Unificação de dois pipelines paralelos (legacy mutável + novo canônico) em um único pipeline baseado em `Chart` dataclass. Métodos esotéricos agora são funções puras de enriquecimento.

## Migração Bulma → Tailwind (Julho 2026)

Substituição do Bulma por Tailwind CSS v4 compilado em build-time, sem mudança de comportamento — garantida pela suíte de testes de comportamento da UI (escrita antes da migração e aprovada nas duas versões). As classes Bulma foram reescritas para o design system próprio do app definido em `input.css`.

## Licença

UNLICENSE — domínio público.
