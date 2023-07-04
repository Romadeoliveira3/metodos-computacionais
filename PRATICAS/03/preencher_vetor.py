#   1) Construa um programa que preenche um vetor de inteiros de 100 números, 
#   colocando 0 nas posições pares e 1 nas ímpares.

def preencher_vetor():
    vetor = []
    for i in range(100):
        if i % 2 == 0:
            vetor.append(0)
        else:
            vetor.append(1)
    return vetor
