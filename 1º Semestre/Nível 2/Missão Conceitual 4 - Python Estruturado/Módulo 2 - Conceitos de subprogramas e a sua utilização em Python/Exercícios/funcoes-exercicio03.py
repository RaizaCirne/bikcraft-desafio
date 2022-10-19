#Implementar uma solução em Python que determine se um Número é ou não Primo.
# N/N ou N/1

def eh_primo(n):               #Recebi o n, o número
    if(n<2):                   #Primeiro teste: Se n for menor que 2 eu ja retorno falso, pois por definição o menor numero primo é 2
        return False           # Retorna falso
    i=n//2                     # Dividir o n por 2 - // divisão inteira
    while(i>1):                # Enquanto i for maior do que 1 fazer o teste
        if(n%i==0):            # Se n for divisivel por i quer dizer que não é primo
            return False
        i=i-1                   # Se isso não for verdade diminuir
    return True

def imprimir_resultado(numero, resultado):
    mensagem = f'O número {numero} NÃO é primo'
    if(resultado):
        mensagem= f'O número {numero} é primo'
        return mensagem


numero = 7                                  #Entramos com um número
resultado=eh_primo(numero)                  #Retornou verdadeiro ou falso se o número é ou não primo
msg=imprimir_resultado(numero, resultado)   #Implementei outra função chamada imprimir_resultado que vou passar um número e o valor do resultado, ou seja, verdadeiro ou falso
print(msg)                                  #Imprimir mensagem