from socket import *
from datetime import *
from subprocess import *

server_name = 'localhost'
server_port = 50007

soc = socket(AF_INET, SOCK_STREAM)
soc.connect((server_name, server_port))

try:
    start_time = datetime.now()
    soc.send("get_time".encode())
    data_encoded = soc.recv(4096)
    end_time = datetime.now()

    response = data_encoded.decode()

    offset = (end_time - start_time) / 2
    result = datetime.strptime(response, '%Y-%m-%d %H:%M:%S.%f') + offset

    print("Request sent at: {0}".format(start_time))
    print("Reply received at : {0}".format(end_time))
    print("Offset (RTT/2) is {0}".format(offset))

    # subprocess.run(["date", "-s", str(result)])
    print("Time is set to: {0}".format(str(result)))
finally:
    soc.close()
