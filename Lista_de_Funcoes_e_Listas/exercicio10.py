# 10 - Decodificador de Sinais de Satélite: Um satélite envia pacotes de dados como uma
# lista de bits (0s e 1s). Um pacote de informação válido é sempre sinalizado pelo padrão
# exato de um 1 seguido imediatamente por dois 0s.
# Retorno exigido: O número total de pacotes válidos detectados e uma lista de
# índices marcando onde cada pacote válido começa.

def decodificador_satelite(lista):
    contador = 0
    lista_index_inicio = []
    for indice,valor in enumerate(lista):
        if valor == 1:
            if(indice+1 < len(lista)-1):
                if(lista[indice+1] == 0 and lista[indice+2] == 0):
                    contador+=1
                    lista_index_inicio.append(indice)
    dados={
        "Pacotes":lista,
        "Quantidade de Pacotes Válidos":contador,
        "Inicio dos pacotes":lista_index_inicio
    }

    return dados

sinais = [0,1,0,0,1,0,0,1,0,1,1,1,0,1,0,0]
dados = decodificador_satelite(sinais)
for key,value in dados.items():
    print(f"{key}:{value}")