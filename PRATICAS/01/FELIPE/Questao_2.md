Pseudocódigo - Utilizando o Portugol:

#-----Problema 2-----#:
função laranjas(quant)
    // Quantidade de laranjas desejadas ao usuário
    duzias <- quant // 12
    // Se for duzia avulsas == 0, caso contrario, o resto deverá ser considerado avulsa
    avulsas <- quant % 12

    valor_duzias <- duzias * 8.35
    // Considerado o preço de R$8,35 para cada dúzia, logo R$0,70 para cada laranja avulsa
    valor_avulsas <- avulsas * 0.70

    valor_total <- valor_duzias + valor_avulsas

    retorne duzias, avulsas, valor_total
fim função

q_laranjas <- LeiaInteiro("Quantas laranjas?")

// Calcula a quantidade de laranjas e o valor total
duzias, avulsas, valor_total <- laranjas(q_laranjas)
Escreva("Quantidade de dúzias:", duzias)
Escreva("Quantidade avulsas:", avulsas)
Escreva("Valor total (R$):", arredondar(valor_total, 2))
