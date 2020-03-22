from time import sleep

class UI:

    def __init__(self):
        self.options = [
            "Genre",
            "Lead studio",
            "Audience score %",
            "Profitability",
            "Rotten tomatoes %",
            "Worldwide gross",
            "Year"
        ]

    def mainMenu(self):
        invalidOption = True
        selectedOption = None

        while invalidOption:
            print("\t*** Sockets in python ***\n")
            print("Please select an option.")
            print("[1] Make a query about a movie")
            print("[2] exit")
            try:
                selectedOption = int(input("Option: "))
                print("")
            except:
                print("Invalid option selected.")
                sleep(2)
                continue

            if selectedOption > 2 or selectedOption < 1:
                print("Invalid option selected.")
                sleep(2)
                continue

            invalidOption = False

        return selectedOption

    def getMoviesName(self):

        selectedMovie = input(
            f'Please specify the movie you want to make a query about: ')

        return selectedMovie

    def getMovieOption(self):

        invalidOption = True
        selectedOption = None

        while invalidOption:
            print("Please specify .")
            for i in range(1, 7):
                print(f"[{i}] {self.options[i - 1]}")
            try:
                selectedOption = int(input("Option: "))
                print("")
            except:
                print("Invalid option selected.")
                sleep(2)
                continue

            if selectedOption > 7 or selectedOption < 1:
                print("Invalid option selected.")
                sleep(2)
                continue

            invalidOption = False

        return selectedOption
