def define_posicoes(linha, coluna, orientacao, tamanh):
    posicoes = []

    for i in range(tamanh):
        if orientacao == "vertical":
            posicoes.append([linha+i, coluna])
        elif orientacao == "horizontal":
            posicoes.append([linha, coluna+i])

    return posicoes 
    

