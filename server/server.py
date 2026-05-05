import grpc
from concurrent import futures
import tasks_pb2
import tasks_pb2_grpc
import socket
import threading

tasks = []
clients = []

# SOCKET SERVER
def socket_server():
    s = socket.socket()
    s.bind(("0.0.0.0", 9000))
    s.listen()
    print("Socket ativo na porta 9000")

    while True:
        conn, addr = s.accept()
        clients.append(conn)
        print("Cliente conectado:", addr)

threading.Thread(target=socket_server, daemon=True).start()

def notify_all(message):
    for c in clients:
        try:
            c.send(message.encode())
        except:
            pass

# gRPC SERVICE
class TaskService(tasks_pb2_grpc.TaskServiceServicer):

    def AddTask(self, request, context):
        tasks.append({"id": request.id, "title": request.title})
        notify_all(f"Nova tarefa: {request.title}")
        return tasks_pb2.TaskResponse(message="Tarefa adicionada")

    def ListTasks(self, request, context):
        return tasks_pb2.TaskList(
            tasks=[tasks_pb2.Task(id=t["id"], title=t["title"]) for t in tasks]
        )

    def DeleteTask(self, request, context):
        global tasks
        tasks = [t for t in tasks if t["id"] != request.id]
        notify_all(f"Tarefa removida ID {request.id}")
        return tasks_pb2.TaskResponse(message="Tarefa removida")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    tasks_pb2_grpc.add_TaskServiceServicer_to_server(TaskService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Servidor gRPC rodando na porta 50051")
    server.wait_for_termination()

serve()
