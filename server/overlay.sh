#!/bin/bash

PATH='/home/pi/camera/'

for file in ${PATH}img*.jpg 
	do 
	#echo "$file"
	#echo "$(/usr/bin/stat -c %z $file)" 
	#echo "${file}.ov.jpg"
	if [[ $file != *.ov.jpg ]]
	then
		echo "$file"
		/usr/bin/convert $file -pointsize 25 -fill white -annotate +40+40 "$(/usr/bin/stat -c %z $file)" "${file}.ov.jpg"
		/bin/rm -f $file
	fi
done
