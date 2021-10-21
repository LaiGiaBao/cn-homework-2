from socket import *
from io import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print('The server is ready to receive')
while True:
    connectionSocket, addr = serverSocket.accept()
    filename = connectionSocket.recv(1024).decode('utf-8')
    fileType = filename.split('.')[1]
    try:
        if fileType == "txt":
            file = open(filename, "r", encoding="utf-8")
            data = file.read()
            message = '\nHTTP/1.1 404 not found\n\nContent-Type: text/html; charset=utf-8\n\n'
            message += data
            connectionSocket.send(message.encode('utf-8'))
            connectionSocket.close()
    except IOError:
        connectionSocket.send('\nHTTP/1.1 404 not found\n\n'.encode('utf-8'))
        connectionSocket.close()