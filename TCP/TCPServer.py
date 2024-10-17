# O módulo socket forma a base de todas as comunicações de rede em Python. Incluindo
# Nesta linha, podemos criar sockets dentro do nosso programa.
from socket import *

# Define a variável inteira serverPort como 12000.
serverPort = 12000

# Essa linha cria o socket do server, denominado serverSocket. O primeiro parâmetro
# indica que a rede subjacente está usando IPv4. 
# o segundo parâmetro indica que o socket é do tipo SOCK_STREAM.
serverSocket = socket(AF_INET, SOCK_STREAM )

# O serverSocket será o socket de entrada. Depois de estabelecer essa
# porta de entrada, ele vai ficar esperando e escutando até que algum cliente bata à porta
serverSocket.bind(('', serverPort))

# Essa linha faz com que o servidor escute as requisições de conexão TCP do cliente. 
# O parmetro especifica o número máximo de conexões em fila (pelo menos 1)
serverSocket.listen(1)

# Aqui, o programa entra em um loop infinito. Ele fica aguardando conexões de clientes
print('The server is ready to receive')
while True :

    # Quando o cliente bate a essa porta, o programa chama o método accept() para o serverSocket, 
    # que cria um novo socket no servidor, chamado connectionSocket, dedicado a
    # esse cliente específico. Cliente e servidor, então, completam a apresentação, criando uma
    # conexão TCP entre o clientSocket do cliente e o connectionSocket do servidor.
    # Após estabelecer a conexão TCP, cliente e servidor podem enviar bytes um para o outro por
    # ela. Com TCP, todos os bytes enviados de um lado têm garantias não apenas de que chegarão
    # ao outro lado, mas também na ordem
    connectionSocket, addr = serverSocket.accept()
    sentence = connectionSocket.recv(1024).decode()
    capitalizedSentence = sentence.upper()
    connectionSocket.send(capitalizedSentence.encode())

    # Depois de enviar a sentença modificada ao cliente, fechamos o socket da
    # conexão. Mas como o serverSocket permanece aberto, outro cliente agora pode bater à
    # porta e enviar uma sentença ao servidor, para que seja modificada
    connectionSocket.close()
