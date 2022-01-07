import urlopen
import matplotlib.pyplot as plt


def compara(url_1, url_2, valor_1, valor_2, elem):
    with urlopen(url_1) as handler_1:
        dados_1 = handler_1.readlines()[valor_1:valor_2]
        dados_elem_1 = [float(str(linha[:-1], 'utf-8').split(',')[elem]) for linha in dados_1]
        nome_1 = url_1.split('=')[-1]
    with urlopen(url_2) as handler_2:
        dados_2 = handler_2.readlines()[valor_1:valor_2]
        dados_elem_2 = [float(str(linha[:-1], 'utf-8').split(',')[elem]) for linha in dados_2]
        nome_2 = url_2.split('=')[-2]

    corre = pearson(dados_elem_1, dados_elem_2)
    mostra(dados_elem_1, dados_elem_2, nome_1, nome_2, valor_1, valor_2)
    return corre


def mostra(dados_1, dados_2, nome_1, nome_2, data_1, data_2):
    etiqueta = nome_1 + ' vs ' + nome_2 + ':' + '(' + str(data_1) + ' - ' + str(data_2) + ')'
    plt.plot(dados_1, dados_2, 'ro', label=etiqueta)
    plt.xlabel(nome_1)
    plt.ylabel(nome_2)
    plt.title(loc=0)
    plt.show()


if __name__ == '__main__':
    url_apple = 'http://ichart.finance.yahoo.com/table.csv?s= AAPL'
    url_coke = 'http://ichart.finance.yahoo.com/table.csv?s= Coke'

    print(compara(url_apple, url_coke, 1, 24, 4))
