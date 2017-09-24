import socket
import random
import time
import struct

SERVER_IP = 'localhost'
SERVER_PORT = 12000
BUFFER_SIZE = 2048

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("The server is ready to receieve on port: " + str(SERVER_PORT))

serverSocket.bind((SERVER_IP, SERVER_PORT))

while True:
    randNum = random.randint(0,10)

    packedSequence, clientAddress = serverSocket.recvfrom(BUFFER_SIZE)
    unpacked = struct.unpack("i", packedSequence)

    receiveTime = time.time()
    packedReceiveTime = struct.pack("d", receiveTime)

    if randNum < 4:
        print("Message With Sequence Number " + str(unpacked) + "dropped.")
        continue
    else:
        print("Responding to ping request with sequence number " + str(unpacked)
              + " received at " + str(receiveTime))
        serverSocket.sendto(packedReceiveTime, clientAddress)
        serverSocket.sendto(packedSequence, clientAddress)
