# a) Implemente uma classe para representar um nó da lista encadeada
class Aula:
    def __init__(self, nome, carga_horaria, aulas_semana):
        self.nome = nome
        self.carga_horaria = carga_horaria
        self.aulas_semana = aulas_semana
        self.semanas = carga_horaria // aulas_semana
        self.total_aulas = self.semanas * aulas_semana
        self.aulas_faltadas = 0
        # Ponteiro para a próxima aula na lista encadeada. 
        # Este é o elemento que faz o encadeamento na lista.
        self.next = None  

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


# b) Implemente uma classe para representar a lista encadeada
class ListaDeAulas:
    def __init__(self):
        self.head = None  # Início da lista encadeada. A cabeça da lista é o primeiro nó.

    def adicionar_aula(self, nome, carga_horaria, aulas_semana):
        nova_aula = Aula(nome, carga_horaria, aulas_semana)
        nova_aula.next = self.head  # O próximo nó da nova aula é a atual cabeça da lista.
        self.head = nova_aula  # A nova aula se torna a nova cabeça da lista.

    def adicionar_falta(self, nome):
        aula_atual = self.head  # Começamos na cabeça da lista.
        while aula_atual is not None:  # Enquanto não chegarmos ao final da lista.
            if aula_atual.nome == nome:  # Se encontrarmos a aula.
                aula_atual.adicionar_falta()  # Adicionamos a falta.
                return
            aula_atual = aula_atual.next  # Vamos para o próximo nó na lista.
        print(f"Aula {nome} não encontrada.")

    def mostrar_aulas(self):
        aula_atual = self.head  # Começamos na cabeça da lista.
        while aula_atual is not None:  # Enquanto não chegarmos ao final da lista.
            print(f'Nome da aula: {aula_atual.nome}, Faltas: {aula_atual.mostrar_faltas()}')
            aula_atual = aula_atual.next  # Vamos para o próximo nó na lista.

    def buscar_aula(self, nome):
        aula_atual = self.head  # Começamos na cabeça da lista.
        while aula_atual is not None:  # Enquanto não chegarmos ao final da lista.
            if aula_atual.nome == nome:  # Se encontrarmos a aula.
                return aula_atual  # Retornamos a aula.
            aula_atual = aula_atual.next  # Vamos para o próximo nó na lista.
        return None  # Se chegarmos ao final da lista sem encontrar a aula, retornamos None.
    
    def inserir_apos(self, nome, novo_nome, carga_horaria, aulas_semana):
        aula_atual = self.head  # Começamos na cabeça da lista.
        while aula_atual is not None:  # Enquanto não chegarmos ao final da lista.
            if aula_atual.nome == nome:  # Se encontrarmos a aula.
                nova_aula = Aula(novo_nome, carga_horaria, aulas_semana)
                nova_aula.next = aula_atual.next  # O próximo nó da nova aula é o nó após a aula atual.
                aula_atual.next = nova_aula  # O próximo nó da aula atual se torna a nova aula.
                return
            aula_atual = aula_atual.next  # Vamos para o próximo nó na lista.
        print(f"Aula {nome} não encontrada.")

    def remover_aula(self, nome):
        aula_atual = self.head  # Começamos na cabeça da lista.
        aula_anterior = None  # Mantemos o controle da aula anterior.

        while aula_atual is not None:  # Enquanto não chegarmos ao final da lista.
            if aula_atual.nome == nome:  # Se encontrarmos a aula.
                if aula_anterior is not None:  # Se a aula não é a cabeça da lista.
                    aula_anterior.next = aula_atual.next  # O próximo nó da aula anterior se torna o próximo nó da aula atual.
                else:  # Se a aula é a cabeça da lista.
                    self.head = aula_atual.next  # A cabeça da lista se torna o próximo nó da aula atual.
                return
            aula_anterior = aula_atual  # Atualizamos a aula anterior.
            aula_atual = aula_atual.next  # Vamos para o próximo nó na lista.
        print(f"Aula {nome} não encontrada.")

    def obter_aula_por_indice(self, indice):
        aula_atual = self.head  # Começamos na cabeça da lista.
        contador = 0  # Mantemos um contador para saber em que índice estamos.

        while aula_atual is not None:  # Enquanto não chegarmos ao final da lista.
            if contador == indice:  # Se chegarmos ao índice desejado.
                return aula_atual  # Retornamos a aula.
            aula_atual = aula_atual.next  # Vamos para o próximo nó na lista.
            contador += 1  # Incrementamos o contador.

        print(f"Índice {indice} não encontrado.")
        return None

    def atualizar_aula_por_indice(self, indice, novo_nome, nova_carga_horaria, novas_aulas_semana):
        aula_atual = self.head  # Começamos na cabeça da lista.
        contador = 0  # Mantemos um contador para saber em que índice estamos.

        while aula_atual is not None:  # Enquanto não chegarmos ao final da lista.
            if contador == indice:  # Se chegarmos ao índice desejado.
                aula_atual.nome = novo_nome
                aula_atual.carga_horaria = nova_carga_horaria
                aula_atual.aulas_semana = novas_aulas_semana
                aula_atual.semanas = nova_carga_horaria // novas_aulas_semana
                aula_atual.total_aulas = aula_atual.semanas * novas_aulas_semana
                return
            aula_atual = aula_atual.next  # Vamos para o próximo nó na lista.
            contador += 1  # Incrementamos o contador.

        print(f"Índice {indice} não encontrado.")

        



