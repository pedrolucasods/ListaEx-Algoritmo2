# Implemente uma função recursiva 'potencia(base, expoente)' para calcular a^b 
# para expoentes inteiros >= 0 sem utilizar o operador de potência '**'.

def potencia(base,expoente):
    if(expoente <=0 ):
        return 1
    else:
        return base*potencia(base,expoente-1)

print(potencia(2,4))