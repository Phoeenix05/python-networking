import socket

T_PORT = 5006
TCP_IP = '192.168.10.57'
BUF_SIZE = 1024

# create a socket object named 'k'
k = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
k.connect((TCP_IP, T_PORT))

while True:
  MSG = str(input(f'Enter a message – '))
  
  if MSG == '.stop': break

  k.send(MSG.encode('utf8'))

# data = k.recv(BUF_SIZE)

k.close()