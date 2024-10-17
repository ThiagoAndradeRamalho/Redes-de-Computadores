# O módulo socket forma a base de todas as comunicações de rede em Python. Incluindo
# Nesta linha, podemos criar sockets dentro do nosso programa.
from socket import *

# Define a variável inteira serverPort como 12000.
serverPort = 12000

# Esta linha cria o socket do server, denominado serverSocket. O primeiro parâmetro
# indica a família do endereço; AF_INET indica que a rede subjacente estáusando IPv4. 
# O segundo parâmetro indica que o socket é do tipo SOCK_DGRAM, o que significa que é um socket UDP.
serverSocket = socket(AF_INET, SOCK_DGRAM )

# Esta linha vincula o nuemero de porta 12000 ao socket do servidor. Assim,
# em UDPServer, o código está designando um número de porta ao socket. 
# Com isso, quando alguém enviar um pacote à porta 12000 no endereço IP do servidor, ele será direcionado a este socket
serverSocket.bind(('', serverPort))

# UDPServer, então, entra em um
# laço while; o laço while permitirá que UDPServer receba e processe pacotes dos clientes indefinidamente. 
# No laço while, UDPServer espera um pacote chegar.
print("The server is ready to receive ")
while True:

    # Quando um pacote chega no
    # socket do serv idor, os dados são colocados na variável message, e o endereço de origen1
    # é colocado na variável clientAddress. A variável clien t Address contén1 o endereço IP
    # e o nú1nero de porta do cliente.
    message , clientAddress = serverSocket.recvfrom(2048)

    # Esta linha é o núcleo da nossa aplicação simples. Ela apanha a linha enviada pelo cliente
    # e, após converter a mensagem em uma cadeia, usa o método upper () para passá-la para
    # le tras maiúsculas
    modifiedMessage = message.decode().upper()

    # Por fim, anexa o endereço do cliente (endereço IP e número de porta) à mensagem
    # em letras maiúsculas (após converter a cadeia em bytes), enviando o pacote resultante ao
    # socket do servidor. A Internet, então, entregará o pacote ao endereço do cliente. 
    # Depois que o servidor envia o pacote, ele permanece no laço while, esperando até que outro pacote UDP chegue
    serverSocket.sendto(modifiedMessage.encode(),clientAddress)