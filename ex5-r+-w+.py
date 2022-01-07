'''Imaginemos que queremos ler um ficheiro e escrever nele. Exemplo de código:'''

def atualiza_fich(nome_fich, texto):
    with open(nome_fich, 'r+') as f_in_out:
        dados = f_in_out.read()
        print(dados)
        f_in_out.write(texto)
        f_in_out.close()

if __name__ == '__main__':
    nome = '/Users/fernandagastal/data/ficheiro.txt'
    texto = 'complicado'
    atualiza_fich(nome, texto)

#O ficheiro vai ser lido e o conteúdo será impresso.

#Já no modo w+, todo o ficheiro será limpo. Assim, se procurarmos ler este ficheiro antes de escrevermos nele,
#não vamos receber nada. Ex:

def atualiza_fich(nome_fich, texto):
    with open(nome_fich, 'w+') as f_in_out:
        f_in_out.write(texto)
        f_in_out.seek(0)
        dados = f_in_out.read()
        print(dados)
        f_in_out.close()

if __name__ == '__main__':
    nome = '/Users/fernandagastal/data/ficheiro.txt'
    texto = 'complicado'
    atualiza_fich(nome, texto)

#Dessa forma, o ficheiro vai ficar reduzido apenas a uma linha com o texto.