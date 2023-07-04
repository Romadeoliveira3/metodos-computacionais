###----Lista de Exercícios 2----###


# Disciplina: IF264 - Métodos Computacionais
# Professore: Paulo Freitas
# Estudante:  Romário Jonas de Oliveira Veloso
# Matrícula:  201028263

##--importar bibliotecas--##

import math
import pandas as pd

##---Inicio dos das funções---##
#-----Problema 1-----#: Média Aritmetica
def media_aritmetica(n1, n2, n3, n4):
    media_anual = (n1 + n2 + n3 + n4) / 4
    return media_anual

#-----Problema 2-----#: Raizes segundo grau
def raizes_eq(a, b, c):
    delta = b**2 - 4*a*c
    
    if delta > 0:
        raiz1 = (-b + math.sqrt(delta)) / (2*a)
        raiz2 = (-b - math.sqrt(delta)) / (2*a)
        return raiz1, raiz2
    elif delta == 0:
        raiz = -b / (2*a)
        return raiz, raiz
    else:
        return None

#-----Problema 3-----#: substitui todas as ocorrência de valores positivos por 1 e todos os valores negativos por 0.
def substituir_valores(vetor):
    for i in range(len(vetor)):
        if vetor[i] > 0:
            vetor[i] = 1
        else:
            vetor[i] = 0


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

    # Solicitar os coeficientes ao usuário
    a = float(input("Digite o valor de A: "))
    b = float(input("Digite o valor de B: "))
    c = float(input("Digite o valor de C: "))

    # Calcular as raízes da equação do segundo grau
    raiz1, raiz2 = raizes_eq(a, b, c)

    # Exibir o resultado
    print("As raízes da equação são:")
    print("Raiz 1:", raiz1)
    print("Raiz 2:", raiz2)

    #-----Problema 3----#:
    # Criar um vetor vazio de tamanho 30
    vetor = [0] * 30

    # Preencher o vetor com números fornecidos pelo usuário
    for i in range(30):
        numero = float(input("Digite um número: "))
        vetor[i] = numero

    # Substituir os valores positivos por 1 e os negativos por 0
    substituir_valores(vetor)

    # Exibir o vetor modificado
    print("Vetor modificado:", vetor)
    
    #-----Problema 4----#:
 
    # Ler o arquivo CSV
    dados = pd.read_csv('InfoAlturas_lista2.csv')

    # a) Maior e menor altura do grupo
    maior_altura = dados['ALTURA'].max()
    menor_altura = dados['ALTURA'].min()
    print("Maior altura do grupo:", maior_altura)
    print("Menor altura do grupo:", menor_altura)

    # b) Média de altura das mulheres
    altura_mulheres = dados.loc[dados['SEXO'] == 'F', 'ALTURA']
    media_altura_mulheres = altura_mulheres.mean()
    print("Média de altura das mulheres:", media_altura_mulheres)

    # c) Número de homens e diferença percentual com as mulheres
    num_homens = dados.loc[dados['SEXO'] == 'M'].shape[0]
    num_mulheres = dados.loc[dados['SEXO'] == 'F'].shape[0]
    diferenca_percentual = ((num_homens - num_mulheres) / num_mulheres) * 100
    print("Número de homens:", num_homens)
    print("Diferença percentual com as mulheres:", diferenca_percentual)


if __name__ == "__main__":
    main()



