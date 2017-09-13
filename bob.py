from socket import *
import expo as ex

g = 1907
p = 784313
s_b = 12067 # Secret known only to Bob
msg_from_Alice = 0 # initialize

server_port = 12000
server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind(("", server_port))
server_socket.listen(1)

while 1:
    connection_socket, addr = server_socket.accept()
    msg_from_Alice = connection_socket.recv(1024).decode()
    # Calculate T_B = g^(s_b) mod p
    msg_to_Alice = str(ex.expo(g, s_b, p)) + "\n"
    connection_socket.send(msg_to_Alice.encode())
    print("Bob sent T_B = ", msg_to_Alice)
    connection_socket.close()

    # Calculate the shared key
    shared_key = ex.expo(int(msg_from_Alice), s_b, p)
    print("Bob calculated the shared key = ", shared_key)
