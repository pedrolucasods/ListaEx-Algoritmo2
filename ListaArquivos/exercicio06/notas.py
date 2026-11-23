import csv,os
from pathlib import Path

pasta_atual = Path(__file__).parent
caminho_arquivo_notas = pasta_atual / "notas.csv"

def criar_arquivo():
    campos = ["numero","nome","nota_1","nota_2"]
    if(caminho_arquivo_notas.is_file()):
        print("Arquivo Já Existe!")
        return
    with open(caminho_arquivo_notas,"w",newline="",encoding="utf-8-sig") as arquivo:
        editor = csv.DictWriter(arquivo,fieldnames=campos,delimiter=";")
        editor.writeheader()
        print("Arquivo Criado!")

def incluir():
    if(not caminho_arquivo_notas.is_file()):
        print("Arquivo Não existe!\nPor Favor crie o Arquivo!")
        return
    with open(caminho_arquivo_notas,"r+",newline="",encoding="utf-8-sig") as arquivo:
        leitor = csv.DictReader(arquivo,delimiter=";")
        campos = leitor.fieldnames
        dados = list(leitor)

        novo_registro = {
            "nome":input("Informe o nome: "),
            "nota_1":float(input("Informe a primeira nota: ")) or 0,
            "nota_2":float(input("Informe a segunda nota: ")) or 0
        }
        os.system('cls')
        if(not novo_registro["nome"]):
            print("Nome inválido!")
            return
        
        arquivo.seek(arquivo.tell()-1)
        if(arquivo.read(1) !="\n"):
            arquivo.write("\n")

        editor = csv.DictWriter(arquivo,fieldnames=campos,delimiter=";")
        if(not dados):
            novo_registro["numero"] = 1
            editor.writerow(novo_registro)
        else:
            ultimo_numero = int(dados[-1]["numero"])
            novo_registro["numero"] = ultimo_numero+1
            editor.writerow(novo_registro)
        arquivo.seek(0)
        next(leitor)
        print("Novo Registro Inserido!")
        novos_dados = list(leitor)
        print("Dados:")
        for registro in novos_dados:
            print("")
            print(f"Nome:{registro["nome"]}\nNota 1:{registro["nota_1"]}\nNota 2:{registro["nota_2"]}\nMedia:{((float(registro["nota_1"])+float(registro['nota_2']))/2):.2f}")
        
def main():
    while True:
        print("======== Menu ========\n1 - Criar Arquivo\n2 - Incluir\n3 - Sair")
        opcao = int(input("Informe uma opcao: "))
        match opcao:
            case 1:
                os.system("cls")
                criar_arquivo()
            case 2:
                os.system("cls")
                incluir()
            case 3:
                os.system("cls")
                print("Flw vlw!...")
                break

main()