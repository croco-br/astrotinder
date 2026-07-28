"""Glossário esotérico — conteúdo explicativo servido ao frontend.

Fonte única de verdade para o glossário da aplicação. Cobertura:

- Planetas (11) + significado individual
- Signos (12) + elemento, qualidade, regente
- Combinações planeta+signo (11 × 12 = 132) — todas redigidas à parte
- Aspectos (5)
- Cabala + cada sephirah (10 + Da'ath)
- Tarot hermético: naipes, cartas de corte, 24 setores, regra cuspial
- 72 Anjos do Shem HaMephorash
- Agathadaimon: letras hebraicas + sufixos

Atribuições seguem o corpus hermético/qabalístico tradicional
(Golden Dawn, Shem HaMephorash). Ortografia das sephiroth alinha-se com
``app/sephiroth.py`` (fonte de verdade, ex.: "Chockmah").
"""

from __future__ import annotations

PLANETS = {
    "sun": {
        "name": "Sol",
        "glyph": "☉",
        "title": "A Identidade e a Vitalidade",
        "description": (
            "O Sol representa a essência do eu, a identidade consciente, a "
            "vitalidade e o propósito central da vida. É o núcleo luminoso "
            "do mapa: aquilo que se busca tornar e irradiar. Governa o ego, "
            "a criatividade espontânea e o princípio paterno."
        ),
    },
    "moon": {
        "name": "Lua",
        "glyph": "☽",
        "title": "As Emoções e o Inconsciente",
        "description": (
            "A Lua simboliza a vida emocional, os instintos, a memória e o "
            "inconsciente. É a necessidade de acolhimento, o humor, a "
            "receptividade e o princípio materno. Indica como se reage "
            "automaticamente e de que se necessita para sentir segurança."
        ),
    },
    "mercury": {
        "name": "Mercúrio",
        "glyph": "☿",
        "title": "A Mente e a Comunicação",
        "description": (
            "Mercúrio rege o pensamento, a razão, a linguagem e o "
            "intercâmbio. É o mensageiro: como se processa, aprende, "
            "transmite e conecta ideias. Governa também a destreza, os "
            "deslocamentos curtos e o discernimento analítico."
        ),
    },
    "venus": {
        "name": "Vénus",
        "glyph": "♀",
        "title": "O Amor e os Valores",
        "description": (
            "Vénus rege o amor, a atração, o prazer, a beleza e o sistema "
            "de valores. Indica o que se aprecia, como se relaciona e de "
            "que forma se busca a harmonia e a afinidade. Governa a "
            "estética, o afeto e a sensualidade."
        ),
    },
    "mars": {
        "name": "Marte",
        "glyph": "♂",
        "title": "A Ação e o Desejo",
        "description": (
            "Marte é a força motriz: o desejo, a coragem, a iniciativa, a "
            "agressividade e a energia física. Mostra como se persegue o "
            "que se quer, como se luta, se defende e se afirma. É a "
            "vontade em movimento."
        ),
    },
    "jupiter": {
        "name": "Júpiter",
        "glyph": "♃",
        "title": "A Expansão e o Sentido",
        "description": (
            "Júpiter rege a expansão, a abundância, a fé, a sabedoria e a "
            "busca de sentido. Indica onde se cresce, onde há "
            "oportunidade e otimismo, e como se atribui significado à "
            "vida. Governa a filosofia, a religião e a generosidade."
        ),
    },
    "saturn": {
        "name": "Saturno",
        "glyph": "♄",
        "title": "A Estrutura e o Limite",
        "description": (
            "Saturno representa a disciplina, a responsabilidade, o tempo, "
            "o limite e a estrutura. Mostra onde se é provado, onde se "
            "deve amadurecer e construir com paciência. É o mestre "
            "rigoroso que transforma esforço em realização duradoura."
        ),
    },
    "uranus": {
        "name": "Urano",
        "glyph": "♅",
        "title": "A Mudança e a Liberdade",
        "description": (
            "Urano é o despertar, a mudança brusca, a originalidade, a "
            "liberdade e a rebelião. Indica onde se quebra o padrão, "
            "onde surge a inovação e o inesperado. Governa a "
            "individualidade, a intuição elétrica e a ruptura com o "
            "passado."
        ),
    },
    "neptune": {
        "name": "Netuno",
        "glyph": "♆",
        "title": "O Sonho e a Transcendência",
        "description": (
            "Netuno rege o sonho, a imaginação, a mística, a compaixão e "
            "a dissolução dos limites. É o princípio da transcendência: "
            "a unificação, a inspiração artística e espiritual, mas "
            "também a ilusão e a névoa."
        ),
    },
    "pluto": {
        "name": "Plutão",
        "glyph": "♇",
        "title": "A Transformação e o Poder",
        "description": (
            "Plutão simboliza a transformação radical, o poder, a morte e "
            "o renascimento, o submundo e a regeneração. Indica onde se "
            "deve morrer para renascer, onde reside o poder oculto e a "
            "profundidade incontrolável."
        ),
    },
    "asc": {
        "name": "Ascendente",
        "glyph": "↑",
        "title": "A Persona e a Aparência",
        "description": (
            "O Ascendente é o grau que nasce no horizonte no momento do "
            "nascimento. Representa a persona, a primeira impressão, o "
            "corpo físico e como o mundo é abordado. É a máscara que se "
            "usa e o filtro através do qual o mapa se expressa."
        ),
    },
}

