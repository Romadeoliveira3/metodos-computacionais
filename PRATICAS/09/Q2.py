###----Lista de Exercícios 6----###

# Disciplina: IF264 - Métodos Computacionais
# Professore: Paulo Freitas
# Estudante:  Romário Jonas de Oliveira Veloso
# Matrícula:  201028263

# Classe para representar uma pilha
class Pilha:
    def __init__(self):
        # Inicializa uma lista vazia para armazenar os itens da pilha
        self.items = []

    # Método para adicionar um item ao topo da pilha
    def push(self, item):
        self.items.append(item)

    # Método para remover e retornar o item do topo da pilha
    def pop(self):
        return self.items.pop()

    # Método para verificar se a pilha está vazia
    def is_empty(self):
        return len(self.items) == 0

# Função para verificar a sintaxe da expressão matemática
def verifica_sintaxe(expressao):
    # Cria uma pilha vazia
    pilha = Pilha()
    
    # Percorre cada símbolo da expressão
    for simbolo in expressao:
        # Se o símbolo for um parêntese esquerdo, adiciona na pilha
        if simbolo == '(':
            pilha.push(simbolo)
        # Se o símbolo for um parêntese direito
        elif simbolo == ')':
            # Verifica se a pilha está vazia (critério 2)
            if pilha.is_empty():
                return f"ERRO! A expressão {expressao} não tem sintaxe correta."
            # Se a pilha não estiver vazia, remove o último parêntese esquerdo
            pilha.pop()

    # Após percorrer toda a expressão, verifica se a pilha está vazia (critério 1)
    if pilha.is_empty():
        return f"A expressão {expressao} tem sintaxe correta."
    else:
        return f"ERRO! A expressão {expressao} não tem sintaxe correta."

# Testando o programa com as entradas fornecidas
entradas = [
    "(A + B) )",
    "((A + B) - ((C - D))",
    "(A + B) - (C + D) - (F + G)",
    "((H) * (((J + K))))",
    "(((A))))"
]

for expressao in entradas:
    print(verifica_sintaxe(expressao))
