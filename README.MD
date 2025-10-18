Aluna: Lauren Kunz e Silva
RA:23118770-2
Curso: Engenharia de Software
Turma: B
6° Semestre:
PROJETO IMPLEMENTAÇÃO E TESTE DE SOFTWARE

Requisito 1 — Adicionar tarefa

Comportamento esperado:
O sistema deve permitir adicionar uma nova tarefa à lista.
Cada tarefa deve conter um título (string).
Quando uma tarefa for adicionada, ela deve aparecer na lista de tarefas pendentes.

Teste (em pseudocódigo):

Criar uma lista vazia.

Adicionar uma tarefa chamada “Estudar TDD”.

Verificar se a lista contém essa tarefa.

Requisito 2 — Marcar tarefa como concluída

Comportamento esperado:
O usuário deve poder marcar uma tarefa como concluída.
Ao fazer isso, o status da tarefa muda de “pendente” para “concluída”.

Teste (em pseudocódigo):

Criar uma lista e adicionar uma tarefa “Ler documentação do Python”.

Marcar essa tarefa como concluída.

Verificar se o status da tarefa é “concluída”.

Requisito 3 — Remover tarefa

Comportamento esperado:
O sistema deve permitir remover uma tarefa existente.
Ao remover, a tarefa deixa de existir na lista.

Teste (em pseudocódigo):

Adicionar duas tarefas: “Estudar” e “Dormir”.

Remover “Dormir”.

Verificar que apenas “Estudar” permanece na lista.

Requisito 4 — Listar tarefas pendentes

Comportamento esperado:
O sistema deve exibir todas as tarefas que ainda não foram concluídas.

Teste (em pseudocódigo):

Adicionar três tarefas.

Marcar uma como concluída.

Verificar que apenas as duas pendentes aparecem na listagem.

Requisito 5 — Contar tarefas concluídas

Comportamento esperado:
O sistema deve permitir saber quantas tarefas já foram concluídas.

Teste (em pseudocódigo):

Adicionar três tarefas.

Marcar duas como concluídas.

Verificar se o número de concluídas é 2.