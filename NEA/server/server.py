import socket
 
mySocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
 
port = 8335
serverIP = "10.2.20.117"

mySocket.bind((serverIP, port))

while True:
  data, addr = mySocket.recvfrom(1024)
  print(f'Data recieved:{data} from address:{addr}')
  if not data:
    break
  else:
    mySocket.sendto(data, addr)