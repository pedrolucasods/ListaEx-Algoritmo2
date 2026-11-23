# 3 - Crie um vetor com 10 números inteiros de 1 a 10. Utilizando a técnica de fatiamento
# (slicing) do Python: (a) Gere uma sublista contendo apenas os elementos localizados
# nos índices pares; (b) Gere uma sublista contendo apenas os números ímpares (por
# valor); (c) Crie uma cópia da lista inteira invertida sem utilizar o método `.reverse()`.
import random

lista_inteiros = [1,2,3,4,5,6,7,8,9,10]
sub_lista_pares = lista_inteiros[::2]
sub_lista_impares = list(filter(lambda x: x%2 !=0 ,lista_inteiros))
lista_inversa = lista_inteiros[::-1]