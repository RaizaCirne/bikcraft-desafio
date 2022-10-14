# O interpretador Python pode procurar o mesmo nome de variável em diferentes escopos.
def multiplicador(numero):
    return a * numero


a = 3  # esta variável tem escopo global
b = multiplicador(5)
print(f"A variável b vale: {b}")

# Na linha 7, ao se chamar a função do multiplicador(), a variável a será procurada.
# Como não existe uma variável a no bloco interno da função, ela é procurada como variável global.
# Uma vez encontrada, o valor recuperado é 3.
