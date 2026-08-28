"""Glossário esotérico — conteúdo explicativo servido ao frontend.

Fonte única de verdade para o glossário da aplicação. Cobertura:

- Planetas (11) + significado individual (luz, sombra, integração)
- Signos (12) + elemento, qualidade, regente (luz, sombra, integração)
- Combinações planeta+signo (11 × 12 = 132) — todas redigidas à parte
- Aspectos (5) com descrição estruturada (luz, sombra, integração)
- Combinações planeta+aspecto (11 × 5 = 55) — como cada planeta vive cada aspecto
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
        "light": (
            "Vontade clara e generosidade natural: a pessoa sabe quem é, "
            "irradia confiança sem precisar diminuir ninguém e cria com "
            "espontaneidade. O Sol em luz dá constância de propósito — a "
            "coragem de ocupar o próprio lugar e de iluminar também o "
            "caminho dos outros."
        ),
        "shadow": (
            "Vaidade, orgulho ferido e necessidade de ser o centro. O Sol "
            "em sombra busca aplauso para se sentir existir, confunde "
            "admiração com valor pessoal e trata críticas como ataques. "
            "Pode virar autoritarismo ou, no extremo oposto, esconder-se "
            "para não falhar em público."
        ),
        "integration": (
            "Separar o próprio valor do reconhecimento recebido: brilhar "
            "por ser, não por parecer. Praticar a generosidade que não "
            "cobra retorno e aceitar que críticas honestas são espelhos, "
            "não ameaças. O Sol integrado serve de farol em vez de querer "
            "ser o único astro do céu."
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
        "light": (
            "Empatia fina e memória afetiva: a pessoa percebe o que os "
            "outros sentem antes das palavras, acolhe sem julgamento e "
            "cuida com instinto certeiro. A Lua em luz dá fluxo emocional "
            "saudável — sentir, nomear e deixar a emoção passar."
        ),
        "shadow": (
            "Mudanças de humor que arrastam quem está perto, defensividade "
            "e apego ao passado. A Lua em sombra absorve emoções alheias "
            "como se fossem suas, guarda mágoas como recordações quentes e "
            "exige do outro a segurança que só o interior pode dar."
        ),
        "integration": (
            "Aprender a ser o próprio porto seguro: nomear o que sente "
            "antes de reagir, criar rituais de cuidado que não dependam de "
            "ninguém e deixar que o passado ensine sem comandar. A Lua "
            "integrada nutre sem se esvaziar."
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
        "light": (
            "Mente viva e elástica: aprende rápido, faz pontes entre "
            "pessoas e ideias, explica o complexo em palavras simples. "
            "Mercúrio em luz é o bom intermediário — ouve de verdade, "
            "pergunta com curiosidade e traduz mundos diferentes um para "
            "o outro."
        ),
        "shadow": (
            "Verborreia que atropela, sarcasmo, dispersão e racionalização "
            "de tudo — inclusive do que deveria ser sentido. Mercúrio em "
            "sombra escuta para responder, não para entender, e usa a "
            "inteligência como arma de defesa: o outro nunca é rápido ou "
            "lógico o suficiente."
        ),
        "integration": (
            "Devolver à mente a função de servir, não de comandar: "
            "praticar a escuta completa, admitir 'não sei' e escolher "
            "menos estímulos com mais profundidade. Mercúrio integrado "
            "fala para construir pontes, não muros."
        ),
    },
    "venus": {
        "name": "Vênus",
        "glyph": "♀",
        "title": "O Amor e os Valores",
        "description": (
            "Vênus rege o amor, a atração, o prazer, a beleza e o sistema "
            "de valores. Indica o que se aprecia, como se relaciona e de "
            "que forma se busca a harmonia e a afinidade. Governa a "
            "estética, o afeto e a sensualidade."
        ),
        "light": (
            "Capacidade rara de valorizar: a pessoa vê beleza no comum, "
            "demonstra afeto com gestos concretos e cria relações onde os "
            "dois lados ganham. Vênus em luz equilibra dar e receber, e "
            "transforma prazer em vínculo, não em consumo."
        ),
        "shadow": (
            "Agradar a qualquer custo, dependência afetiva e valor medido "
            "em aparência. Vênus em sombra evita conflito até se perder de "
            "si, confunde possessão com amor e usa o encanto como moeda de "
            "troca — a harmonia exterior esconde o desequilíbrio interior."
        ),
        "integration": (
            "Descobrir o que se valoriza quando ninguém está olhando: "
            "praticar o 'não' sem culpa, escolher vínculos por afinidade "
            "real e não por medo da perda. Vênus integrada ama da própria "
            "plenitude, não da carência."
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
        "light": (
            "Coragem de começar: a pessoa entra em campo primeiro, defende "
            "quem precisa de proteção e converte raiva em ação útil. "
            "Marte em luz é direto sem ser cruel, competitivo sem "
            "humilhar, e sabe esperar o momento de golpear."
        ),
        "shadow": (
            "Impulsividade, impaciência e agressividade que machuca — "
            "física ou verbalmente. Marte em sombra confunde velocidade "
            "com eficiência, vira raiva contra o mundo ou contra si, e "
            "cria inimigos onde poderia criar aliados."
        ),
        "integration": (
            "Dar à energia um alvo digno: exercício regular, projetos com "
            "prazo, assertividade treinada. Aprender a pausa entre o "
            "estímulo e a resposta — ali nasce a força de verdade. Marte "
            "integrado é o fogo que aquece, não o que queima."
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
        "light": (
            "Otimismo contagiante com raízes reais: a pessoa enxerga o "
            "quadro grande, abre portas para si e para os outros e crê "
            "que o esforço vale a pena. Júpiter em luz ensina e aprende "
            "ao mesmo tempo, e transforma sorte em gratidão."
        ),
        "shadow": (
            "Exagero, promessas gigantes e arrogância de quem se acha "
            "dono da verdade. Júpiter em sombra aposta alto para não "
            "sentir vazio, confunde quantidade com qualidade e faz sermões "
            "em vez de diálogos."
        ),
        "integration": (
            "Casar a visão com o chão: grandes sonhos em pequenos passos "
            "verificáveis, fé que se prova em ação, humildade de saber "
            "que o mapa nunca é o território. Júpiter integrado expande "
            "sem estourar os limites da realidade."
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
        "light": (
            "Mestria conquistada: a pessoa entrega no prazo, sustenta "
            "compromissos quando todos desistem e vira referência pelo "
            "que construiu tijolo a tijolo. Saturno em luz respeita o "
            "tempo — o próprio e o dos outros — e dá autoridade sem "
            "precisar de cargo."
        ),
        "shadow": (
            "Rigidez, pessimismo e autocrítica que paralisa. Saturno em "
            "sombra impõe a si o que impõe aos outros, confunde sofrimento "
            "com mérito e adia a vida 'para quando estiver pronto' — dia "
            "que nunca chega."
        ),
        "integration": (
            "Trocar punição por padrão: exigir excelência com gentileza, "
            "celebrar marcos intermediários e aceitar que limites são "
            "espinha dorsal, não jaula. Saturno integrado vira o "
            "arquiteto sereno da própria vida."
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
        "light": (
            "Genialidade prática: a pessoa vê soluções onde todos vêem "
            "muro, atualiza o que estava ultrapassado e defende a "
            "liberdade — a própria e a dos outros. Urano em luz rompe "
            "padrões porque enxerga além deles, não por rebeldia vazia."
        ),
        "shadow": (
            "Rebeldia automática, agitação sem direção e medo de "
            "compromisso. Urano em sombra rompe por romper, troca tudo "
            "toda hora para não se encontrar em nada e considera "
            "constância uma prisão."
        ),
        "integration": (
            "Escolher quais normas vale a pena quebrar: liberdade com "
            "raízes, inovação a serviço de algo duradouro. Permitir-se "
            "ser diferente sem precisar provar isso a cada instante. "
            "Urano integrado é o trovão que fertiliza a terra."
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
        "light": (
            "Compaixão sem fronteiras e imaginação que cria mundos: a "
            "pessoa sintoniza o invisível, inspira coletivos inteiros e "
            "vê o divino no cotidiano. Netuno em luz é o artista, o "
            "místico e o curador que dissolve separações com ternura."
        ),
        "shadow": (
            "Fuga, idealização e vítimismo. Netuno em sombra confunde "
            "sonho com realidade, bebe (literal ou figuradamente) para "
            "não sentir, salva os outros para não se olhar e transforma "
            "empatia em esponja que encharca."
        ),
        "integration": (
            "Ancorar a visão: práticas espirituais com disciplina, arte "
            "com técnica, compaixão com limites claros. Verificar os "
            "fatos antes de se apaixonar pela história. Netuno integrado "
            "é o oceano que sabe ser também praia."
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
        "light": (
            "Fênix em pessoa: a pessoa atravessa crises e sai mais "
            "inteira, enxerga o que está por trás das máscaras e usa o "
            "poder para regenerar — o próprio e o coletivo. Plutão em "
            "luz não teme o escuro porque conhece os tesouros dele."
        ),
        "shadow": (
            "Controle, manipulação e obsessão. Plutão em sombra testa "
            "lealdades, guarda segredos como armas e prefere destruir a "
            "perder o controle — o próprio medo de vulnerabilidade "
            "transforma-se em tirania."
        ),
        "integration": (
            "Render-se ao processo: deixar morrer o que já acabou, "
            "praticar a confiança radical, usar o poder de enxergar o "
            "oculto para curar e não para subjugar. Plutão integrado é o "
            "rio subterrâneo que irriga em vez de inundar."
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
        "light": (
            "Presença autêntica: a persona se tornou aliada, não "
            "prisioneira. A pessoa entra em salas com o corpo e a "
            "postura comunicando quem realmente é, inicia situações com "
            "naturalidade e sabe se apresentar sem se esconder."
        ),
        "shadow": (
            "Identidade confundida com personagem: vive-se para a imagem "
            "e não para o ser. O Ascendente em sombra vira armadura "
            "soldada no rosto — ninguém, nem a própria pessoa, sabe quem "
            "está por trás."
        ),
        "integration": (
            "Usar a máscara conscientemente: saber quando vestir e "
            "quando tirar, alinhar a aparência aos valores profundos e "
            "deixar a intimidade ver além do horizonte. O Ascendente "
            "integrado é a porta, não a casa."
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
        "light": (
            "Coragem de primeiro: a energia ariana entra onde ninguém "
            "entrou, decide com clareza em meio à confusão e inspira "
            "pela simplicidade do 'vamos fazer'. O melhor de Áries é a "
            "honestidade do fogo que nasce — sem segundas intenções."
        ),
        "shadow": (
            "Impulsividade que quebra, egocentrismo de quem confunde "
            "velocidade com importância e impaciência com quem pensa "
            "devagar. Áries em sombra começa tudo e termina quase nada, "
            "e trata hesitação alheia como covardia."
        ),
        "integration": (
            "Transformar impulso em direção: escolher batalhas que valem "
            "a vitória, ouvir até o fim antes de agir e celebrar também "
            "o passo dos outros. O fogo ariano integrado acende o "
            "caminho sem queimar quem caminha junto."
        ),
    },
    "Tau": {
        "name": "Touro", "glyph": "♉", "element": "Terra", "quality": "Fixo",
        "ruler": "Vênus",
        "description": (
            "Signo de Terra Fixo, regido por Vênus. Estabilidade, "
            "paciência, sensualidade e apego aos valores materiais. "
            "Representa a construção lenta e a fruição do que é sólido."
        ),
        "light": (
            "Rocha em que se apoia: a energia taurina sustenta projetos "
            "longos, produz beleza tangível e dá segurança a quem está "
            "por perto. O melhor de Touro é a paciência fértil — o tempo "
            "como aliado, o corpo como instrumento de prazer honesto."
        ),
        "shadow": (
            "Teimosia que vira muro, apego que confunde posse com amor e "
            "resistência automática a qualquer mudança, mesmo a que "
            "salva. Touro em sombra confunde conforto com vida e "
            "acumula por medo de faltar."
        ),
        "integration": (
            "Praticar o soltar: revisar o que já cumpriu sua função, "
            "arriscar o novo em pequenas doses e lembrar que segurança "
            "morre dentro de si, não no armário. A terra taurina "
            "integrada é jardim, não cofre."
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
        "light": (
            "Vivacidade mental que contagia: a energia geminiana conecta "
            "pessoas e ideias, aprende qualquer assunto com prazer e "
            "traz leveza aos pesados. O melhor de Gêmeos é a curiosidade "
            "sem preconceito — o mundo como pátio de escola infinita."
        ),
        "shadow": (
            "Dispersão que não conclui, fala que atropela e superficialidade "
            "que fere quando disfarça de piada. Gêmeos em sombra muda de "
            "tema para não sentir, e de pessoa para não se aprofundar."
        ),
        "integration": (
            "Dar profundidade à largura: concluir um projeto antes de "
            "abrir três, escolher onde a curiosidade vale investimento e "
            "usar a palavra para aproximar, não para seduzir e fugir. O "
            "ar geminiano integrado é vento que move moinhos, não "
            "ciclone."
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
        "light": (
            "Refúgio humano: a energia canceriana percebe a dor não "
            "dita, cria lares onde quer que esteja e protege com uma "
            "fidelidade que atravessa anos. O melhor de Câncer é a "
            "memória do coração — ninguém fica esquecido nem faminto "
            "por perto."
        ),
        "shadow": (
            "Mágoa guardada como herança, manipulação pela culpa e "
            "carapaça que impede o próprio abraço. Câncer em sombra "
            "protege tanto que sufoca, e recolhe-se ferido sem avisar "
            "o que doeu."
        ),
        "integration": (
            "Dizer a necessidade antes do silêncio: transformar mágoa "
            "em conversa, cuidar sem controlar e proteger também a si "
            "mesmo da própria maré. A água canceriana integrada é o "
            "portão do lar sempre aberto para quem respeita a casa."
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
        "light": (
            "Coração real: a energia leonina anima pelo simples prazer "
            "de ver o outro feliz, cria com paixão que inspira e "
            "defende os seus com nobreza. O melhor de Leão é a "
            "generosidade radiante — aplaude o brilho alheio sem se "
            "sentir diminuído."
        ),
        "shadow": (
            "Vaidade que exige palco, orgulho que não pede desculpas e "
            "drama quando falta admiração. Leão em sombra confunde ser "
            "amado com ser aplaudido, e some afeto quando o público "
            "olha para outro."
        ),
        "integration": (
            "Brilhar pelo fazer, não pelo aplauso: separar autoestima "
            "de plateia, usar a liderança para criar outros líderes e "
            "aceitar que o coração vale tanto no anonimato. O fogo "
            "leonino integrado é sol que ilumina sem cobrar sombra."
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
        "light": (
            "Santidade do detalhe: a energia virginiana enxerga o que "
            "todos deixam passar, melhora o que já era bom e serve "
            "com competência discreta. O melhor de Virgem é o cuidado "
            "como oração — o mundo funciona melhor porque alguém "
            "observou de perto."
        ),
        "shadow": (
            "Crítica que machuca, perfeccionismo que paralisia e "
            "ansiedade de controle disfarçada de organização. Virgem em "
            "sombra aponta o cisco no olho alheio e o mastro no próprio, "
            "e nunca se acha boa o suficiente."
        ),
        "integration": (
            "Trocar julgamento por serviço: oferecer correção só quando "
            "pedida, celebrar o 'bom o suficiente' e dirigir a precisão "
            "para dentro em forma de autocuidado, não de autocobrança. "
            "A terra virginiana integrada é oficina onde se conserta "
            "com afeto."
        ),
    },
    "Lib": {
        "name": "Libra", "glyph": "♎", "element": "Ar", "quality": "Cardinal",
        "ruler": "Vênus",
        "description": (
            "Signo de Ar Cardinal, regido por Vênus. Equilíbrio, "
            "harmonia, parceria e estética. Representa a relação com o "
            "outro e a busca da justiça e da beleza."
        ),
        "light": (
            "Diplomacia que transforma: a energia libriana ouve todos os "
            "lados, costura acordos onde havia guerra e traz beleza e "
            "justiça aos espaços. O melhor de Libra é o senso de "
            "equidade — a balança pesa o direito do outro com o mesmo "
            "cuidado."
        ),
        "shadow": (
            "Indecisão que transfere o custo, conciliação que trai a si "
            "mesma e charme que evita o conflito necessário. Libra em "
            "sombra cede em silêncio, cobra em segredo e posterga a "
            "escolha até que ela se faça sozinha — pior."
        ),
        "integration": (
            "Se equilibrar como critério: nomear as próprias "
            "preferências antes de negociar, aceitar que desagradar "
            "faz parte da honestidade e decidir com prazos. O ar "
            "libriano integrado é a balança que se sustenta com o "
            "próprio peso."
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
        "light": (
            "Fidelidade absoluta ao real: a energia escorpiana não se "
            "contenta com máscaras, sustenta os outros nas piores horas "
            "e renasce de cada crise mais forte. O melhor de Escorpião "
            "é a lealdade profunda — quem prova de merecer, ganha uma "
            "fortaleza de afeto."
        ),
        "shadow": (
            "Ciúme que vigia, rancor que não expira e controle que "
            "testa quem ama. Escorpião em sombra prefere a dor de "
            "destruir à vulnerabilidade de confiar, e usa o que sabe "
            "do outro como arma."
        ),
        "integration": (
            "Escolher confiança como ato de coragem: falhar em voz alta, "
            "perdoar sem esquecer a lição e usar o poder de ver o oculto "
            "para proteger, não para ferir. A água escorpiana integrada "
            "é o poço que dá de beber sem exigir afogamento."
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
        "light": (
            "Flecha que aponta o alto: a energia sagitariana enxerga "
            "sentido onde há só rotina, ensina com entusiasmo "
            "contagiante e abre horizontes reais — geográficos e "
            "espirituais. O melhor de Sagitário é a fé otimista que "
            "move montanhas em passo de festa."
        ),
        "shadow": (
            "Franqueza que fere sem necessidade, promessas gigantes sem "
            "perna e dogmatismo do novo convertido. Sagitário em sombra "
            "confunde liberdade com impossibilidade de compromisso e "
            "sermão com sabedoria."
        ),
        "integration": (
            "Casar visão com verbo: pensar antes de falar 'é só "
            "franqueza', transformar horizonte em itinerário com datas "
            "e honrar compromissos como parte da liberdade. O fogo "
            "sagitário integrado é a flecha que escolhe o alvo antes "
            "de voar."
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
        "light": (
            "Mestria do tempo longo: a energia capricorniana assume o "
            "que ninguém quer, constrói em cima de pedra e entrega "
            "obras que atravessam gerações. O melhor de Capricórnio é a "
            "autoridade serena de quem venceu a própria montanha — e "
            "estende a mão a quem sobe."
        ),
        "shadow": (
            "Frieza que confunde controle com comando, vício de trabalho que "
            "adia a vida e desprezo pelo próprio descanso. Capricórnio "
            "em sombra mede o valor só pelo topo da montanha e chega "
            "lá sozinho, com o coração congelado."
        ),
        "integration": (
            "Reconhecer o preço: celebrar marcos com quem ajudou, "
            "agendar o prazer com a mesma disciplina do trabalho e "
            "aceitar vulnerabilidade como parte da autoridade. A terra "
            "capricorniana integrada é a montanha com fontes de água "
            "no caminho."
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
        "light": (
            "Visão a serviço do coletivo: a energia aquariana enxerga "
            "o futuro antes dos outros, acolhe os excluídos do padrão "
            "e transforma ideais em projetos concretos. O melhor de "
            "Aquário é a amizade sem hierarquia — ama a humanidade em "
            "cada indivíduo."
        ),
        "shadow": (
            "Distância emocional que machuca, contrariedade por "
            "princípio e fuga do íntimo para o abstrato. Aquário em "
            "sombra ama a humanidade de longe mas não sabe abraçar "
            "quem está perto, e usa a originalidade como muro."
        ),
        "integration": (
            "Descer do conceito para o abraço: praticar a presença "
            "afetiva com quem não concorda, aceitar que pertencer não "
            "escraviza e deixar o coração participar das decisões. O "
            "ar aquariano integrado é a rede que sustenta sem aprisionar."
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
        "light": (
            "Compaixão que dissolve fronteiras: a energia pisciana "
            "perdoa o imperdoável, cria beleza do invisível e acolhe "
            "os que não têm mais para onde ir. O melhor de Peixes é a "
            "entrega mística — a certeza silenciosa de que tudo está "
            "conectado."
        ),
        "shadow": (
            "Fuga da realidade, vitimismo que paralisa e absorção das "
            "doenças alheias como se fossem próprias. Peixes em sombra "
            "espera ser salvo em vez de nadar, e confunde sacrifício "
            "com amor."
        ),
        "integration": (
            "Ancorar a sensibilidade: limites claros como ato de "
            "amor, práticas que dão corpo ao sonho (arte, ritual, "
            "serviço) e discriminação entre ajuda e mártir. A água "
            "pisciana integrada é o rio que corre para o mar sem "
            "transbordar a margem."
        ),
    },
}

# 11 × 12 = 132 combinações. Cada texto tem cinco linhas de leitura prática.
# O planeta indica o tema; o signo descreve o comportamento observável desse tema.
_PLANET_COMBINATION_FOCUS = {
    "sun": "identidade, vitalidade e direção pessoal",
    "moon": "necessidades emocionais e reações automáticas",
    "mercury": "pensamento, fala e decisões",
    "venus": "afeto, prazer e critérios de escolha",
    "mars": "iniciativa, desejo e forma de defender interesses",
    "jupiter": "crescimento, confiança e busca de oportunidades",
    "saturn": "limites, responsabilidades e construção de resultados",
    "uranus": "liberdade, mudança e relação com regras",
    "neptune": "imaginação, sensibilidade e limites pessoais",
    "pluto": "poder, crises e processos de transformação",
    "asc": "primeira impressão, corpo e modo de começar",
}

_SIGN_COMBINATION_BEHAVIOURS = {
    "Ari": ("tomar a frente e decidir depressa", "ser direto e preferir movimento", "metas curtas com autonomia", "agir antes de ouvir tudo", "pausar antes de responder e dividir a iniciativa"),
    "Tau": ("manter o que funciona e avançar passo a passo", "demonstrar constância mais do que pressa", "ritmo previsível, recursos e tempo", "resistir a mudanças necessárias", "rever prioridades sem abandonar tudo de uma vez"),
    "Gem": ("buscar informação, comparar opções e conversar", "criar vínculo pelo diálogo e pela curiosidade", "variedade, trocas e tarefas curtas", "mudar de assunto ou perder o foco", "anotar decisões e concluir uma coisa por vez"),
    "Can": ("proteger pessoas próximas e lembrar do que viveu", "medir segurança antes de se abrir", "ambiente acolhedor e relações de confiança", "guardar mágoas ou reagir de forma defensiva", "dizer o que precisa antes de se fechar"),
    "Leo": ("assumir presença e colocar algo pessoal no que faz", "ser caloroso e esperar reconhecimento sincero", "visibilidade, autoria e espaço para criar", "levar críticas como rejeição pessoal", "separar valor próprio de aplauso imediato"),
    "Vir": ("observar detalhes e procurar como melhorar", "cuidar por meio de ajuda concreta", "rotina clara, método e utilidade", "corrigir demais ou adiar por perfeccionismo", "definir o suficiente e celebrar progresso"),
    "Lib": ("considerar todos os lados antes de escolher", "preservar acordo, respeito e boa convivência", "parcerias, negociação e critérios justos", "ceder demais ou postergar uma decisão", "nomear preferências e estabelecer limites"),
    "Sco": ("investigar o que está por trás das situações", "buscar lealdade, privacidade e profundidade", "autonomia sobre recursos e conversas francas", "testar pessoas ou tentar controlar o cenário", "confiar gradualmente e falar sem jogos"),
    "Sag": ("ampliar horizontes, estudar e experimentar", "valorizar franqueza, espaço e objetivos em comum", "aprendizado, viagens e desafios que crescem", "prometer demais ou ignorar detalhes", "transformar visão em etapas verificáveis"),
    "Cap": ("organizar objetivos e assumir o que precisa ser feito", "mostrar compromisso por responsabilidade", "metas mensuráveis, prazo e autoridade clara", "endurecer-se ou tratar descanso como falha", "medir progresso sem reduzir a vida ao resultado"),
    "Aqu": ("questionar padrões e buscar soluções diferentes", "aproximar-se por amizade, ideias e liberdade", "inovação, grupos e espaço para experimentar", "afastar-se quando a emoção pede presença", "explicar mudanças e manter acordos humanos"),
    "Pis": ("perceber clima, nuances e necessidades não ditas", "acolher, imaginar junto e evitar dureza", "tempo para criar, ajudar e recuperar energia", "absorver problemas alheios ou escapar da realidade", "confirmar fatos e proteger tempo, dinheiro e energia"),
}


def _combination_description(planet: str, sign: str) -> str:
    """Return a concrete five-line interpretation for one planet-sign pair."""
    daily, relationships, work, pressure, guidance = _SIGN_COMBINATION_BEHAVIOURS[sign]
    planet_name = PLANETS[planet]["name"]
    sign_name = SIGNS[sign]["name"]
    focus = _PLANET_COMBINATION_FOCUS[planet]
    lines_by_planet = {
        "sun": (
            f"Sol em {sign_name}: a identidade procura se realizar por {daily}.",
            f"A vitalidade cresce quando pode {daily}, sem depender da aprovação alheia.",
            f"Na convivência, a forma de ser reconhecido passa por {relationships}.",
            f"Em projetos, assume mais presença quando há {work}.",
            f"Se o ego se sente ameaçado, pode {pressure}; o caminho é {guidance}.",
        ),
        "moon": (
            f"Lua em {sign_name}: a sensação de segurança depende de {daily}.",
            f"O humor reage rápido ao ambiente e tende a {daily} para se proteger.",
            f"Nos vínculos íntimos, precisa de espaço para {relationships}.",
            f"A rotina emocional fica mais estável com {work}.",
            f"Quando se sente exposto, pode {pressure}; ajuda {guidance}.",
        ),
        "mercury": (
            f"Mercúrio em {sign_name}: a mente entende melhor o mundo ao {daily}.",
            f"Ao falar e decidir, tende a {daily}, dando este ritmo às conversas.",
            f"Em trocas com outras pessoas, comunica-se melhor ao {relationships}.",
            f"Aprendizado e trabalho mental fluem com {work}.",
            f"Sob excesso de informação, pode {pressure}; convém {guidance}.",
        ),
        "venus": (
            f"Vênus em {sign_name}: atração e prazer nascem de {daily}.",
            f"Escolhe pessoas, lugares e objetos que permitam {relationships}.",
            f"Demonstra afeto ao {relationships}, mais por atitudes do que por promessas.",
            f"Seus valores favorecem escolhas com {work}.",
            f"Quando falta reciprocidade, pode {pressure}; é útil {guidance}.",
        ),
        "mars": (
            f"Marte em {sign_name}: a iniciativa dispara quando é preciso {daily}.",
            f"Desejo, coragem e irritação seguem um estilo que tende a {daily}.",
            f"Em conflitos, defende seus interesses ao {relationships}.",
            f"Canaliza melhor energia física e ambição com {work}.",
            f"Se encontra resistência, pode {pressure}; força bem usada pede {guidance}.",
        ),
        "jupiter": (
            f"Júpiter em {sign_name}: confiança cresce ao {daily}.",
            f"Procura oportunidades que permitam {daily} e ampliem sua visão de mundo.",
            f"Generosidade e fé aparecem quando pode {relationships}.",
            f"Estudo, carreira e expansão rendem mais com {work}.",
            f"No entusiasmo, pode {pressure}; prospera ao {guidance}.",
        ),
        "saturn": (
            f"Saturno em {sign_name}: amadurecimento exige aprender a {daily} com constância.",
            f"Responsabilidades pesam mais quando precisa {daily}, mas também desenvolvem domínio.",
            f"Nos compromissos, leva a sério a necessidade de {relationships}.",
            f"Constrói resultados duradouros por meio de {work}.",
            f"Diante do medo de falhar, pode {pressure}; a disciplina saudável é {guidance}.",
        ),
        "uranus": (
            f"Urano em {sign_name}: liberdade pede novas formas de {daily}.",
            f"Quebra hábitos quando percebe que já não pode {daily} do seu jeito.",
            f"Nos grupos e vínculos, valoriza poder {relationships} sem roteiro rígido.",
            f"Inova melhor em contextos com {work}.",
            f"Se se sente controlado, pode {pressure}; a mudança funciona melhor ao {guidance}.",
        ),
        "neptune": (
            f"Netuno em {sign_name}: imaginação e empatia se ativam ao {daily}.",
            f"Percebe sinais sutis e pode idealizar situações que envolvam {daily}.",
            f"Nos afetos, busca uma conexão onde seja possível {relationships}.",
            f"Inspiração vira algo concreto quando há {work}.",
            f"Sem limites claros, pode {pressure}; protege-se ao {guidance}.",
        ),
        "pluto": (
            f"Plutão em {sign_name}: transformações profundas começam ao {daily}.",
            f"Há necessidade de entender o que está em jogo antes de {daily} por completo.",
            f"Nos vínculos, intensidade e confiança passam por {relationships}.",
            f"Exerce poder de regeneração em projetos que exigem {work}.",
            f"Quando teme perder controle, pode {pressure}; transforma a situação ao {guidance}.",
        ),
        "asc": (
            f"Ascendente em {sign_name}: a primeira impressão vem de {daily}.",
            f"O corpo e a postura comunicam uma tendência a {daily} antes mesmo das palavras.",
            f"Ao conhecer pessoas, aproxima-se ao {relationships}.",
            f"Começa tarefas e organiza a imagem pública melhor com {work}.",
            f"Em território novo, pode {pressure}; ganha presença ao {guidance}.",
        ),
    }
    return "\n".join(lines_by_planet[planet])


COMBINATIONS = {
    planet: {
        sign: _combination_description(planet, sign)
        for sign in SIGNS
    }
    for planet in PLANETS
}

# 11 × 10 × 5 = 550 combinações planeta+aspecto+planeta (pares ordenados,
# sem auto-par). Cada texto descreve como a função do planeta A vive o
# dinamismo do aspecto com o planeta B. Geradas por template a partir de:
#   - _PLANET_ASPECT_FUNCTIONS: função psíquica, desvio e dom de cada planeta
#   - _ASPECT_PAIR_DYNAMICS: dinâmica da relação por aspecto
_PLANET_ASPECT_FUNCTIONS = {
    "sun": {"func": "a identidade e a vontade de ser", "strain": "impor o próprio brilho", "gift": "a presença que inspira"},
    "moon": {"func": "as necessidades emocionais", "strain": "reagir defensivamente", "gift": "a sensibilidade que acolhe"},
    "mercury": {"func": "o pensamento e a comunicação", "strain": "racionalizar o que deveria sentir", "gift": "a mente que conecta"},
    "venus": {"func": "o afeto e os valores", "strain": "ceder para agradar", "gift": "o encanto que harmoniza"},
    "mars": {"func": "o desejo e a iniciativa", "strain": "agir por impulso", "gift": "a coragem que move"},
    "jupiter": {"func": "a expansão e a busca de sentido", "strain": "prometer além do possível", "gift": "a fé que abre portas"},
    "saturn": {"func": "a estrutura e o compromisso", "strain": "endurecer os limites", "gift": "a disciplina que sustenta"},
    "uranus": {"func": "a liberdade e a originalidade", "strain": "romper sem avisar", "gift": "a visão que renova"},
    "neptune": {"func": "a imaginação e a sensibilidade", "strain": "se perder na névoa", "gift": "a empatia que dissolve fronteiras"},
    "pluto": {"func": "a intensidade e o poder de transformar", "strain": "tentar controlar o cenário", "gift": "a profundidade que regenera"},
    "asc": {"func": "a presença e a primeira impressão", "strain": "esconder-se atrás da imagem", "gift": "a porta aberta para o mundo"},
}

_ASPECT_PAIR_DYNAMICS = {
    "conjunction": {
        "name": "conjunção",
        "open": "se fundem numa só força",
        "perspective": (
            "{a} expressa {fa} através de {fb}: as duas vozes soam juntas, "
            "e é isso que dá ao par sua marca registrada."
        ),
        "daily": (
            "No cotidiano, onde uma função aparece, a outra está logo ao "
            "lado — {fa} nunca falam sozinhas."
        ),
        "shadow": (
            "Sob pressão, uma função pode afogar a outra: há risco de "
            "{a_strain} ou de {b_strain} em nome da fusão."
        ),
        "integration": (
            "O caminho é dar a cada função seu momento de brilho: "
            "{a_gift} e {b_gift} se reforçam quando as duas vozes são "
            "ouvidas."
        ),
    },
    "sextile": {
        "name": "sextil",
        "open": "dialogam com fluidez e criam oportunidades",
        "perspective": (
            "{a} encontra em {fb} apoio leve e receptivo: portas se abrem "
            "sempre que {fa} tomam a iniciativa de tocá-las."
        ),
        "daily": (
            "No cotidiano, convites, contatos e ideias conectam as duas "
            "funções na hora certa — basta aceitar."
        ),
        "shadow": (
            "O risco é a porta aberta e ninguém entrando: pode vir "
            "{a_strain} por comodidade ou o potencial ficar em 'um dia eu'."
        ),
        "integration": (
            "O caminho é transformar oportunidade em projeto: {a_gift} e "
            "{b_gift} rendem quando há escolha consciente."
        ),
    },
    "square": {
        "name": "quadratura",
        "open": "puxam em direções que se atritam",
        "perspective": (
            "Quando {fa} tentam avançar, esbarram no contrapeso de {fb} — "
            "a fricção é desconfortável, mas gera energia de crescimento."
        ),
        "daily": (
            "No cotidiano, os mesmos conflitos voltam em cenários "
            "diferentes: as duas funções disputam espaço e nenhuma "
            "desiste."
        ),
        "shadow": (
            "Sob pressão, uma função bloqueia a outra em loop: há risco de "
            "{a_strain} ou de culpar {b} pelo impasse."
        ),
        "integration": (
            "O caminho é transformar fricção em músculo: {a_gift} e "
            "{b_gift} convivem quando as duas funções ganham método e vez."
        ),
    },
    "trine": {
        "name": "trígono",
        "open": "fluem juntas com naturalidade",
        "perspective": (
            "{a} encontra em {fb} a mesma língua: as duas funções cooperam "
            "sem esforço, e o talento parece inato."
        ),
        "daily": (
            "No cotidiano, tudo desliza — {fa} e {fb} se apoiam com tanta "
            "facilidade que a pessoa pode nem notar o dom."
        ),
        "shadow": (
            "O risco é a acomodação dourada: há chance de {a_strain} por "
            "falta de desafio ou de deixar o talento adormecido."
        ),
        "integration": (
            "O caminho é investir no dom com disciplina: {a_gift} e "
            "{b_gift} viram mestria quando a vontade cobra o que a sorte "
            "não cobra."
        ),
    },
    "opposition": {
        "name": "oposição",
        "open": "formam um eixo de polaridades a equilibrar",
        "perspective": (
            "{a} vive um polo e encontra o outro fora de si: {fb} aparecem "
            "com força justamente nas pessoas e situações que provocam."
        ),
        "daily": (
            "No cotidiano, o pêndulo alterna — ora {fa} mandam, ora {fb} "
            "cobram, e o ponto médio parece sempre adiável."
        ),
        "shadow": (
            "Sob pressão, projeta no outro o que pertence a si: há risco "
            "de {a_strain} ou de exigir de {b} o que só a integração dá."
        ),
        "integration": (
            "O caminho é reconhecer os dois polos como partes de si: "
            "{a_gift} e {b_gift} se completam quando a alternância vira "
            "consciência."
        ),
    },
}


def _aspect_pair_description(aspect: str, a: str, b: str) -> str:
    """Return the five-line reading of planet A in aspect with planet B."""
    dyn = _ASPECT_PAIR_DYNAMICS[aspect]
    fa = _PLANET_ASPECT_FUNCTIONS[a]
    fb = _PLANET_ASPECT_FUNCTIONS[b]
    a_name, b_name = PLANETS[a]["name"], PLANETS[b]["name"]
    return "\n".join([
        f"{a_name} em {dyn['name']} com {b_name}: {fa['func']} e {fb['func']} {dyn['open']}.",
        dyn["perspective"].format(a=a_name, fa=fa["func"], fb=fb["func"]),
        dyn["daily"].format(fa=fa["func"], fb=fb["func"]),
        dyn["shadow"].format(a_strain=fa["strain"], b_strain=fb["strain"], b=b_name),
        dyn["integration"].format(a_gift=fa["gift"], b_gift=fb["gift"]),
    ])


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
        "light": (
            "Fusão poderosa: os dois planetas funcionam como um só, "
            "concentrando a energia num único ponto de foco. Quando os "
            "princípios envolvidos colaboram, a conjunção dá "
            "espontaneidade, força de realização e um talento evidente — "
            "a pessoa nem percebe que aquilo é especial, tão natural lhe "
            "parece."
        ),
        "shadow": (
            "Fusão cega: quando os princípios se contradizem, a "
            "conjunção vira pressão constante — um planeta afoga o outro "
            "e nenhum se expressa limpo. A pessoa não consegue separar "
            "as duas funções da vida e reage às duas ao mesmo tempo."
        ),
        "integration": (
            "Conhecer o par: identificar qual planeta fala primeiro e "
            "dar a cada função seu momento de brilho. A conjunção "
            "integrada é um casamento bem-sucedido — identidade comum "
            "sem perder as vozes individuais."
        ),
    },
    "sextile": {
        "name": "Sextil", "glyph": "⚹", "angle": 60, "orb": 5,
        "harmony": "harmônico",
        "description": (
            "Sextil (60°, orbe 5°). Aspecto harmonioso de oportunidade e "
            "fluxo suave entre elementos compatíveis. Indica facilidade e "
            "potencial, mas requer esforço consciente para ser aproveitado."
        ),
        "light": (
            "Porta entreaberta: o sextil liga elementos que se "
            "compreendem (Fogo–Ar ou Terra–Água) e cria oportunidades "
            "que aparecem com naturalidade — convites, contatos, ideias "
            "que chegam na hora certa. É o aspecto da comunicação "
            "frutífera e do talento social."
        ),
        "shadow": (
            "Oportunidade desperdiçada: por ser suave, o sextil não "
            "cobra nada — e a pessoa pode atravessar a vida inteira com "
            "as portas abertas sem nunca entrar. O potencial fica em "
            "'um dia eu...'."
        ),
        "integration": (
            "Tratar o sextil como trampolim, não como poltrona: dizer "
            "sim aos convites que ele traz e transformar cada "
            "oportunidade em projeto concreto. O sextil integrado é o "
            "networking que vira amizade e obra."
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
        "light": (
            "Motor de crescimento: a fricção da quadratura gera energia "
            "que não deixa a pessoa parar. Quem trabalha a quadratura "
            "constrói músculo psicológico — resolve problemas que "
            "outros fogem, cria estruturas novas sob pressão e alcança "
            "maturidade antes dos pares. Grande parte das biografias "
            "notáveis é sustentada por quadraturas bem usadas."
        ),
        "shadow": (
            "Ciclo de crise: as duas funções se bloqueiam "
            "alternadamente — ora uma vence à força, ora a outra "
            "sabota. A pessoa vive os mesmos conflitos repetidos com "
            "pessoas e cenários diferentes, sempre com a sensação de "
            "bater de frente com o mundo."
        ),
        "integration": (
            "Nomear o padrão para sair do loop: as duas funções têm "
            "direito de existir, mas não ao mesmo tempo e do mesmo "
            "jeito. A quadratura integrada é o atleta que transforma "
            "resistência em força — o peso do halter é o que "
            "constrói o músculo."
        ),
    },
    "trine": {
        "name": "Trígono", "glyph": "△", "angle": 120, "orb": 7,
        "harmony": "harmônico",
        "description": (
            "Trígono (120°, orbe 7°). Aspecto harmonioso de fluxo natural "
            "entre elementos do mesmo elemento. Indica talento, apoio e "
            "facilidade inata; pode, porém, gerar acomodação."
        ),
        "light": (
            "Dom flui: os dois planetas falam a mesma língua "
            "(mesmo elemento) e cooperam sem esforço — é o talento que "
            "parece inato, a sorte que acompanha, a facilidade que "
            "outros invejam. O trígono dá regeneração e um caminho onde "
            "tudo desliza."
        ),
        "shadow": (
            "Acomodação dourada: como nada exige esforço, nada é "
            "desenvolvido até a mestria. O talento vira potencial "
            "adormecido, e a pessoa pode chegar aos 40 sem ter "
            "transformado o dom em obra — afinal, nunca precisou lutar "
            "por ele."
        ),
        "integration": (
            "Escolher conscientemente onde investir o dom: o trígono "
            "não cobra, então quem cobra é a própria vontade. "
            "Disciplina aplicada ao talento natural é a diferença "
            "entre o 'era bom nisso' e o 'foi mestre nisso'."
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
        "light": (
            "Consciência pela polaridade: a oposição é um pêndulo que "
            "ensina os dois extremos. Quem a integra torna-se "
            "mediador nato — conhece os dois lados de dentro, alterna "
            "com consciência e ensina outros a equilibrar. É o aspecto "
            "do diálogo e do amadurecimento relacional."
        ),
        "shadow": (
            "Projeção e vaivém: a pessoa vive um dos polos e encontra "
            "o outro 'fora' — em parceiros que encarnam justamente o "
            "que se recusa a ver. Alternam-se períodos de excesso de um "
            "lado e depois do outro, sem nunca o ponto de equilíbrio."
        ),
        "integration": (
            "Recolher a projeção: reconhecer no outro o próprio polo "
            "rejeitado e praticar a alternância consciente — ser os "
            "dois, em doses medidas. A oposição integrada é a "
            "culminação: o pleno dia da lua cheia, quando opostos se "
            "olham e se reconhecem."
        ),
    },
}

ASPECT_COMBINATIONS = {
    aspect: {
        pa: {
            pb: _aspect_pair_description(aspect, pa, pb)
            for pb in PLANETS if pb != pa
        }
        for pa in PLANETS
    }
    for aspect in ASPECTS
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
            "hebrew": "נצח", "title": "Vitória", "planet": "Vênus",
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
            "auge de controle e comando."
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
        {"sign": "Ari", "half": "2ª metade [15°–30°]", "title": "Príncipe de Moedas", "suit": "Moedas", "element": "Terra"},
        {"sign": "Tau", "half": "1ª metade [0°–15°)", "title": "Príncipe de Moedas", "suit": "Moedas", "element": "Terra"},
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
        "“Bom Demônio” da tradição helenística e hermética — o espírito "
        "guardião pessoal, equivalente ao <em>nous</em> ou gênio de cada "
        "indivíduo. Este método constrói o <strong>nome do anjo da "
        "guarda</strong> a partir de três letras hebraicas derivadas dos "
        "graus do <strong>Sol</strong>, da <strong>Lua</strong> e do "
        "<strong>Ascendente</strong>. Cada letra é atribuída segundo uma "
        "correspondência entre as 22 letras do alfabeto hebraico e os 360° "
        "do zodíaco. Uma quarta letra, o <strong>sufixo</strong>, é "
        "acrescentada: <em>El</em> para nascimentos diurnos (06h–18h) e "
        "<em>Iah</em> para nascimentos noturnos. As correspondências "
        "tradicionais de cada letra (gênero, forma e caráter) ajudam a "
        "interpretar a natureza do guardião."
    ),
    "suffixes": {
        "El": "Sufixo diurno (nascimento entre 06h e 18h). «El» é um dos nomes divinos hebraicos, sufixo de força e claridade solar.",
        "Iah": "Sufixo noturno (nascimento fora das 06h–18h). «Iah» é a forma curta de Yahweh, sufixo de mistério e receptividade lunar.",
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
        "aspect_combinations": ASPECT_COMBINATIONS,
        "kabbalah": KABBALAH,
        "tarot": TAROT,
        "angels": ANGELS,
        "agathadaimon": AGATHADAIMON,
    }
