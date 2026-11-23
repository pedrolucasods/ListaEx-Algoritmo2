import csv
from pathlib import Path

pasta_atual = Path(__file__).parent
caminho_arquivo_cliente = pasta_atual.parent / "exercicio01" / "clientes.csv"

def atualizar_cliente(cod_cli):
    if(int(cod_cli)<=0):
        print("Codigo Inválido!")
        return
    with open(caminho_arquivo_cliente,"r",newline="",encoding="utf-8-sig") as arquivo_cliente:
        leitor = csv.DictReader(arquivo_cliente,delimiter=";")
        campos = leitor.fieldnames
        dados_clientes = list(leitor)
        if(not dados_clientes):
            print("Nenhum Cliente Cadastrado!")
            return

        busca_cliente = next(filter(lambda x: int(x["cod_cli"]) == int(cod_cli), dados_clientes),None)
        if(not busca_cliente):
            print("Cliente Não encontrado!")
            return
        index_cliente = dados_clientes.index(busca_cliente)
        print(f"Informe os dados de {busca_cliente["nome"]}:")
        novos_dados_cliente = {
            "cod_cli":busca_cliente["cod_cli"],
            "nome":input("Informe o novo nome: ") or busca_cliente["nome"],
            "endereco":input("Informe o novo endereco: ") or busca_cliente["endereco"],
            "fone":input("Informe o novo fone: ") or busca_cliente["fone"]
        }
        dados_clientes.remove(busca_cliente)
        dados_clientes.insert(index_cliente,novos_dados_cliente)
    with open(caminho_arquivo_cliente,"w",newline="",encoding="utf-8-sig") as arquivo:
        editor = csv.DictWriter(arquivo,fieldnames=campos,delimiter=";")
        editor.writeheader()
        editor.writerows(dados_clientes)
        print("Cliente Alterado!")

atualizar_cliente(2)
