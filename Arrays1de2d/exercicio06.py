# 6 - Construa um programa em Python nativo para ler uma matriz 3x3 de inteiros
# digitados pelo usuário: (a) Preencha a matriz utilizando laços aninhados em listas de
# listas (`list[list]`); (b) Imprima a matriz em formato tabular formatado; (c) Exiba os
# elementos da diagonal principal (onde índice da linha i == coluna j) e da diagonal
# secundária (onde i + j == 2).
import os

matriz = []
for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input(f'Informe o valor da posição [{i}][{j}]: '))
        linha.append(valor)
    matriz.append(linha)

os.system('cls')
print('======== Matriz Completa ========')
for i in range(3):
    for j in range(3):
        print(f"[{matriz[i][j]}]",end="")
    print('\t')

print('\n======== Diagonal principal ========')
for i in range(3):
    for j in range(3):
        if(i == j):
            print(f"[{matriz[i][j]}]",end="")
        else:
            print('[]',end='')
    print('\t')


print('\n======== Diagonal Secundaria ========')
for i in range(3):
    for j in range(3):
        if(i + j == 2):
            print(f"[{matriz[i][j]}]",end="")
        else:
            print('[]',end='')
    print('\t')
    
