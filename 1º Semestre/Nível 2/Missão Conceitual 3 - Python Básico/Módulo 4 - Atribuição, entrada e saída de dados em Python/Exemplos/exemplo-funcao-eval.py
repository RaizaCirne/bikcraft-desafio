# A função eval() recebe uma string, mas trata como um valor numérico

s = '1 + 2'
type(s)

# Para tratar a entrada do usuário como um número e, com isso, realizar operações algébricas, por exemplo, é necessário utilizar a função eval() em conjunto com a input(), veja:

numero = eval(input('Entre com um inteiro: '))
numero = numero + 2
print(numero)
