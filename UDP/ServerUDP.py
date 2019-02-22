from socket import *
import datetime

server_name = '192.168.1.73'
server_port = 50007

# create UDP datagram socket
with socket(AF_INET, SOCK_DGRAM) as soc:
    # bind UDL socket with address and port
    soc.bind((server_name, server_port))
    try:
        while True:
            # UDP socket waiting to receive message from outside world
            print('Waiting to receive message')
            data, address = soc.recvfrom(4096)

            # print debug message
            print(len(data), address)
            print(data)

            # validate received message. send response thereafter
            if data.decode() == "get_time":
                sent = soc.sendto(str(datetime.datetime.now()).encode(), address)
                print("Data sent!")
    finally:
        soc.close()