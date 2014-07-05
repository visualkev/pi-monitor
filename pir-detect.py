#!/usr/bin/python

import datetime
import RPi.GPIO as gpio
import subprocess

print gpio.RPI_REVISION
print gpio.VERSION
gpio.setmode(gpio.BOARD)

gpio.setwarnings(False)

gpio.setup(3, gpio.IN)
gpio.setup(7, gpio.IN)

retcode = subprocess.call(["/home/pi/cam.sh"])

gpo.add_event_detect(3, gpio.RISING)
gpo.add_event_detect(7, gpio.RISING)


while True:
	#gpio.wait_for_edge(3, gpio.RISING)
	if gpio.event_detected(3):
		print 'motion!'
		#process = subprocess.Popen(["/usr/bin/raspistill", "-n", "-t", "60000", "--timelapse", "1000", "-o", "/home/pi/camera/img%04d.jpg", "-l", "/home/pi/camera/latest.jpg", "-w", "640", "-h", "480", "-q", "20"], stdout=subprocess.PIPE).communicate()[0]	
		process = subprocess.Popen(['/home/pi/startcam.sh'], stdout=subprocess.PIPE).communicate()[0]
		#print process
	
	if gpio.event_detected(7):
		gpio.cleanup()
		process = subprocess.Popen(['/home/pi/lbshutdown.sh'], stdout=subprocess.PIPE).communicate()[0]
	

gpio.cleanup()

#raspistill -n -t 0 -tl 1000 -o /home/pi/camera/img%04d.jpg -l /home/pi/camera/latest.jpg -w 640 -h 480 -q 20
