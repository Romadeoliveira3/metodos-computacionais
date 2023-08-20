import datetime

# Classe para representar um documento
class Documento:
    def __init__(self, nome, data_manutencao):
        self.nome = nome
        self.data_manutencao = data_manutencao

# Função para imprimir os documentos
def imprimir_documentos(documentos, data_simulada):
    print(f"Data de execução: {data_simulada}\n")

    # Ordenando os documentos pela data de manutenção e nome
    documentos.sort(key=lambda x: (x.data_manutencao, x.nome))

    for doc in documentos:
        diferenca_dias = (doc.data_manutencao - data_simulada).days

        # Verificando se a manutenção está atrasada
        if diferenca_dias < 1:
            print(f"Documento {doc.nome} impresso com sucesso.")
            print("ATENÇÃO! Equipamento está bloqueado devido a atraso na manutenção.\n")
            continue
        # Verificando se a manutenção é para o dia seguinte
        elif diferenca_dias == 1:  # Correção aqui: a diferença de dias deve ser 0 para o alerta de manutenção no dia seguinte
            print(f"Documento {doc.nome} impresso com sucesso.")
            print("ATENÇÃO! A manutenção desse equipamento é amanhã.\n")
            continue
        print(f"Documento {doc.nome} impresso com sucesso.\n")

# Lista de documentos
documentos = [
    Documento("Manutencao_eqA", datetime.date(2023, 2, 27)),
    Documento("Manutencao_eqB", datetime.date(2023, 2, 20)),
    Documento("Manutencao_eqC", datetime.date(2023, 3, 3)),
    Documento("Manutencao_eqD", datetime.date(2023, 3, 8)),
    Documento("Manutencao_eqE", datetime.date(2023, 2, 23)),
    Documento("Manutencao_eqF", datetime.date(2023, 2, 21)),
    Documento("Manutencao_eqG", datetime.date(2023, 3, 2)),
    Documento("Manutencao_eqH", datetime.date(2023, 2, 24)),
    Documento("Manutencao_eqI", datetime.date(2023, 3, 10)),
    Documento("Manutencao_eqJ", datetime.date(2023, 3, 3)),
    Documento("Manutencao_eqK", datetime.date(2023, 2, 16)), 
    Documento("Manutencao_eqL", datetime.date(2023, 2, 19)),
    Documento("Manutencao_eqM", datetime.date(2023, 3, 10)),
    Documento("Manutencao_eqN", datetime.date(2023, 2, 17)),
    Documento("Manutencao_eqO", datetime.date(2023, 2, 22))
]

# Chamando a função para imprimir os documentos com a data simulada
data_simulada = datetime.date(2023, 2, 16)
imprimir_documentos(documentos, data_simulada)
