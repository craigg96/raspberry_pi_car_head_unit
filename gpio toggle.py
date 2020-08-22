








#!/usr/bin/python

import RPi.GPIO as GPIO
import time
import subprocess, os
import signal

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
buttons = [25,24,23,18,15,14] #gpoi that coresponds to button 1-6
button_function = ['rearview','view_dashcam','save_dashcam','odb','toggle_screen','empty']

def getfunction(pin)
    function = 
    return function
def getpin(function)
    pin = 
    return pin


def init_button(button)
	GPIO.setup(button,GPIO.IN, pull_up_down=GPIO.PUD_UP)

for pin in range(buttons)
	init_button(pin)

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