from socket import *
import expo as ex

g = 1907
p = 784313
s_a = 160011 # Secret known only to Alice

# Calculate T_A = g^(s_a) mod p
msg = str(ex.expo(g, s_a, p)) + "\n"
print("Alice generated T_A = ",msg)

# Create TCP connection with Bob
server_name = "localhost"
server_port = 12000 # the port Bob is listening on
client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect((server_name, server_port))
client_socket.send(msg.encode())
msg_from_Bob = client_socket.recv(1024).decode()
client_socket.close()

shared_key = ex.expo(int(msg_from_Bob), s_a, p)
print("Alice calculated shared key = ", shared_key)
