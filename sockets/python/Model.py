import csv

class Model:
    def __init__(self):
        self.movies = []
        self.loadMovies()

    def loadMovies(self):
        with open('movies.csv') as csv_file:
            lines_file = csv.DictReader(csv_file)
            for row in lines_file:
                self.movies.append([
                    row['Film'],
                    row['Genre'],
                    row['Lead Studio'],
                    row['Audience score %'],
                    row['Profitability'],
                    row['Rotten Tomatoes %'],
                    row['Worldwide Gross'],
                    row['Year'],
                ])

    def queryMovie(self, payload):
        splitPayload = payload.split('|')

        if len(splitPayload) < 1 and len(splitPayload) > 2:
            return "0|"

        try:
            opCode = int(splitPayload[0])
        except:
            return "0|"

        moviesName = splitPayload[1]

        # python ^3.8
        if movie := self.getMoviesData(moviesName):
            return f"1|{movie[opCode]}"
        else:
            return "0|"

    
    def getMoviesData(self, moviesName):
        for movie in self.movies:
            if movie[0].upper() == moviesName.upper():
                return movie

        return False

model = Model()

model.queryMovie('3|the duchess')