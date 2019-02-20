from socket import *
import datetime

server_name = 'localhost'
server_port = 50007

# create UDP socket
with socket(AF_INET, SOCK_DGRAM) as soc:
    soc.bind((server_name, server_port))
    while True:
        print('Waiting to receive message')
        data, address = soc.recvfrom(4096)

        print(len(data), address)
        print(data)

        if data.decode() == "getTime":
            print
            sent = soc.sendto(str(datetime.datetime.now()).encode(), address)
            print("Data sent!")
