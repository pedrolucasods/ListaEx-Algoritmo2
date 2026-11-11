# 7 - Análise de Turbulência em Voo: Os sensores de um avião registram a altitude a cada
# minuto (lista de números). Uma turbulência severa é caracterizada por uma queda de
# altitude maior que 500 metros em um único minuto.
# Retorno exigido: True ou False se houve turbulência severa, e a maior queda
# registrada em um minuto durante todo o voo.

def verificar_altitude(lista):
    if(not len(lista)):
        raise ValueError("Nenhum Registro Encontrado!")
    maior_queda = 0
    severa = False
    if(len(lista)>1):
        for i in range(len(lista)):
            if(i == 0):
                maior_queda = lista[0]-lista[-1] if (lista[0]-lista[-1])>0 else 0
                print(lista[i]-lista[i+1])
                if(maior_queda)>500:
                    severa = True
            else:
                if((i+1) <= len(lista)-1):
                    print(lista[i]-lista[i+1])
                    if(lista[i]-lista[i+1])>500:
                        severa = True
                    if((lista[i]-lista[i+1])>maior_queda):
                        maior_queda=lista[i]-lista[i+1]
                else:
                    break

    dados = {
        "Maior_queda":maior_queda,
        "Severa": severa
    }
    return dados

altitudes = [700,750,200,400,700,1000,100,900,800]
dados = verificar_altitude(altitudes)
for key,value in dados.items():
    print(f"{key}:{value}")


