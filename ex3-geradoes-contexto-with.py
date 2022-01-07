'''Por defeito, quando esamos a escrever num ficheiro, os dados vão primeiro para uma memória tampão
e só posteriormente são escritos em disco. A operação de fecho de um ficheiro começa por esvaziar a memória
tampão e só depois fecha efetivamente o ficheiro.

Podemos forçar o esvaziamento recorrendo ao método flush.

O fato de se usar uma memória tampão pode colocar problemas caso haja um fim inesperado da execução do programa devido a
um erro. Podemos evitar o uso desse ipo de memória com um parâmetro adicional no método open, mas tal tem custos
ao nível de desempenho.

Deve, pois, ser pesado o uso, ou não, da memória tampão e como o método flush nos pode ajudar.

Podemos garantir que o ficheiro seja encerrado de forma conveniente, mesmo quando ocorre uma interrupção anormal do
programa. A solução baseia-se no conceito de GESTORES DE CONTEXTO e no uso da instrução WITH.

a) gestores de contexto - são objetos que têm associadas duas operações, uma de entrada e outra de saída.
São executadas quando se entra ou se sai de um contexto, respectivamente.

A instrução with define um contexto, tendo como sintaxe:

with expressao as var:
    bloco

A parte as var é opcional; expressao tem de ser, ou gerar, um gestor de contexto;
var é o nome que vai ficar associado ao objeto. É como se tivesse sido feita uma atribuição do nome var à expressão.
Acontece que o objetivo devolvido pela instrução open é um gestor de contexto. Podemos, então, fazer algo como:

with open(ficheiro, 'r', as meu_fich:
    bloco

Assim, temos a garantia de que, mesmo que ocorra um erro durante a execução do bloco, o ficheiro será fechado.

'''