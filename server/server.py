from concurrent import futures
import grpc

import tasks_pb2
import tasks_pb2_grpc


tarefas = []
contador = 1


class TaskService(tasks_pb2_grpc.TaskServiceServicer):

    def AddTask(self, request, context):
        global contador

        tarefa = {
            "id": contador,
            "title": request.title
        }

        tarefas.append(tarefa)

        print("\n==============================")
        print("Nova atualização enviada")
        print(f"Tarefa adicionada: {request.title}")
        print("==============================\n")

        contador += 1

        return tasks_pb2.Empty()

    def ListTasks(self, request, context):

        print("\nCliente conectado")
        print("Listando tarefas...\n")

        resposta = tasks_pb2.TaskList()

        for tarefa in tarefas:
            item = resposta.tasks.add()
            item.id = tarefa["id"]
            item.title = tarefa["title"]

        return resposta

    def DeleteTask(self, request, context):

        global tarefas

        tarefas = [
            t for t in tarefas if t["id"] != request.id
        ]

        print("\n==============================")
        print("Nova atualização enviada")
        print(f"Tarefa removida: {request.id}")
        print("==============================\n")

        return tasks_pb2.Empty()


def serve():

    servidor = grpc.server(
        futures.ThreadPoolExecutor(max_workers=10)
    )

    tasks_pb2_grpc.add_TaskServiceServicer_to_server(
        TaskService(),
        servidor
    )

    servidor.add_insecure_port('[::]:50051')

    print("\n==============================")
    print("Servidor iniciado...")
    print("gRPC rodando na porta 50051")
    print("==============================\n")

    servidor.start()

    servidor.wait_for_termination()


if __name__ == '__main__':
    serve()