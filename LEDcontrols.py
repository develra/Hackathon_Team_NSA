import RPi.GPIO as GPIO
import time
import sys
import argparse

led1 = 21
led2 = 20
led3 = 16
led4 = 12

ledpins = [led1, led2, led3, led4]
oldstate = [0, 0, 0, 0]
ledstates = [0, 0, 0, 0]


#Use broadcom pin number scheme
GPIO.setmode(GPIO.BCM)

#Setup 4 board LEDs, pulldown resistor so defaults as off.
GPIO.setup(led1, GPIO.OUT, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(led2, GPIO.OUT, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(led3, GPIO.OUT, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(led4, GPIO.OUT, pull_up_down=GPIO.PUD_DOWN)

parser = argparse.ArgumentParser(description='Set 4 LED states.')
parser.add_argument('--leds', '-L', nargs='+', type=int)
parser.add_argument('--pins', '-P', nargs='+', type=int)


def help():
	print "When defining a new state, the function performs an 'or' operation in order to only change leds wanted to be changed."

def LEDTest():
	while True:
		GPIO.output(led1, 1)
		time.sleep(1)
		GPIO.output(led2, 1)
		time.sleep(1)
		GPIO.output(led3, 1)
		time.sleep(1)
		GPIO.output(led4, 1)
		time.sleep(1)
		GPIO.output(led4, 0)
		time.sleep(1)
		GPIO.output(led3, 0)
		time.sleep(1)
		GPIO.output(led2, 0)
		time.sleep(1)
		GPIO.output(led1, 0)
		time.sleep(1)

def show():
	i = 0
	for state in ledstates:
		GPIO.output(ledpins[i], state)
		i = i + 1

def changestate(newstate,usepins):
	if len(newstate) != 4 or len(usepins) != 4:
		sys.exit("Incorrectly filled out parameters, but define for all 4 states.")

	print "New State:"
	print newstate
	print "Using Pins:"
	print usepins
	i = 0
	
	for val in usepins:
		print val
		if val == 1:
			ledstates[i] = newstate[i] #Only change if it wanted to be changed
		i = i + 1


args = parser.parse_args()
print args
print vars(args)
newleds = vars(args)['leds']
usingpins = vars(args)['pins']
print "New LED Pins:"
print newleds
print "Map of Pins Changing:"
print usingpins

changestate(newleds,usingpins) #Change the state machine

show() #Write change to the leds


