# 10 - Um sistema acadêmico armazena as notas de 4 alunos em 3 avaliações através de
# uma matriz NumPy 4x3: (a) Dado a matriz de notas iniciais `notas = np.array([[5.0, 7.5,
# 6.0], [8.0, 9.0, 4.0], [3.5, 5.0, 6.5], [7.0, 6.0, 8.5]])`, calcule e exiba a média final de
# cada aluno; (b) Identifique qual avaliação (coluna) obteve a maior média geral da turma
# usando `np.argmax()`; (c) Aplique um reajuste automático atribuindo a nota mínima
# `6.0` a todas as avaliações com nota inferior a 6.0; (d) Remova a última coluna
# (Avaliação 3) da matriz utilizando `np.delete(..., axis=1)`.

import numpy as np

notas = np.array([[5.0, 7.5,6.0], [8.0, 9.0, 4.0], [3.5, 5.0, 6.5], [7.0, 6.0, 8.5]])
medias_materias = []
notas_sem_ultima_materia = np.delete(notas, notas.shape[1] - 1, axis=1)

for i in range(len(notas)):
    soma = 0
    for j in range(len(notas[i])):
        if(notas[i][j] < 6):
            notas[i][j] = 6
        soma+=notas[i][j]
        print(f"[{notas[i][j]}]",end='')
    medias_materias = ((np.sum(notas,axis=0)/len(notas[i]))).tolist()
    print(f" media = {soma/len(notas[i]):.2f}",end='')
    print('\t')

print(f"\nMedias de cada Máteria\n:{medias_materias}\nMateria com Maior médida: {medias_materias.index(max(medias_materias))}")