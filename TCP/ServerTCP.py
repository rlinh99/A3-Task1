from socket import *
import datetime

# define server ip address and port
server_name = '192.168.1.73'
server_port = 50007

# create TCP socket
soc = socket(AF_INET, SOCK_STREAM)
# bind TCP socket with address and port
soc.bind((server_name, server_port))
# listening to incoming TCP requests.
soc.listen(5)

try:
    while True:
        # accept connections socket from outside
        (client_socket, address) = soc.accept()
        try:
            # receive message from accepted socket
            request = client_socket.recv(1024)
            print("Received")
            # validate received request
            if str(request.decode()) == 'get_time':
                # send server's current time as response
                response = datetime.datetime.now()
                client_socket.send(str(response).encode())
        finally:
            client_socket.close()
finally:
    soc.close()
