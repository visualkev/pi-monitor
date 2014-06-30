#!/bin/bash

if [ $(ls -l /home/kev/frames | wc -l) -eq 1 ]
then 
	exit 1
fi
stamp=$(date +%d%m%Y%H%M)

/home/kev/overlay.sh

ls /home/kev/frames/*ov > /home/kev/stills

mencoder -nosound -ovc lavc -lavcopts vcodec=mpeg4:aspect=16/9:vbitrate=8000000 -vf scale=640:480 -o /home/kev/vid/timelapse${stamp}.avi -mf type=jpeg:fps=5 mf://@/home/kev/stills

rm -f /home/kev/frames/*
