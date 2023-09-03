from socket import *

# Endereço do servidor
serverName = 'localhost'
# Porta do servidor
serverPort = 8000

# Criando um socket com uma determinada familia e tipo
clientSocket = socket(AF_INET, SOCK_STREAM)
# Estabelendo a conexão cliente-servidor
clientSocket.connect((serverName, serverPort))
print('Conectado em {}, {}'.format(serverPort, serverName))

nameMessage = clientSocket.recv(1024).decode()
name = input("Nome: ")
clientSocket.send(name.encode())

# Recebendo a mensagem do servidor com as opções e enviando a opção do cliente
print("Primeira questao:")
message1 = clientSocket.recv(1024).decode()
print(message1)
option1 = input("Opção para primeira questao: ")
print("")
clientSocket.send(option1.encode())

# Recebendo a mensagem do servidor com as opções e enviando a opção do cliente
print("Segunda questao:")
message2 = clientSocket.recv(1024).decode()
print(message2)
option2 = input("Opção para segunda questao: ")
clientSocket.send(option2.encode())

# Recebendo a mensagem do servidor com as opções e enviando a opção do cliente
print("Terceira Questao:")
message3 = clientSocket.recv(1024).decode()
print(message3)
option3 = input("Opção para terceira questao: ")
print("")
clientSocket.send(option3.encode())


#MOSTRANDO USUARIOS
usuarios = clientSocket.recv(1024).decode()
print("Lista de usuarios: ")
print(usuarios)


# Fechando a conexão
clientSocket.close()