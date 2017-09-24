import socket
import time
import struct

CLIENT_IP = 'localhost'
CLIENT_PORT = 12000
BUFFER_SIZE = 2048

sequenceNum = 0
numReceived = 0
lastPing = 10
oList = []
rList = []

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
clientSocket.settimeout(1)

print("Pinging: ", CLIENT_IP, " || Port Number: ", CLIENT_PORT, " :")

while sequenceNum < lastPing:
    packedSequence = struct.pack("i", sequenceNum)
    sequenceNum +=1
     
    startTime = time.time()
    
    clientSocket.sendto(packedSequence, (CLIENT_IP, CLIENT_PORT))

    try:
        packedReceiveTime, serverAddress = clientSocket.recvfrom(BUFFER_SIZE)
        unpackedReceiveTime = struct.unpack("d", packedReceiveTime)
        packedSequence, serverAddress = clientSocket.recvfrom(2048)

        numReceived += 1

        receiveTime = unpackedReceiveTime[0]
        OTT = receiveTime - startTime
        oList.append(float(OTT))
        RTT = ((time.time()) - startTime)
        rList.append(float(RTT))
        print("Ping Message Number: ", sequenceNum, "|| RTT: ", RTT, " || OTT: "
              , OTT, " secs")
        
    except socket.timeout:
        print("Ping Message Number: ", sequenceNum, " Has Timed Out!")

numReceived = float(numReceived)
sequenceNum = float(sequenceNum)
lastPercent = float(numReceived/sequenceNum)
lastPercent = (1 - lastPercent) * 100

maxRTT = max(rList)
minRTT = min(rList)
avgRTT = sum(rList)/len(rList)

maxOTT = max(oList)
minOTT = min(oList)
avgOTT = sum(oList)/len(oList)

#Number of packets sent, received, lost (% loss rate)
#Min, Max, Avg RTT and OTT for all acknowledged ping packets
print(" \n")
print("Number of Packets Sent: ", sequenceNum, " || Received: ",
      numReceived, " || Lost: ", lastPercent, "%")
print("RTT Min: ", minRTT, " || RTT Max: ", maxRTT, " || RTT Avg: ",
      avgRTT)
print("OTT Min: ", minOTT, " || OTT Max: ", maxOTT, " || OTT Avg: ",
      avgOTT)

clientSocket.close()
