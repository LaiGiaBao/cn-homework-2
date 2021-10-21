from socket import *
serverName = '127.0.0.1'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
sentence = input('Name a file: ')
clientSocket.send(sentence.encode())
message = clientSocket.recv(1024)
print('From Server: ', message.decode())
clientSocket.close()