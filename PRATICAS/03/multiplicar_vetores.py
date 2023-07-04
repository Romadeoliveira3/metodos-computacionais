#   3) Construa um programa que multiplique os valores de um vetor de reais de 20 posições
#   pelos valores de um outro vetor de reais de 20 posições. O primeiro vetor deve ser inicializado
#   com valores crescentes a partir de 1 e o segundo vetor com valores decrescentes a partir de 20. 
#   Os resultados das multiplicações devem ser armazenados num terceiro vetor.

def multiplicar_vetores():
    vetor1 = [float(i) for i in range(1, 21)]
    vetor2 = [float(i) for i in range(20, 0, -1)]
    vetor_resultado = []
    for i in range(20):
        resultado = vetor1[i] * vetor2[i]
        vetor_resultado.append(resultado)
    return vetor_resultado
