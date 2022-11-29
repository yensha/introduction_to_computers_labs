import socket
 
HOST = '10.3.141.1'
PORT = 8000
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
print('Connected to: ' + str(HOST) +':8000')
 
while True:
    outdata = input('Send: ')
    #先判斷是否 == EXIT, yes-->break 迴圈-->close connect
    #斷線是client斷而不是server
    if outdata == 'EXIT': 
        print('Closed connection.')
        break
    #在send data過去
    s.send(outdata.encode())
    indata = s.recv(1024)
    print('Echo: ' + indata.decode())
s.close()
