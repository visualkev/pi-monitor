#!/bin/bash
homedir='/opt/pi-monitor/'
imgdir='/opt/img-dir/'
remote='kev@10.9.1.6:frames/'


SIZE=`du -sh ${imgdir} | awk '{print $1}'`
suffix='M'
echo $(du -sh ${imgdir})
echo $SIZE
SIZEN=${SIZE%$suffix}
if [ $SIZEN -ge 100 ]
then
	myproc=$(ps -ef | grep rsync | grep -v grep | wc -c)
	if [ $myproc -eq 0 ]
	then
		rsync -avzt --remove-source-files --exclude *jpg~ ${imgdir}img*jpg ${remote}
	fi
fi
