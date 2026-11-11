# 2 - Deslocamento (Shift) à Direita: Crie uma função que receba uma lista e um inteiro n.
# A função deve retornar uma nova lista com os elementos deslocados n posições para a
# direita. Os elementos que "saírem" do final devem reaparecer no início.

def deslocar(posicoes,lista):
    nova_lista = lista
    for i in range(posicoes):
        removido = lista.pop()
        nova_lista.insert(0,removido)
    return nova_lista
    
lista_teste = [1,2,3,4]
print(deslocar(1,lista_teste))