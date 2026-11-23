#  Merge de Listas Ordenadas: Desenvolva uma função que receba duas listas que já
# estão ordenadas de forma crescente. A função deve retornar uma única lista contendo
# todos os elementos de ambas, também ordenada. Não é permitido concatenar e aplicar
# algoritmo de ordenação depois.
import random

def merge_lista(lista_1,lista_2):
    print(lista_1)
    print(lista_2)
    lista_mergeada = []
    soma_tamanho = len(lista_1)+len(lista_2)
    while len(lista_mergeada)!=soma_tamanho:
        menor_l1 = menor_numero_da_lista(lista_1)
        menor_l2 = menor_numero_da_lista(lista_2)

        if(type(menor_l1) is int and menor_l2 is None):
            lista_mergeada.append(menor_l1)
            lista_1.remove(menor_l1)
        elif(type(menor_l2) is int and menor_l1 is None):
            lista_mergeada.append(menor_l2)
            lista_2.remove(menor_l2)
        elif(menor_l1<menor_l2):
            lista_mergeada.append(menor_l1)
            lista_1.remove(menor_l1)
        elif(menor_l2 < menor_l1 or menor_l1==menor_l2):
            lista_mergeada.append(menor_l2)
            lista_2.remove(menor_l2)
        else:
            break
    if(lista_1<lista_2):
        lista_mergeada.extend(lista_1)
        lista_mergeada.extend(lista_2)
    else:
        lista_mergeada.extend(lista_2)
        lista_mergeada.extend(lista_1)

    return lista_mergeada
        
def menor_numero_da_lista(lista):
    if(len(lista) == 0):
        return None
    menor = lista[0]
    for i in range(len(lista)):
        if(i == 0):
            pass
        else:
            if(lista[i]<menor):
                menor = lista[i]
            else:
                pass
    return menor


lista_a = [ random.randint(1,239) for i in range(random.randint(1,12))]
lista_b = [ random.randint(1,293) for i in range(random.randint(1,6))]
print(merge_lista(lista_a,lista_b))