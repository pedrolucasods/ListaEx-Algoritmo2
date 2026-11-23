# 8 - Apuração de Urna Eletrônica: Recebemos uma lista gigantesca embaralhada
# contendo os IDs dos candidatos que receberam votos. O voto em branco é o ID 0. O
# sistema não sabe previamente quais são os IDs válidos.
# Retorno exigido: Uma estrutura em formato de lista de listas (ex: [[id,
# total_votos], ...]) resumindo a eleição, o ID do candidato vencedor e a
# porcentagem de votos em branco.
import random

def urna_eletronica(lista):
    candidatos = []
    for id in lista:
        if(id not in candidatos):
            candidatos.append(id)
    total_votos = []
    for candidato in candidatos:
        quantidade_votos = 0
        for voto in lista:
            if(voto == candidato):
                quantidade_votos+=1
        total_votos.append([candidato,quantidade_votos])

    vencedor,qtd = total_votos[0][0],total_votos[0][1]
    for participante in total_votos:
        if(participante[0] == vencedor or participante[0] == 0):
            pass
        else:
            if(participante[1]>qtd or vencedor==0):
                vencedor,qtd = participante[0],participante[1]

    empate = [vencedor]
    qtd_zero = 0
    for p_igual in total_votos:
        if(p_igual[1] == qtd and p_igual[0] not in empate and p_igual[0]!=0):
            empate.append(p_igual[0])
        elif(p_igual[0] == 0):
            qtd_zero = p_igual[1]


    dados = {
        "resumo":total_votos,
        "vencedor":vencedor if len(empate)==1 else f" Houve Empate entres os candidatos {empate}",
        "Quantidade_nulos":f"{((qtd_zero/len(lista_votos)*100))}%"
    }
    return dados

lista_votos = [random.randint(0,3) for i in range(10)]
dados = urna_eletronica(lista_votos)
for key,value in dados.items():
    print(f"{key}:{value}")