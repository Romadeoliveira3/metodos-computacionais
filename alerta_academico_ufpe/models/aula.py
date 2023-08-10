class Aula:
    def __init__(self, nome, carga_horaria, aulas_semana, semanas=None, total_aulas=None, aulas_faltadas=0, percentual_faltas=0):
        self.nome = nome
        self.carga_horaria = carga_horaria
        self.aulas_semana = aulas_semana
        self.semanas = semanas if semanas is not None else carga_horaria // aulas_semana
        self.total_aulas = total_aulas if total_aulas is not None else self.semanas*aulas_semana
        self.aulas_faltadas = aulas_faltadas
        self.percentual_faltas = percentual_faltas

        self.head = None  # Início da lista encadeada. A cabeça da lista é o primeiro nó.

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

    def adicionar_aula(self, nome, carga_horaria, aulas_semana):
        nova_aula = Aula(nome, carga_horaria, aulas_semana)
        nova_aula.next = self.head  # O próximo nó da nova aula é a atual cabeça da lista.
        self.head = nova_aula  # A nova aula se torna a nova cabeça da lista.
    
    def mostrar_aulas(self):
        aula_atual = self.head  # Começamos na cabeça da lista.
        while aula_atual is not None:  # Enquanto não chegarmos ao final da lista.
            print(f'Nome da aula: {aula_atual.nome}, Faltas: {aula_atual.mostrar_faltas()}')
            aula_atual = aula_atual.next  # Vamos para o próximo nó na lista.