SIGNS = {
    "Ari": {
        "name": "Áries", "glyph": "♈", "element": "Fogo", "quality": "Cardinal",
        "ruler": "Marte",
        "description": (
            "Signo de Fogo Cardinal, regido por Marte. É o início do "
            "zodíaco: iniciativa, coragem, pioneirismo e impulso. "
            "Representa o surgimento da individualidade e a vontade de "
            "agir agora."
        ),
    },
    "Tau": {
        "name": "Touro", "glyph": "♉", "element": "Terra", "quality": "Fixo",
        "ruler": "Vénus",
        "description": (
            "Signo de Terra Fixo, regido por Vénus. Estabilidade, "
            "paciência, sensualidade e apego aos valores materiais. "
            "Representa a construção lenta e a fruição do que é sólido."
        ),
    },
    "Gem": {
        "name": "Gêmeos", "glyph": "♊", "element": "Ar", "quality": "Mutável",
        "ruler": "Mercúrio",
        "description": (
            "Signo de Ar Mutável, regido por Mercúrio. Curiosidade, "
            "versatilidade, comunicação e movimento mental. Representa o "
            "intercâmbio, a multiplicidade e o aprender."
        ),
    },
    "Can": {
        "name": "Câncer", "glyph": "♋", "element": "Água", "quality": "Cardinal",
        "ruler": "Lua",
        "description": (
            "Signo de Água Cardinal, regido pela Lua. Emoção, nutrimento, "
            "lar, memória e proteção. Representa o acolhimento e o "
            "vínculo afetivo e familiar."
        ),
    },
    "Leo": {
        "name": "Leão", "glyph": "♌", "element": "Fogo", "quality": "Fixo",
        "ruler": "Sol",
        "description": (
            "Signo de Fogo Fixo, regido pelo Sol. Criatividade, orgulho, "
            "generosidade e necessidade de brilhar. Representa a "
            "expressão radiante do eu e o reconhecimento."
        ),
    },
    "Vir": {
        "name": "Virgem", "glyph": "♍", "element": "Terra", "quality": "Mutável",
        "ruler": "Mercúrio",
        "description": (
            "Signo de Terra Mutável, regido por Mercúrio. Análise, "
            "serviço, precisão, discernimento e humildade. Representa o "
            "aperfeiçoamento e o trabalho útil e detalhado."
        ),
    },
    "Lib": {
        "name": "Libra", "glyph": "♎", "element": "Ar", "quality": "Cardinal",
        "ruler": "Vénus",
        "description": (
            "Signo de Ar Cardinal, regido por Vénus. Equilíbrio, "
            "harmonia, parceria e estética. Representa a relação com o "
            "outro e a busca da justiça e da beleza."
        ),
    },
    "Sco": {
        "name": "Escorpião", "glyph": "♏", "element": "Água", "quality": "Fixo",
        "ruler": "Plutão (Marte, tradicional)",
        "description": (
            "Signo de Água Fixo, regido por Plutão (Marte na tradição). "
            "Intensidade, profundidade, transformação, segredo e poder. "
            "Representa o mergulho nas profundezas e a regeneração."
        ),
    },
    "Sag": {
        "name": "Sagitário", "glyph": "♐", "element": "Fogo", "quality": "Mutável",
        "ruler": "Júpiter",
        "description": (
            "Signo de Fogo Mutável, regido por Júpiter. Liberdade, "
            "filosofia, viagem, sentido e otimismo. Representa a "
            "expansão e a busca da verdade e do horizonte."
        ),
    },
    "Cap": {
        "name": "Capricórnio", "glyph": "♑", "element": "Terra", "quality": "Cardinal",
        "ruler": "Saturno",
        "description": (
            "Signo de Terra Cardinal, regido por Saturno. Ambição, "
            "disciplina, estrutura, mestria e responsabilidade. "
            "Representa a escalada e a realização duradoura."
        ),
    },
    "Aqu": {
        "name": "Aquário", "glyph": "♒", "element": "Ar", "quality": "Fixo",
        "ruler": "Urano (Saturno, tradicional)",
        "description": (
            "Signo de Ar Fixo, regido por Urano (Saturno na tradição). "
            "Originalidade, comunidade, ideais, rebeldia e visão de "
            "futuro. Representa o indivíduo no coletivo."
        ),
    },
    "Pis": {
        "name": "Peixes", "glyph": "♓", "element": "Água", "quality": "Mutável",
        "ruler": "Netuno (Júpiter, tradicional)",
        "description": (
            "Signo de Água Mutável, regido por Netuno (Júpiter na "
            "tradição). Compaixão, mística, sonho, dissolução e "
            "entrega. Representa a unificação e o retorno à fonte."
        ),
    },
}

