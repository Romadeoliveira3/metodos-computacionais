###----Lista_01----###

# Disciplina: IF264 - Métodos Computacionais
# Professore: Paulo Freitas
# Estudante:  Romário Jonas de Oliveira Veloso
# Matrícula:  201028263

#-----Problema 1-----#:

def num_algarismo(algarismo):
    #Um numero inteiro positivo entre 100 e 999
    if algarismo < 100 or algarismo > 999:
        print("O número deve estar entre 100 e 999")
        return  num_algarismo(int(input("Digite um numero inteiro entre de 100 a 999:")))
    
    unidades = algarismo % 10
    dezenas =  (algarismo // 10) % 10
    centenas = algarismo // 100



    return unidades, dezenas, centenas

algarismo = int(input("Digite um numero inteiro entre de 100 a 999:"))
unidades, dezenas, centenas = num_algarismo(algarismo)

print("Unidade:", unidades)
print("Dezena:", dezenas)
print("Centena:", centenas)

#-----Problema 2-----#:

#Quantidade de laranjas desejadas ao usuário;
def laranjas(quant):
    #Quantas dúzias?
    duzias = quant//12
    #Se for duzia avulsas == 0, caso contrario, o resto deverá ser considerado avulsa;
    avulsas = quant%12

    valor_duzias = duzias * 8.35
    #Considerado o preço de R$8,35 para cada dúzia, logo R$0,70 para cada laranja avulsa;
    valor_avulsas = avulsas * 0.70

    valor_total = valor_duzias + valor_avulsas

    return duzias, avulsas, valor_total

q_laranjas = int(input("Quantas laranjas?"))

#Calcula a quantidade de laranjas e o valor total

duzias, avulsas, valor_total = laranjas(q_laranjas)
print("Quantidade de dúzias: {}, Quantidade avulsas: {}, Valor total (R$): {:.2f}".format(duzias, avulsas, valor_total))

#-----Problema 3-----#:

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


# Solicitar os números de intervalo ao usuário
inicio = int(input("Digite o número de início do intervalo (mínimo: 2): "))
fim = int(input("Digite o número de fim do intervalo (máximo: 103): "))

# Verificar se os números estão dentro do intervalo desejado
while inicio < 2 or fim > 103:
    print("Intervalo inválido. Digite novamente.")
    inicio = int(input("Digite o número de início do intervalo (mínimo: 2): "))
    fim = int(input("Digite o número de fim do intervalo (máximo: 103): "))

# Calcular os números perfeitos dentro do intervalo
numeros_perfeitos = calcular_numeros_perfeitos(inicio, fim)

# Exibir os números perfeitos encontrados
print("Números perfeitos encontrados no intervalo [", inicio, "-", fim, "]:")
if len(numeros_perfeitos) > 0:
    for numero in numeros_perfeitos:
        print(numero)
else:
    print("Nenhum número perfeito encontrado no intervalo.")


#-----Problema 4-----#:

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
