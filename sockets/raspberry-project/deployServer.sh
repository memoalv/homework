#!/bin/bash

# send files to raspberry server
rsync -avz --exclude {'node_modules','package-lock.json'} server/ pi@10.1.1.1:/home/pi/scripts/socketServer

# install dependencies
ssh pi@192.168.0.55 "cd /home/pi/scripts/socketServer && npm install --production"