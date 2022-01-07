import gzip


def cria_gzip(ficheiro, texto):
    with gzip.open(ficheiro, 'wb') as f:
        f.write(texto)


if __name__ == '__main__':
    prefixo = '/Users/fernandagastal/data/'
    texto = b'Mundo estranho este...'
    cria_gzip(prefixo + 'ficheiro.txt.gz', texto)
