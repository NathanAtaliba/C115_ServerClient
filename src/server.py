from socket import *
import pymongo

  # Conectar-se ao servidor MongoDB (localhost, porta padrão 27017)
try:
  client = pymongo.MongoClient("mongodb://localhost:27017/")
  # Acessar um banco de dados
  db = client["test"]
  # Acessar uma coleção
  users = db["users"]
  questions = db["questions"]
  print('Conectado com sucesso!')
except Exception as e:
  print("Ocorreu um erro ao conectar com o bando de dados!")

#Json formatado com as perguntas
questions = {
  "pergunta1" : "Qual é a capital de são Paulo? \n",
  "options1":{
  "1 - ": "São Paulo \n",
  "2 - ": "Rio de janeiro \n",
  "3 - ": "Belo Horizonte \n",
  "4 - ": "Brasilia \n", 
  },

  "pergunta2" : "Qual é a capital de Rio de Janeiro? \n",
  "options2":{
  "1 - ": "São Paulo \n",
  "2 - ": "Rio de janeiro \n",
  "3 - ": "Belo Horizonte \n",
  "4 - ": "Brasilia \n",
  },

  "pergunta3" : "Qual é a capital de Minas gerais? \n",
  "options3":{
  "1 - ": "São Paulo \n",
  "2 - ": "Rio de janeiro \n",
  "3 - ": "Belo Horizonte \n",
  "4 - ": "Brasilia \n",  
  }
}

respostas = ['1','2','3']
# Porta do servidor  
serverPort = 5000
# Criando um socket com uma determinada familia e tipo
serverSocket = socket(AF_INET, SOCK_STREAM)
# Associando o servidor a um determinado endereço e porta
serverSocket.bind(('', serverPort))
# Configura e inicia o ouvinte TCP
serverSocket.listen(1)
# Tempo máximo que o servidor irá esperar pela resposta do cliente
serverSocket.settimeout(1000)

print("Server is ready")


while True:
  # Aceita a conexão
  connectionSocket, addr = serverSocket.accept()
  
  # Pegando o nome do usuario
  connectionSocket.send(("Entre com seu nome: ").encode())
  nome = connectionSocket.recv(1024).decode()


  # Envia a primeira questao e recebe a resposta do cliente
  connectionSocket.send(questions["pergunta1"].encode())
  connectionSocket.send(questions["options1"]["1 - "].encode())
  connectionSocket.send(questions["options1"]["2 - "].encode())
  connectionSocket.send(questions["options1"]["3 - "].encode())
  escolha1 = connectionSocket.recv(1024).decode()

  # Envia a segunda questao e recebe a resposta do cliente
  connectionSocket.send(questions["pergunta2"].encode())
  connectionSocket.send(questions["options2"]["1 - "].encode())
  connectionSocket.send(questions["options2"]["2 - "].encode())
  connectionSocket.send(questions["options2"]["3 - "].encode())
  escolha2 = connectionSocket.recv(1024).decode()

  # Envia a terceira questao e recebe a resposta do cliente
  connectionSocket.send(questions["pergunta3"].encode())
  connectionSocket.send(questions["options3"]["1 - "].encode())
  connectionSocket.send(questions["options3"]["2 - "].encode())
  connectionSocket.send(questions["options3"]["3 - "].encode())
  escolha3 = connectionSocket.recv(1024).decode()
  
  escolhas = [escolha1, escolha2, escolha3]
  contagemAcerto = 0
  contagemErro = 0
  for escolha in range(0, len(escolhas)):
    if escolhas[escolha] == respostas[escolha]:
      contagemAcerto = contagemAcerto + 1
      contagemErro = contagemErro
    else:
      contagemAcerto = contagemAcerto
      contagemErro = contagemErro + 1

  users.insert_one({"nome": nome, "Acertos": str(contagemAcerto),"Erros":  str(contagemErro)})
  print("Usuarios: ")
  usersList = users.find()

  usuarios_str = "\n".join([f"Nome: {user['nome']}, Acertos: {user['Acertos']}, Erros: {user['Erros']}" for user in usersList])
  connectionSocket.send(usuarios_str.encode())
  for user in usersList:
    print("Nome: ", user["nome"]  ," Acertos: ", user["Acertos"]," Erros: ", user["Erros"])
  
  # Fecha a conexão
  connectionSocket.close()