# 11 × 12 = 132 combinações planeta+signo, todas redigidas à parte.
COMBINATIONS = {
    "sun": {
        "Ari": "A identidade se afirma pela iniciativa e pela coragem; a vontade é pioneira e o ego se acende na ação imediata.",
        "Tau": "A identidade se constrói com lentidão e firmeza; a vitalidade é estável e a vontade busca segurança e sensorialidade.",
        "Gem": "A identidade se expressa pela palavra e pela curiosidade; o brilho está na versatilidade e no intercâmbio de ideias.",
        "Can": "A identidade é emocional e protetora; a vitalidade nutre e o ego se identifica com o lar e a memória.",
        "Leo": "A identidade se realiza na expressão radiante; a vontade é criativa, generosa e o ego busca reconhecimento.",
        "Vir": "A identidade se refina pela análise e pelo serviço; a vitalidade se dedica a aperfeiçoar e a discernir.",
        "Lib": "A identidade se forma na relação; a vontade busca equilíbrio, harmonia e o reconhecimento do outro.",
        "Sco": "A identidade é intensa e transformadora; a vontade penetra as profundezas e o ego renasce das crises.",
        "Sag": "A identidade se expande pela busca de sentido; a vitalidade é entusiasta e a vontade visa à liberdade e à verdade.",
        "Cap": "A identidade se forja na disciplina e na ambição; a vitalidade é sóbria e o ego busca realização e autoridade.",
        "Aqu": "A identidade é original e visionária; a vontade se volta para o coletivo e o ego se afirma pela diferença.",
        "Pis": "A identidade é fluida e compassiva; a vitalidade se dissolve na unidade e o ego se entrega à imaginação.",
    },
    "moon": {
        "Ari": "As emoções são rápidas e inflamáveis; a necessidade é de independência e de ação imediata.",
        "Tau": "As emoções são estáveis e sensoriais; a necessidade é de segurança material e de conforto.",
        "Gem": "As emoções são mentais e mutáveis; a necessidade é de estímulo, variedade e comunicação.",
        "Can": "As emoções são profundas e protetoras; a necessidade é de pertencer, nutrir e ser nutrido.",
        "Leo": "As emoções são calorosas e dramáticas; a necessidade é de reconhecimento, criatividade e afeto generoso.",
        "Vir": "As emoções se filtram pela análise; a necessidade é de utilidade, ordem e de se sentir útil.",
        "Lib": "As emoções se equilibram na relação; a necessidade é de harmonia, companhia e beleza.",
        "Sco": "As emoções são intensas e secretas; a necessidade é de fusão, profundidade e controlo emocional.",
        "Sag": "As emoções são expansivas e otimistas; a necessidade é de liberdade, sentido e aventura.",
        "Cap": "As emoções são contidas e responsáveis; a necessidade é de estrutura, dignidade e segurança duradoura.",
        "Aqu": "As emoções são desapegadas e ideais; a necessidade é de liberdade e de vínculos comunitários.",
        "Pis": "As emoções são fluidas e universais; a necessidade é de entrega, compaixão e transcendência.",
    },
    "mercury": {
        "Ari": "O pensamento é rápido e direto; a comunicação é assertiva, pioneira e por vezes precipitada.",
        "Tau": "O pensamento é prático e lento; a comunicação é ponderada, sensual e valoriza o concreto.",
        "Gem": "O pensamento é ágil e multifacetado; a comunicação é viva, curiosa e dispersa.",
        "Can": "O pensamento é emocional e mnemónico; a comunicação é intuitiva e protegida pela memória.",
        "Leo": "O pensamento é criativo e expressivo; a comunicação é dramática, generosa e orgulhosa das ideias.",
        "Vir": "O pensamento é analítico e preciso; a comunicação é detalhada, crítica e orientada ao serviço.",
        "Lib": "O pensamento é comparativo e diplomático; a comunicação busca equilíbrio, justiça e estética.",
        "Sco": "O pensamento é penetrante e estratégico; a comunicação é reservada, inquiridora e profunda.",
        "Sag": "O pensamento é sintético e visionário; a comunicação é entusiasta, franca e filosófica.",
        "Cap": "O pensamento é estruturado e ambicioso; a comunicação é sóbria, pragmática e focada em resultados.",
        "Aqu": "O pensamento é inventivo e abstrato; a comunicação é original, impessoal e voltada ao futuro.",
        "Pis": "O pensamento é intuitivo e poético; a comunicação é vaga, simbólica e permeável.",
    },
    "venus": {
        "Ari": "O amor é ardente e direto; os valores são corajosos e a atração busca a conquista.",
        "Tau": "O amor é sensual e constante; os valores são materiais e a atração busca a posse e o conforto.",
        "Gem": "O amor é lúdico e cerebral; os valores são variados e a atração busca o diálogo.",
        "Can": "O amor é protetor e nostálgico; os valores são familiares e a atração busca segurança emocional.",
        "Leo": "O amor é generoso e teatral; os valores são criativos e a atração busca admiração.",
        "Vir": "O amor é devotado e detalhista; os valores são práticos e a atração busca a utilidade e a perfeição.",
        "Lib": "O amor é harmonioso e cooperativo; os valores são estéticos e a atração busca o equilíbrio.",
        "Sco": "O amor é intenso e possessivo; os valores são profundos e a atração busca a fusão total.",
        "Sag": "O amor é livre e entusiasta; os valores são filosóficos e a atração busca a aventura partilhada.",
        "Cap": "O amor é sério e duradouro; os valores são ambiciosos e a atração busca o compromisso e o estatuto.",
        "Aqu": "O amor é desapegado e amigável; os valores são ideais e a atração busca a liberdade e a mente.",
        "Pis": "O amor é místico e compassivo; os valores são universais e a atração busca a entrega e a união.",
    },
    "mars": {
        "Ari": "A ação é impetuosa e pioneira; a energia é abundante e o desejo é de liderar.",
        "Tau": "A ação é lenta e persistente; a energia é estável e o desejo é de possuir.",
        "Gem": "A ação é versátil e nervosa; a energia é mental e o desejo é de variedade.",
        "Can": "A ação é emocional e defensiva; a energia protege a família e o desejo é de segurança.",
        "Leo": "A ação é criativa e orgulhosa; a energia é radiante e o desejo é de brilhar.",
        "Vir": "A ação é meticulosa e útil; a energia se canaliza no trabalho e o desejo é de aperfeiçoar.",
        "Lib": "A ação é diplomática e hesitante; a energia busca parcerias e o desejo é de harmonia.",
        "Sco": "A ação é estratégica e intensa; a energia é magnética e o desejo é de poder e transformação.",
        "Sag": "A ação é entusiasta e itinerante; a energia é expansiva e o desejo é de liberdade.",
        "Cap": "A ação é disciplinada e ambiciosa; a energia é controlada e o desejo é de realização.",
        "Aqu": "A ação é original e rebelde; a energia é elétrica e o desejo é de inovar.",
        "Pis": "A ação é intuitiva e fluida; a energia é dispersa e o desejo se dissolve ou se entrega.",
    },
    "jupiter": {
        "Ari": "A expansão é pioneira e corajosa; a fé está na iniciativa e a busca de sentido é aventurosa.",
        "Tau": "A expansão é estável e sensata; a fé está na segurança material e a abundância é concreta.",
        "Gem": "A expansão é intelectual e social; a fé está na palavra e o sentido vem da variedade.",
        "Can": "A expansão é protetora e familiar; a fé é tradicional e a abundância nutre os seus.",
        "Leo": "A expansão é criativa e generosa; a fé é entusiasta e o sentido vem do reconhecimento.",
        "Vir": "A expansão é analítica e prática; a fé se prova no detalhe e o sentido vem do serviço.",
        "Lib": "A expansão é relacional e estética; a fé está na justiça e o sentido vem do equilíbrio.",
        "Sco": "A expansão é intensa e transformadora; a fé provém das crises e o sentido nasce da profundidade.",
        "Sag": "A expansão é livre e filosófica; a fé é ilimitada e o sentido vem da busca da verdade.",
        "Cap": "A expansão é disciplinada e estruturada; a fé é pragmática e o sentido vem da realização duradoura.",
        "Aqu": "A expansão é original e humanitária; a fé é idealista e o sentido vem do coletivo.",
        "Pis": "A expansão é mística e compassiva; a fé é transcendente e o sentido vem da entrega universal.",
    },
    "saturn": {
        "Ari": "A disciplina restringe a impulsão; a estrutura se constrói na iniciativa contida e na paciência com a ação.",
        "Tau": "A disciplina se assenta na constância; a estrutura é material e os limites são sensuais e pacientes.",
        "Gem": "A disciplina organiza o pensamento; a estrutura vem da concentração e os limites são mentais.",
        "Can": "A disciplina protege com rigor; a estrutura se forma na família e os limites são emocionais.",
        "Leo": "A disciplina tempera o orgulho; a estrutura se faz na expressão madura e os limites são criativos.",
        "Vir": "A disciplina se manifesta no trabalho; a estrutura é metódica e os limites são perfeccionistas.",
        "Lib": "A disciplina exige justiça; a estrutura se constrói na relação e os limites são equilibrados.",
        "Sco": "A disciplina aprofunda o controlo; a estrutura é transformadora e os limites são intensos.",
        "Sag": "A disciplina foca a expansão; a estrutura vem da responsabilidade e os limites são filosóficos.",
        "Cap": "A disciplina é soberana; a estrutura é ambiciosa e os limites são a própria realização.",
        "Aqu": "A disciplina ordena a originalidade; a estrutura vem do coletivo e os limites são ideais.",
        "Pis": "A disciplina contém a dissolução; a estrutura é compassiva e os limites são espirituais.",
    },
    "uranus": {
        "Ari": "A mudança é abrupta e pioneira; a liberdade se conquista pela ação e a rebeldia é instintiva.",
        "Tau": "A mudança abala a estabilidade; a liberdade é material e a inovação chega de forma inesperada.",
        "Gem": "A mudança é mental e rápida; a liberdade é de ideias e a originalidade é comunicativa.",
        "Can": "A mudança é emocional e familiar; a liberdade é de pertencer e a inovação chega ao lar.",
        "Leo": "A mudança é criativa e dramática; a liberdade é de expressão e a originalidade é radiante.",
        "Vir": "A mudança é técnica e analítica; a liberdade é de método e a inovação é precisa.",
        "Lib": "A mudança é relacional e estética; a liberdade é de parcerias e a originalidade é harmónica.",
        "Sco": "A mudança é radical e profunda; a liberdade é de transformação e a rebeldia é magnética.",
        "Sag": "A mudança é expansiva e itinerante; a liberdade é filosófica e a originalidade é visionária.",
        "Cap": "A mudança é estrutural e ambiciosa; a liberdade é de realização e a inovação é disciplinada.",
        "Aqu": "A mudança é revolucionária e ideal; a liberdade é total e a originalidade é pura.",
        "Pis": "A mudança é mística e dissolutiva; a liberdade é de entrega e a inovação é inspirada.",
    },
    "neptune": {
        "Ari": "O sonho é pioneiro e heróico; a transcendência vem da ação idealizada e a imaginação é inflamada.",
        "Tau": "O sonho é sensual e pacífico; a transcendência vem da beleza material e a imaginação é terrosa.",
        "Gem": "O sonho é mental e difuso; a transcendência vem da ideia e a imaginação é verbal e nebulosa.",
        "Can": "O sonho é emocional e nostálgico; a transcendência vem da memória e a imaginação é protetora.",
        "Leo": "O sonho é criativo e glamoroso; a transcendência vem da expressão idealizada e a imaginação é radiante.",
        "Vir": "O sonho é depurativo e idealista; a transcendência vem do serviço e a imaginação é precisa e crítica.",
        "Lib": "O sonho é estético e romântico; a transcendência vem da harmonia e a imaginação é relacional.",
        "Sco": "O sonho é profundo e magnético; a transcendência vem da crise e a imaginação é intensa e oculta.",
        "Sag": "O sonho é místico e visionário; a transcendência vem da fé e a imaginação é filosófica.",
        "Cap": "O sonho é ambicioso e estruturado; a transcendência vem da realização e a imaginação é pragmática.",
        "Aqu": "O sonho é ideal e coletivo; a transcendência vem do futuro e a imaginação é inventiva.",
        "Pis": "O sonho é oceânico e universal; a transcendência é total e a imaginação se dissolve na unidade.",
    },
    "pluto": {
        "Ari": "A transformação é instintiva e pioneira; o poder se conquista pela ação e a regeneração é violenta.",
        "Tau": "A transformação é lenta e material; o poder se fixa nos valores e a regeneração é tenaz.",
        "Gem": "A transformação é mental e dispersa; o poder se manifesta pela palavra e a regeneração é ideológica.",
        "Can": "A transformação é emocional e familiar; o poder se exerce na linhagem e a regeneração é protetora.",
        "Leo": "A transformação é criativa e dramática; o poder se mostra no brilho e a regeneração é radiante.",
        "Vir": "A transformação é analítica e purificadora; o poder se manifesta no trabalho e a regeneração é depurativa.",
        "Lib": "A transformação é relacional e justa; o poder se equilibra nas parcerias e a regeneração é estética.",
        "Sco": "A transformação é total e intensa; o poder é magnético e a regeneração nasce da própria morte.",
        "Sag": "A transformação é filosófica e expansiva; o poder se manifesta pela verdade e a regeneração é visionária.",
        "Cap": "A transformação é estrutural e ambiciosa; o poder se consolida na autoridade e a regeneração é duradoura.",
        "Aqu": "A transformação é coletiva e revolucionária; o poder se difunde nas massas e a regeneração é ideal.",
        "Pis": "A transformação é mística e dissolutiva; o poder se exerce pela entrega e a regeneração é universal.",
    },
    "asc": {
        "Ari": "A persona é pioneira e direta; a primeira impressão é de coragem e energia.",
        "Tau": "A persona é serena e sensual; a primeira impressão é de estabilidade e calma.",
        "Gem": "A persona é curiosa e vivaz; a primeira impressão é de inteligência e movimento.",
        "Can": "A persona é acolhedora e tímida; a primeira impressão é de sensibilidade e proteção.",
        "Leo": "A persona é radiante e generosa; a primeira impressão é de calor e presença.",
        "Vir": "A persona é modesta e atenta; a primeira impressão é de discrição e cuidado.",
        "Lib": "A persona é encantadora e diplomática; a primeira impressão é de harmonia e elegância.",
        "Sco": "A persona é magnética e reservada; a primeira impressão é de intensidade e mistério.",
        "Sag": "A persona é entusiasta e franca; a primeira impressão é de otimismo e liberdade.",
        "Cap": "A persona é séria e contida; a primeira impressão é de competência e responsabilidade.",
        "Aqu": "A persona é original e distante; a primeira impressão é de independência e idealismo.",
        "Pis": "A persona é doce e etérea; a primeira impressão é de compaixão e mistério.",
    },
}

