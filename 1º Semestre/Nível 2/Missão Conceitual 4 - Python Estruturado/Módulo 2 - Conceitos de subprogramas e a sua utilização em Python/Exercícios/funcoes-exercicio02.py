#Implementar uma solução em Python que calcule o fatorial de um número
# Fatorial é N! = (N - 1)!
# 0! = 0
# 1! = 1

# Estratégia 01 (iterativa - mais comum)
def fatorial_iterativo(n):
    f=1                         # Vai ser meu acumulador
    for i in range(1, n+1):
        f=f*i                   # Acumulo de multiplicações
    return f

# Estratégia 02
def fatorial_recursivo(n):
    if((n==0) or (n==1)):             #Se n for igual a zero ou n for igual a 1
        return 1                      # retorno 1
    return n*fatorial_recursivo(n-1)  #Se nao for faz a chamada recursiva

numero = 5
print(f'O fatorial de {numero} é: {fatorial_iterativo(numero)}')
print(f'O fatorial de {numero} é: {fatorial_recursivo(numero)}')