#!/bin/bash
homedir='/opt/pi-monitor/'
imgdir='/opt/img-dir/'

s=$(date +'%Y%m%d%H%M')

raspistill -n -t 60000 -tl 1000 -o ${imgdir}img${s}%04d.jpg -l ${imgdir}latest.jpg -w 640 -h 480 -q 20

