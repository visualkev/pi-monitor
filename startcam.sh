#!/bin/bash
s=$(date +'%Y%m%d%H%M')
raspistill -n -t 60000 -tl 1000 -o /home/pi/camera/img${s}%04d.jpg -l /home/pi/camera/latest.jpg -w 640 -h 480 -q 20

