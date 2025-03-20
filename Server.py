import socket

HOST = "0.0.0.0"  # Escuta em todas as interfaces
PORT = 5000  # Porta fixa para comunicação

# Criar socket TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)  # Aceita apenas 1 conexão

print(f"Servidor aguardando conexão na porta {PORT}...")
conn, addr = server_socket.accept()
print(f"Conectado por {addr}")

while True:
    data = conn.recv(1024).decode()  # Recebe mensagem do cliente
    if not data or data.lower() == "sair":
        print("Conexão encerrada pelo cliente.")
        break
    print(f"Cliente: {data}")

    msg = input("Você: ")  # Envia resposta
    conn.sendall(msg.encode())

conn.close()
server_socket.close()
