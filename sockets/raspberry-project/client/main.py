import time
from socketClient import socketClient
from dht22 import dht22


while True:
    # read data from sensor
    sensor = dht22()
    try:
        sensorReading = sensor.read()
        print(f'Successful reading {sensorReading}')
    except Exception:
        print('Error while reading sensor')

    # instantiate socket
    sc = socketClient('10.1.1.1', 8080)
    # send data
    sc.sendDict(
        {
            'type': 'tempLog',
            'temp': sensorReading[1],
            'hum': sensorReading[0]
        }
    )

    # cleanup
    del sensor
    del sc

    time.sleep(60)
