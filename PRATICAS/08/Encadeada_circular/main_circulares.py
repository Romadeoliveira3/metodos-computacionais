import unittest
from aulas_circulares import *
from memory_profiler import memory_usage

def run_test(test_class, test_method):
    suite = unittest.TestSuite()
    suite.addTest(test_class(test_method))
    runner = unittest.TextTestRunner()
    runner.run(suite)

def get_average_memory_usage(tests):
    total_memory_usage = 0
    for test_class, test_method in tests:
        mem_usage = memory_usage((run_test, (test_class, test_method)))
        total_memory_usage += max(mem_usage)  # Use max memory usage for each test
    return total_memory_usage / len(tests)

class TestAula(unittest.TestCase):
    def setUp(self):
        self.aula = Aula("Matemática", 60, 3)

    def test_adicionar_falta(self):
        self.aula.adicionar_falta()
        self.assertEqual(self.aula.aulas_faltadas, 1)

    def test_mostrar_faltas(self):
        self.aula.adicionar_falta()
        self.assertEqual(self.aula.mostrar_faltas(), 1)

class TestListaDeAulas(unittest.TestCase):
    def setUp(self):
        self.lista_de_aulas = ListaDeAulas()

    def test_inserir_inicio(self):
        self.lista_de_aulas.inserir_inicio("Matemática", 60, 3)
        self.assertEqual(self.lista_de_aulas.head.nome, "Matemática")
        self.assertEqual(self.lista_de_aulas.tail.nome, "Matemática")

    def test_inserir_final(self):
        self.lista_de_aulas.inserir_inicio("Matemática", 60, 3)
        self.lista_de_aulas.inserir_final("Física", 60, 3)
        self.assertEqual(self.lista_de_aulas.tail.nome, "Física")
        self.assertEqual(self.lista_de_aulas.head.next.nome, "Física")

    def test_buscar_aula(self):
        self.lista_de_aulas.inserir_inicio("Matemática", 60, 3)
        aula = self.lista_de_aulas.buscar_aula("Matemática")
        self.assertEqual(aula.nome, "Matemática")

    def test_inserir_apos(self):
        self.lista_de_aulas.inserir_inicio("Matemática", 60, 3)
        self.lista_de_aulas.inserir_apos("Matemática", "Física", 60, 3)
        self.assertEqual(self.lista_de_aulas.head.next.nome, "Física")

    def test_remover_aula(self):
        self.lista_de_aulas.inserir_inicio("Matemática", 60, 3)
        self.lista_de_aulas.remover_aula("Matemática")
        self.assertIsNone(self.lista_de_aulas.buscar_aula("Matemática"))

    def test_atualizar_aula(self):
        self.lista_de_aulas.inserir_inicio("Matemática", 60, 3)
        self.lista_de_aulas.atualizar_aula("Matemática", "Português", 60, 3)
        self.assertEqual(self.lista_de_aulas.head.nome, "Português")

if __name__ == "__main__":
    tests = [(TestAula, 'test_adicionar_falta'), (TestAula, 'test_mostrar_faltas'), (TestListaDeAulas, 'test_inserir_inicio'), (TestListaDeAulas, 'test_inserir_final'), (TestListaDeAulas, 'test_buscar_aula'), (TestListaDeAulas, 'test_inserir_apos'), (TestListaDeAulas, 'test_remover_aula'), (TestListaDeAulas, 'test_atualizar_aula')]
    average_memory_usage = get_average_memory_usage(tests)
    print(f'Average max memory usage for tests: {average_memory_usage} MiB')
