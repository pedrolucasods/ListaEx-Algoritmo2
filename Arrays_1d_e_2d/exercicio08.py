# 8 - Utilizando o NumPy: (a) Crie uma matriz 4x4 preenchida com números inteiros
# aleatórios entre 10 e 99 (`np.random.randint()`); (b) Calcule a soma de cada linha
# (axis=1) e a média de cada coluna (axis=0); (c) Altere a forma da matriz (reshape) de
# 4x4 para 2x8 e exiba a nova estrutura.
import numpy as np

matriz = np.array([np.random.randint(10,99,4) for i in range(4)])
medias = []
print("======= Matriz Original ======")
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        soma = 0
        if(i == 0):
            for k in range(4):
                soma+=matriz[k][j]
            medias.append(float(soma/4))
        print(f"[{matriz[i][j]}]",end='')

    
    print(f" soma = {sum(matriz[i])}")
    print(f'\t')

print(f"===== Medias de cada coluna respectivamente =====\n{medias}")
def transformar_matriz4x4_para_2x8(matriz):
    matriz_transformada = []
    linha = []
    while(len(matriz_transformada)<2):
        for i in range(len(matriz)):
            if(len(linha) == 8) and linha not in matriz_transformada:
                matriz_transformada.append(linha)
                linha = []
            for j in range(len(matriz[i])):
                linha.append(matriz[i][j])

    return matriz_transformada

matriz_2x8 = matriz.reshape(2,8) # Com função própria
matriz_2x8_funcao_manual = transformar_matriz4x4_para_2x8(matriz)
print("\n====== Matriz 2x8 ======")
for i in range(len(matriz_2x8_funcao_manual)):
    for j in range(len(matriz_2x8_funcao_manual[i])):
        print(f"[{matriz_2x8_funcao_manual[i][j]}]",end='')
    print('\t')
print('\n')

