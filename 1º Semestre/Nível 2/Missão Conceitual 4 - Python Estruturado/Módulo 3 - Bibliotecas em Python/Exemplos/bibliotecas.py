#Implementar uma solução em Python que calcule as raízes de uma equação do segundo grau
#Exemplo: dada a equação x² + 5x + 6 = -, as raízes são {-3, -2}.

def entrada_dados():                       # Função que vai me ajudar a entrar com os dados
    coeficiente = quantidade = eval(input('Digite o valor do coeficiente: ')) #usuário digita os dados aqui
    return coeficiente

def calc_delta(a,b,c):                     # Calcula o delta - recebe a,b e c
    delta = b*b-4*a*c
    return delta

import numpy as np                        #Usando o pacote numpy para resolver este problema

def calcular_raizes(a,b,c,delta):         #Recebendo coeficientes a, b, c e recebendo também o delta.
    if(delta<0):                          # Aqui começam os testes
        resultado='A equação não possui raízes ou números reais'
    elif(delta==0):
        x=-b/(2*a)
        resultado=f'A equação possui apenas a raíz: {x}'
    else:
        x1 = (-b-np.sqrt(delta))/(2*a)       #np.sqrt é a raiz quadrada de delta
        x2 = (-b+np.sqrt(delta))/(2*a)
        resultado=f'A equação possui as raízes: {x1}, {x2}'
    return resultado

# Agora temos o resultado
#f(x)=ax^2+bx+c
a = entrada_dados()
b= entrada_dados()
c = entrada_dados()

delta=calc_delta(a,b,c)

resultado=calcular_raizes(a,b,c,delta)
print(resultado)