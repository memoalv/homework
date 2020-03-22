from time import sleep
from graph.GraphHandler import GraphHandler


class UI:

    def mainMenu(self):
        invalidOption = True
        selectedOption = None

        while invalidOption:
            print("\t*** Heuristic search in the London tube ***\n")
            print("Please select an option.")
            print("[1] Search the route between two stations")
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

    def getStation(self, stage="start"):

        invalidStation = True
        selectedStation = None
        graph = GraphHandler()

        while invalidStation:
            selectedStation = input(f'Please specify the {stage} station: ')

            if not graph.validStation(selectedStation):
                print('Please enter a valid station name.')
                continue

            invalidStation = False

        selectedStation = graph.getStationsData(selectedStation)

        return selectedStation

    def getSearchStrategy(self):

        invalidSearchStrat = True
        selectedSearchStrat = None

        while invalidSearchStrat:
            print("Please specify the search strategy that's going to be used.")
            print("[1] Depth-first")
            print("[2] Breadth-first")
            try:
                selectedSearchStrat = int(input("Option: "))
                print("")
            except:
                print("Invalid option selected.")
                sleep(2)
                continue

            if selectedSearchStrat > 2 or selectedSearchStrat < 1:
                print("Invalid option selected.")
                sleep(2)
                continue

            invalidSearchStrat = False

        return selectedSearchStrat

    def getSearchPriority(self):

        invalidSearchPriority = True
        selectedSearchPriority = None

        while invalidSearchPriority:
            print("Please specify the parameter that's going to be prioritized.")
            print("[1] Distance")
            print("[2] Time")
            try:
                selectedSearchPriority = int(input("Option: "))
                print("")
            except:
                print("Invalid option selected.")
                sleep(2)
                continue

            if selectedSearchPriority > 2 or selectedSearchPriority < 1:
                print("Invalid option selected.")
                sleep(2)
                continue

            invalidSearchPriority = False

        return selectedSearchPriority
