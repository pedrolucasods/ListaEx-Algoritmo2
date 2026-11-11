# 4 - Utilizando a biblioteca NumPy: (a) Crie um array 1D com os números inteiros de 10
# a 50 (inclusive) com passo 5 usando `np.arange()`; (b) Eleve todos os elementos do
# array ao quadrado de forma vetorizada (sem laço `for`); (c) Aplique uma filtragem por
# indexação booleana para extrair apenas os valores superiores a 500.
import numpy as np

lista_inteiros = np.arange(0,50,5)
lista_quadrada = lista_inteiros ** 2
indexs_maiores = list(np.where(lista_quadrada > 500))[0]
# print(indexs_maiores)
# print(indexs_maiores[0])

# print(indexs_maiores[0].tolist())
lista_maiores = list(lista_quadrada[indexs_maiores].tolist())
print(lista_maiores)