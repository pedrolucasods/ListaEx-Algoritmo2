import csv,os
from pathlib import Path

pasta_atual = Path(__file__).parent
caminho_arquivo_produto = pasta_atual / "produtos.csv"

def criar_arquivo():
    campos = ["codigo","descricao","preco"]
    if(caminho_arquivo_produto.is_file()):
        print("Arquivo Já Existe!")
        return
    with open(caminho_arquivo_produto,"w",newline="",encoding="utf-8-sig") as arquivo:
        editor = csv.DictWriter(arquivo,fieldnames=campos,delimiter=";")
        editor.writeheader()
        print("Arquivo Criado!")

def cadastrar_produto():
    if(not caminho_arquivo_produto.is_file()):
        print("Arquivo de produtos não existe, crie o arquiv na opção 1 !!")
        return
    novo_produto = {
        "codigo":input('Informe o codigo do produto: ').lower(),
        "descricao":input('Informe a descricao do produto: '),
        "preco":float(input("Informe o preco do produto: "))
    }

    if(any(valor =="" or not(valor) for valor in novo_produto.values())):
        print("Produto Inválido!")
        return

    with open(caminho_arquivo_produto,"r",newline="",encoding="utf-8-sig") as arquivo:
        leitor = csv.DictReader(arquivo,delimiter=";")
        campos = leitor.fieldnames
        dados = list(leitor)
        produto_mesmo_codigo = next(filter(lambda x: x["codigo"].lower() == novo_produto["codigo"],dados),None)
        if(dados and produto_mesmo_codigo):
            print("Produto com mesmo codigo cadastrado!")
            return

    with open(caminho_arquivo_produto,"a",newline="",encoding="utf-8-sig") as arquivo_produto:
        editor = csv.DictWriter(arquivo_produto,fieldnames=campos,delimiter=";")
        editor.writerow(novo_produto)
    print("Produto Cadastrado!")

def listar_todos_produtos():
    if(not caminho_arquivo_produto.is_file()):
        print("Arquivo de produtos não existe, crie o arquiv na opção 1 !!")
        return
    with open(caminho_arquivo_produto,"r",newline="",encoding="utf-8-sig") as arquivo:
        leitor = csv.DictReader(arquivo,delimiter=";")
        dados = list(leitor)

    if(not dados):
        print("Não Existe Produto Cadastrado!")
        return
    print("Dados: ")
    for produto in dados:
        print("")
        print(f"Codigo: {produto["codigo"]}\nDescricao: {produto['descricao']}\nPreco: R${produto['preco']}")
    print("")

def listar_produto_especifico():
    if(not caminho_arquivo_produto.is_file()):
        print("Arquivo de produtos não existe, crie o arquivo na opção 1 !!")
        return

    with open(caminho_arquivo_produto,"r",newline="",encoding="utf-8-sig") as arquivo:
        leitor = csv.DictReader(arquivo,delimiter=";")
        dados = list(leitor)

    if(not dados):
        print("Não Existe Produto Cadastrado!")
        return

    codigo = input("Informe o codigo do produto: ")
    if(not codigo or codigo == ""):
        print("Codigo Inválido!")
        return

    produto = next(filter(lambda x: x['codigo'] == codigo,dados),None)
    if(not produto):
        print("Produto Não Encontrado!")
        return

    for key,value in produto.items():
        print(f"{key}: {value}")
    
def atualizar_produto():
    if(not caminho_arquivo_produto.is_file()):
        print("Arquivo de produtos não existe, crie o arquivo na opção 1 !!")
        return
    
    with open(caminho_arquivo_produto,"r",newline="",encoding="utf-8-sig") as arquivo:
        leitor = csv.DictReader(arquivo,delimiter=";")
        campos = leitor.fieldnames
        dados = list(leitor)

    if(not dados):
        print("Não Existe Produto Cadastrado!")
        return

    codigo = input("Infomre o codigo do produto: ")
    if(not codigo or codigo == ""):
        print("Codigo Inválido!")
        return

    busca_produto = next(filter(lambda x: x['codigo'] == codigo,dados),None)
    if(not busca_produto):
        print("Produto Não Encontrado!")
        return

    index_produto = dados.index(busca_produto)
    novos_dados = {
        "codigo":input("Informe o novo codigo: ") or busca_produto['codigo'],
        "descricao":input("Informe a nova descricao: ") or busca_produto['descricao'],
        "preco":float(input("Informe o nov preco: ")) or busca_produto['preco']
    }

    produto_mesmo_codigo = next(filter(lambda x: x["codigo"] == novos_dados["codigo"] and novos_dados["codigo"]!= busca_produto["codigo"],dados),None)
    if(produto_mesmo_codigo):
        print("Codigo já está sendo utilizado!")
        return

    dados.remove(busca_produto)
    dados.insert(index_produto,novos_dados)

    with open(caminho_arquivo_produto,"w",newline="",encoding="utf-8-sig") as arquivo_produto:
        editor = csv.DictWriter(arquivo_produto,fieldnames=campos,delimiter=";")
        editor.writeheader()
        editor.writerows(dados)
        print("Produto Alterado!")

def deletar_produto():
    if(not caminho_arquivo_produto.is_file()):
        print("Arquivo de produtos não existe, crie o arquivo na opção 1 !!")
        return

    with open(caminho_arquivo_produto,"r",newline="",encoding="utf-8-sig") as arquivo:
        leitor = csv.DictReader(arquivo,delimiter=";")
        campos = leitor.fieldnames
        dados = list(leitor)

    if(not dados):
        print("Não Existe Produto Cadastrado!")
        return
    
    codigo = input("Infomre o codigo do produto: ")
    if(not codigo or codigo == ""):
        print("Codigo Inválido!")
        return

    busca_produto = next(filter(lambda x: x['codigo'] == codigo,dados),None)
    if(not busca_produto):
        print("Produto Não Encontrado!")
        return
    dados.remove(busca_produto)

    with open(caminho_arquivo_produto,'w',newline='',encoding="utf-8-sig") as arquivo_produto:
        editor = csv.DictWriter(arquivo_produto,fieldnames=campos,delimiter=';')
        editor.writeheader()
        editor.writerows(dados)
    print("Produto Deletado!")

def main():
    while True:
        print("=========== Menu ===========\n")
        print("1 - Criar Arquivo\n2 - Cadastrar Produto\n3 - Listar Todos Produto\n4 - Listar Produto Especifico\n5 - Atualizar Produto\n6 - Deletar Produto\n7 - Fechar Sistema")
        opcao = int(input("Informe uma opcao: "))
        match opcao:
            case 1:
                os.system("cls")
                criar_arquivo()
            case 2:
                os.system("cls")
                cadastrar_produto()
            case 3:
                os.system("cls")
                listar_todos_produtos()
            case 4:
                os.system("cls")
                listar_produto_especifico()
            case 5:
                os.system("cls")
                atualizar_produto()
            case 6:
                os.system("cls")
                deletar_produto()
            case 7:
                os.system("cls")
                print("Até mais fio...")
                break
            
main()