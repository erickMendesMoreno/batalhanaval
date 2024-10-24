def define_posicoes(linha, coluna, orientacao, tamanho):
    posicoes = []

    for i in range(tamanho):
        if orientacao == "vertical":
            posicoes.append([linha+i, coluna])
        elif orientacao == "horizontal":
            posicoes.append([linha, coluna+i])

    return posicoes 
    
def preenche_frota(frota,nome_nav,linha, coluna, orientacao, tamanho):
    nova_posi=define_posicoes(linha,coluna,orientacao,tamanho)
    if nome_nav in frota:
        frota[nome_nav].append(nova_posi)
    else:
        frota[nome_nav]=[nova_posi]
    return frota
def faz_jogada(tabu, linha, coluna):
 
    if tabu[linha][coluna] == 1:
        tabu[linha][coluna] = 'X' 
    else:
        tabu[linha][coluna] = '-' 
    return tabu
def posiciona_frota(frota):
    tabunv = [[0 for i in range(10)] for i in range(10)]
    for nome_nav, posicoes in frota.items():
        for posicao in posicoes:
            for linha, coluna in posicao:
                tabunv[linha][coluna] = 1

    return tabunv