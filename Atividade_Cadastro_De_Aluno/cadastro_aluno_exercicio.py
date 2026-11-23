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
import os,time

sala_de_aula = []

def menu():
    while True:
        print(f'########### Menu ########### \n1 - Ver Todos os Alunos\n2 - Cadastrar Aluno\n3 - Remover Aluno\n4 - Media de Todos os Alunos\n5 - Aluno com Maior Média\n6 - Fechar Sistema')
        opcao = int(input('Informe um opção: '))
        match opcao:
            case 1:
                os.system('cls')
                print('Turma: ')
                if(sala_de_aula):
                    for alunos in sala_de_aula:
                        alunos['media'] = sum(alunos['Notas'])/4
                        print(alunos)
                else:
                    print('Sala Está Vazia')
                
                input('\nPress Enter..')
                os.system('cls')
            case 2:
                os.system('cls')
                novo_aluno = {
                    'Nome':input('Informe o nome do Aluno: ')
                }

                aluno_igual = False
                if(sala_de_aula):
                    for aluno in sala_de_aula:
                        for key,value in aluno.items():
                            if(key == "Nome" and value.lower() == novo_aluno["Nome"].lower()):
                                aluno_igual = True
                                break

                if(aluno_igual):
                    os.system("cls")
                    print("Aluno Já Cadastrado!")
                    input("Press Enter...")
                else:
                    novo_aluno["Notas"] = [int(input(f'Informe a {i+1}º nota do aluno: ')) for i in range(4)]
                    salvar_aluno = cadastro(novo_aluno)
                    os.system('cls')
                    print(salvar_aluno)
            case 3:
                os.system('cls')
                if(sala_de_aula):
                    nome_aluno = input('Informe o nome do Aluno:')
                    nao_encontrado = True
                    for aluno in sala_de_aula:
                        for key,value in aluno.items():
                            if(key == 'Nome' and value.lower() == nome_aluno.lower()):
                                nao_encontrado = False
                                sala_de_aula.remove(aluno)
                                print('Aluno Removido!')
                                break
                    if(nao_encontrado):
                        os.system('cls')
                        print('Aluno Não Encontrado!')
                else:
                    os.system('cls')
                    print('Sua Turma Está Vazia')
                
                input('Press Enter...')
            case 4:
                os.system('cls')
                if(sala_de_aula):
                    medias_alunos = [sum(alunos['Notas'])/4 for alunos in sala_de_aula]
                    media_geral = sum(medias_alunos)/len(medias_alunos)
                    print(f"Media Geral Da Turma: {media_geral:.2f}")
                else:
                    print('Sala Está Vazia')
                
                input('Press enter...')
                os.system('cls')
                
            case 5:
                os.system('cls')
                if(sala_de_aula):
                    medias = [sum(alunos['Notas'])/4 for alunos in sala_de_aula]
                    alunos_medias_altas = [alunos['Nome'] if (sum(alunos['Notas'])/4 == max(medias)) else 0 for alunos in sala_de_aula]
                    escolhidos = list(filter(lambda x: x!=0,alunos_medias_altas))
                    print(f"Maior Media : {max(medias)}\nAlunos com essa media:\n{escolhidos}\n")
                else:
                    print('Sala Está Vazia')
                

                input('Press enter...')
                os.system('cls')
                
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
            for alunos in sala_de_aula:
                for chave,valor in alunos.items():
                    if(chave == 'Nome'):
                        if(aluno['Nome'] == valor):
                            return 'Erro, aluno já está cadastrado!'
            sala_de_aula.append(aluno)
            return "Aluno Cadastrado com Sucesso!"

menu()


