from funcoes import *
espaco = {
    "porta-aviões":4,
    "navio-tanque":3,
    "contratorpedeiro":2,
    "submarino": 1
}   
frota = {
    "porta-aviões":[],
    "navio-tanque":[],
    "contratorpedeiro":[],
    "submarino": [],
}
quantidade = {
    "porta-aviões":1,
    "navio-tanque":2,
    "contratorpedeiro":3,
    "submarino": 4,
}

orientacoes = [ "vertical","horizontal"]
for nome, posicao in frota.items():
    for i in range(quantidade[nome]):
        valida = False
        while not valida:
            print(f"Insira as informações referentes ao navio {nome} que possui tamanho {espaco[nome]}")
            linha = int(input("Linha: "))
            coluna = int(input("Coluna: "))
            if espaco[nome] > 1 :
                orientacao = orientacoes[int(input("[1] Vertical [2] Horizontal >"))-1]
            else:
                orientacao = orientacoes[0] #verical
            pos = [linha,coluna]
            valida = posicao_valida(frota,linha,coluna,orientacao,espaco[nome])
            if not valida:
                print("Esta posição não está válida!")
        frota = preenche_frota(frota,nome,linha,coluna,orientacao,espaco[nome])
    
print(frota)