ASPECTS = {
    "conjunction": {
        "name": "Conjunção", "glyph": "☌", "angle": 0, "orb": 8,
        "harmony": "neutro",
        "description": (
            "Dois planetas muito próximos (0°, orbe 8°). As energias se "
            "fundem e se intensificam, agindo como uma só força. Pode ser "
            "construtiva ou disruptiva conforme a natureza dos planetas "
            "envolvidos."
        ),
    },
    "sextile": {
        "name": "Sextil", "glyph": "⚹", "angle": 60, "orb": 5,
        "harmony": "harmónico",
        "description": (
            "Sextil (60°, orbe 5°). Aspecto harmonioso de oportunidade e "
            "fluxo suave entre elementos compatíveis. Indica facilidade e "
            "potencial, mas requer esforço consciente para ser aproveitado."
        ),
    },
    "square": {
        "name": "Quadratura", "glyph": "□", "angle": 90, "orb": 6,
        "harmony": "tenso",
        "description": (
            "Quadratura (90°, orbe 6°). Aspecto tenso de conflito e "
            "fricção entre elementos incompatíveis. Gera desafio e crise, "
            "mas também motivação, força e crescimento por superação."
        ),
    },
    "trine": {
        "name": "Trígono", "glyph": "△", "angle": 120, "orb": 7,
        "harmony": "harmónico",
        "description": (
            "Trígono (120°, orbe 7°). Aspecto harmonioso de fluxo natural "
            "entre elementos do mesmo elemento. Indica talento, apoio e "
            "facilidade inata; pode, porém, gerar acomodação."
        ),
    },
    "opposition": {
        "name": "Oposição", "glyph": "☍", "angle": 180, "orb": 8,
        "harmony": "tenso",
        "description": (
            "Oposição (180°, orbe 8°). Aspecto tenso de polaridade entre "
            "forças opostas. Gera tensão e projeção, mas também "
            "consciência e a necessidade de integrar e equilibrar os "
            "opostos."
        ),
    },
}

