import grpc
import tasks_pb2
import tasks_pb2_grpc
import socket
import threading

# SOCKET CLIENT
def listen_updates():
    s = socket.socket()
    s.connect(("server", 9000))
    while True:
        msg = s.recv(1024).decode()
        print(f"\n🔔 Update: {msg}")

threading.Thread(target=listen_updates, daemon=True).start()

# gRPC CLIENT
channel = grpc.insecure_channel('server:50051')
stub = tasks_pb2_grpc.TaskServiceStub(channel)

while True:
    print("\n1-Adicionar\n2-Listar\n3-Deletar\n0-Sair")
    op = input("Escolha: ")

    if op == "1":
        titulo = input("Título: ")
        stub.AddTask(tasks_pb2.TaskRequest(id=1, title=titulo))

    elif op == "2":
        res = stub.ListTasks(tasks_pb2.Empty())
        for t in res.tasks:
            print(t.id, t.title)

    elif op == "3":
        tid = int(input("ID: "))
        stub.DeleteTask(tasks_pb2.TaskId(id=tid))

    elif op == "0":
        break
