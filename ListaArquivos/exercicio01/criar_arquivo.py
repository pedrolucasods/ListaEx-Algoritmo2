import csv
from pathlib import Path

diretorio_atual = Path(__file__).resolve().parent
caminho_arquivo_clientes = diretorio_atual / "clientes.csv"
caminho_arquivo_recebimento = diretorio_atual / "recebimento.csv"

campos_clientes = ["cod_cli","nome","endereco","fone"]
campos_recebimento = ["num_doc","valor_doc","data_emissao","data_vencimento","cod_cli"]


def criar_arquivo(caminho,campos):
    with open(caminho,"w",newline="",encoding="utf-8-sig") as arquivo:
        escritor = csv.DictWriter(arquivo, fieldnames=campos, delimiter=";")
        escritor.writeheader()

criar_arquivo(caminho_arquivo_clientes,campos_clientes)
criar_arquivo(caminho_arquivo_recebimento,campos_recebimento)