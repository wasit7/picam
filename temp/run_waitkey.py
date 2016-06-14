import subprocess
import time
from itertools import count
import RPi.GPIO as GPIO
import time


def fix_wait(period):
	nexttime=time.time() + period
	for i in count():
		now=time.time()
		tosleep = nexttime - now	
		if (tosleep) > 0:
			time.sleep(tosleep)
			nexttime += period
		else:
			nexttime = now + period
		yield i, nexttime

def capture():
	subprocess.call(['./capture.sh'],shell=True)

def upload():
	subprocess.call(['./upload_img.sh'],shell=True)
	subprocess.call(['rm /home/pi/algaecstu/img/*'],shell=True)


if __name__=='__main__':
	#GPIO.setmode(GPIO.BCM)
	#pin=24
	#w=fix_wait(10)
	x=''
	while x!='q':
		#print time.time()
		
		#capture
		capture()
		x=raw_input()
		#pump on
		#print '>>pump on'
		#GPIO.setup(pin,GPIO.OUT)
		#GPIO.output(pin,1)
		#w.next()
		#pump off	
		#GPIO.output(pin,0)
		#GPIO.cleanup()
		#upload()
		#w.next()
