
class Tarefa:
    def __init__(self, nome, descricao):
        if not nome:
            raise ValueError("Nome da tarefa não pode ser vazio.")
        self.nome = nome
        self.descricao = descricao
        self.status = "em andamento"

    def marcar_concluida(self):
        if self.status == "concluída":
            return "Tarefa já concluída."
        self.status = "concluída"

    def marcar_em_andamento(self):
        if self.status == "concluída":
            return "Não é possível reabrir tarefa concluída."
        self.status = "em andamento"

    def editar(self, nome, descricao):
        if not nome:
            raise ValueError("Nome da tarefa não pode ser vazio.")
        self.nome = nome
        self.descricao = descricao


class ListaDeTarefas:
    def __init__(self):
        self.tarefas = []

    def adicionar(self, tarefa):
        self.tarefas.append(tarefa)

    def remover(self, tarefa):
        if tarefa in self.tarefas:
            self.tarefas.remove(tarefa)
        else:
            raise ValueError("Tarefa não encontrada.")
