def calcular_media(valores):
    soma = sum(valores)
    media = soma / len(valores)
    return round(media, 3)


valores = []
valor = 0

# Solicitar os valores ao usuário
while valor >= 0:
    valor = float(input("Digite um valor (digite um número negativo para sair): "))
    if valor >= 0:
        valores.append(valor)

# Calcular a média dos valores
media = calcular_media(valores)

# Exibir a média com 3 casas decimais
print("Média: {:.3f}".format(media))

# Verificar se a média está acima do limiar
if media > 5:
    print("A média {:.3f} está acima do limiar estabelecido.".format(media))
