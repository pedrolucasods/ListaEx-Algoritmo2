# 3 - Concatenação Alternada: Desenvolva uma função que receba duas listas (de
# tamanhos possivelmente diferentes) e retorne uma única lista intercalando os elementos
# de ambas até o fim da menor, adicionando o restante da maior ao final.

def concatenacao_alteranada(lista_1,lista_2):
    lista_concatenada = []
    for valor in lista_1:
        lista_concatenada.append(valor)
        for valor2 in lista_2:
            lista_concatenada.append(valor2)
            lista_2.remove(valor2)
            break
    return lista_concatenada

lista_teste = [1,1,1]
lista_outra = [2,3,2]
print(concatenacao_alteranada(lista_teste,lista_outra))