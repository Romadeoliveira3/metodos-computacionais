//Atividade Pseudocódigos
//Questão 01)

Algoritmo SomaMediaDesvioPadrao
    var
        numeros: vetor[1..5] de real
        soma, media, desvioPadrao: real
        i: inteiro

    soma <- 0

    // Entrada dos números
    para i <- 1 até 5 faça
        escreva("Digite o ", i, "º número: ")
        leia(numeros[i])
        soma <- soma + numeros[i]
    fimPara

    // Cálculo da média
    media <- soma / 5

    // Cálculo do desvio padrão
    desvioPadrao <- 0
    para i <- 1 até 5 faça
        desvioPadrao <- desvioPadrao + ((numeros[i] - media) * (numeros[i] - media))
    fimPara
    desvioPadrao <- raizQuadrada(desvioPadrao / 5)
    // Saída dos resultados
    escreva("A soma dos números é: ", soma)
    escreva("A média dos números é: ", media)
    escreva("O desvio padrão dos números é: ", desvioPadrao)
FimAlgoritmo
