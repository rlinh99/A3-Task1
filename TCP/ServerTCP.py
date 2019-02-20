from socket import *
import datetime

server_name = 'localhost'
server_port = 50007

soc = socket(AF_INET, SOCK_STREAM)
soc.bind((server_name, server_port))
soc.listen(5)

while True:
    # accept connections from outside
    (client_socket, address) = soc.accept()
    try:
        request = client_socket.recv(1024)
        print("Received")
        print(request)
        if str(request.decode()) == 'get_time':
            print("test")
            response = datetime.datetime.now()
            client_socket.send(str(response).encode())
    finally:
        client_socket.close()
    # in this case, we'll pretend this is a threaded server
