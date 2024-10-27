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

#Programa
espaco = {
    "porta-aviões":4,
    "navio-tanque":3,
    "contratorpedeiro":2,
}   
frota = {
    "porta-aviões":[],
    "navio-tanque":[],
    "contratorpedeiro":[],
    "submarino": [],
}
frota_jogador = {
    "porta-aviões":[],
    "navio-tanque":[],
    "contratorpedeiro":[],
    "submarino": [],
}

for nome, posicao in frota.items():
    if nome == 'submarino':
        print('Insira as informações referentes ao navio', nome, 'que possui tamanho', 1)
        linha = int(input('Qual a linha que você deseja'))
        coluna = int(input('Qual a coluna que você deseja'))
        valido = posicao_valida(frota, linha, coluna, 'vertical', espaco[nome])
        while valido != True:
                print('Insira as informações referentes ao navio', nome, 'que possui tamanho', espaco[nome])
                linha = int(input('Qual a linha que você deseja'))
                coluna = int(input('Qual a coluna que você deseja'))
                orientacao = int(input('Selecione a posição: 1 - vertical e 2 - horizontal'))
                valido = posicao_valida(frota, linha, coluna, 'vertical', espaco[nome])
        position = preenche_frota(linha, coluna, orientacao, espaco[nome])
        frota_jogador[nome].append(position)
        posicao.append([linha, coluna])
    else:
        i = 0
        while i < espaco[nome]:
            print('Insira as informações referentes ao navio', nome, 'que possui tamanho', espaco[nome])
            linha = int(input('Qual a linha que você deseja'))
            coluna = int(input('Qual a coluna que você deseja'))
            orientacao = int(input('Selecione a posição: 1 - vertical e 2 - horizontal'))
            valido = posicao_valida(frota, linha, coluna, orientacao, espaco[nome])
            while valido != True:
                print('Insira as informações referentes ao navio', nome, 'que possui tamanho', espaco[nome])
                linha = int(input('Qual a linha que você deseja'))
                coluna = int(input('Qual a coluna que você deseja'))
                orientacao = int(input('Selecione a posição: 1 - vertical e 2 - horizontal'))
                valido = posicao_valida(frota, linha, coluna, orientacao, espaco[nome])
            posicao.append([linha, coluna])
            position = preenche_frota(frota, nome, linha, coluna, orientacao, espaco[nome])
            frota_jogador[nome].append(position)
            i += 1
print(frota)
