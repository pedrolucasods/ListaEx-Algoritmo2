# Crie uma função recursiva que receba um número inteiro N e imprima a contagem regressiva de N até 1.

def contagem_regressiva(n):
    if(n == 1):
        return 1
    else:
        print(n)
        return contagem_regressiva(n-1)

print(contagem_regressiva(10))