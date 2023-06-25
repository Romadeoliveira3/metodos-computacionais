Pseudocódigo - Utilizando o Portugol:

#-----Problema 4-----#:
função calcular_media(valores)
    soma <- somar(valores)
    media <- soma / tamanho(valores)
    retorne arredondar(media, 3)
fim função

valores <- []
valor <- 0

enquanto valor >= 0 faça
    valor <- LeiaReal("Digite um valor (digite um número negativo para sair): ")
    se valor >= 0 então
        valores.adicionar(valor)
    fim se
fim enquanto

media <- calcular_media(valores)

Escreva("Média:", formatar(media, "0.000"))

se media > 5 então
    Escreva("A média", formatar(media, "0.000"), "está acima do limiar estabelecido.")
fim se
