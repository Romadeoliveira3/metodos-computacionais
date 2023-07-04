# 4) Leia um vetor de 16 posições e troque os 8 primeiros valores pelos 8 últimos e vice-versa.
# Escreva ao final o vetor obtido.

def trocar_valores(vetor):
    if len(vetor) != 16:
        print("O vetor deve ter 16 posições.")
        return

    # Troca dos valores
    vetor[:8], vetor[8:] = vetor[8:], vetor[:8]

    return vetor
