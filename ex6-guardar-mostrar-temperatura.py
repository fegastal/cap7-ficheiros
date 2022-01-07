'''Problema de dados climatéricos de algumas cidades de Portugal. Comecemos por uma visão simples
do problema: ler um ficheiro no qual estão guardadas as temperaturas médias mensais ao longo de um dado ano.
Apenas pretendemos ler e mostrar os resultados através de um gráfico:

import matplotlib.pyplot
plt = matplotlib.pyplot

_


def ler(ficheiro):
    with open(ficheiro, 'r') as f_ent:
        dados_car = f_ent.read().split()
        dados = []
        for elem in dados_car:
            dados.append(float(elem))
    return dados

ou:

def ler_1(ficheiro):
    with open(ficheiro, 'r') as f_ent:
        dados_car = f_ent.read().split()
        dados = [float(elem) for elem in dados_car]
    return dados

ou:

def ler_2(ficheiro):
    with open(ficheiro, 'r') as f_ent:
        dados = [float(elem) for elem in f_ent.read().split()]
    return dados

ou:

def ler_3(ficheiro):
    with open(ficheiro, 'r') as f_ent:
        return [float(elem) for elem in f_ent.read().split()]

_

def mostra(xetiq, yetiq, tiit, x, y):
    plt.xlabel(xetiq)
    plt.ylabel(yetiq)
    plt.title(tit)
    plt.plot(x, y)

def main(ficheiro):
    dados = ler(ficheiro)
    mostra('Meses', 'Temperatura', 'Exemplo', range(1, 13), dados)
    plt.show()

if __name__ == '__main__':
    main('/data/dados_simples.txt')


O programa principal executa em sequência duas tarefas:
1) primeiro lê os dados
2) mostra os resultados, por recurso do módulo matplotlib. O ficheiro é aberto para leitura e o contexto
é definido com o recurso à instrução "with". Os dados são lidos de uma só vez e separados pelo método split (linha 6).
Depois, transformamos as cadeias de caracteres que representam os números em algarismos em vírgula flutuante (float).

O código pode ser ainda simplificado nesse aspecto, pois estamos perante um padrão conhecido:
um CICLO que acrescenta no final de uma lista (inicialmente vazia) o resultado de uma certa operação.

Podemos, então, recorrer a listas por COMPREENSÃO. Se eliminarmos as variáveis que são usadas como memória
TEMPORÁRIA, o programa fica menor ainda, como se pode ver em def ler_1, ler_2 e ler_3.

'''