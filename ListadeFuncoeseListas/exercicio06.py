# 6 - Sistema de Alerta de Manutenção de Frota: Um ônibus transmite diariamente a
# quilometragem percorrida. Você receberá uma lista com esses trajetos diários e o limite
# de quilometragem para a revisão do motor.
# Retorno exigido: A quilometragem total acumulada, o dia (índice da lista) em
# que o limite foi ultrapassado, e um booleano (True ou False) indicando se o
# ônibus precisa ser recolhido imediatamente.
import random

def alerta_manutencao(limite,lista):
    total_km = sum(lista)
    contador = 0
    dias_passou = []
    for indice,valor in enumerate(lista):
        if(valor>limite):
            contador+=1
            dias_passou.append(indice+1)
    dados = {
        "lista_kms":lista,
        "limite":limite,
        "total":total_km,
        "dias_passou":dias_passou,
        "recolhimento":"Precisa" if (True if len(lista) else False) else "Não Precisa"
    }
    return dados

lista_velocidade = [random.randint(1,10) for i in range(random.randint(1,5))]
dados = alerta_manutencao(random.randint(1,5),lista_velocidade)
for key,value in dados.items():
    print(f"{key}:{value}")
