palavra = input('Entre com uma palavra: \n')                  # A linha 1 representa a solicitação ao usuário para que ele insira uma palavra a ser armazenada na variável palavra;
while palavra != 'sair':                                      # A linha 2 cria o laço while, que depende da condição <valor da variável palavra ser diferente de ‘sair’>;
    palavra = input('Digite sair para encerrar o laço: \n')   # A linha 3 será repetida enquanto a condição for verdadeira, ou seja, enquanto o valor da variável palavra for diferente de ‘sair’. Quando esses valores forem iguais, a condição do laço while será falsa e o laço, encerrado;
print('Você digitou sair e agora está fora do laço')          # A linha 4 representa a impressão da mensagem fora do laço while.

#obs: Perceba que, ao digitar ‘sair’ logo na primeira solicitação, a linha 3 do nosso programa não é executada nenhuma vez. Ou seja, o programa nem chega a entrar no laço while.