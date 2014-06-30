#!/bin/bash

PATH='/home/pi/camera/'
SIZE=`/usr/bin/du -sh camera/ | /usr/bin/awk '{print $1}'`
suffix='M'
echo $(/usr/bin/du -sh camera/)
echo $SIZE
SIZEN=${SIZE%$suffix}
echo "${SIZEN}"

if [ $SIZEN -ge 150 ]
then
	find camera/ -type f -mmin +12 -delete
fi

