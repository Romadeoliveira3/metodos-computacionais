###----Lista de Exercícios 10----###

# Disciplina: IF264 - Métodos Computacionais
# Professore: Paulo Freitas
# Estudante:  Romário Jonas de Oliveira Veloso
# Matrícula:  201028263

###-----------Módulos------------###

import random
import time
from Q1 import *


###-----------Questão 1------------###

# Definindo o array de teste
arr = [64, 34, 25, 12, 22, 11, 90]

# Testando selection sort
print("Array original:", arr)
sorted_arr = selection_sort(arr.copy())
print("Array ordenado com selection sort:", sorted_arr)

# Testando insertion sort
print("\nArray original:", arr)
sorted_arr = insertion_sort(arr.copy())
print("Array ordenado com insertion sort:", sorted_arr)

# Testando bubble sort
print("\nArray original:", arr)
sorted_arr = bubble_sort(arr.copy())
print("Array ordenado com bubble sort:", sorted_arr)

# Testando merge sort
print("\nArray original:", arr)
sorted_arr = merge_sort(arr.copy())
print("Array ordenado com merge sort:", sorted_arr)

# Testando quick sort
print("\nArray original:", arr)
sorted_arr = quick_sort(arr.copy())
print("Array ordenado com quick sort:", sorted_arr)


###-----------Questão 2------------###

# a)
listaA = [820, 239, 771, 781, 977, 603, 883, 996, 466, 469, 324, 757, 921,
588, 618, 678, 629, 452, 341, 496, 565, 151, 107, 426, 838]
print("Resultado com Selection Sort:", selection_sort(listaA.copy()))
print("Resultado com Insertion Sort:", insertion_sort(listaA.copy()))
print("Resultado com Bubble Sort:", bubble_sort(listaA.copy()))
print("Resultado com Merge Sort:", merge_sort(listaA.copy()))
print("Resultado com Quick Sort:", quick_sort(listaA.copy()))

# b)
listaB = [45, 2, 50, 167, 0, 49, 7, 7, 18, 38, 90, 9, 1, 15, 85, 1, 0, 3, 87, 245, 9,
21, 67, 134, 25]
print("\nResultado com Selection Sort:", selection_sort(listaB.copy()))
print("Resultado com Insertion Sort:", insertion_sort(listaB.copy()))
print("Resultado com Bubble Sort:", bubble_sort(listaB.copy()))
print("Resultado com Merge Sort:", merge_sort(listaB.copy()))
print("Resultado com Quick Sort:", quick_sort(listaB.copy()))

# c)
listaC = ["abacaxi", "computador"]
# Aqui temos que ordenar as letras de cada palavra individualmente.
listaC_sorted = [''.join(quick_sort(list(word))) for word in listaC]
print("\nResultado para as letras com Quick Sort:", listaC_sorted)

# d)
listaD = ['Jose', 'Fabiano', 'Cristina', 'Ana Vitoria', 'Fabricio', 'Ricardo', 'Josefa',
'Esmeralda', 'Priscila', 'Zenaide', 'Antonio', 'Cristovao', 'Pedro', 'Maria',
'Nivaldo']
print("\nResultado com Selection Sort:", selection_sort(listaD.copy()))
print("Resultado com Insertion Sort:", insertion_sort(listaD.copy()))
print("Resultado com Bubble Sort:", bubble_sort(listaD.copy()))
print("Resultado com Merge Sort:", merge_sort(listaD.copy()))
print("Resultado com Quick Sort:", quick_sort(listaD.copy()))

###-----------Questão 3------------###

numerosAleatorios = random.sample(range(1,1000),500)

def calc_time(func, arr):
    start_time = time.time()
    func(arr.copy())
    return (time.time() - start_time) * 1000

times = {
    "Selection Sort": calc_time(selection_sort, numerosAleatorios),
    "Insertion Sort": calc_time(insertion_sort, numerosAleatorios),
    "Bubble Sort": calc_time(bubble_sort, numerosAleatorios),
    "Merge Sort": calc_time(merge_sort, numerosAleatorios),
    "Quick Sort": calc_time(quick_sort, numerosAleatorios)
}

for algo, t in times.items():
    print(f"Tempo de execução de {algo}: {t:.2f} ms")

