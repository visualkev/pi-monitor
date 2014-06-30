#!/usr/bin/python

import datetime
import RPi.GPIO as gpio
import subprocess

print gpio.RPI_REVISION
print gpio.VERSION
gpio.setmode(gpio.BOARD)

gpio.setwarnings(False)

gpio.setup(3, gpio.IN)

retcode = subprocess.call(["/home/pi/cam.sh"])

while True:
	gpio.wait_for_edge(3, gpio.RISING)
	print 'motion!'
	#process = subprocess.Popen(["/usr/bin/raspistill", "-n", "-t", "60000", "--timelapse", "1000", "-o", "/home/pi/camera/img%04d.jpg", "-l", "/home/pi/camera/latest.jpg", "-w", "640", "-h", "480", "-q", "20"], stdout=subprocess.PIPE).communicate()[0]	
	process = subprocess.Popen(['/home/pi/startcam.sh'], stdout=subprocess.PIPE).communicate()[0]
	print process

gpio.cleanup()

#raspistill -n -t 0 -tl 1000 -o /home/pi/camera/img%04d.jpg -l /home/pi/camera/latest.jpg -w 640 -h 480 -q 20
