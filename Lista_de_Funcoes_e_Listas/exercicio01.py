# 1 - Média Móvel: Escreva uma função que receba uma lista de números e um número
# inteiro k (tamanho da janela). A função deve retornar uma lista com as médias de cada
# sublista contígua de tamanho k.
lista_numeros = [8,8,8,1,1,2]

def media_movel(valor_k,lista):
    lista_media = []
    valor_restante = len(lista) - valor_k
    soma = 0
    if(valor_k>len(lista) or valor_k<1):
        return "Erro, valor K inválido!"

    for i in range(valor_k):
        soma+=lista[i]
    lista_media.append(soma/valor_k)
    lista.reverse()
    soma = 0
    for j in range(valor_restante):
        soma+=lista[j]
    lista_media.append(soma/valor_restante)
    return lista_media

print(media_movel(3,lista_numeros))


