#!/usr/bin/python

import RPi.GPIO as GPIO
import time
import subprocess, os
import signal

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
RearView_Switch = 14  # pin 18
GPIO.setup(RearView_Switch,GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    
   state = 0
   while True :
      	time.sleep(0.1)

	#the next two blocks are used for toggeling between the camera and android auto.
      	if GPIO.input(RearView_Switch)==0 and state == 0:
         	print "  Started Full Screen"
         	rpistr = "raspivid -t 0 -vf -h 480 -w 800" #amend this string for your screen
         	p=subprocess.Popen(rpistr,shell=True, preexec_fn=os.setsid)
         	state = 1
         	while GPIO.input(RearView_Switch)==0:
             		time.sleep(0.1)

      	if GPIO.input(RearView_Switch)==0 and state == 1:
         	print "Return to Android Auto" 
         	state = 0
         	os.killpg(p.pid, signal.SIGTERM)
         	while GPIO.input(RearView_Switch)==0:
            		time.sleep(0.1)
      
	
except KeyboardInterrupt:
  print "  Quit"
  GPIO.cleanup() 