import time
import grpc

import tasks_pb2
import tasks_pb2_grpc


canal = grpc.insecure_channel('server:50051')

stub = tasks_pb2_grpc.TaskServiceStub(canal)

print("\n==============================")
print("CLIENTE CONECTADO")
print("==============================\n")


tarefas = [
    "Estudar Redes",
    "Fazer trabalho",
    "Configurar Docker"
]


# ADICIONAR TAREFAS
for nome in tarefas:

    stub.AddTask(
        tasks_pb2.Task(title=nome)
    )

    print(f"Tarefa adicionada: {nome}")

    time.sleep(1)


# LISTAR TAREFAS
print("\n==============================")
print("LISTA DE TAREFAS")
print("==============================\n")

lista = stub.ListTasks(tasks_pb2.Empty())

for tarefa in lista.tasks:
    print(f"{tarefa.id} - {tarefa.title}")

time.sleep(2)


# REMOVER TAREFA
stub.DeleteTask(
    tasks_pb2.TaskId(id=2)
)

print("\nTarefa removida: 2")

time.sleep(2)


# LISTA FINAL
print("\n==============================")
print("LISTA FINAL")
print("==============================\n")

lista = stub.ListTasks(tasks_pb2.Empty())

for tarefa in lista.tasks:
    print(f"{tarefa.id} - {tarefa.title}")


print("\n==============================")
print("CLIENTE FINALIZADO")
print("==============================\n")