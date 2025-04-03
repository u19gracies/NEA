import socket

port = 8335  # The port used by the server

mySocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

mySocket.sendto(b"Some user data", ("10.2.20.117", port))

while True:
    data, addr = mySocket.recvfrom(1024)
    print(f'Data recieved:{data} from address:{addr}')

