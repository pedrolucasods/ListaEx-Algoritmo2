# 2 - Dada a lista estática de salários `salarios = [2500.0, 3200.0, 1800.0, 4500.0,
# 2100.0]`: (a) Atualize o salário no índice 2 para 2300.0; (b) Peça ao usuário um valor de
# salário para buscar e verificar se existe na lista usando o operador `in`; (c) Se existir,
# remova-o usando `.remove()`; (d) Extraia e remova o último elemento da lista utilizando
# `.pop()` e exiba o elemento removido.

salarios = [2500.0, 3200.0, 1800.0, 4500.0,2100.0]
print(salarios)
salarios[2] = 2300.0
print(f"Atualização Salario index 2\n{salarios}")

buscar_valor = float(input('Informe o valor para procurar: '))
resultado_busca = True if buscar_valor in salarios else False
if(resultado_busca):
    salarios.remove(buscar_valor)
print(f"Valor removido\n{salarios}")

ultimo_elemento = salarios.pop(salarios.index(salarios[-1]))
print(ultimo_elemento)
print(salarios)
