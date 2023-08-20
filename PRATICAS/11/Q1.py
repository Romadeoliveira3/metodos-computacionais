###----Lista de Exercícios 6----###

# Disciplina: IF264 - Métodos Computacionais
# Professore: Paulo Freitas
# Estudante:  Romário Jonas de Oliveira Veloso
# Matrícula:  201028263


# a) Implemente uma classe para representar uma árvore binária.
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BinaryTree:
    def __init__(self):
        self.root = None

    # b) Implemente uma função para verificar a altura da árvore.
    def altura(self, node):
        if node is None:
            return 0
        else:
            left_height = self.altura(node.left)
            right_height = self.altura(node.right)
            return max(left_height, right_height) + 1

    # c) Implemente uma função para verificar se um dado elemento pertence à árvore.
    def pertence(self, node, key):
        if node is None:
            return False
        if node.val == key:
            return True
        return self.pertence(node.left, key) or self.pertence(node.right, key)

    # d) Imprimir os elementos da árvore nas três ordens de percurso apresentadas em sala:
    def pre_ordem(self, node):
        if node:
            print(node.val)
            self.pre_ordem(node.left)
            self.pre_ordem(node.right)

    def em_ordem(self, node):
        if node:
            self.em_ordem(node.left)
            print(node.val)
            self.em_ordem(node.right)

    def pos_ordem(self, node):
        if node:
            self.pos_ordem(node.left)
            self.pos_ordem(node.right)
            print(node.val)

    # e) Implemente uma função para verificar se a árvore é (i) cheia, (ii) completa ou (iii) degenerada
    def is_full(self, node):
        if node is None:
            return True
        if node.left is None and node.right is None:
            return True
        if node.left is not None and node.right is not None:
            return self.is_full(node.left) and self.is_full(node.right)
        return False

    def is_complete(self, node, index, number_nodes):
        if node is None:
            return True
        if index >= number_nodes:
            return False
        return (self.is_complete(node.left, 2 * index + 1, number_nodes) and
                self.is_complete(node.right, 2 * index + 2, number_nodes))

    def is_degenerated(self, node):
        if node is None:
            return True
        if node.left is not None and node.right is not None:
            return False
        return (self.is_degenerated(node.left) or self.is_degenerated(node.right))

# Testando a implementação
tree = BinaryTree()
tree.root = Node(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

print("Altura da árvore:", tree.altura(tree.root))
print("Elemento 3 pertence à árvore:", tree.pertence(tree.root, 3))
print("Elemento 6 pertence à árvore:", tree.pertence(tree.root, 6))
print("\nPercurso pré-ordem:")
tree.pre_ordem(tree.root)
print("\nPercurso em-ordem:")
tree.em_ordem(tree.root)
print("\nPercurso pós-ordem:")
tree.pos_ordem(tree.root)
print("\nÁrvore é cheia:", tree.is_full(tree.root))
print("Árvore é completa:", tree.is_complete(tree.root, 0, 5))
print("Árvore é degenerada:", tree.is_degenerated(tree.root))
