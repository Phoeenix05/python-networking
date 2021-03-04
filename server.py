import socket

T_PORT = 5006
TCP_IP = '192.168.10.57'
BUF_SIZE = 30

# create a socket object named 'k'
k = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
k.bind((TCP_IP, T_PORT))
k.listen(1)

con, addr = k.accept()
print(f'Connection address is: {addr}')

while True :
    data = con.recv(BUF_SIZE)
    
    if not data: break
    
    print ("Received data", data)

con.send(data)
con.close()