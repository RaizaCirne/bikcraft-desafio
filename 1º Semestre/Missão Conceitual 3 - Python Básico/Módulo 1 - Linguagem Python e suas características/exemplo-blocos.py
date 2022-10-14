""" Blocos: São definidos pela identação
Todos os blocos são iniciados com : (dois pontos) na linha superior
e representados pelo acréscimo de 4 espaços a esquerda."""

# Exemplo de blocos em Python
a = 0
for i in range(30):
    if a % 2 == 0:
        a += 1
        continue
    else:
        if a % 5 == 0:
            break
        else:
            a += 3
print (a)