KABBALAH = {
    "intro": (
        "A Cabala (Qabalah) é a tradição mística judaica que descreve a "
        "emanação do Divino em dez estágios — as <strong>10 sephiroth</strong> "
        "— ligadas por 22 caminhos correspondentes às 22 letras do alfabeto "
        "hebraico. O diagrama que as organiza é a <strong>Árvore da Vida</strong>, "
        "estruturada em três pilares: o da <em>Misericórdia</em> (direita, "
        "ativo/masculino), o da <em>Severidade</em> (esquerda, passivo/feminino) "
        "e o do <em>Equilíbrio</em> (central, reconciliador). A energia flui de "
        "Kether (Coroa, o ápice) até Malkuth (Reino, a manifestação material). "
        "Existe ainda uma sephirah oculta, <em>Da'ath</em> (Conhecimento), o "
        "abismo que separa o supernal do inferior. A Aurora Dourada atribuiu "
        "cada planeta a uma sephirah, base do método astrológico-cabalístico "
        "desta aplicação."
    ),
    "sephiroth": {
        "Kether": {
            "hebrew": "כתר", "title": "Coroa", "planet": "Netuno",
            "pillar": "Equilíbrio",
            "description": (
                "A primeira emanação: o Ponto primordial, a Vontade pura e a "
                "unidade indivisa. É a fonte de toda manifestação, o divino "
                "antes de qualquer forma. Cor resplandecente."
            ),
        },
        "Chockmah": {
            "hebrew": "חכמה", "title": "Sabedoria", "planet": "Urano",
            "pillar": "Misericórdia",
            "description": (
                "O princípio ativo e masculino, a Força dinâmica e criadora, o "
                "Pai. Energia pura em movimento, originação e impulso "
                "abstrato antes da forma."
            ),
        },
        "Binah": {
            "hebrew": "בינה", "title": "Entendimento", "planet": "Saturno",
            "pillar": "Severidade",
            "description": (
                "O princípio passivo e feminino, a Forma, a Mãe. Compreensão "
                "que dá contorno à força de Chockmah, estrutura, limitação e "
                "tempo. O grande mar primordial."
            ),
        },
        "Daath": {
            "hebrew": "דעת", "title": "Conhecimento", "planet": "Plutão",
            "pillar": "Equilíbrio (oculta)",
            "description": (
                "A sephirah oculta, o Abismo entre o supernal e o inferior. "
                "É o Conhecimento que une e separa, a ponte da transformação: "
                "atravessá-lo é morrer para o ego e renascer. Não conta nas "
                "10 sephiroth clássicas."
            ),
        },
        "Chesed": {
            "hebrew": "חסד", "title": "Misericórdia", "planet": "Júpiter",
            "pillar": "Misericórdia",
            "description": (
                "A expansão, a abundância, o amor construtor e a "
                "misericórdia. Autoridade benévola que organiza e edifica, "
                "dando sustentação e crescimento."
            ),
        },
        "Geburah": {
            "hebrew": "גבורה", "title": "Severidade", "planet": "Marte",
            "pillar": "Severidade",
            "description": (
                "A força, a severidade, o julgamento e a destruição que "
                "limpa. Disciplina e coragem que cortam o supérfluo para "
                "restaurar o equilíbrio. O guerreiro da Árvore."
            ),
        },
        "Tiferet": {
            "hebrew": "תפארת", "title": "Beleza", "planet": "Sol",
            "pillar": "Equilíbrio",
            "description": (
                "O Coração da Árvore, o reconciliador entre a força e a "
                "forma. Beleza, harmonia e o Eu central, o Deus "
                "sacrificado que une o céu e a terra. Centro da "
                "consciência."
            ),
        },
        "Netzach": {
            "hebrew": "נצח", "title": "Vitória", "planet": "Vénus",
            "pillar": "Misericórdia",
            "description": (
                "A vitória através da emoção, da natureza, do instinto e "
                "da arte. O sentimento, o desejo e a força vital que "
                "perpetua a vida. Beleza natural e paixão."
            ),
        },
        "Hod": {
            "hebrew": "הוד", "title": "Glória", "planet": "Mercúrio",
            "pillar": "Severidade",
            "description": (
                "A glória do intelecto, a forma, a razão e a comunicação. "
                "O pensamento que estrutura e nomeia; base da magia e da "
                "ciência. Ordem mental."
            ),
        },
        "Yesod": {
            "hebrew": "יסוד", "title": "Fundação", "planet": "Lua",
            "pillar": "Equilíbrio",
            "description": (
                "A fundação, o plano astral e o subconsciente. É a ponte "
                "entre o mundo das ideias e a manifestação física: sonhos, "
                "instintos e a imaginação que molda a realidade."
            ),
        },
        "Malkuth": {
            "hebrew": "מלכות", "title": "Reino", "planet": "Terra / Ascendente",
            "pillar": "Equilíbrio",
            "description": (
                "O Reino, o mundo físico e material, o corpo e a "
                "manifestação densa. É onde todas as emanações se "
                "concretizam. A matéria sagrada e o ponto de partida da "
                "subida de volta a Kether."
            ),
        },
    },
}

TAROT = {
    "intro": (
        "A <strong>Astrologia Hermética</strong> (método dos 24 signos) "
        "subdivide cada signo zodiacal em duas metades de 15° — primeira "
        "metade [0°,15°) e segunda metade [15°,30°] — regendo cada metade "
        "por uma <strong>carta de corte do Tarot</strong> (Rei, Rainha ou "
        "Príncipe) pertencente a um <strong>naipe</strong>. Os quatro naipes "
        "correspondem aos quatro elementos: <em>Bastões</em>=Fogo, "
        "<em>Moedas</em>=Terra, <em>Espadas</em>=Ar e <em>Taças</em>=Água. "
        "Os 24 setores resultantes formam o zodíaco hermético. Planetas "
        "situados em graus <strong>cuspiais</strong> (≤5° ou ≥25°) recebem "
        "um <strong>título hermético</strong> — a carta de corte que rege a "
        "metade em questão — e são destacados na roda."
    ),
    "suits": {
        "Bastões": {
            "element": "Fogo",
            "description": (
                "Naipe de Fogo: ação, vontade, paixão, criatividade e "
                "iniciativa. A energia que empreende e move."
            ),
        },
        "Moedas": {
            "element": "Terra",
            "description": (
                "Naipe de Terra (Pentáculos): matéria, recursos, trabalho, "
                "corpo e o prático. A energia que constrói e sustenta."
            ),
        },
        "Espadas": {
            "element": "Ar",
            "description": (
                "Naipe de Ar: intelecto, pensamento, comunicação, "
                "conflito e discernimento. A energia que corta e clarifica."
            ),
        },
        "Taças": {
            "element": "Água",
            "description": (
                "Naipe de Água (Copos): emoção, relacionamento, intuição "
                "e o coração. A energia que sente e une."
            ),
        },
    },
    "court_cards": {
        "Rei": (
            "Expressão madura e ativa (masculina) do elemento: domínio, "
            "autoridade e exteriorização. O Rei encarna o elemento no seu "
            "auge de controlo e comando."
        ),
        "Rainha": (
            "Expressão madura e receptiva (feminina) do elemento: "
            "interiorização, nutrimento e mestria acolhedora. A Rainha "
            "encarna o elemento na sua profundidade e sustentação."
        ),
        "Príncipe": (
            "Expressão jovem e em movimento (Cavaleiro) do elemento: "
            "deslocamento, busca e dinamismo. O Príncipe encarna o "
            "elemento em ação, ainda em formação."
        ),
    },
    "cuspal_rule": (
        "Graus ≤5° recebem o título da <em>primeira</em> metade do signo; "
        "graus ≥25° recebem o título da <em>segunda</em> metade. Entre 6° e "
        "24° não há título hermético."
    ),
    # Os 24 setores, em ordem zodiacal. Cada setor: signo, metade, título,
    # naipe e elemento.
    "sectors": [
        {"sign": "Ari", "half": "1ª metade [0°–15°)", "title": "Rainha de Bastões", "suit": "Bastões", "element": "Fogo"},
        {"sign": "Ari", "half": "2ª metade [15°–30°]", "title": "Principe de Moedas", "suit": "Moedas", "element": "Terra"},
        {"sign": "Tau", "half": "1ª metade [0°–15°)", "title": "Principe de Moedas", "suit": "Moedas", "element": "Terra"},
        {"sign": "Tau", "half": "2ª metade [15°–30°]", "title": "Rei de Espadas", "suit": "Espadas", "element": "Ar"},
        {"sign": "Gem", "half": "1ª metade [0°–15°)", "title": "Rei de Espadas", "suit": "Espadas", "element": "Ar"},
        {"sign": "Gem", "half": "2ª metade [15°–30°]", "title": "Rainha de Taças", "suit": "Taças", "element": "Água"},
        {"sign": "Can", "half": "1ª metade [0°–15°)", "title": "Rainha de Taças", "suit": "Taças", "element": "Água"},
        {"sign": "Can", "half": "2ª metade [15°–30°]", "title": "Príncipe de Bastões", "suit": "Bastões", "element": "Fogo"},
        {"sign": "Leo", "half": "1ª metade [0°–15°)", "title": "Príncipe de Bastões", "suit": "Bastões", "element": "Fogo"},
        {"sign": "Leo", "half": "2ª metade [15°–30°]", "title": "Rei de Moedas", "suit": "Moedas", "element": "Terra"},
        {"sign": "Vir", "half": "1ª metade [0°–15°)", "title": "Rei de Moedas", "suit": "Moedas", "element": "Terra"},
        {"sign": "Vir", "half": "2ª metade [15°–30°]", "title": "Rainha de Espadas", "suit": "Espadas", "element": "Ar"},
        {"sign": "Lib", "half": "1ª metade [0°–15°)", "title": "Rainha de Espadas", "suit": "Espadas", "element": "Ar"},
        {"sign": "Lib", "half": "2ª metade [15°–30°]", "title": "Príncipe de Taças", "suit": "Taças", "element": "Água"},
        {"sign": "Sco", "half": "1ª metade [0°–15°)", "title": "Príncipe de Taças", "suit": "Taças", "element": "Água"},
        {"sign": "Sco", "half": "2ª metade [15°–30°]", "title": "Rei de Bastões", "suit": "Bastões", "element": "Fogo"},
        {"sign": "Sag", "half": "1ª metade [0°–15°)", "title": "Rei de Bastões", "suit": "Bastões", "element": "Fogo"},
        {"sign": "Sag", "half": "2ª metade [15°–30°]", "title": "Rainha de Moedas", "suit": "Moedas", "element": "Terra"},
        {"sign": "Cap", "half": "1ª metade [0°–15°)", "title": "Rainha de Moedas", "suit": "Moedas", "element": "Terra"},
        {"sign": "Cap", "half": "2ª metade [15°–30°]", "title": "Príncipe de Espadas", "suit": "Espadas", "element": "Ar"},
        {"sign": "Aqu", "half": "1ª metade [0°–15°)", "title": "Príncipe de Espadas", "suit": "Espadas", "element": "Ar"},
        {"sign": "Aqu", "half": "2ª metade [15°–30°]", "title": "Rei de Taças", "suit": "Taças", "element": "Água"},
        {"sign": "Pis", "half": "1ª metade [0°–15°)", "title": "Rei de Taças", "suit": "Taças", "element": "Água"},
        {"sign": "Pis", "half": "2ª metade [15°–30°]", "title": "Rainha de Bastões", "suit": "Bastões", "element": "Fogo"},
    ],
}

