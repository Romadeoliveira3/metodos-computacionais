#   6) Faça um programa que multiplica uma matriz 3 x 3 de inteiros por um escalar k e imprima
#   o resultado na tela. O usuário deve fornecer os valores da matriz e de k.

def multiplicar_matriz_por_escalar(matriz, k):
    resultado = []
    for linha in matriz:
        linha_resultado = [elemento * k for elemento in linha]
        resultado.append(linha_resultado)
    return resultado