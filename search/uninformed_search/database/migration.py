import mysql.connector
import csv

dbConnection = mysql.connector.connect(
    host='localhost',
    user='',
    passwd='',
    database='london_tube'
)

cursor = dbConnection.cursor()

with open('/home/memo/python_scripts/1_busqueda/graph/lines.csv') as f:
    reader = csv.DictReader(f)

    unorderedList = []
    for row in reader:
        unorderedList.append(row)

    orderedList = sorted(unorderedList, key=lambda k: int(k['line']))

    newLineInsert = (
        "INSERT INTO `lines` (name, colour, stripe) VALUES"
        "(%s, %s, %s)"
    )
    for item in orderedList:

        stripe = item['stripe'] if item['stripe'] != 'NULL' else None
        cursor.execute(newLineInsert, (item['name'], item['colour'], stripe))

    dbConnection.commit()

with open('/home/memo/python_scripts/1_busqueda/graph/stations.csv') as f:
    reader = csv.DictReader(f)

    unorderedList = []
    for row in reader:
        unorderedList.append(row)

    unorderedList.append({
        'id': '189',
        'latitude': 0,
        'longitude': 0,
        'name': None,
        'display_name': None,
        'zone': None,
        'total_lines': None,
        'rail': None
    })

    orderedList = sorted(unorderedList, key=lambda k: int(k['id']))

    newLineInsert = (
        "INSERT INTO `stations` (latitude, longitude, name, display_name, zone, total_lines, rail) VALUES"
        "(%s, %s, %s, %s, %s, %s, %s)"
    )
    for item in orderedList:
        display_name = item['display_name'] if item['display_name'] != 'NULL' else None
        cursor.execute(newLineInsert, (float(item['latitude']), float(item['longitude']), item['name'],
                                       display_name, item['zone'], item['total_lines'], item['rail']))

    dbConnection.commit()


with open('/home/memo/python_scripts/1_busqueda/graph/lineDefinition.csv') as f:
    reader = csv.DictReader(f)

    for row in reader:
        newLineInsert = (
            "INSERT INTO `lineDefinition` (station1, station2, line) VALUES"
            "(%s, %s, %s)"
        )
        cursor.execute(newLineInsert, (int(row['station1']), int(row['station2']), int(row['line'])))

    dbConnection.commit()

dbConnection.close()