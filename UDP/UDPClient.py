# O módulo socket forma a base de todas as comunicações de rede em Python. Incluindo
# esta linha, poderemos criar sockets dentro do nosso progra1na.
from socket import *

# Aqui, oferecemos uma cadeia contendo ou o endereço IP do servidor (p. ex., "128.138.32.126") ou o nome
# de hospedeiro do servidor (p. ex., "cis.poly.edu"). Se usannos o nome do hospedeiro, então
# uma pesquisa DNS será automaticamente realizada para obter o endereço IP.
serverName = 'localhost'

# Define a variável inteira serverPort como 12000.
serverPort = 12000

# Esta linha cria o socket do cliente, denominado clientSocket. O primeiro parâmetro
# indica a família do endereço; AF_INET indica que a rede subjacente estáusando IPv4. 
# O segundo parâmetro indica que o socket é do tipo SOCK_DGRAM, o que significa que é um socket UDP.
clientSocket = socket(AF_INET, SOCK_DGRAM )

# Quando esse comando input() é executado, o usuário no cliente recebe o texto "Input lowercase sentence:". 
# Então, o usuário usa seu teclado para digitar uma linha, que é colocada na variável message
message = input('Input lowercase sentence :') 

# Nesta linha, usamos o metodo encode() para convertemos a mensagem do tipo cadeia para o tipo byte, para enviar bytes a um socket; 
# sendto() acrescenta o endereço de destino (serverName, serverPort) à mensagem
# e envia o pacote resultante pelo socket do processo, clientSocket.
clientSocket.sendto(message.encode(),(serverName, serverPort))

# Quando um pacote chega da Internet no socket do cliente, os dados são
# colocados na variável modifiedMessage, e o endereço de origem do pacote é colocado na variável serverAddress
#A variável serverAddress tem tanto o endereço IP do servidor quanto o número de porta do servidor. 
# O método recvfrom também toma o tamanho do buffer, 2048, co1no entrada.
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)

# Aqui, usamos o método decode() para converter os bytes do pacote de volta para uma cadeia,
print(modifiedMessage.decode())

# Ao final, fechamos o socket do cliente para encerrar a conexão, e então o processo é concluido
clientSocket.close()