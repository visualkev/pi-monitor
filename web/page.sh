#!/bin/bash

# ---variables---
base='/home/pi/'
parts="${base}parts/"
hpage="${base}/camera/index.html"

# ---code---
cat ${parts}page-part1 > $hpage
du -sh ${base}camera >> $hpage
echo " :|: File Count: ~" >> $hpage
ls -1 ${base}camera | wc -l >> $hpage
cat ${parts}page-part2 >> $hpage
date >> $hpage
cat ${parts}page-part3 >> $hpage 

