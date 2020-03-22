from graph.GraphHandler import GraphHandler
import queue as Q
from haversine import haversine

graphHandler = GraphHandler()

class Search:

    def __init__(self):
        self.fail = False
        self.found = False
        self.visitedStations = []
        self.fringe = []

    def uninformedSearch(self, strategy, start, goal):

        self.fringe.append(node([start, None]))

        graphDef = graphHandler.graphDef

        while (not self.fail) and (not self.found):

            if len(self.fringe) == 0:
                self.fail = True
                raise Exception("Empty fringe.")
            else:
                # TODO: which strategy is which
                if (strategy == 1):
                    activeNode = self.fringe.pop()
                else:
                    activeNode = self.fringe.pop(0)

                if (not (activeNode.data[0] in self.visitedStations)):

                    self.visitedStations.append(activeNode.data[0])
                    if activeNode.data[0] == goal:
                        self.found = True
                        return activeNode
                    else:
                        rawSuccesors = graphDef[activeNode.data[0]]
                        succesors = []
                        for rawSuccesor in rawSuccesors:
                            succesor = node(rawSuccesor)
                            succesor.setParent(activeNode)

                            succesors.append(succesor)

                        self.fringe = self.fringe + succesors

    def heuristicSearch(self, priority, start, goal):

        self.fringe = Q.PriorityQueue()

        self.fringe.put(node(start['id'], None))

        graphDef = graphHandler.graphDef

        while (not self.fail) and (not self.found):

            if self.fringe.qsize() == 0:
                self.fail = True
                raise Exception("Empty fringe.")
            else:

                activeNode = self.fringe.get()

                if (not (str(activeNode.id) in self.visitedStations)):

                    self.visitedStations.append(str(activeNode.id))     

                    if str(activeNode.id) == str(goal['id']):
                        self.found = True
                        return activeNode
                    else:
                        rawSuccesors = graphDef[str(activeNode.id)]

                        for rawSuccesor in rawSuccesors:
                            succesor = node(rawSuccesor[0], rawSuccesor[1])
                            # prioridad 1 = distancia
                            rawCost = rawSuccesor[2] if priority == 1 else rawSuccesor[3]
                            succesor.setParent(activeNode)
                            succesor.setCost(priority, rawCost, goal)
                            self.fringe.put(succesor)


class node:
    def __init__(self, id, line):
        self.parent = None
        self.id = id
        self.line = line
        self.cost = 0

    def __lt__(self, other):
        return self.costPlusHeuristic < other.costPlusHeuristic

    def setParent(self, parent):
        self.parent = parent

    def setCost(self, priority, rawCost, goal):
        station = graphHandler.getStationsData(self.id)
        stationCoordinates = (float(station['latitude']), float(station['longitude']))
        goalCoordinates =  (float(goal['latitude']), float(goal['longitude']))
        self.cost = rawCost if not self.parent else rawCost + self.parent.cost
        self.costPlusHeuristic = rawCost + haversine(stationCoordinates, goalCoordinates)

    def backTrack(self):
        if self.parent:
            self.parent.backTrack()
        self.printNode()

    def printNode(self):
        station = graphHandler.getStationsData(self.id)['name']
        line = graphHandler.getLinesData(self.line)
        print(f'{station} - {line}')
