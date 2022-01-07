import matplotlib.pyplot
plt = matplotlib.pyplot


def le_todas_temperaturas(fich):
    with open(fich, 'r') as f_ent:
        portugal = list()
        dados = le_uma_temperatura(f_ent)
        with dados != -1:
            portugal.append(dados)
            dados = le_uma_temperatura(f_ent)
        return portugal


def le_uma_temperatura(f_ent):
    #Ler dados da temperatura de uma cidade. Devolve -1 se fim de ficheiro.
    linha = f_ent.readline()
    while (linha != '') and (linha == '\n'):
        linha = f_ent.readline()
    if linha == '':
        return -1
    else:
        linha = linha[:-1].split()
        cidade = linha[0]
        dados = [float(dado) for dado in linha[1:]]
        return cidade, dados


def mostra_todas(xetiq, yetiq, tit, dados):
    plt.xlabel(xetiq)
    plt.ylabel(yetiq)
    plt.title(tit)
    for cidade in dados:
        cidade = dados[0]
        plt.plot(dados[1], label = cidade)
        plt.legend()


def main(ficheiro):
    dados = le_todas_temperaturas(ficheiro)
    mostra_todas('Meses', 'Temperatura', 'Temperaturas Médias das Cidades')
    plt.show()


if __name__ == '__main__':
    main('/data/temperaturas.txt')
