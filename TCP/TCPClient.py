# O módulo socket forma a base de todas as comunicações de rede em Python. Incluindo
# Nesta linha, podemos criar sockets dentro do nosso programa.
from socket import *

# Aqui, oferecemos uma cadeia contendo ou o endereço IP do servidor (p. ex., "128.138.32.126") ou o nome
# de hospedeiro do servidor (p. ex., "cis.poly.edu"). Se usannos o nome do hospedeiro, então
# uma pesquisa DNS será automaticamente realizada para obter o endereço IP.
serverName = 'localhost'

# Define a variável inteira serverPort como 12000.
serverPort = 12000

# Essa linha cria o socket do cliente, denominado clientSocket. O primeiro parâmetro
# indica que a rede subjacente está usando IPv4. 
# o segundo parâmetro indica que o socket é do tipo SOCK_STREAM.
clientSocket = socket (AF_INET, SOCK_STREAM )

# Lembre-se de que, antes de um cliente poder enviar dados ao servidor (e vice-versa) usando
# um socket TCP, primeiro deve ser estabelecida uma conexão TCP entre eles, o que é feito
# por meio dessa linha. O parâmetro do método connect() é o endereço do lado servidor da conexão
clientSocket.connect((serverName, serverPort))

# Essa linha obtém uma sentença do usuário. A cadeia sentence continua a reunir caracteres 
# até que o usuário termine a linha digitando um Enter
sentence = input('Input lowercase sentence : ')

# Essa linha envia a cadeia sentence pelo socket do cliente e para a conexão TCP. E então deixa os bytes da cadeia
# sentence na conexão TCP. O cliente, então, espera para receber bytes do servidor.
clientSocket.send(sentence.encode())

# Quando os caracteres chegam do servidor, eles são colocados na cadeia modifiedSentence. 
# Os caracteres continuam a ser acumulados em modifiedSentence até que a linha termine com um caractere de Enter. 
modifiedSentence = clientSocket.recv(1024)

# O método decode() é usado para converter os bytes do pacote de volta para uma cadeia,
print('From Server: ', modifiedSentence.decode())

#Essa última linha fecha o socket e a conexão TCP entre cliente e servidor.
clientSocket.close()