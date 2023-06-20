import socket
import time

HOST_IP = '127.0.0.1' # server ip address
HOST_PORT = 32000
MAX_DATA_SIZE = 1024

print(f'Connection to the server {HOST_IP}:{HOST_PORT}...')
while True:
    try:
        s = socket.socket()
        s.connect((HOST_IP, HOST_PORT))
    except ConnectionRefusedError:
        print('Impossible to connect to the server! Reconnect...')
        time.sleep(4)
    else:
        print('connection established with the server')
        break
        
# ------------------- utilisation du socket --------------------
while True:
    data_received = s.recv(MAX_DATA_SIZE)
    if not data_received:
        break

    print(f'Server: {data_received.decode()}')
    text_sent = None
    while not text_sent:
        text_sent = input('You: ')
    s.sendall(text_sent.encode())

s.close()

# ******************** Auteur ********************
# ----------------- Jeremy Lane -----------------

# ******************************* Porfolio *******************************
# ----------------- https://jeremylane.pythonanywhere.com/ -----------------