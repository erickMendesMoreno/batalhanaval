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

def afundados(info_pos, estado_atual):
    navios_afundados = 0
    for navios, lista_de_posicoes in info_pos.items():
        for posicoes_navio in lista_de_posicoes:
            if all(estado_atual[x][y] == 'X' for x, y in posicoes_navio):
                navios_afundados += 1 

    return navios_afundados

def posicao_valida(info_navis, linha_escolhida, coluna_escolhida, ort, tmnh):
    if ort == 'vertical':
        if linha_escolhida + tmnh > 10:
            return False
    if ort == 'horizontal':
        if coluna_escolhida + tmnh > 10:
            return False
    definida = define_posicoes(linha_escolhida,coluna_escolhida, ort, tmnh)
    for pos_requerida in definida:
        for lista_navios in info_navis.values():
            for navio in lista_navios:
                for pos_navio in navio:   
                    if pos_requerida == pos_navio:
                        return False
    return True