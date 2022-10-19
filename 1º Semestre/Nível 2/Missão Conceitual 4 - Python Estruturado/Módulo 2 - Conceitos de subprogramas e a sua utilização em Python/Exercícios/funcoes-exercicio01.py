# Implementar uma solução em Python que retorne a soma de todos os elementos pares de uma lista

def ehPar(n):               #função para verificar se o elemento é par #função recebe um parâmetro
    r = (n%2==0)            # Pergunto se resto da divisão é zero, se for, vai retornar verdadeiro
    return r                # Se não for par retorna o resultado return

def somar_par(lst):         #Somatório recebeu o parametro da lista, o lst
    soma=0                  #Tenho uma variável acumuladora, a soma
    for num in lst:         # Varrer a lista
        if(ehPar(num)):     # Se o num for par
            soma=soma+num   # Faz a soma
    return soma             #Se for par retorna a soma

lista = [10, 2, 5, 7, 6, 3] # Tenho a lista e os elementos
soma=somar_par(lista)       # Passo a lista pro somar_par #Quero que ele some apenas os elementos pares da lista
print(f'O somatório dos elementos pares da lista é: {soma}')