'''Dado um tipo de arquivo:

Nome, Testes, Projeto, Normal, Recurso, Nota

Ernesto Costa, 75, 60, 45, 52, ?
Zeus Euclides, 12, 34, 45, 30, ?
Anaximandro Heraclito, 36, 47, 67, 12,?

O resultado se dá na forma de lista. Através do método writer, podemos querer introduzir os dados de um novo aluno
(escrever no icheiro uma nova linha).

import csv


def insere_linha_csv(fich, linha):
    with open(fich, 'a') as nome_fich:
        csv_writer = csv.writer(nome_fich)
        csv_writer.witerow(linha)
'''

import csv

def le_csv(nome_fich):
    #Lê um ficheiro em formato csv.
    with open(nome_fich) as fich:
        csv_reader = csv.reader(fich)
        dados = []
        for linha in csv_reader:
            dados.append(linha)
    return dados