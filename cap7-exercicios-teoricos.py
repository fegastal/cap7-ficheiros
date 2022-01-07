'''Exercícios Teóricos | Capítulo 7

1) Quais são as características dos ficheiros?

Ficheiros são locais nos quais guardamos informação de forma permanente.
Existem dois tipos:

a) de texto: uma (eventualmente muito longa) cadeia de caracteres.
b) binários


2) Como identificar um ficheiro vazio?

>>> import os
>>> os.stat("file").st_size == 0
True


3) Qual é o construtor do tipo ficheiro?

<nome_ficheiro>.<operação>.


4) Qual é a diferença entre seek e tell?

O comando tell nos indica a posição da janela relativamente ao início do ficheiro.
O comando seek nos permite reposicionar a janela. O funcionamento dele depende do tipo de ficheiro (binário ou texto).

tell - fich.tell() - indica a posição relativamente ao início
seek - fich.seek(pos,como=0) - movimenta para nova posição


5) Só existem ficheiros de texto? Senão, que outros tipos existem e quais são as diferenças?

Existem também ficheiros binários. Um arquivo binário é todo arquivo de computador que não está
em formato texto. Ele pode ser um programa de computador, arquivo de imagem digital, arquivo de
som, biblioteca compartilhada, arquivo de dados e vários outros arquivos. Qualquer arquivo que não
esteja em formato de texto, é considerado um arquivo binário.

Arquivos binários podem ter qualquer tipo de padrão em seus valores. Exemplos de arquivos binários
são os executáveis PE e ELF, que são formatos de arquivos executáveis dos sistemas Windows e Linux
respectivamente. Outro exemplo seria os formatos de arquivos de imagem BMP ou PNG, onde os arquivos
são usados para armazenar informações como cor e luminosidade de cada pixel de uma imagem.

No fim um arquivo binário não é muito diferente de um arquivo de texto. Com a diferença que
cada byte de um arquivo de texto é usado para representar um caractere, e em arquivos binários cada
byte pode ser usado para representar qualquer valor.


6) Os ficheiros de texto são uma longa cadeia de caracteres. Existe a operação de fatiamento para ficheiros?

Uma operação muito interessante que Python fornece para manipulação de strings é
o fatiamento (slicing). Fatiamento significa extrair apenas uma parte da string, ou seja,
uma substring. Com essa operação, podemos delimitar os limites inferior e superior do pedaço
da string que queremos acessar. Por exemplo, se quisermos acessar a substring da posição 0 até a posição
4 na string s original, podemos fazer o seguinte:

>>> print s[0:5]
'hello'
>>> print s[:5]
'hello'
>>> print s[2:4]
ll
>>> print s[7:13]
'world!'
>>> print s[7:]
'world!'
>>> print s[:]
'hello, world!'

url = "http://localhost:8000/arquivo.iso"
protocolo = url[0:url.index(':')]


7) É possível ter um ficheiro aberto simultaneamente para leitura e para escrita?

Não, a escrita em um ficheiro é a operação inversa da leitura.
<ficheiro>.write(<cadeia_de_caracteres>)


8) Qual é a importância de usar sempre o método close?

É uma boa prática de programação fechar qualquer ficheiro que já não esteja sendo usado.
Usar a operação close, aplicada ao nome associado ao ficheiro:

meu_ficheiro.close()

Desse modo, além de libertarmos espaço, evitamos eventuais corrupções da informação guardada no caso de acontecer
alguma situação anômala.


9) Para que serve a construção with?

Gestores de contexto - são objetos que têm associadas duas operações, uma de entrada e outra de saída.
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


10) O que é o tipo de dados bytes?

Os bytes representam todas as letras (maiúsculas e minúsculas), sinais de pontuação, acentos,
caracteres especiais e até informações que não podemos ver, mas que servem para comandar o
computador e que podem inclusive ser enviados pelo teclado ou por outro dispositivo de entrada de dados e instruções.

Para que isso aconteça, os computadores utilizam uma tabela que combina números binários com símbolos:
a tabela ASCII (American Standard Code for Information Interchange). Nela, cada byte representa um
caractere ou um sinal.

1 Byte = 8 bits

8 bits => palavra de 1 byte


11) O que é e para que serve o módulo csv?

O chamado formato CSV (Comma Separated Values) é o formato mais comum de importação e exportação de
planilhas e bancos de dados.

O módulo csv implementa classes para ler e gravar dados tabulares no formato CSV.
Ele permite que os programadores digam “escreva esses dados no formato preferido pelo Excel”
ou “leia os dados desse arquivo gerado pelo Excel”, sem conhecer os detalhes precisos do formato CSV
usado pelo Excel. Os programadores também podem descrever os formatos CSV entendidos por outros aplicativos
ou definir seus próprios formatos CSV para fins especiais.

Os objetos de reader e writer do módulo csv leem e escrevem sequências. Os programadores também
podem ler e gravar dados no formato de dicionário usando as classes DictReader e DictWriter.

>>> import csv
>>> with open('eggs.csv', newline='') as csvfile:
...     spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
...     for row in spamreader:
...         print(', '.join(row))
Spam, Spam, Spam, Spam, Spam, Baked Beans
Spam, Lovely Spam, Wonderful Spam

import csv
with open('eggs.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
    spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])


12) O que é e para que serve o módulo urllib?

É o módulo de manipulação de URL para python. É usado para buscar URLs (Uniform Resource Locators).
Ele usa a função urlopen e é capaz de buscar URLs usando uma variedade de protocolos diferentes.

Urllib é um pacote que coleta vários módulos para trabalhar com URLs, como:

urllib.request para abrir e ler.
urllib.parse para análise de URLs
urllib.error para as exceções levantadas
urllib.robotparser para analisar arquivos robots.txt

Se o urllib não estiver presente em seu ambiente, execute o código abaixo para instalá-lo.
pip install urllib

urllib.request ajuda a definir funções e classes para abrir URLs (principalmente HTTP).
Uma das maneiras mais simples de abrir esses URLs é:

urllib.request.urlopen (url)

import urllib.request
request_url = urllib.request.urlopen('https://www.geeksforgeeks.org/')
print(request_url.read())

O código-fonte da URL, ou seja, Geeksforgeeks.

urllib.parse.urlparse	Separa diferentes componentes de URL
urllib.parse.urlunparse	Junte diferentes componentes de URL
urllib.parse.urlsplit	É semelhante a urlparse(), mas não divide os parâmetros
urllib.parse.urlunsplit	Combina o elemento de tupla retornado por urlsplit() para formar URL
urllib.parse.urldeflag	Se o URL contiver fragmento, ele retornará um URL removendo o fragmento.


'''
