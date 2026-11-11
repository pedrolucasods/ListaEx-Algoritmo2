# 9- Escala Crítica de Plantão Médico: Um hospital fornece uma lista onde cada elemento
# é uma sublista com os dias do mês em que um médico específico pode trabalhar. O
# diretor quer saber qual é o dia do mês que tem a menor cobertura de profissionais.
# Retorno exigido: O dia (número) com a menor quantidade de médicos
# disponíveis e uma lista com os índices (IDs) dos médicos que farão plantão
# nesse dia crítico.

def validar_escala(lista):
    todos_dias = []
    for medico in lista:
        for dia_plantao in medico:
            todos_dias.append(dia_plantao)
    qtd_medico_no_dia = []

    for dia in todos_dias:
        contador = 0
        for i in range(len(todos_dias)):
            if(dia == todos_dias[i]):
                contador+=1
        if([dia,contador] not in qtd_medico_no_dia):
            qtd_medico_no_dia.append([dia,contador])

    dia_critico,qtd = qtd_medico_no_dia[0][0],qtd_medico_no_dia[0][1]
    for item in qtd_medico_no_dia:
        if(item[0] == dia_critico):
            pass
        else:
            if(item[1]<qtd):
                dia_critico,qtd = item[0],item[1]

    dias_criticos = []
    dias_criticos.append(dia_critico)
    for outro_dia in qtd_medico_no_dia:
        if outro_dia[0] in dias_criticos:
            pass
        else:
            if(outro_dia[1] == qtd):
                dias_criticos.append(outro_dia[0])

    medicos_dia_critico = []
    for medico_dia in lista:
        for dias in medico_dia:
            if(dias in dias_criticos and lista.index(medico_dia) not in medicos_dia_critico):
                medicos_dia_critico.append(lista.index(medico_dia))

    dados = {
        "Quantidade medicos de cada dia":qtd_medico_no_dia,
        "Dia com menor número de médicos ":dias_criticos[0] if len(dias_criticos) == 1 else dias_criticos,
        "Medicos do dia critíco": medicos_dia_critico
    }

    return dados

plantao = [
    [1,2,3,4,6],
    [2,4,6,7],
    [1,3,4,7,9],
    [4,8]
]

dados = validar_escala(plantao)

for key,value in dados.items():
    print(f"{key}:{value}")