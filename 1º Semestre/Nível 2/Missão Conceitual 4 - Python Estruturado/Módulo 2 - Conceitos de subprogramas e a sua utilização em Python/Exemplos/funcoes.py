# Implementar uma solução em Python que retorne o menor elemento de uma lista.

def encontrar_minimo(lista):      # palavra chave def é a definição de função # encontrar_minimo é o nome que dou para a função # Passei o parâmetro que é a lista
    minimo = lista[0]             # minimo = lista[0] -> O menor elemento é o primeiro, é uma hipótese.
    for elem in lista:            # Implementação de solução usando PROGRAMAÇÃO FUNCIONAL
        if(elem < minimo):        # Testando elemento # Se o elemento for menor que o elemento que chamei de minimo, então quem vai ser o minimo vai ser o elemento
        minimo = elem             # minimo vai ser o elemento
    return minimo             # retorno o menor elemento

lista_teste = [2, 10, 3, 1, 4, 5]
menor = encontrar_minimo(lista_teste)
print('O menor elemento da lista é [{}]'.format(menor))