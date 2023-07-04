###----Lista de Exercícios 2----###


# Disciplina: IF264 - Métodos Computacionais
# Professore: Paulo Freitas
# Estudante:  Romário Jonas de Oliveira Veloso
# Matrícula:  201028263


##---Inicio dos das funções---##

def media_aritmetica(n1, n2, n3, n4):
    media_anual = (n1 + n2 + n3 + n4) / 4
    return media_anual

##---Função Main() para rodar o código---##

def main():
    #-----Problema 1-----#
    print("#-----Problema 1-----#: Média Aritmetica")
    
    # Chamar a função media_aritmetica()
    n1, n2, n3, n4 = map(float, input("Digite as notas do 1º, 2º, 3º e 4º bimestre, separadas por espaço: ").split())
    media = media_aritmetica(n1, n2, n3, n4)

    # Exibir o resultado
    print("A média aritmética anual é:", media)
    
    #-----Problema 2-----#
    print("#-----Problema 2-----#: Equação do 2º Grau")
    
    # Chamar a função media_aritmetica()

if __name__ == "__main__":
    main()



