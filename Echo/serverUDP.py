import socket

SERVER_IP = 'localhost'
SERVER_PORT = 12000
BUFFER_SIZE = 2048
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

serverSocket.bind((SERVER_IP, SERVER_PORT))

print("Server is ready to receive!")

while True:
    MESSAGE, clientAddress = serverSocket.recvfrom(BUFFER_SIZE)
    print("Client's Address: " + str(clientAddress) + " || " +
          "Client's Message: " + MESSAGE)
    modifiedMessage = MESSAGE.decode().upper()
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)
