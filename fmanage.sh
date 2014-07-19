#!/bin/bash

homedir='/opt/pi-monitor/'
imgdir='/opt/img-dir/'

#PATH='/home/pi/camera/'
SIZE=`/usr/bin/du -sh ${imgdir} | /usr/bin/awk '{print $1}'`
suffix='M'
echo $(/usr/bin/du -sh ${imgdir})
echo $SIZE
SIZEN=${SIZE%$suffix}
echo "${SIZEN}"

if [ $SIZEN -ge 150 ]
then
	find $imgdir -type f -mmin +12 -delete
fi

