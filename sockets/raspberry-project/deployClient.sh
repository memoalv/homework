#!/bin/bash

# send files to raspberry client
rsync -avz --exclude '__pycache__' client/ pi@10.1.1.3:/home/pi/scripts/socketClient