# 72 Anjos do Shem HaMephorash: signo, bin (0–5), intervalo de 5°, virtude
# (palavra-chave) e descrição (uma frase). Alinha com app/angels.py.
ANGELS = [
    {"angel": "Vehuiah", "sign": "Ari", "bin": 0, "degrees": "0°–5°", "virtue": "Força de vontade, novos começos", "description": "Dá força de vontade e iniciativa para empreender novos começos."},
    {"angel": "Jeliel", "sign": "Ari", "bin": 1, "degrees": "5°–10°", "virtue": "Amor e fidelidade", "description": "Inspira amor fiel e a capacidade de atrair e reter o afeto."},
    {"angel": "Sitael", "sign": "Ari", "bin": 2, "degrees": "10°–15°", "virtue": "Proteção contra a adversidade", "description": "Protege contra infortúnios, acidentes e armas; favorece a construção."},
    {"angel": "Elemiah", "sign": "Ari", "bin": 3, "degrees": "15°–20°", "virtue": "Proteção nas viagens", "description": "Protege nas viagens e descobre os traidores; ajuda a superar adversidades."},
    {"angel": "Mahasiah", "sign": "Ari", "bin": 4, "degrees": "20°–25°", "virtue": "Reconciliação e paz", "description": "Favorece a reconciliação, a paz interior e a facilidade de aprender."},
    {"angel": "Lelahel", "sign": "Ari", "bin": 5, "degrees": "25°–30°", "virtue": "Cura, luz e fama", "description": "Traz cura, fama legítima e renovação pela luz solar."},
    {"angel": "Achaiah", "sign": "Tau", "bin": 0, "degrees": "0°–5°", "virtue": "Paciência e descoberta", "description": "Inspira paciência e a descoberta dos segredos da natureza."},
    {"angel": "Cahethel", "sign": "Tau", "bin": 1, "degrees": "5°–10°", "virtue": "Bênção das colheitas, devoção", "description": "Abençoa as colheitas e eleva a devoção; afasta os espíritos maus."},
    {"angel": "Haziel", "sign": "Tau", "bin": 2, "degrees": "10°–15°", "virtue": "Misericórdia e perdão", "description": "Concede misericórdia, perdão e a amizade dos grandes."},
    {"angel": "Aladiah", "sign": "Tau", "bin": 3, "degrees": "15°–20°", "virtue": "Cura e graça", "description": "Cura doenças e favorece a graça diante da justiça e do perdão."},
    {"angel": "Laoviah", "sign": "Tau", "bin": 4, "degrees": "20°–25°", "virtue": "Proteção contra a ruína", "description": "Protege contra incêndios e ruínas; traz vitória e reputação."},
    {"angel": "Hahahiah", "sign": "Tau", "bin": 5, "degrees": "25°–30°", "virtue": "Sabedoria, objetos perdidos", "description": "Concede sabedoria e ajuda a encontrar objetos perdidos."},
    {"angel": "Yesalel", "sign": "Gem", "bin": 0, "degrees": "0°–5°", "virtue": "Fidelidade e memória", "description": "Favorece a fidelidade e a memória; protege contra a calúnia."},
    {"angel": "Mebahel", "sign": "Gem", "bin": 1, "degrees": "5°–10°", "virtue": "Libertação e justiça", "description": "Liberta os oprimidos e sustenta a justiça contra a falsidade."},
    {"angel": "Hariel", "sign": "Gem", "bin": 2, "degrees": "10°–15°", "virtue": "Ciência e pureza", "description": "Inspira a ciência, a cura e a pureza de costumes."},
    {"angel": "Hekamiah", "sign": "Gem", "bin": 3, "degrees": "15°–20°", "virtue": "Lealdade e proteção", "description": "Protege contra as armas e favorece a lealdade e a coragem."},
    {"angel": "Lauviah", "sign": "Gem", "bin": 4, "degrees": "20°–25°", "virtue": "Sonhos e revelações", "description": "Concede sonhos proféticos e revelações durante o sono."},
    {"angel": "Caliel", "sign": "Gem", "bin": 5, "degrees": "25°–30°", "virtue": "Verdade e justiça", "description": "Revela a verdade nos processos e faz triunfar a causa dos inocentes."},
    {"angel": "Leuviah", "sign": "Can", "bin": 0, "degrees": "0°–5°", "virtue": "Graça e memória", "description": "Concede a graça das águas e a memória; suaviza as provações."},
    {"angel": "Pahaliah", "sign": "Can", "bin": 1, "degrees": "5°–10°", "virtue": "Conversão e despertar", "description": "Inspira a conversão e o despertar espiritual dos negligentes."},
    {"angel": "Nelchael", "sign": "Can", "bin": 2, "degrees": "10°–15°", "virtue": "Vitória sobre os caluniadores", "description": "Liberta dos caluniadores e dos adversários; favorece o estudo."},
    {"angel": "Ieiaiel", "sign": "Can", "bin": 3, "degrees": "15°–20°", "virtue": "Reputação e prosperidade", "description": "Traz fama, prosperidade e o reconhecimento por boas ações."},
    {"angel": "Melahel", "sign": "Can", "bin": 4, "degrees": "20°–25°", "virtue": "Cura e viagem segura", "description": "Cura doenças e protege nas viagens pelas águas e pelas terras."},
    {"angel": "Haheuiah", "sign": "Can", "bin": 5, "degrees": "25°–30°", "virtue": "Proteção contra malfeitores", "description": "Protege contra os malfeitores e os animais ferozes; guarda os fugitivos."},
    {"angel": "Nith-Haiah", "sign": "Leo", "bin": 0, "degrees": "0°–5°", "virtue": "Sabedoria e magia", "description": "Concede sabedoria e o dom da magia e das ciências ocultas."},
    {"angel": "Haaiah", "sign": "Leo", "bin": 1, "degrees": "5°–10°", "virtue": "Sabedoria e diplomacia", "description": "Inspira a sabedoria e o sucesso nas negociações e nas missões."},
    {"angel": "Ierathel", "sign": "Leo", "bin": 2, "degrees": "10°–15°", "virtue": "Libertação e paz", "description": "Liberta da opressão e confunde os maus; traz paz e iluminação."},
    {"angel": "Seheiah", "sign": "Leo", "bin": 3, "degrees": "15°–20°", "virtue": "Vida longa e proteção", "description": "Concede longa vida e protege contra incêndios e epidemias."},
    {"angel": "Reyel", "sign": "Leo", "bin": 4, "degrees": "20°–25°", "virtue": "Cura e visão", "description": "Cura e afasta os espíritos maus; inspira a visão e a contemplação."},
    {"angel": "Omael", "sign": "Leo", "bin": 5, "degrees": "25°–30°", "virtue": "Paciência e fecundidade", "description": "Inspira a paciência e a multiplicação dos seres; une as almas gêmeas."},
    {"angel": "Lecabel", "sign": "Vir", "bin": 0, "degrees": "0°–5°", "virtue": "Luz e conhecimento", "description": "Concede luz e conhecimento; favorece a abundância nas colheitas."},
    {"angel": "Vasahiah", "sign": "Vir", "bin": 1, "degrees": "5°–10°", "virtue": "Justiça e fortuna", "description": "Favorece a justiça, a fortuna e a benevolência dos magistrados."},
    {"angel": "Iehuiah", "sign": "Vir", "bin": 2, "degrees": "10°–15°", "virtue": "Obediência e proteção", "description": "Protege os juízes e inspira a obediência e a fidelidade."},
    {"angel": "Lehaiah", "sign": "Vir", "bin": 3, "degrees": "15°–20°", "virtue": "Paciência e leitura", "description": "Concede paciência e o gosto pela leitura; favorece a fortuna."},
    {"angel": "Chavakiah", "sign": "Vir", "bin": 4, "degrees": "20°–25°", "virtue": "Reconciliação familiar", "description": "Restabelece a paz nas famílias e favorece a reconciliação e o testamento."},
    {"angel": "Menadel", "sign": "Vir", "bin": 5, "degrees": "25°–30°", "virtue": "Libertação e reencontro", "description": "Liberta do cativeiro e faz encontrar os ausentes e os objetos perdidos."},
    {"angel": "Aniel", "sign": "Lib", "bin": 0, "degrees": "0°–5°", "virtue": "Sabedoria e vitória", "description": "Concede sabedoria e a vitória; inspira a ciência e a filosofia."},
    {"angel": "Haamiah", "sign": "Lib", "bin": 1, "degrees": "5°–10°", "virtue": "Proteção dos ritos e verdade", "description": "Protege os rituais e a busca da verdade; favorece os cultos divinos."},
    {"angel": "Rehael", "sign": "Lib", "bin": 2, "degrees": "10°–15°", "virtue": "Cura e longevidade", "description": "Cura as doenças e concede longa vida; restaura a saúde dos pais."},
    {"angel": "Ieiazel", "sign": "Lib", "bin": 3, "degrees": "15°–20°", "virtue": "Libertação e amizade", "description": "Liberta os prisioneiros e inspira a impressão e a amizade dos sábios."},
    {"angel": "Hahahel", "sign": "Lib", "bin": 4, "degrees": "20°–25°", "virtue": "Vocação e missão", "description": "Inspira a vocação religiosa e protege os missionários contra os inimigos."},
    {"angel": "Mikael", "sign": "Lib", "bin": 5, "degrees": "25°–30°", "virtue": "Ordem e justiça", "description": "Estabelece a ordem e a justiça; confunde os falsos testemunhos."},
    {"angel": "Veuliah", "sign": "Sco", "bin": 0, "degrees": "0°–5°", "virtue": "Prosperidade e libertação", "description": "Concede prosperidade e liberta dos inimigos; favorece as empresas."},
    {"angel": "Yelaiah", "sign": "Sco", "bin": 1, "degrees": "5°–10°", "virtue": "Vitória no combate", "description": "Concede a vitória nos combates e a fama nas empresas arriscadas."},
    {"angel": "Sealiah", "sign": "Sco", "bin": 2, "degrees": "10°–15°", "virtue": "Despertar e prosperidade", "description": "Desperta os negligentes e favorece a prosperidade dos que buscam a luz."},
    {"angel": "Ariel", "sign": "Sco", "bin": 3, "degrees": "15°–20°", "virtue": "Segredos e sonhos", "description": "Revela os segredos ocultos e inspira os sonhos proféticos."},
    {"angel": "Asaliah", "sign": "Sco", "bin": 4, "degrees": "20°–25°", "virtue": "Visão e contemplação", "description": "Concede a visão e a contemplação das coisas divinas."},
    {"angel": "Mihael", "sign": "Sco", "bin": 5, "degrees": "25°–30°", "virtue": "Paz, união e fidelidade", "description": "Favorece a paz conjugal, a fidelidade e a união das almas gêmeas."},
    {"angel": "Vehuel", "sign": "Sag", "bin": 0, "degrees": "0°–5°", "virtue": "Grandeza e consolação", "description": "Inspira a grandeza e a consolação dos aflitos; eleva os ânimos."},
    {"angel": "Daniel", "sign": "Sag", "bin": 1, "degrees": "5°–10°", "virtue": "Eloquência e misericórdia", "description": "Concede a eloquência e a misericórdia; favorece a justiça e os advogados."},
    {"angel": "Hahasiah", "sign": "Sag", "bin": 2, "degrees": "10°–15°", "virtue": "Mistérios e alquimia", "description": "Revela os mistérios e as ciências ocultas; inspira a alquimia e a filosofia."},
    {"angel": "Imamiah", "sign": "Sag", "bin": 3, "degrees": "15°–20°", "virtue": "Libertação e força", "description": "Liberta dos inimigos e dá a força de suportar as provações."},
    {"angel": "Nanael", "sign": "Sag", "bin": 4, "degrees": "20°–25°", "virtue": "Ciências abstratas", "description": "Inspira as ciências abstratas e a meditação; favorece os mestres espirituais."},
    {"angel": "Nithael", "sign": "Sag", "bin": 5, "degrees": "25°–30°", "virtue": "Imortalidade e soberania", "description": "Concede a longevidade e o sucesso dos soberanos; protege contra a morte súbita."},
    {"angel": "Mebaiah", "sign": "Cap", "bin": 0, "degrees": "0°–5°", "virtue": "Consolação e renascimento", "description": "Consola os aflitos e favorece o renascimento e a continuidade das obras."},
    {"angel": "Poiel", "sign": "Cap", "bin": 1, "degrees": "5°–10°", "virtue": "Realização dos desejos", "description": "Concede a realização dos desejos e a fortuna; cura as doenças."},
    {"angel": "Nemamiah", "sign": "Cap", "bin": 2, "degrees": "10°–15°", "virtue": "Prosperidade e elevação", "description": "Favorece a prosperidade e a elevação das grandes almas; protege os comandantes."},
    {"angel": "Ieialel", "sign": "Cap", "bin": 3, "degrees": "15°–20°", "virtue": "Honra e fortuna", "description": "Concede a honra e a fortuna; cura as doenças e afasta a tristeza."},
    {"angel": "Harahel", "sign": "Cap", "bin": 4, "degrees": "20°–25°", "virtue": "Tesouro e comércio", "description": "Protege os tesouros e o comércio; inspira a cura e o trabalho ordeiro."},
    {"angel": "Mitzrael", "sign": "Cap", "bin": 5, "degrees": "25°–30°", "virtue": "Cura e longevidade", "description": "Cura e prolonga a vida; favorece a obediência e a disciplina."},
    {"angel": "Umabel", "sign": "Aqu", "bin": 0, "degrees": "0°–5°", "virtue": "Amizade e astronomia", "description": "Inspira a amizade e o gosto pela astronomia e pelas ciências."},
    {"angel": "Iah-Hel", "sign": "Aqu", "bin": 1, "degrees": "5°–10°", "virtue": "Sabedoria e serenidade", "description": "Concede a sabedoria e a serenidade; favorece a paz e o recolhimento."},
    {"angel": "Anauel", "sign": "Aqu", "bin": 2, "degrees": "10°–15°", "virtue": "Comércio e prudência", "description": "Protege o comércio e inspira a prudência e a prosperidade nos negócios."},
    {"angel": "Mehiel", "sign": "Aqu", "bin": 3, "degrees": "15°–20°", "virtue": "Inspiração e amizade", "description": "Inspira os escritores e favorece a amizade dos sábios e dos homens célebres."},
    {"angel": "Damabiah", "sign": "Aqu", "bin": 4, "degrees": "20°–25°", "virtue": "Proteção contra as águas", "description": "Protege contra os naufrágios e os infortúnios ligados às águas."},
    {"angel": "Manakel", "sign": "Aqu", "bin": 5, "degrees": "25°–30°", "virtue": "Cura e calma da cólera", "description": "Cura e apazigua a cólera; favorece o sono e a serenidade."},
    {"angel": "Ayel", "sign": "Pis", "bin": 0, "degrees": "0°–5°", "virtue": "Vida longa e cura", "description": "Concede longa vida e a cura; favorece a transformação e a prosperidade."},
    {"angel": "Habuhiah", "sign": "Pis", "bin": 1, "degrees": "5°–10°", "virtue": "Cura e fecundidade", "description": "Cura e favorece a fecundidade e a prosperidade das colheitas."},
    {"angel": "Rochel", "sign": "Pis", "bin": 2, "degrees": "10°–15°", "virtue": "Reencontro e honra", "description": "Faz encontrar os objetos perdidos e as pessoas ausentes; concede honrarias."},
    {"angel": "Yabamiah", "sign": "Pis", "bin": 3, "degrees": "15°–20°", "virtue": "Alquimia e regeneração", "description": "Inspira a alquimia e a regeneração; protege contra as forças destrutivas."},
    {"angel": "Haiaiel", "sign": "Pis", "bin": 4, "degrees": "20°–25°", "virtue": "Vitória e paz", "description": "Concede a vitória e a paz; protege contra as armas e a calúnia."},
    {"angel": "Mumiah", "sign": "Pis", "bin": 5, "degrees": "25°–30°", "virtue": "Conclusão e ciência", "description": "Preside às operações misteriosas e conclui as obras; favorece a ciência."},
]

