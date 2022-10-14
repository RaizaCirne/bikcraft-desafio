# Atribuição múltipla
a, b = 1, 2
print('Antes da troca')
print(f"O valor das variáveis: a={a}, b={b}")
# Primeira troca
temp = a
a = b
b = temp
print ('Primeira troca')
print(f"O valor das variáveis: a={a}, b={b}")
# Segunda troca
a, b = b, a
print('Segunda troca')
print(f"O valor das variáveis: a={a}, b={b}")