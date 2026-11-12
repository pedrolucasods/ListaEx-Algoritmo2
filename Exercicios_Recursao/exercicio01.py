# Escreva uma função recursiva que receba uma lista de números inteiros
# E retorne a soma de todos os seus elementos sem utilizar o comando 'sum()' nem laços 'for/while'.

def soma_recursiva(lista):
    if(not lista):
        return 0
    else:
        return lista.pop(0)+soma_recursiva(lista)

lista = [1,2,3,4,5]
print(soma_recursiva(lista))