AGATHADAIMON = {
    "intro": (
        "O <strong>Agathadaimon</strong> (ou <em>Agathos Daimon</em>) é o "
        "“Bom Demónio” da tradição helenística e hermética — o espírito "
        "guardião pessoal, equivalente ao <em>nous</em> ou génio de cada "
        "indivíduo. Este método constrói o <strong>nome do anjo da "
        "guarda</strong> a partir de três letras hebraicas derivadas dos "
        "graus do <strong>Sol</strong>, da <strong>Lua</strong> e do "
        "<strong>Ascendente</strong>. Cada letra é atribuída segundo uma "
        "correspondência entre as 22 letras do alfabeto hebraico e os 360° "
        "do zodíaco. Uma quarta letra, o <strong>sufixo</strong>, é "
        "acrescentada: <em>El</em> para nascimentos diurnos (06h–18h) e "
        "<em>Iah</em> para nascimentos noturnos. As correspondências "
        "tradicionais de cada letra (género, forma e caráter) ajudam a "
        "interpretar a natureza do guardião."
    ),
    "suffixes": {
        "El": "Sufixo diurno (nascimento entre 06h e 18h). «El» é um dos nomes divinos hebraicos, suffix de força e claridade solar.",
        "Iah": "Sufixo noturno (nascimento fora das 06h–18h). «Iah» é a forma curta de Yahweh, suffix de mistério e receptividade lunar.",
    },
    "hebrew_letters": {
        "Aleph": "Andrógina; porém mais masculina do que feminina; espiritual; geralmente com asas; do tipo bem mais magro.",
        "Bet": "Masculino. Ativa e ligeira e colorida.",
        "Gimel": "Feminina; grisalha, bela porém mutável. Rosto e corpo bem mais arredondado.",
        "Daleth": "Feminina. Muito bela e atraente. Rosto e corpo bem mais arredondados.",
        "He": "Feminina. Fera, forte, fogosa.",
        "Vav": "Masculino. Forte e estável. Um pouco desajeitada e pesada.",
        "Zayin": "Masculino. Delgado e inteligente.",
        "Het": "Feminina. Cara arredondada. Sem muita expressão.",
        "Teth": "Feminina. Tendendo a forte e fogosa.",
        "Yod": "Feminina. Muito branca e um pouco delicada.",
        "Kaph": "Masculino. Grande e forte.",
        "Lamed": "Feminina. Bem proporcional.",
        "Mem": "Andrógina. Porém mais feminina do que masculina. Reflexiva, sonhadora.",
        "Nun": "Masculino. Um rosto quadrado mostrando determinação. Um pouco obscuro.",
        "Samekh": "Masculino. Rosto delgado e expressivo.",
        "Ayin": "Masculino. Um pouco mecânico.",
        "Peh": "Feminina. Fera, forte e dedicada.",
        "Tsadi": "Feminina. Pensativa e intelectual.",
        "Qoph": "Masculino. Face e corpo arredondados.",
        "Resh": "Masculino. Orgulhoso e dominante.",
        "Shin": "Andrógina. Porém mais masculino do que feminino. Fera, ativo.",
        "Tav": "Andrógina. Porém mais masculino do que feminino. Obscuro e pardo.",
    },
    "hebrew_unicode": {
        "Aleph": "א", "Bet": "ב", "Gimel": "ג", "Daleth": "ד", "He": "ה",
        "Vav": "ו", "Zayin": "ז", "Het": "ח", "Teth": "ט", "Yod": "י",
        "Kaph": "כ", "Lamed": "ל", "Mem": "מ", "Nun": "נ", "Samekh": "ס",
        "Ayin": "ע", "Peh": "פ", "Tsadi": "צ", "Qoph": "ק", "Resh": "ר",
        "Shin": "ש", "Tav": "ת", "El": "אֵל", "Iah": "יָהּ",
    },
}


def as_dict() -> dict:
    """Return the full glossary as a JSON-serialisable dict."""
    return {
        "planets": PLANETS,
        "signs": SIGNS,
        "combinations": COMBINATIONS,
        "aspects": ASPECTS,
        "kabbalah": KABBALAH,
        "tarot": TAROT,
        "angels": ANGELS,
        "agathadaimon": AGATHADAIMON,
    }
