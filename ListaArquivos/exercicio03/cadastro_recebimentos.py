import csv
from pathlib import Path

pasta_atual = Path(__file__).resolve().parent
caminho_arquivo_recebimento = pasta_atual.parent / "exercicio01" / "recebimento.csv"
caminho_arquivo_cliente = pasta_atual.parent / "exercicio01" / "clientes.csv"
def cadastro_recebimento(valor_doc,data_emissao,data_vencimento,cod_cli,):
    novo_recebimento = {
        "valor_doc":valor_doc,
        "data_emissao":data_emissao,
        "data_vencimento":data_vencimento,
        "cod_cli":cod_cli
    }
    if(any(valores == "" or valores == None for valores in novo_recebimento.values())):
        print("Campos Inválidos!")
        return
    with open(caminho_arquivo_cliente,"r",encoding="utf-8-sig") as arquivo_cliente:
        leitor = csv.DictReader(arquivo_cliente,delimiter=";")
        dados = list(leitor)
        cliente = next(filter(lambda x: int(x['cod_cli']) == int(novo_recebimento["cod_cli"]),dados),None)
    if(not cliente):
        print("Cliente Não Encontrado!")
        return

    with open(caminho_arquivo_recebimento,"r+",newline="",encoding="utf-8-sig") as arquivo_recebimento:
        leitor = csv.DictReader(arquivo_recebimento,delimiter=";")
        campos = leitor.fieldnames
        dados = list(leitor)
        arquivo_recebimento.seek(arquivo_recebimento.tell()-1)
        if arquivo_recebimento.read(1) != "\n":
            arquivo_recebimento.write("\n")
        editor = csv.DictWriter(arquivo_recebimento,fieldnames=campos,delimiter=";")
        if(not dados):
            novo_recebimento["num_doc"] = 1
            editor.writerow(novo_recebimento)
        else:
            ultimo_cod_cli = int(dados[-1]["num_doc"])
            novo_recebimento["num_doc"] = ultimo_cod_cli+1
            editor.writerow(novo_recebimento)
        print("Recebimento registrado!")

            

cadastro_recebimento("12","18-12-2000","18-12-2000","2")
