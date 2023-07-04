# 7) Leia uma matriz 20 x 20. Leia também um valor X. 
# O programa deverá fazer uma busca desse valor na matriz e, ao final escrever a 
# localização (linha e coluna) ou uma mensagem de “não encontrado”.

def buscar_valor(matriz, valor):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] == valor:
                return i, j
    return None