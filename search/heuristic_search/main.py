from Search import Search
from UserInterface import UI

UI = UI()

exit = False
while not exit:

    option = UI.mainMenu()
    # option = 1

    if option == 1:
        startingStation = UI.getStation()
        # startingStation = {
        #     'id': '1',
        #     'latitude': '51.5028',
        #     'longitude': '-0.2801',
        #     'name': 'Acton Town'
        # }
        goalStation     = UI.getStation('goal')
        # goalStation     = {
        #     'id': '187',
        #     'latitude': '51.6476',
        #     'longitude': '-0.1318',
        #     'name': 'Oakwood'
        # }
        searchPriority  = UI.getSearchPriority()
        # searchPriority  = 2

        searchAlgorithm = Search()
        successNode = searchAlgorithm.heuristicSearch(searchPriority, startingStation, goalStation)
        print("\rRoute:")
        successNode.backTrack()
        print(f"\nTotal cost: {successNode.cost}")
        print('\n')
        input("Press enter to continue...")

    elif option == 2:
        exit = True
