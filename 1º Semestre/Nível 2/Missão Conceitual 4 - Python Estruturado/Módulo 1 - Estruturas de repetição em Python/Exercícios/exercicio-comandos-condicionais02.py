# Implementar uma solução em Python que resolva a seguinte questão:
# - Se a nota for maior ou igual a 7, o estudante foi aprovado.
# - Se a nota for menor que 7 e maior ou igual a 5, o estudante está em recuperação.
# - Se a nota for menor que 5, o estudando está reprovado

media = 8.5

if(media>=7.0):
  situacao = "Aprovado"
elif(media>=5.0):
  situacao = "Em recuperação"
else:
  situacao = "Reprovado"

print(f'O estudante está: {situacao}')
