import socket

SERVER_IP = "192.168.1.100"  # Altere para o IP do servidor na rede local
PORT = 5000

# Criar socket TCP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER_IP, PORT))

print("Conectado ao servidor. Digite 'sair' para encerrar.")

while True:
    msg = input("Você: ")
    client_socket.sendall(msg.encode())  # Envia mensagem para o servidor
    if msg.lower() == "sair":
        break

    data = client_socket.recv(1024).decode()  # Recebe resposta do servidor
    print(f"Servidor: {data}")

client_socket.close()
