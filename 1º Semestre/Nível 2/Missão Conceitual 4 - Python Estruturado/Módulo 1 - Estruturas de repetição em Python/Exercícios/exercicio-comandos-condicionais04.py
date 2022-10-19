#Implementar uma solução em Python que some todos os números pares de uma lista.
# Por exemplo, se a lista for [10,2,5,7,6,3], o resultado deve ser igual a 18.

#Estratégia 01

lista = [10, 2, 5, 7, 6, 3]  # Entramos com a lista
n=len(lista)                 # Calcular o comprimento da lista - o n=len(lista) significa que o n é igual a 6, pois temos 6 elementos na lista
soma=0                       # Criação de uma variável que vai acumular a soma
for i in range(n):           # Percorrer os elementos dentro de um range/intervalo # o n é 6, então o range(n) vai gerar 0, 1, 2, 3, 4, 5. São 6 elementos, mas a indexação começa a partir do zero. # O i vai ser 0, depois vai ser 1, depois 2 até chegar o 5.
  if(lista[i]%2==0):         # Fazer o teste - Se tiver resto 0 o elemento é par
    soma=soma+lista[i]       # Se o elemento é par faz a soma aqui, se não for, não leva em consideração e passa para o próximo
print(f'O somatório dos elementos pates da lista é: {soma}')

#Estratégia 02
# Usa melhor a programação funcional

lista = [10, 2, 5, 7, 6, 3]   #Recebi a lista

soma=0                        # Variável acumuladora
for num in lista:             # Laço #num pega os elementos da lista
  if(num%2==0):               # Teste
    soma=soma+num
print(f'O somatório dos elementos pares da lista é: {soma}')