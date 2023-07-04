###----03_-_Atividade_Sobre_vetores_e_matrizes----###

# Disciplina: IF264 - Métodos Computacionais
# Professore: Paulo Freitas
# Estudante:  Romário Jonas de Oliveira Veloso
# Matrícula:  201028263

##----Importar_Modulos----##

from preencher_vetor import preencher_vetor
from somar_vetor import somar_vetor
from multiplicar_vetores import multiplicar_vetores
from trocar_valores import trocar_valores
from somar_matrizes import soma_matrizes
from multiplicar_matriz_por_escalar import multiplicar_matriz_por_escalar
from buscar_valor import buscar_valor

# Verificarmos se o arquivo "main.py" está sendo executado diretamente usando a condição
# 'if __name__ == "__main__:". Se esta condição for verdadeira, chamamos a função main()

def main():
    #-----Problema 1-----#
    print("#-----Problema 1-----#:")
    # Chamar a função preencher_vetor()
    vetor_preenchido = preencher_vetor()
    print("Vetor Preenchido:", vetor_preenchido)

    #-----Problema 2-----#
    print("#-----Problema 2-----#:")
    # Chamar a função somar_vetor()
    soma = somar_vetor()
    print("A soma dos elementos do vetor é:", soma)

    #-----Problema 3-----#
    print("#-----Problema 3-----#:")
    # Chamar a função multiplicar_vetores()
    vetor_multiplicado = multiplicar_vetores()
    print("Vetor Resultado:", vetor_multiplicado)

    #-----Problema 4-----#
    print("#-----Problema 4-----#:")
    # Chamar a função trocar_valores()
    vetor = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    vetor_trocado = trocar_valores(vetor)
    print("Vetor Resultante:", vetor_trocado)

    #-----Problema 5-----#
    print("#-----Problema 5-----#:")
    # Chamar função soma_matrizes()
    matriz1 = [[1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15]]

    matriz2 = [[10, 20, 30, 40, 50],
            [60, 70, 80, 90, 100],
            [110, 120, 130, 140, 150]]

    resultado = soma_matrizes(matriz1, matriz2)

    if resultado:
        print("Matriz Resultante:")
        for linha in resultado:
            print(linha)

    #-----Problema 6-----#
    print("#-----Problema 6-----#: Multiplicar por escalar")
    # Chamar multiplicar_matriz_por_escalar()
    matriz = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]

    k = int(input("Digite o valor do escalar k: "))

    resultado = multiplicar_matriz_por_escalar(matriz, k)

    print("Matriz Resultante:")
    for linha in resultado:
        print(linha)

    #-----Problema 7-----#
    print("#-----Problema 7-----#: Buscar Valor dentre 1 e 400")
    # Chamar função buscar_valor(matriz, valor)
    # matriz = [[1, 2, 3, ..., 20],
    #         [21, 22, 23, ..., 40],
    #         ...
    #         [381, 382, 383, ..., 400]]
    matriz = []
    for i in range(20):
        linha = []
        for j in range(1, 21):
            elemento = j + 20 * i
            linha.append(elemento)
        matriz.append(linha)

    valor = int(input("Digite o valor a ser buscado: "))

    resultado = buscar_valor(matriz, valor)

    if resultado:
        linha, coluna = resultado
        print(f"O valor {valor} foi encontrado na posição [{linha}][{coluna}].")
    else:
        print("Valor não encontrado na matriz.")


if __name__ == "__main__":
    main()
