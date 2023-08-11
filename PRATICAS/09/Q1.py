###----Lista de Exercícios 6----###

# Disciplina: IF264 - Métodos Computacionais
# Professore: Paulo Freitas
# Estudante:  Romário Jonas de Oliveira Veloso
# Matrícula:  201028263


#   Questão 1) Sobre a implementação de pilhas, faça o que se pede:
#   a) Implemente uma classe para representar um nó de uma pilha.
class No:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None

# b) Implementação de uma classe para representar a pilha e criação de uma pilha vazia:
class Pilha:
    def __init__(self):
        self.topo = None

#   c) Implementação das funções para inserir e remover um elemento da pilha:
class Pilha:
    def __init__(self):
        self.topo = None

    # i) Inserir um elemento
    def push(self, dado):
        novo_no = No(dado)
        novo_no.proximo = self.topo
        self.topo = novo_no

    # ii) Remover um elemento
    def pop(self):
        if self.topo:
            valor = self.topo.dado
            self.topo = self.topo.proximo
            return valor
        else:
            print("Pilha vazia!")
            return None

#   Rodar o código
pilha = Pilha()
pilha.push(5)
pilha.push(10)
print(pilha.pop())  # Deve imprimir 10
print(pilha.pop())  # Deve imprimir 5
print(pilha.pop())  # Deve imprimir "Pilha vazia!" e retornar None
