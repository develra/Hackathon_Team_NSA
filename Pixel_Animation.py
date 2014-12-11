from __future__ import division
import time
import random
from neopixel import *
from numpy  import *



# LED strip configuration:
LED_COUNT   = 24      # Number of LED pixels.
LED_PIN     = 18      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA     = 5       # DMA channel to use for generating signal (try 5)
LED_INVERT  = False   # True to invert the signal (when using NPN transistor level shift)
red = Color(255,0,0)
off = Color(0,0,0)
green = Color(0,255,0)
blue = Color(0,0,255)
ledStatus = []

def recording(dur,pix):
	while True:
		numPix = pix.numPixels()
		numlit = 0 #Number of LEDs at the top lit first
		numTotal = pix.numPixels()
		interval = dur / numPix
		#print "Time to record: " + str(dur)
		#print "Number of Pixels: " + str(numPix)
		#print "Sleeping for time: " + str(interval)
		while numlit <= numPix:
			for i in xrange(0,numlit):
				pix.setPixelColor(i, Color(25,12,0) )
			numlit = numlit + 1
			pix.show()
			time.sleep(interval/4)

		numlit = 0 #Number of LEDs at the top lit first
        	while numlit <= numPix:
                	for i in xrange(0,numlit):
                        	pix.setPixelColor(i, Color(25,0,25 ) )
                	numlit = numlit + 1
                	pix.show()
                	time.sleep(interval/4)



# Main program logic follows:
if __name__ == '__main__':
	# Create NeoPixel object with appropriate configuration.
	strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT)
	# Intialize the library (must be called once before other functions).
	strip.begin()

	#Turn off String
	for i in xrange(0,strip.numPixels()):
		strip.setPixelColor(i, Color(0,0,0) )

	# recording(5,strip) #Ring Animation
	alternate = array([[ red, off, red, off, red, off, red, off, red, off, red, off, red, off, red, off, red, off, red, off, red, off, red, off ],
	 [off, red, off, red, off, red, off, red, off, red, off, red, off, red, off, red, off, red, off, red, off, red, off, red ]])
	
	# led = 0
	# for x in xrange(0,strip.numPixels() ):
	# 	if x % 2 == 0:
	# 		strip.setPixelColor(led, Color(255,0,0))
	# 	elif x % 2 != 0:
	# 		strip.setPixelColor(led, Color(0,255,0))
	# 	led += 1
	# strip.show()
	# time.sleep(0.2)

	# led = 0
	# for x in xrange(0,strip.numPixels() ):
	# 	if x % 2 == 0:
	# 		strip.setPixelColor(led, Color(0,255,0))
	# 	elif x % 2 != 0:
	# 		strip.setPixelColor(led, Color(0,0,255))
	# 	led += 1
	# strip.show()
	# time.sleep(0.2)
	strip.setBrightness(255)
	recording(5,strip)


