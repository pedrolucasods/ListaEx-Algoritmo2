# 4 - Em um motor gráfico, os obstáculos circulares são uma lista de tuplas (pos_x, pos_y,
# raio). Você recebe também a tupla do jogador (jog_x, jog_y, jog_raio).
# A colisão ocorre se a distância entre os centros (use a soma das diferenças absolutas de
# X e Y como simplificação) for menor que a soma dos raios.
# Retorno Exigido: Um booleano True ou False indicando se o jogador colidiu com
# algum obstáculo e a quantidade exata de obstáculos com os quais ele está colidindo
# simultaneamente.
# Na Main: Defina uma lista com vários obstáculos espalhados pelo mapa e uma variável
# separada para as coordenadas do jogador, forçando uma posição onde ele encoste em
# pelo menos dois obstáculos ao mesmo tempo. Chame a função e exiba uma mensagem
# de status ("Impacto Detectado!" ou "Caminho Livre") e a quantidade de objetos
# atingidos.

def motor_grafico(lista, jogador):
    qtd_colisacao = 0
    for obstaculo in lista:
        diferenca_x = abs(obstaculo[0]-jogador[0])
        diferenca_y = abs(obstaculo[1]-jogador[1])
        soma_raio = (jogador[2]+obstaculo[2])
        if((diferenca_x+diferenca_y) < soma_raio):
            qtd_colisacao+=1
    dados = {
        "Esta colidindo?":True if qtd_colisacao>0 else False,
        "Quantidade de obstaculo colidindo":qtd_colisacao
    }
    return dados

obstaculos = [
    (15, 10, 5),
    (15, 10, 6),
    (70, 70, 5),
    (70, 70, 5),
    (90, 90, 5) 
]

jogador = (15, 10, 3)

dados = motor_grafico(obstaculos,jogador)
for key,value in dados.items():
    print(f"{key}:{value}")