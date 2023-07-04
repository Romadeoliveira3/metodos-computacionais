# 5) Construa um algoritmo que efetue e apresente o resultado da soma entre duas matrizes 3 x 5. 
# Inicialize a matriz com valores quaisquer e imprima o resultado na tela.

def soma_matrizes(matriz1, matriz2):
    if len(matriz1) != len(matriz2) or len(matriz1[0]) != len(matriz2[0]):
        print("As matrizes devem ter a mesma dimensão.")
        return

    resultado = []
    for i in range(len(matriz1)):
        linha = []
        for j in range(len(matriz1[0])):
            soma = matriz1[i][j] + matriz2[i][j]
            linha.append(soma)
        resultado.append(linha)

    return resultado
