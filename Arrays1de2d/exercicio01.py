# 1 - Escreva um programa em Python que solicite ao usuário a quantidade N de números
# inteiros que deseja cadastrar. Construa uma lista vazia e preencha-a dinamicamente em
# tempo de execução utilizando o método append(). Em seguida, percorra a lista e exiba:
# (a) o maior e o menor valor digitados; (b) a média aritmética dos elementos; e (c) a
# quantidade de números pares
lista_numeros = []
qtd_numeros = int(input('Informe a quantidade de número: '))
for i in range(qtd_numeros):
    numero = int(input(f"Informe o {i+1}º valor: "))
    lista_numeros.append(numero)

maior = lista_numeros[0]
menor = lista_numeros[0]
qtd_pares = 0
soma = 0
for n in lista_numeros:
    soma+=n
    if(n > maior or n == maior):
        maior = n
    if(n < menor or n == menor):
        menor = n
    if(n%2 == 0):
        qtd_pares+=1

dados = {
    'Lista':lista_numeros,
    'Maior':maior,
    'Menor':menor,
    'Quantidade de Pares':qtd_pares,
    'Media':soma/qtd_numeros
}

for key,value in dados.items():
    print(f"{key}: {value}")