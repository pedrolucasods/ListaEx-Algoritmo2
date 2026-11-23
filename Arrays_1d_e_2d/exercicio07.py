# 7 - Dada a matriz nativa 3x2 `matriz = [[1, 2], [3, 4], [5, 6]]`: (a) Permita que o usuário
# atualize o valor da linha 1, coluna 0 para 99; (b) Escreva uma função que construa e
# retorne a matriz transposta (tamanho 2x3), onde as linhas da matriz original viram
# colunas.

matriz = [[1, 2], [3, 4], [5, 6]]
print("========= Matriz Normal ========")
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if(i == 1 and j == 0):
                matriz[i].pop(j)
                matriz[i].insert(0,99)

        print(f"[{matriz[i][j]}]",end='')
    print('\t')

def transpor_matriz(matriz):
    transposta = []
    for i in range(len(matriz)):
        if(len(transposta) == 2):
            break
        else:
            for j in range(len(matriz[i])):
                if(j == 0 and i == 0):
                    transposta.append([matriz[i][j+1],matriz[i+1][j+1],matriz[i+2][j+1]])
                    break
                else:
                    transposta.append([matriz[i-1][j],matriz[i][j],matriz[i+1][j]])
                    break

    return transposta

transposta = transpor_matriz(matriz)
print("\n========= Matriz Transposta ========")

for i in range(len(transposta)):
    for j in range(len(transposta[i])):
        print(f"[{transposta[i][j]}]",end='')
    print('\t')
            

            
