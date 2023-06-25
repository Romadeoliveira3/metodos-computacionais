Pseudocódigo - Utilizando o Portugol:

#-----Problema 3-----#:
função calcular_numeros_perfeitos(inicio, fim)
    numeros_perfeitos <- []
    
    para num de inicio até fim faça
        divisores <- []
        para i de 1 até num faça
            se num % i == 0 então
                divisores.adicionar(i)
            fim se
        fim para
        se somar(divisores) == num então
            numeros_perfeitos.adicionar(num)
        fim se
    fim para
    
    retorne numeros_perfeitos
fim função

inicio <- LeiaInteiro("Digite o número de início do intervalo (mínimo: 2): ")
fim <- LeiaInteiro("Digite o número de fim do intervalo (máximo: 103): ")

enquanto inicio < 2 ou fim > 103 faça
    Escreva("Intervalo inválido. Digite novamente.")
    inicio <- LeiaInteiro("Digite o número de início do intervalo (mínimo: 2): ")
    fim <- LeiaInteiro("Digite o número de fim do intervalo (máximo: 103): ")
fim enquanto

numeros_perfeitos <- calcular_numeros_perfeitos(inicio, fim)

Escreva("Números perfeitos encontrados no intervalo [", inicio, "-", fim, "]:")
se tamanho(numeros_perfeitos) > 0 então
    para cada numero em numeros_perfeitos faça
        Escreva(numero)
    fim para
senão
    Escreva("Nenhum número perfeito encontrado no intervalo.")
fim se

Escreva("")