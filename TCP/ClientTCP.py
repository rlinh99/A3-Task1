from socket import *
from datetime import *
import subprocess

# define Address and Port
server_name = '192.168.1.73'
server_port = 50007

# create TCP stream socket
soc = socket(AF_INET, SOCK_STREAM)
# connect client socket to server socket
soc.connect((server_name, server_port))

try:
    # start sending message via TCP socket
    start_time = datetime.now()
    soc.send("get_time".encode())
    # receive message from socket
    data_encoded = soc.recv(4096)
    end_time = datetime.now()

    response = data_encoded.decode()

    # calculation
    offset = (end_time - start_time) / 2
    # parse time string into datetime, calculate result client time
    result = datetime.strptime(response, '%Y-%m-%d %H:%M:%S.%f') + offset

    print("Request sent at: {0}".format(start_time))
    print("Reply received at : {0}".format(end_time))
    print("Offset (RTT/2) is {0}".format(offset))

    # optional: mock linux command line argument to set system time
    # only works with linux, run with sudo permission
    subprocess.run(["date", "-s", str(result)])
    print("Time is set to: {0}".format(str(result)))
finally:
    soc.close()
