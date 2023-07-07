###----Lista de Exercícios 3----###

# Disciplina: IF264 - Métodos Computacionais
# Professore: Paulo Freitas
# Estudante:  Romário Jonas de Oliveira Veloso
# Matrícula:  201028263

##--importar bibliotecas--##

import math
import pandas as pd
import numpy as np

##--Tabela inicial--##
produtos = ["Sabonete", "Conjunto de pratos", "vaso para plantas", "Brinquedo infantil", "Bola de basquete", "Enfeite natalino", "Canetas coloridas", "Cadernos", "Quadros diversos", "Ração para cachorros"]
precos = [3, 954.99, 12.50, 42.20, 125.40, 30, 25.50, 10, 5.45, 150]
matriz = [produtos, precos]

# Imprimir matriz inicial
print("Matriz inicial:")
for i in range(len(matriz[0])):
    print(matriz[0][i], " - R$", round(matriz[1][i], 2))

#(a)  Adicione à matriz o item “Pote de vidro”, cujo valor unitário é de R$23,90. Imprima na tela 
# o resultado dessa etapa.

# Adicionar o item "Pote de vidro" com valor unitário de R$23,90
matriz[0].append("Pote de vidro")
matriz[1].append(23.90)

# Imprimir matriz após adicionar o item
print("\nResultado após adicionar o item:")
for i in range(len(matriz[0])):
    print(matriz[0][i], " - R$", matriz[1][i])


# b) A loja deixou de vender produtos perecíveis, então retire o item “Ração para cachorros” e
# seu preço do cadastro. Imprima na tela o resultado dessa etapa.

# Remover o item "Ração para cachorros" e seu preço
indice = matriz[0].index("Ração para cachorros")
matriz[0].pop(indice)
matriz[1].pop(indice)

# Imprimir matriz após remover o item
print("\nResultado após remover o item:")
for i in range(len(matriz[0])):
    print(matriz[0][i], " - R$", matriz[1][i])

# c) O período natalino acabou, então substitua o item “Enfeite natalino” do cadastro, bem
# como seu preço, pelo item “Acessório carnavalesco” que custa R$15,25. Imprima na tela o
# resultado dessa etapa

# Substituir "Enfeite natalino" por "Acessório carnavalesco" com preço R$15,25
indice = matriz[0].index("Enfeite natalino")
matriz[0][indice] = "Acessório carnavalesco"
matriz[1][indice] = 15.25

# Imprimir matriz após substituição do item
print("\nResultado após substituir o item:")
for i in range(len(matriz[0])):
    print(matriz[0][i], " - R$", matriz[1][i])


# d) Por fim, utilizando a biblioteca numpy para converter a lista em um array (vetor), imprima
# na tela todos os produtos listados com formato semelhante ao apresentado na tabela acima.
# Ou seja, os produtos devem ser impressos um abaixo do outro e os respectivos preços
# devem aparecer ao lado, conforme o exemplo a seguir
# ['Sabonete', 3.0]
# ['Conjunto de pratos', 954.99]
# ['vaso para plantas', 12.5]
# ['Brinquedo infantil', 42.2]
# ['Bola de basquete', 125.4]
# ['Acessório carnavalesco', 15.25]
# ['Canetas coloridas', 25.5]
# ['Cadernos', 10.0]
# ['Quadros diversos', 5.45]
# ['Pote de vidro', 23.9]

# Converter as listas em um array NumPy
array_produtos = np.array(produtos)
array_precos = np.array(precos)

# Imprimir os produtos e preços
for i in range(len(array_produtos)):
    print([array_produtos[i], array_precos[i]])

