#!/bin/bash
SIZE=`du -sh camera/ | awk '{print $1}'`
suffix='M'
echo $(du -sh camera/)
echo $SIZE
SIZEN=${SIZE%$suffix}
if [ $SIZEN -ge 100 ]
then
	myproc=$(ps -ef | grep rsync | grep -v grep | wc -c)
	if [ $myproc -eq 0 ]
	then
		rsync -avzt --remove-source-files --exclude *jpg~ /home/pi/camera/img*jpg kev@10.9.1.6:frames/
	fi
fi
