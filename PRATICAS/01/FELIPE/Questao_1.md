Pseudocódigo - Utilizando o Portugol:

#-----Problema 1-----#:
função num_algarismo(algarismo)
    // Um numero inteiro positivo entre 100 e 999
    se algarismo < 100 ou algarismo > 999 então
        Escreva("O número deve estar entre 100 e 999")
        retorne num_algarismo(LeiaInteiro("Digite um número inteiro entre 100 e 999:"))
    fim se
    
    unidades <- algarismo % 10
    dezenas <- (algarismo // 10) % 10
    centenas <- algarismo // 100
    
    retorne unidades, dezenas, centenas
fim função

algarismo <- LeiaInteiro("Digite um número inteiro entre 100 e 999:")
unidades, dezenas, centenas <- num_algarismo(algarismo)

Escreva("Unidade:", unidades)
Escreva("Dezena:", dezenas)
Escreva("Centena:", centenas)

Escreva("")

