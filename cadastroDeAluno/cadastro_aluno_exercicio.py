# Crie um sistema de cadastro de alunos utilizando dicionários em Python. Para cada aluno,
# o sistema deverá armazenar seu nome e quatro notas.

# O sistema deverá apresentar um menu de opções para que o usuário possa realizar as seguintes operações:

# -Adicionar um aluno: permitir que o usuário cadastre um novo aluno, informando seu nome e suas quatro notas.
# -Remover um aluno: permitir que o usuário escolha e remova um aluno já cadastrado.
# -Calcular a média de todos os alunos: exibir a média das notas de cada aluno cadastrado.
# -Identificar o aluno com a maior média: informar o nome do aluno que possui a maior média.
# -Exibir todos os alunos: imprimir o nome, as quatro notas e a média de cada aluno cadastrado.
# -Sair do sistema: disponibilizar uma opção para encerrar a execução do programa.

# O programa deverá continuar apresentando o menu e permitindo novas operações até que o usuário escolha a opção de sair.
import json,os,time

def menu():
    while True:
        print(f'########### Menu ########### \n1 - Ver Todos os Alunos\n2 - Cadastrar Aluno\n3 - Remover Aluno\n4 - Media de Todos os Alunos\n5 - Aluno com Maior Média\n6 - Fechar Sistema')
        opcao = int(input('Informe um opção: '))
        match opcao:
            case 1:
                os.system('cls')
                sala = abrir_arquivo()
                print('Turma: ')
                if(sala):
                    for alunos in sala:
                        alunos['media'] = sum(alunos['Notas'])/4
                        print(alunos)
                else:
                    print('Sala Está Vazia')
                while True:
                    input('\nPress Enter..')
                    os.system('cls')
                    break
            case 2:
                os.system('cls')
                novo_aluno = {
                    'Nome':input('Informe o nome do Aluno: '),
                    'Notas':[int(input(f'Informe a {i+1}º do aluno: ')) for i in range(4)]
                }
                salvar_aluno = cadastro(novo_aluno)
                os.system('cls')
                print(salvar_aluno)
            case 3:
                os.system('cls')
                lista = abrir_arquivo()
                if(lista):
                    nome_aluno = input('Informe o nome do Aluno:')
                    nao_encontrado = True
                    for aluno in lista:
                        for key,value in aluno.items():
                            if(key == 'Nome' and value == nome_aluno):
                                nao_encontrado = False
                                lista.remove(aluno)
                                salvar_arquivo(lista)
                                print('Aluno Removido!')
                                break
                    if(nao_encontrado):
                        os.system('cls')
                        print('Aluno Não Encontrado!')
                else:
                    os.system('cls')
                    print('Sua Turma Está Vazia')
                while True:
                    input('Press Enter...')
                    break
            case 4:
                os.system('cls')
                lista = abrir_arquivo()
                if(lista):
                    medias_alunos = [sum(alunos['Notas'])/4 for alunos in lista]
                    media_geral = sum(medias_alunos)/len(medias_alunos)
                    print(f"Media Geral Da Turma: {media_geral}")
                else:
                    print('Sala Está Vazia')
                while True:
                    input('Press enter...')
                    os.system('cls')
                    break
            case 5:
                lista = abrir_arquivo()
                os.system('cls')
                if(lista):
                    medias = [sum(alunos['Notas'])/4 for alunos in lista]
                    alunos_medias_altas = [alunos['Nome'] if (sum(alunos['Notas'])/4 == max(medias)) else 0 for alunos in lista]
                    escolhidos = list(filter(lambda x: x!=0,alunos_medias_altas))
                    print(f"Maior Media : {max(medias)}\nAlunos com essa media:\n{escolhidos}\n")
                else:
                    print('Sala Está Vazia')
                while True:
                    input('Press enter!')
                    os.system('cls')
                    break
            case 6:
                os.system('cls')
                print("Fechando o sistema",end="",flush=True)
                
                for i in range(3):
                    print('.',end='',flush=True)
                    time.sleep(1)
                os.system('cls')
                print('Tenha um bom Dia!')
                break
            case _:
                os.system('cls')
                print('Caso Inválido!')

                


            
def cadastro(aluno):
    chaves_aluno = aluno.keys()
    if("Nome" not in chaves_aluno or "Notas" not in chaves_aluno or len(chaves_aluno) !=2):
        return 'Falha ao Cadastrar Aluno!'
    else:
        if(len(aluno["Nome"]) < 3 or len(aluno['Notas']) < 4 ):
            return 'Informações Inválidas'
        else:
            lista = abrir_arquivo()
            for alunos in lista:
                for chave,valor in alunos.items():
                    if(chave == 'Nome'):
                        if(aluno['Nome'] == valor):
                            return 'Erro, aluno já está cadastrado!'
            lista.append(aluno)
            salvar_arquivo(lista)
            return "Aluno Cadastrado com Sucesso!"

def abrir_arquivo():
    with open("sala.json",'r', encoding='utf-8') as arquivo:
        return json.load(arquivo)

def salvar_arquivo(dados_atual):
    with open('sala.json','w', encoding='utf-8') as arquivo:
        json.dump(dados_atual, arquivo, indent=4, ensure_ascii=False)

menu()


