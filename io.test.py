#!/usr/bin/python

import datetime
import RPi.GPIO as gpio
import subprocess

now=datetime.datetime.now()
nowstr=now.strftime("%Y%m%d%H%M")
print nowstr
print gpio.RPI_REVISION
print gpio.VERSION
gpio.setmode(gpio.BOARD)

gpio.setwarnings(False)

gpio.setup(3, gpio.IN)

retcode = subprocess.call(["/home/pi/cam.sh"])
#retcode = subprocess.call(["python", "-m SimpleHTTPServer 8001 & > /dev/null 2>&1"])

while True:
	gpio.wait_for_edge(3, gpio.RISING)
	print 'motion!'
	process = subprocess.Popen(["/usr/bin/raspistill", "-n", "-t", "60000", "--timelapse", "1000", "-o", "/home/pi/camera/img%04d.jpg", "-l", "/home/pi/camera/latest.jpg", "-w", "640", "-h", "480", "-q", "20"], stdout=subprocess.PIPE).communicate()[0]	
	#process = subprocess.Popen(['date'], stdout=subprocess.PIPE).communicate()[0]
	print process

gpio.cleanup()

#raspistill -n -t 0 -tl 1000 -o /home/pi/camera/img%04d.jpg -l /home/pi/camera/latest.jpg -w 640 -h 480 -q 20
