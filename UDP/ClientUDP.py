from socket import *
import datetime
import subprocess

server_name = '192.168.1.73'
server_port = 50007
# Create UDP datagram socket
soc = socket(AF_INET, SOCK_DGRAM)

server_address = (server_name, server_port)

try:
    # send data to destination socket
    print("Sending UDP packet to server")
    # record start time
    start_time = datetime.datetime.now()
    sent = soc.sendto('get_time'.encode(), server_address)
    # receive response from server
    data_encoded, server = soc.recvfrom(4096)
    # record end time
    end_time = datetime.datetime.now()

    # decode response message to str
    response = data_encoded.decode()

    print('Received response from server')

    # calculate final result client time
    offset = (end_time - start_time) / 2
    # parse time string into datetime, calculate result client time
    result = datetime.datetime.strptime(response, '%Y-%m-%d %H:%M:%S.%f') + offset

    print("Request sent at: {0}".format(start_time))
    print("Reply received at : {0}".format(end_time))
    print("Offset (RTT/2) is {0}".format(offset))
    # optional: mock linux command line argument to set system time
    # only works with linux, run with sudo permission
    subprocess.run(["date", "-s", str(result)])
    print("Time is set to: {0}".format(str(result)))
finally:
    soc.close()
