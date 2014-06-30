#!/bin/bash

cd /home/pi/camera/ 
python -m SimpleHTTPServer 8001 & > /dev/null 2>&1

#raspistill -n -t 0 -tl 1000 -o /home/pi/camera/img%04d.jpg -l /home/pi/camera/latest.jpg -w 640 -h 480 -q 20

