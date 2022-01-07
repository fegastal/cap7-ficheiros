'''Uso das operações de leitura de um ficheiro'''

meu_ficheiro = open('toto.txt', 'r')
todo_ficheiro = meu_ficheiro.read()
todo_ficheiro

#'Um ficheiro pequeno,\ncom caracteres estranhos.\n\npara testar a leitura \\n de\nficheiros.\ne outras coisas \\t mais!'

print(todo_ficheiro)
#Um ficheiro pequeno,
#com caracteres estranhos.
#para testar a leitura \n de
#ficheiros.
#e outras coisas \t mais!

meu_ficheiro.close()
meu_ficheiro = open('toto.txt', 'r')
uma_linha = meu_ficheiro.readline()
uma_linha
#'Um ficheiro pequeno,\n'

print(uma_linha)
#'Um ficheiro pequeno,\n'

meu_ficheiro.close()
meu_ficheiro = open('toto.txt', 'r')
lista_linhas = meu_ficheiro.readlines()
lista_linhas
#['Um ficheiro pequeno\n', 'com caracteres estranhos.\n','\n', 'para testar a leitura \\n de\n', 'ficheiros.\n',
#'e outras coisas \\t mais!']

meu_ficheiro.close()
meu_ficheiro = open('toto.txt', 'r')
alguns_caracteres = meu_ficheiro.read(10)
alguns_caracteres
#'Um ficheir'
alguns_caracteres = meu_ficheiro.read(10)
alguns_caracteres
#'o pequeno,\ncom '