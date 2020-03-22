import socket
from UserInterface import UI

ui = UI()

exitFlag = False
while not exitFlag:

    selectedOption = ui.mainMenu()

    if selectedOption == 1:

        movie = ui.getMoviesName()
        option = ui.getMovieOption()

        clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        clientSocket.connect(('localhost', 8080))
        
        clientSocket.send(f'{option}|{movie}'.encode())
        data = clientSocket.recv(1024).decode('utf-8')
        
        response = data.split('|')

        if response[0] == '1':
            print(f"The {ui.options[option]} for the movie '{movie}' is: {response[1]}")
            pass
        else:
            print(f"The movie '{movie}' wasn't found")

        input("\nPress enter to continue...")
        print("\n\n")

        clientSocket.close()

        continue

    exitFlag = True