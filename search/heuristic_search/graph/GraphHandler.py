import csv
from pathlib import Path


class GraphHandler:
    def __init__(self):
        self.fullPath = Path(__file__).parent
        self.lines = []
        self.stations = []
        self.graphDef = {}

        self.loadLines()
        self.loadStations()
        self.defineHeuristicGraph()

    def loadLines(self):
        with open(f'{self.fullPath}/lines.csv') as csv_file:
            lines_file = csv.DictReader(csv_file)
            for row in lines_file:
                self.lines.append({
                    'id': row['line'],
                    'name': row['name']
                })

    def getLinesData(self, lineParam):
        lineParam = str(lineParam)
        for line in self.lines:
            if line["id"] == lineParam:
                return line["name"]
            if line["name"] == lineParam:
                return line["id"]
        return None

    def loadStations(self):
        with open(f'{self.fullPath}/stations.csv') as csv_file:
            stations_file = csv.DictReader(csv_file)
            for row in stations_file:
                self.stations.append({
                    'id': row['id'],
                    'name': row['name'],
                    'latitude': row['latitude'],
                    'longitude': row['longitude']
                })

    def getStationsData(self, stationParam):
        stationParam = str(stationParam)
        for station in self.stations:
            if station["id"] == stationParam:
                return station

            stationsName = station["name"]
            if stationsName.upper() == stationParam.upper():
                return station
        return None

    def validStation(self, stationToEval):
        for station in self.stations:
            currentStation = station['name']
            if currentStation.upper() == stationToEval.upper():
                return True
        return False

    def defineGraph(self):
        with open(f'{self.fullPath}/lineDefinition.csv') as csv_file:
            graph_file = csv.DictReader(csv_file)
            for row in graph_file:
                if row['station1'] not in self.graphDef:
                    self.graphDef[row['station1']] = []
                relation = [row['station2'], row['line']]
                self.graphDef[row['station1']].append(relation)

                if row['station2'] not in self.graphDef:
                    self.graphDef[row['station2']] = []
                relation = [row['station1'], row['line']]
                self.graphDef[row['station2']].append(relation)

    def defineHeuristicGraph(self):
        with open(f'{self.fullPath}/LineAndCostDefinitions.csv') as csv_file:
            graph_file = csv.DictReader(csv_file)
            for row in graph_file:

                station1Key = ""
                station2Key = ""
                lineKey = ""
                distanceKey = ""
                timeKey = ""

                for key in row.keys():
                    if 'station2' in key:
                        station2Key = key
                    if 'line' in key:
                        lineKey = key
                    if 'distance' in key:
                        distanceKey = key
                    if 'time' in key:
                        timeKey = key
                
                station2Value = row[station2Key].strip()

                if row['station1'] not in self.graphDef:
                    self.graphDef[row['station1']] = []
                relation = [int(row[station2Key].strip()), int(row[lineKey].strip()), float(
                    row[distanceKey].strip()), float(row[timeKey].strip())]
                self.graphDef[row['station1']].append(relation)

                if station2Value not in self.graphDef:
                    self.graphDef[station2Value] = []
                relation = [int(row['station1'].strip()), int(row[lineKey].strip()), float(
                    row[distanceKey].strip()), float(row[timeKey].strip())]
                self.graphDef[station2Value].append(relation)
