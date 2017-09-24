import socket

CLIENT_IP = 'localhost'
CLIENT_PORT = 12000
BUFFER_SIZE = 2048
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

for i in range(0,3):
    MESSAGE = raw_input("Enter a message in all lowercase: ")
    
    try:
        clientSocket.settimeout(.2)
        clientSocket.sendto(MESSAGE.encode(), (CLIENT_IP, CLIENT_PORT))
        
        modifiedMessage, serverAddress = clientSocket.recvfrom(BUFFER_SIZE)
        print("Successfully connected to: " + CLIENT_IP +
              " on Port: " + str(CLIENT_PORT))
        print("Original: " + MESSAGE)
        print("New: " + modifiedMessage.decode())
        print(" ")

    except socket.timeout:
        print("Cannot connect to: " + CLIENT_IP +
              " on Port: " + str(CLIENT_PORT))
        print(" ")

clientSocket.close()
