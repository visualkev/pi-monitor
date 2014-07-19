#!/usr/bin/python

homedir='/opt/pi-monitor/'
imgdir='/opt/img-dir/'

import datetime
import RPi.GPIO as gpio
import subprocess

print gpio.RPI_REVISION
print gpio.VERSION
gpio.setmode(gpio.BOARD)

gpio.setwarnings(False)

gpio.setup(3, gpio.IN)
gpio.setup(7, gpio.IN)

gpo.add_event_detect(3, gpio.RISING)
gpo.add_event_detect(7, gpio.RISING)


while True:
	#gpio.wait_for_edge(3, gpio.RISING)
	if gpio.event_detected(3):
		print 'motion!'
		process = subprocess.Popen([homedir.'startcam.sh'], stdout=subprocess.PIPE).communicate()[0]
		#print process
	
	if gpio.event_detected(7):
		gpio.cleanup()
		process = subprocess.Popen([homedir.'lbshutdown.sh'], stdout=subprocess.PIPE).communicate()[0]
	

gpio.cleanup()

