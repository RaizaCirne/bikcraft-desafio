def multiplicador(numero):
    a = 2  # esta variável tem escopo local
    print(f"Dentro da função, a variável vale: {a}")
    return a * numero


a = 3  # esta variável tem escopo global
b = multiplicador(5)
print(f"Fora da função, a variável a vale: {a}")

# As linhas 2, 3 e 4 compõem o bloco interno à função chamada multiplicador().
# Embora as variáveis das linhas 2 e 6 tenham o mesmo nome, elas são abstrações a endereços de memória diferentes.
# Dentro da função multiplicador(), a chamada ao nome a recupera o valor 2.
# Fora da função multiplicador(), a chamada ao nome a recupera o valor 3.