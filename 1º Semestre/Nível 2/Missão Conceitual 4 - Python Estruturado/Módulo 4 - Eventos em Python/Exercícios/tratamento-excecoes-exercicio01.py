# Implementar uma solução em Python que faça o tratamento de exceção para verificar se uma entrada é numérica e que, além disso, insista que o usuário digite um Número válido.

while True:                                            #Comando iterativo. Fica preso aqui até que o usuário entre com valor válido
    try:
        x = int(input("Digite um número: "))
        break                                           #No break ele sai do laço e termina a execução
    except ValueError:
        print("Entre com um número válido.")