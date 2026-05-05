# 📋 Gestor de Tarefas Multi-Usuário (Grupo 7)

## 📖 Descrição

Este projeto consiste em um sistema distribuído de gestão de tarefas (To-Do List) multi-usuário, desenvolvido no âmbito da disciplina de Sistemas Distribuídos.

O sistema permite que vários clientes adicionem, listem e removam tarefas em tempo real, com sincronização entre diferentes dispositivos.

---

## 🎯 Objetivos

* Implementar um sistema distribuído com múltiplos clientes
* Utilizar gRPC para operações CRUD
* Implementar comunicação em tempo real com Sockets
* Demonstrar funcionamento em ambiente Docker
* Comparar gRPC com RMI em termos de manutenção e desempenho

---

## 🧩 Tecnologias Utilizadas

* Python 🐍
* gRPC
* Sockets TCP
* Docker & Docker Compose
* Git & GitHub

---

## ⚙️ Funcionalidades

### ✔ CRUD de Tarefas (gRPC)

* Adicionar tarefa
* Listar tarefas
* Remover tarefa

### ✔ Live Update (Sockets)

* Notificação em tempo real quando:

  * Uma tarefa é adicionada
  * Uma tarefa é removida

### ✔ Multiusuário

* Vários clientes conectados simultaneamente
* Atualizações sincronizadas

---

## 🏗️ Estrutura do Projeto

```
grupo7-gestor-tarefas/
│
├── proto/
│   └── tasks.proto
│
├── server/
│   └── server.py
│
├── client/
│   └── client.py
│
├── Dockerfile.server
├── Dockerfile.client
├── docker-compose.yml
└── README.md
```

---

## 🚀 Como Executar o Projeto

### 🔹 Pré-requisitos

* Docker instalado
* Docker Desktop em execução

---

### 🔹 Passos

```bash
docker compose up --build
```

---

## 🧪 Funcionamento

1. O servidor inicia (gRPC + Socket)
2. Dois clientes são executados
3. Um cliente adiciona uma tarefa
4. O outro cliente recebe atualização em tempo real

---

## 💡 Exemplo de Uso

```
Cliente 1:
Adicionar tarefa → "Estudar Redes"

Cliente 2:
🔔 Update: Nova tarefa: Estudar Redes
```

---

## 📊 Comparação: gRPC vs RMI

| Critério    | gRPC            | RMI             |
| ----------- | --------------- | --------------- |
| Linguagem   | Multiplataforma | Apenas Java     |
| Contratos   | Arquivos .proto | Interfaces Java |
| Performance | Alta (binário)  | Média           |
| Manutenção  | Fácil           | Mais complexa   |

### 🧠 Conclusão

O gRPC apresenta maior flexibilidade, melhor desempenho e facilidade de manutenção devido ao uso de arquivos `.proto`, sendo mais adequado para sistemas distribuídos modernos.

---

## 👨‍💻 Autor(es)

Grupo 7 – Sistemas Distribuídos
Lucas Mário Armando
Porfirio Aristides
Albano Hussene 
---

## 📅 Data de Entrega

07 de Maio de 2026

---

## 🔗 Repositório

(https://github.com/lucas19700/grupo7-gestor-tarefas.git)
