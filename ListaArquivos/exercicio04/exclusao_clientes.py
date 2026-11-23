import csv
from pathlib import Path

pasta_atual = Path(__file__).parent
caminho_arquivo_cliente = pasta_atual.parent / "exercicio01" / "clientes.csv"
caminho_arquivo_recebimento = pasta_atual.parent / "exercicio01" / "recebimento.csv"

def excluir_cliente(cod_cli):
    cliente_excluido = False
    with open(caminho_arquivo_cliente,"r",newline="",encoding="utf-8-sig") as arquivo_cliente:
        leitor_clientes = csv.DictReader(arquivo_cliente,delimiter=";")
        campos_clientes = leitor_clientes.fieldnames
        dados_clientes = list(leitor_clientes)

    busca_cliente = next(filter(lambda x: int(x["cod_cli"]) == int(cod_cli),dados_clientes),None)
    if(not busca_cliente):
        print("Cliente não encontrado!")
        return
    dados_clientes.remove(busca_cliente)
    with open(caminho_arquivo_cliente,"w", newline="",encoding="utf-8-sig") as f:
        editor = csv.DictWriter(f,fieldnames=campos_clientes, delimiter=";")
        editor.writeheader()
        editor.writerows(dados_clientes)
        cliente_excluido = True

    if(cliente_excluido):
        with open(caminho_arquivo_recebimento,"r",encoding="utf-8-sig") as arquivo_recebimento:
            leitor_recebimento = csv.DictReader(arquivo_recebimento, delimiter=";")
            campos_recebimento = leitor_recebimento.fieldnames
            dados_recebimento = list(leitor_recebimento)

        busca_recebimentos = list(filter(lambda x: int(x["cod_cli"]) == int(cod_cli),dados_recebimento))
        print(dados_recebimento)
        if(busca_recebimentos):
            for recebimento in busca_recebimentos:
                dados_recebimento.remove(recebimento)
            with open(caminho_arquivo_recebimento,"w", newline="",encoding="utf-8-sig") as f:
                editor_recebimento = csv.DictWriter(f,fieldnames=campos_recebimento,delimiter=";")
                editor_recebimento.writeheader()
                editor_recebimento.writerows(dados_recebimento)
        
            print("Cliente Excluido!")

excluir_cliente("3")