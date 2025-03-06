import socket

s = socket.socket()
print("Socket successfully created!")

port = 80

s.bind(('', port))
print(f'Socket binded to {port}')

s.listen(5)
print('Socket is listening')

while True:
    c, addr = s.accept()
    print(f'Connection received from {addr}')

    c.send('Connected!')

    c.close()
    break