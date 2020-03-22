from graph.GraphHandler import GraphHandler

class UninformedSearch:
    
    def __init__(self):
        self.fail            = False
        self.found           = False
        self.visitedStations = []
        self.fringe          = []

    def search(self, strategy, start, goal):

        self.fringe.append(node([start, None]))

        graphDef = GraphHandler().graphDef

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
                        
class node:
    def __init__(self, data):
        self.parent = None
        self.data   = data

    def setParent(self, parent):
        self.parent = parent

    def backTrack(self):
        if self.parent:
            self.parent.backTrack()
        self.printNode()
        
    def printNode(self):
        graph = GraphHandler()
        station = graph.getStationsData(self.data[0])
        line    = graph.getLinesData(self.data[1])
        print(f'{station} - {line}')