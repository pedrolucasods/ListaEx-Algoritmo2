# 5 - Uma imagem digital é formada por pixels. Você receberá uma lista de tuplas, onde
# cada tupla contém três inteiros (R, G, B) representando as cores Vermelho, Verde e
# Azul de um pixel (valores de 0 a 255).
# Transforme o formato original dos dados convertendo uma tupla de três elementos em
# um único valor inteiro (a média, usando divisão inteira), além de identificar uma
# condição específica absoluta.
# Crie uma nova lista contendo a média inteira de cada tupla e um contador informando
# quantos pixels da imagem original eram puramente pretos (0, 0, 0).
# Na Main: Crie uma lista simulando os pixels de uma foto pequena, garantindo que
# contenha pelo menos um ou dois pixels totalmente pretos e outros variados. Passe essa
# lista para a função e imprima a nova "imagem" processada, além do relatório
# informando a quantidade exata de pixels escuros puros encontrados.

def transform_pixel(lista):
    lista_media = list(map(lambda x: f"{(sum(x)/3):.2f}",lista))
    quantidade_pretos = 0
    for item in lista:
        if(item[0] == 0 and item[1] == 0 and item[2] == 0) :
            quantidade_pretos+=1

    dados = {
        "Media dos Pixels":lista_media,
        "Quantidade Pretos":quantidade_pretos
    }
    return dados




lista_pixel = [
    (255, 255, 255),
    (0, 0, 0),
    (120, 80, 40),
    (0, 0, 0),
    (50, 200, 100),
    (210, 210, 210),
    (15, 30, 45)
]

dados = transform_pixel(lista_pixel)
for key,value in dados.items():
    print(f"{key}:{value}")
