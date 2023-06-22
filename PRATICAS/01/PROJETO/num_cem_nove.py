def num_algarismo(algarismo):
    #Um numero inteiro positivo entre 100 e 999
    if algarismo < 100 or algarismo > 999:
        print("O número deve estar entre 100 e 999")
        return  num_algarismo(int(input("Digite um numero inteiro entre de 100 a 999:")))
    
    unidades = algarismo % 10
    dezenas =  (algarismo // 10) % 10
    centenas = algarismo // 100



    return unidades, dezenas, centenas