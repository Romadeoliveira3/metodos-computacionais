import random
import time

# Criar uma lista com 10.000 elementos aleatórios
lista = random.sample(range(1, 100000), 10000)
numero_buscado = random.choice(lista)

# Busca linear
def busca_linear(lista, num):
    for i in lista:
        if i == num:
            return True
    return False

# Busca binária
def busca_binaria(lista, num):
    low = 0
    high = len(lista) - 1
    while low <= high:
        mid = (low + high) // 2
        if lista[mid] == num:
            return True
        elif lista[mid] < num:
            low = mid + 1
        else:
            high = mid - 1
    return False

# Medir tempo da busca linear
inicio = time.time()
busca_linear(lista, numero_buscado)
tempo_linear = time.time() - inicio

# Ordenar a lista e medir o tempo da busca binária
lista.sort()
inicio = time.time()
busca_binaria(lista, numero_buscado)
tempo_binario = time.time() - inicio

print(f"Tempo da busca linear: {tempo_linear:.6f} segundos")
print(f"Tempo da busca binária: {tempo_binario:.6f} segundos")
