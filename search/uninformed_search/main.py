from UninformedSearch import UninformedSearch
from UserInterface import UI

UI = UI()
searchAlgorithm = UninformedSearch()

exit = False
while not exit:

    option = UI.mainMenu()

    if option == 1:
        startingStation = UI.getStation()
        goalStation     = UI.getStation('goal')
        searchStrategy  = UI.getSearchStrategy()

        successNode = searchAlgorithm.search(searchStrategy, startingStation, goalStation)
        print("\rRoute:")
        successNode.backTrack()
        print('\n\n\n')

    elif option == 2:
        exit = True
