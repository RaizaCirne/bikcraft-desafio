# Implementar uma solução em Python que faça o tratamento de exceção para verificar se a entrada é, de fato, um número.

try:                                                #Bloco try/clausula try
    x = int(input("Digite um número: "))            # Tentando seguir o fluxo normal. Pedindo para o usuário digitar um número e convertendo para um inteiro
except ValueError:                                  # Se o usuário entrar com letra o programa vai quebrar o fluxo. Vai gerar uma exceção do tipo ValueError:
    print("Entre com um número válido.")           # Vai aparecer a mensagem que eu quero que apareça para o usuário