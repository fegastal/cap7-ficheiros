'''Podemos visualizar os dados ao extrair as temperaturas relativas a Portugal.

1) A solução apresentada cumpre seu papel, mas não deixa de ter um defeito importante:
não sabemos a que cidade corresponde cada curva. Mas existe uma solução:
alterar o ficheiro de modo que, no início de cada linha, esteja o nome da cidade. depois, é só alterar
a função que lê uma linha e a função que mostra os resultados, como a seguir.

2) Primeiro obtemos os dados e depois visualizamos o resultado. A extração de dados é feita retirando a info relevante
por cada cidade e colocando-a num dicionário. Este dicionáriotem por chaves os nomes das cidades. A cada uma delas
está associado um outro dicionário com duas chaves: pluviosidade e temperatura. Os respectivos valores são guardados
numa lista.

def main(fich):
    dicio = dados_portugal(fich)
    mostra(dicio)

def dados_portugal(fich):
    f_ent = open(fich, 'r')
    portugal = dict()

    ficha = le_cidade(f_ent)
    while ficha != -1:
        cidade, pluviosidade, temperatura = ficha
        portugal.update({cidade:{'pluviosidade':pluviosidade, 'temperatura':temperatura}})
        ficha = le_cidade(f_ent)
    f_ent.close()
    return portugal

def le_cidade(f_ent):
    #Procura a primeira linha significativa
    linha = f_ent.readline()

    while (linha !='') and (linha == '\n'):
        linha = f_ent.readline()

    if linha == '':
        return -1
    else:
        #Extrai dados
        cidade = linha[:-1]
        pluviosidade = [float(dado) for dado in f_ent.readline()[:-1].split('\t')[1:]]
        temperatura = [float(dado) for dado in f_ent.readline()[:-1].split('\t')[1:]]
        return (cidade, pluviosidade, temperatura)

#Resolvendo a visualização:

def mostra(dados):
    meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro',
    'Novembro', 'Dezembro']
    chuva = []
    cidades = []
    temp = []
    for c, v in dados.items():
        chuva.append(v['pluviosidade'])
        temp.append(v['temperatura'])
        cidades.append(c)

    figura = plt.figure()
    fig_1 = figura.add_subplot(211)
    plt.title('Cidades de Portugal')
    fig_2 = figura.add_subplot(212)

    for indice in range(len(cidades)):
        fig_1.plot(chuva[indice])
        fig_2.plot(chuva[indice])

    fig_1.set_ylabel('Pluviosidade (mm)')
    fig_2.set_xlabel('Temperatura (C)')
    plt.xticks(range(0,12), meses, rotation = 17)
    plt.legend(cidades, loc=0)

    plt.show()

'''

import matplotlib.pyplot
plt = matplotlib.pyplot


def le_todas_temperaturas(fich):
    with open(ficheiro, 'r') as f_ent:
        portugal = list()
        dados = le_uma_temperatura(f_ent)
        with dados != -1:
            portugal.append(dados)
            dados =  le_uma_temperatura(f_ent)
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
        dados = [float(dado) for dado in linha [1:]]
        return cidade, dados

def mostra_todas(xetiq, yetiq, tit, dados):
    plt.xlabel(xetiq)
    plt.ylabel(yetiq)
    plt.title(tit)
    for cidade in dados:
        cidade = dado[0]
        plt.plot(dado[1], label = cidade)
        plt.legend()

def main(ficheiro):
    dados = le_todas_temperaturas(ficheiro)
    mostra_todas('Meses', 'Temperatura', 'Temperaturas Médias das Cidades')
    plt.show()

if __name__ == '__main__':
    main('/data/temperaturas.txt')