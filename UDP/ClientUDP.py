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
    data_encoded, server = soc.recvfrom(4096)
    end_time = datetime.datetime.now()
    response = data_encoded.decode()

    print('Received')

    offset = (end_time - start_time) / 2
    result = datetime.datetime.strptime(response, '%Y-%m-%d %H:%M:%S.%f') + offset

    print("Request sent at: {0}".format(start_time))
    print("Reply received at : {0}".format(end_time))
    print("Offset (RTT/2) is {0}".format(offset))

    # subprocess.run(["date", "-s", str(result)])
    print("Time is set to: {0}".format(str(result)))
finally:
    soc.close()
