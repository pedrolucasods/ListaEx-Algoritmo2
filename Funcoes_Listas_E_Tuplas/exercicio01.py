# 1 - Uma estufa inteligente possui vários sensores. O microcontrolador envia uma lista
# de tuplas no formato (id_sensor, temperatura, umidade). As regras de segurança dizem
# que a temperatura não pode passar de 35°C e a umidade não pode ficar abaixo de 20%.
# Você precisa rastrear simultaneamente o maior valor de uma variável e o menor de
# outra, enquanto filtra dados.
# Retorno Exigido: Uma lista contendo apenas os id_sensor que dispararam algum
# alarme de perigo, e uma tupla (maior_temperatura, menor_umidade) registrada em todo
# o período.
# Na Main: Crie uma lista simulando pelo menos 4 sensores (certifique-se de forçar pelo
# menos um alerta de temperatura e um de umidade). Chame a função passando essa lista.
# Imprima no terminal quais sensores entraram em alerta e exiba os picos máximos e
# mínimos.

def microcontrolador(lista):
    id_sensor_perigo = list(filter(lambda x: x!=-1,[item[0] if item[1]>35 or item[2]<20 else -1 for item in lista]))
    maior_temperatua = lista[0][1]
    menor_umidade = lista[0][2]
    for item in lista:
        if(item[1]>=maior_temperatua):
            maior_temperatua = item[1]
        if(item[2]<=menor_umidade):
            menor_umidade=item[2]

    extremos = (maior_temperatua,menor_umidade)

    dados = {
        "Sensores em Alerta":id_sensor_perigo,
        "Extremos":extremos
    }
    return dados

lista_estufa = [
    (1,23,40),
    (2,25,19),
    (3,36,19),
    (4,36,19)
]

dados = microcontrolador(lista_estufa)
for key,value in dados.items():
    print(f"{key}:{value}")