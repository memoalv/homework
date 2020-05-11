import socket
import json

class socketClient:

    def __init__(self, host, port):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((host, port))

    def sendDict(self, dict):
        serializedData = json.dumps(dict)
        print('Sending reading...')
        self.socket.send(serializedData.encode())

        response = self.socket.recv(1024).decode('utf-8')
        response = json.loads(response)

        if response['status'] == 1:
            print('Successfully sent reading to server')
        else:
            print('Server responded with an error')
            
        return response
