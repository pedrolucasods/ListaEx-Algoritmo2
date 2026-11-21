import csv
from pathlib import Path

pasta_atual = Path(__file__).resolve().parent
caminho_arquivo = pasta_atual.parent / "exercicio01" / "clientes.csv"

def cadastrar_clientes(nome,endereco,fone):
    cliente_novo = {"nome":str(nome).lower(),"endereco":str(endereco).lower(),"fone":str(fone).lower()}
    if(all(valores == "" or valores == None for valores in cliente_novo.values())):
        print("Cliente Inválido!")
        return
    if(not caminho_arquivo.exists()):
        print("O arquivo não existe!")
    else:
        with open(caminho_arquivo,"r+",newline="",encoding="utf-8-sig") as arquivo:
            leitor = csv.DictReader(arquivo,delimiter=";")
            campos = leitor.fieldnames
            dados = list(leitor)

            arquivo.seek(arquivo.tell() - 1)
            if arquivo.read(1) != "\n":
                arquivo.write("\n")
            
            editor = csv.DictWriter(arquivo,fieldnames=campos,delimiter=";")
            if not dados:
                cliente_novo["cod_cli"] = 1
                editor.writerow(cliente_novo)
                print("Cliente Cadastrado!")
            else:
                cliente_igual = False
                for cliente in dados:
                    cliente_antigo = {"nome":cliente["nome"],"endereco":cliente["endereco"],"fone":cliente["fone"]}
                    if(cliente_antigo == cliente_novo):
                        cliente_igual = True
                        break
                if(cliente_igual):
                    print("Já cliente já está cadastrado!")
                else:
                    ultimo_cod_cli =  int(dados[-1]["cod_cli"])
                    cliente_novo["cod_cli"] = ultimo_cod_cli+1
                    editor.writerow(cliente_novo)
                    print("Cliente Cadastrado!")



cadastrar_clientes("Jocaas3","aasdjf","eitakd")