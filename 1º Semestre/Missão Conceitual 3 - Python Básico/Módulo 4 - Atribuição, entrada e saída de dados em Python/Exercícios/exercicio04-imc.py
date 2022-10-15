# Como exercício prático, tente escrever um programa para calcular e informar o IMC (índice de massa corpórea) do usuário, que deverá fornecer seu peso e sua altura.
# Lembre-se de que o IMC é calculado pela fórmula: IMC = peso / altura

peso = eval(input('Qual é o seu peso? '))
altura = eval(input('Qual é a sua altura? '))
imc = peso/(altura**2)
print('IMC = ', imc)