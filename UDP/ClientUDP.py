from socket import *
import datetime
import subprocess

server_name = 'localhost'
server_port = 50007
# Create a UDP socket
soc = socket(AF_INET, SOCK_DGRAM)

server_address = (server_name, server_port)

try:
    # Send data
    print("Sending")
    start_time = datetime.datetime.now()
    sent = soc.sendto('getTime'.encode(), server_address)
    # Receive response
    print('waiting to receive')
    data_encoded, server = soc.recvfrom(4096)
    end_time = datetime.datetime.now()
    data = data_encoded.decode()
    print('Received')
    print(data)
finally:
    soc.close()
