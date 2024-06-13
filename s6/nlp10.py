# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 21:49:04 2024

@author: cerpc
"""

import random
import nltk

text = """Sociedade Esportiva Palmeiras (pronúncia em português: [sosiedˈadʒi ispoɾtʃˈivə pawmˈejɾəs]), conhecida popularmente como Palmeiras, é um clube poliesportivo brasileiro da cidade de São Paulo, capital do estado homônimo. Foi fundado em 26 de agosto de 1914 e suas cores, presentes no escudo e bandeira oficial, são o verde e branco.[3] O vermelho, presente desde sua fundação em 1914, foi excluído durante a Segunda Guerra Mundial, por pressão do governo de Getúlio Vargas, na mesma reunião que formalizou a mudança de nome de Palestra Italia para Palmeiras.[4]

Tem como modalidade esportiva principal o futebol, como um dos clubes mais vencedores e de maior relevância em todo o continente, além de estar entre aqueles com maior torcida do país.[5] Seus títulos mais importantes conquistados no futebol são as Copas Libertadores da América de 1999,[6] 2020[7] e de 2021,[8] e a Copa Rio (internacional) de 1951, considerado na época como um Mundial de Clubes de futebol[9] e reconhecido como tal pela FIFA, por meio do presidente da entidade, Joseph Blatter, em agosto de 2014, sendo uma decisão do Comitê Executivo da FIFA de 7 de junho[10][11][12][13][14] e por meio de documento encaminhado ao Ministério do Esporte do Brasil em novembro do mesmo ano.[15][16] A entidade, no entanto, não reconhece a competição como um torneio FIFA e reforçou este posicionamento em outubro de 2017, quando reconheceu os vencedores da Copa Intercontinental como campeões mundiais,[17] sem, também, promover a unificação da Copa Intercontinental com a sua atual competição.[18][19] No âmbito internacional, o clube também conquistou a Copa Mercosul de 1998 e a Recopa Sul-Americana de 2022.[20]

Eleito o melhor time do mundo de 2021 no ranking da Federação Internacional de História e Estatísticas do Futebol (IFFHS, na sigla em inglês),[21] o Palmeiras é a equipe brasileira com o maior número de títulos de abrangência nacional conquistados, sendo o único a vencer todas as competições oficiais que disputou criadas no País, inicialmente pela Confederação Brasileira de Desportos (CBD) e, a partir de 1980, pela Confederação Brasileira de Futebol (CBF).[22] O alviverde possui 18 conquistas deste porte,[23] com destaque maior para seus 12 títulos do Campeonato Brasileiro (atual recordista):[24] 1960, 1967,(1) 1967,(2) 1969, 1972, 1973, 1993, 1994, 2016, 2018, 2022 e 2023. Além destes campeonatos, o Palmeiras já venceu no país as Copas do Brasil de 1998, 2012, 2015 e de 2020, a Supercopa do Brasil de 2023 e a Copa dos Campeões de 2000, competições também organizadas pela entidade máxima do futebol brasileiro.

No Estado de São Paulo, o Palmeiras também é um dos principais vencedores, com 26 conquistas do Campeonato Paulista de Futebol e mais dois títulos extra da mesma competição. Em 1996, o alviverde conquistou o estadual daquele ano com a melhor campanha de uma equipe na era profissional neste campeonato.[25] Na ocasião, foi campeão com 83 pontos ganhos em 90 possíveis, com um índice de aproveitamento de 92,2% dos pontos disputados e 102 gols marcados em 30 jogos realizados. Desde então, esta marca jamais foi alcançada por qualquer outra equipe na competição.[26]

No mais recente Ranking Nacional de Clubes da CBF, que leva em conta o comportamento das equipes nas últimas cinco temporadas e que foi divulgado em dezembro de 2023, o Palmeiras é o segundo colocado, com 15 372 pontos.[2] No último ranking da confederação que levou em conta um período histórico mais abrangente do futebol brasileiro e que foi divulgado em 2011, o Palmeiras foi o líder, com 2 366 pontos.[27] Em 2005, no dia 11 de outubro, foi sancionada na cidade de São Paulo a Lei n.º 14 060, que definiu o dia 20 de setembro como o "Dia da Sociedade Esportiva Palmeiras", que passou a ser lembrado anualmente na capital paulista, já que passou a integrar o Calendário Oficial do Município.[28]."""

n = 5

ngrams = {}

words = nltk.word_tokenize(text)
for i in range(len(words) - n):
    gram = ' '.join(words[i:i + n])
    if gram not in ngrams.keys():
        ngrams[gram] = []
    ngrams[gram].append(words[n + i])
    
currentGram = ' '.join(words[0:n])
result = currentGram
for i in range(30):
    if currentGram not in ngrams.keys():
        break
    possibilities = ngrams[currentGram]
    nextItem = possibilities[random.randrange(len(possibilities))]
    result += ' ' + nextItem
    rwords = nltk.word_tokenize(result)
    currentGram = ' '.join(rwords[len(rwords) - n:len(words)])

print(result)    