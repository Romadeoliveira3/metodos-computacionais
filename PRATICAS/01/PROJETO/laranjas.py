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