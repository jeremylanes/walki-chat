import socket

HOST_IP = '' # accept all
HOST_PORT = 32000
MAX_DATA_SIZE = 1024

s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST_IP, HOST_PORT))
s.listen()

print(f"Waiting for connection on port {HOST_PORT}...")
connection_socket, client_address = s.accept()
print(f'Connection established with {client_address[0]}:{client_address[1]}')

while True:
    text_sent = input('You: ')
    if not text_sent:
        continue
    connection_socket.sendall(text_sent.encode())
    data_received = connection_socket.recv(MAX_DATA_SIZE)
    if not data_received:
        break
    print(f'Client: {data_received.decode()}')

s.close()
connection_socket.close()

# ******************** Autor ********************
# ----------------- Jeremy Lane -----------------

# ******************************* Porfolio *******************************
# -------------------------- www.jeremy.berlin --------------------------