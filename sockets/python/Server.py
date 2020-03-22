from Model import Model
import socket

moviesModel = Model()

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind(('localhost', 8080))
serverSocket.listen(5)

while True:
    connection, address = serverSocket.accept()
    buffer = connection.recv(64).decode('utf-8')
    if len(buffer) > 0:
        queryResult = moviesModel.queryMovie(buffer)
        connection.send(queryResult.encode())