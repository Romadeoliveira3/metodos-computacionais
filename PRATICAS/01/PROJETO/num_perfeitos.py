def calcular_numeros_perfeitos(inicio, fim):
    numeros_perfeitos = []

    for num in range(inicio, fim+1):
        divisores = []
        for i in range(1, num):
            if num % i == 0:
                divisores.append(i)
        if sum(divisores) == num:
            numeros_perfeitos.append(num)

    return numeros_perfeitos
