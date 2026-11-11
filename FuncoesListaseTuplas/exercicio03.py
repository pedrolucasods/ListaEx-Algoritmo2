# 3 - O sistema do caixa gera um recibo na forma de uma lista de tuplas (codigo_produto,
# quantidade, preco_unitario).
# Você deve multiplicar valores internos da tupla para criar dados novos (valor total do
# item), acumular um montante geral e guardar o registro do maior valor calculado.
# Retorno Exigido: O valor total da compra e uma tupla (codigo_produto,
# valor_total_do_item) representando exclusivamente o item que teve o maior custo
# absoluto na nota fiscal.
# Na Main: Monte uma lista de tuplas representando o "carrinho" de um cliente com 3 ou
# mais itens diferentes. Execute a função recebendo os retornos e imprima no terminal o
# valor total da nota fiscal (formatado com R$ e duas casas decimais) e os detalhes do
# produto que saiu mais caro na conta final.


def gerar_recibo(lista):
    total_cada_item = [(produto[0],produto[1]*produto[2]) for produto in lista]
    maior_valor = total_cada_item[0][1]
    for valor in total_cada_item:
        if(valor[1]>maior_valor):
            maior_valor = valor[1]

    filtro_caros = list(map(lambda t: tuple(list(t)+["Valor Alto"]) if t[1] == maior_valor else t ,total_cada_item))

    total_compra = 0
    for item_valor in total_cada_item:
        total_compra+=item_valor[1]

    dados = {
        "Total Cada Item":filtro_caros,
        "Total Compra R$":total_compra
    }
    return dados


carrinho_compras = [
    ("PROD001", 1, 120.00),
    ("PROD002", 1, 120.00),
    ("PROD003", 5, 8.75),
    ("PROD004", 2, 45.90)
]

dados = gerar_recibo(carrinho_compras)
for key,value in dados.items():
    print(f"{key}:{value}")