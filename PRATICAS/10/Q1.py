###----Lista de Exercícios 6----###

# Disciplina: IF264 - Métodos Computacionais
# Professore: Paulo Freitas
# Estudante:  Romário Jonas de Oliveira Veloso
# Matrícula:  201028263


# a) Implemente uma classe para representar um nó de uma fila.
class No:
    def __init__(self, valor):
        self.valor = valor  # Valor armazenado no nó
        self.proximo = None  # Referência para o próximo nó na fila

# b) Implemente uma classe para representar a fila e crie uma fila vazia.
class Fila:
    def __init__(self):
        self.inicio = None  # Início da fila (primeiro elemento)
        self.fim = None  # Fim da fila (último elemento)

    # c) Implemente uma função da classe da fila para:
    # i) Inserir um elemento;
    def inserir(self, valor):
        novo_no = No(valor)  # Cria um novo nó com o valor fornecido
        
        # Se a fila estiver vazia, o novo nó será o início e o fim
        if self.inicio is None:
            self.inicio = novo_no
            self.fim = novo_no
        else:
            # Caso contrário, adiciona o novo nó ao fim da fila
            self.fim.proximo = novo_no
            self.fim = novo_no

    # ii) Remover um elemento.
    def remover(self):
        if self.inicio is None:
            print("Fila vazia!")  # Não há elementos para remover
            return None
        
        # Remove o nó do início da fila
        valor_removido = self.inicio.valor
        self.inicio = self.inicio.proximo
        
        # Se o início se tornar None, a fila está vazia, então o fim também deve ser None
        if self.inicio is None:
            self.fim = None
        
        return valor_removido

# Testando a implementação
fila = Fila()
fila.inserir(1)
fila.inserir(2)
fila.inserir(3)

print(fila.remover())  # Deve imprimir 1
print(fila.remover())  # Deve imprimir 2
print(fila.remover())  # Deve imprimir 3
print(fila.remover())  # Deve imprimir "Fila vazia!" e retornar None
