import unittest
from todo import Tarefa, ListaDeTarefas

class TestTodoList(unittest.TestCase):

    def setUp(self):
        self.lista = ListaDeTarefas()
        self.tarefa = Tarefa("Comprar pelucias", "Ir até a loja comprar pelucias")

    # REQ-01: Adicionar tarefas
    def test_adicionar_tarefa(self):
        self.lista.adicionar(self.tarefa)
        self.assertIn(self.tarefa, self.lista.tarefas)

    def test_adicionar_tarefa_sem_nome(self):
        with self.assertRaises(ValueError):
            Tarefa("", "Descrição")

    # REQ-02: Marcar tarefa como concluída
    def test_marcar_concluida(self):
        self.tarefa.marcar_concluida()
        self.assertEqual(self.tarefa.status, "concluída")

    def test_marcar_concluida_ja_concluida(self):
        self.tarefa.marcar_concluida()
        mensagem = self.tarefa.marcar_concluida()
        self.assertEqual(mensagem, "Tarefa já concluída.")

    # REQ-03: Marcar tarefa como em andamento
    def test_marcar_em_andamento(self):
        self.tarefa.marcar_em_andamento()
        self.assertEqual(self.tarefa.status, "em andamento")

    def test_marcar_em_andamento_tarefa_concluida(self):
        self.tarefa.marcar_concluida()
        mensagem = self.tarefa.marcar_em_andamento()
        self.assertEqual(mensagem, "Não é possível reabrir tarefa concluída.")

    # REQ-04: Editar tarefa
    def test_editar_tarefa(self):
        self.tarefa.editar("Comprar perfumes", "Ir a loja comprar perfumes")
        self.assertEqual(self.tarefa.nome, "Comprar perfumes")
        self.assertEqual(self.tarefa.descricao, "Ir a loja comprar perfumes")

    def test_editar_tarefa_sem_nome(self):
        with self.assertRaises(ValueError):
            self.tarefa.editar("", "Nova descrição")

    # REQ-05: Remover tarefa
    def test_remover_tarefa(self):
        self.lista.adicionar(self.tarefa)
        self.lista.remover(self.tarefa)
        self.assertNotIn(self.tarefa, self.lista.tarefas)

    def test_remover_tarefa_inexistente(self):
        with self.assertRaises(ValueError):
            self.lista.remover(Tarefa("Não existe", "Teste"))

if __name__ == '__main__':
    unittest.main()
