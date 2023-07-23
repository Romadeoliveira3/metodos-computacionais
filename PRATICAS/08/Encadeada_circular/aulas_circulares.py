'''Questão 2) Sobre a implementação de listas encadeadas circulares, faça o que se pede:
a) Implemente uma classe para representar um nó de uma lista encadeada circular.
b) Implemente uma classe para representar a lista encadeada circular e crie uma lista
encadeada circular vazia.'''

class Aula:
    def __init__(self, nome=None, carga_horaria=None, aulas_semana=None, next=None, prev=None):
        self.nome = nome
        self.carga_horaria = carga_horaria
        self.aulas_semana = aulas_semana
        if self.carga_horaria and self.aulas_semana:
            self.semanas = carga_horaria // aulas_semana
            self.total_aulas = self.semanas * aulas_semana
        self.aulas_faltadas = 0
        self.next = next  # Ponteiro para a próxima aula na lista encadeada.
        self.prev = prev  # Ponteiro para a aula anterior na lista encadeada.

        
    def adicionar_falta(self):
        self.aulas_faltadas += 1
        self.verificar_situacao()

    def verificar_situacao(self):
        percentual_faltas = (self.aulas_faltadas / self.total_aulas) * 100
        if percentual_faltas > 25:
            print(f"Alerta! Você ultrapassou o limite de faltas na disciplina {self.nome}. Percentual de faltas: {percentual_faltas}%")
        else:
            faltas_restantes = (self.total_aulas * 0.25) - self.aulas_faltadas
            print(f"Você pode faltar mais {faltas_restantes} aulas na disciplina {self.nome} sem ser reprovado por falta.")

    def mostrar_faltas(self):
        return self.aulas_faltadas


class ListaDeAulas:
    def __init__(self):
        self.head = None  # Início da lista encadeada. A cabeça da lista é o primeiro nó.
        self.tail = None  # Fim da lista encadeada. A cauda da lista é o último nó.

# c) Implemente uma função da classe da lista encadeada circular para
# i) Inserir um elemento no início da lista
    def inserir_inicio(self, nome, carga_horaria, aulas_semana):
        nova_aula = Aula(nome, carga_horaria, aulas_semana)
        if self.head is None:
            self.head = nova_aula
            self.tail = nova_aula
            nova_aula.next = nova_aula
            nova_aula.prev = nova_aula
        else:
            nova_aula.next = self.head
            nova_aula.prev = self.tail
            self.head.prev = nova_aula
            self.tail.next = nova_aula
            self.head = nova_aula

# ii) Inserir um elemento no final da lista;
    def inserir_final(self, nome, carga_horaria, aulas_semana):
        nova_aula = Aula(nome, carga_horaria, aulas_semana)
        if self.head is None:
            self.head = nova_aula
            self.tail = nova_aula
            nova_aula.next = nova_aula
            nova_aula.prev = nova_aula
        else:
            nova_aula.next = self.head
            nova_aula.prev = self.tail
            self.head.prev = nova_aula
            self.tail.next = nova_aula
            self.tail = nova_aula

# iii) Buscar um elemento da lista dado o seu valor
    def buscar_aula(self, nome):
        if self.head is None:
            return None

        aula_atual = self.head
        while True:
            if aula_atual.nome == nome:
                return aula_atual
            aula_atual = aula_atual.next
            if aula_atual == self.head:
                break

        return None
    
# iv) Inserir um elemento depois de um elemento da lista cujo valor é fornecido;
    def inserir_apos(self, nome, novo_nome, carga_horaria, aulas_semana):
        aula_atual = self.buscar_aula(nome)
        if aula_atual is None:
            print(f"Aula {nome} não encontrada.")
        else:
            nova_aula = Aula(novo_nome, carga_horaria, aulas_semana)
            nova_aula.next = aula_atual.next
            nova_aula.prev = aula_atual
            aula_atual.next.prev = nova_aula
            aula_atual.next = nova_aula
            if aula_atual == self.tail:
                self.tail = nova_aula

# v) Remover um elemento da lista fornecendo-se o seu valor;
    def remover_aula(self, nome):
        aula_atual = self.buscar_aula(nome)
        if aula_atual is None:
            print(f"Aula {nome} não encontrada.")
        else:
            if aula_atual.prev is not None:
                aula_atual.prev.next = aula_atual.next
            else:
                self.head = aula_atual.next
            if aula_atual.next is not None:
                aula_atual.next.prev = aula_atual.prev
            else:
                self.tail = aula_atual.prev
            # Se a aula removida era a única aula na lista
            if self.head == aula_atual:
                self.head = None
            if self.tail == aula_atual:
                self.tail = None

# vi) Remover um elemento da lista fornecendo-se o seu valor;
    def atualizar_aula(self, nome_atual, novo_nome, nova_carga_horaria, novas_aulas_semana):
        aula_atual = self.buscar_aula(nome_atual)
        if aula_atual is None:
            print(f"Aula {nome_atual} não encontrada.")
        else:
            aula_atual.nome = novo_nome
            aula_atual.carga_horaria = nova_carga_horaria
            aula_atual.aulas_semana = novas_aulas_semana
            aula_atual.semanas = nova_carga_horaria // novas_aulas_semana
            aula_atual.total_aulas = aula_atual.semanas * novas_aulas_semana
