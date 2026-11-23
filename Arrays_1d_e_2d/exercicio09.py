# 9 - Desenvolva um programa completo em Python nativo para controle de estoque de
# uma empresa. Utilize duas listas paralelas: `produtos` (strings) e `quantidades`
# (inteiros). Implemente um menu interativo dentro de um laço `while` com as opções: 1.
# Cadastrar Produto; 2. Listar Estoque; 3. Atualizar Quantidade; 4. Excluir Produto; 5.
# Sair. Garantir a integridade dos índices sincronizados entre as duas listas.
import os

produtos = []
quantidades = []

while True:
    print(f'########### Menu ########### \n1 - Cadastrar Produto\n2 - Listar Estoque\n3 - Atualizar Quantidade\n4 - Excluir Produto\n5 - Fechar Sistema')
    opcao = int(input('Informe um opção: '))
    match opcao:
        case 1:
            os.system('cls')
            print('======= Cadastro =======')
            msg = ''
            novo_produto = input('Informe o nome do produto: ')
            quantidade_inicial = int(input('Informe a quantidade inicial: '))
            if(novo_produto.title() not in produtos) or (quantidade_inicial>=0):
                produtos.append(novo_produto.title())
                quantidades.append(quantidade_inicial)
                msg = f'Produto "{novo_produto.title()}" cadastrado!\n'
            else:
                print("Produto já existente ou Quantidade Inválida!")
            os.system('cls')
            print(msg)
        case 2:
            os.system('cls')
            print('======= Estoque =======')
            if(produtos):
                for i in range(len(produtos)):
                    print(f"{i+1} - {produtos[i]} = {quantidades[i]}")
            else:
                print("Sem Produtos Informados!")
            input('\nPress Enter..')
            os.system('cls')
        case 3:
            os.system('cls')
            print('======= Atualizar Quantidade =======')
            if(produtos):
                for i in range(len(produtos)):
                    print(f"{i+1} - {produtos[i]} = {quantidades[i]}")
                produto = int(input('Informe o Número do Produto: '))
                if(produto < 1 or produto >len(produtos)):
                    print('Produto Inválido!')
                else:
                    print(f"{produtos[produto-1]} = {quantidades[produto-1]}")
                    quantidade_nova = int(input('\nInforme a novo Quantidade:'))
                    if(quantidade_nova>=0):
                        quantidades.pop(produto-1)
                        quantidades.insert(produto-1,quantidade_nova)
                        os.system('cls')
                        print("Quantidade Atualizada!\n")
                    else:
                        print('Quantidade Inválida!')
            else:
                os.system('cls')
                print("Sem Produtos Cadastrados!")
                input('\nPress Enter..')
        case 4:
            os.system('cls')
            print('======= Deletar Produto =======')
            if(produtos):
                for i in range(len(produtos)):
                    print(f"{i+1} - {produtos[i]} = {quantidades[i]}")
                produto = int(input('Informe o Número do Produto: '))
                if(produto < 1 or produto>len(produtos)):
                    print('Produto Inválido!')
                else:
                    produto_deletado = produtos.pop(produto-1)
                    if(produto_deletado not in produtos):
                        quantidades.pop(produto-1)
                        os.system('cls')
                        print(f'Produto "{produto_deletado}" foi deletado!')
                    else:
                        print("Produto Não foi Deletado!")
                    
            else:
                os.system('cls')
                print("Sem Produtos Cadastrados!")
            input('\nPress Enter..')
        case 5:
            os.system('cls')
            print("Sistema Encerrado!")
            break
        case _:
            os.system('cls')
            print('Opção Inválida!\n')
