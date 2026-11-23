# 5 - Controle de Qualidade Agrícola: Uma fazenda colhe maçãs e as classifica pelo peso
# (em gramas). Você receberá a lista de pesos, o peso mínimo para exportação e o peso
# máximo.
# Retorno exigido: Uma lista contendo os pesos aprovados, uma segunda lista com
# os pesos descartados, e a porcentagem de perda da safra (número float).
import random

def validar_macas(minimo,maximo,lista):
    if(minimo > maximo):
        raise ValueError("Minímo Precisa ser Menor que o Máximo")
    lista_todos = [item for item in lista]
    lista_aprovados = []
    for peso in lista_todos:
        if(peso <= maximo and peso>=minimo):
            lista_aprovados.append(peso)
            lista_todos.remove(peso)

    dados = {
        "todos_pesos":lista,
        "pesos_aprovados":lista_aprovados,
        "perca_safra":f"{(100 - ((sum(lista_aprovados) / sum(lista)) * 100)):.2f}%"
    }
    return dados


lista_peso = [random.randint(1,30) for i in range(random.randint(4,10))]

dados = validar_macas(3,14,lista_peso)
for key,value in dados.items():
    print(f"{key}:{value}")
