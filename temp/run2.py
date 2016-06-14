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
	GPIO.setmode(GPIO.BCM)
	pin_v1=22
	pin_v2=23
	pin_light=24
	pin_pump=25
	
	GPIO.setup(pin_v1,GPIO.OUT)
	GPIO.setup(pin_v2,GPIO.OUT)
	GPIO.setup(pin_pump,GPIO.OUT)
	GPIO.setup(pin_light,GPIO.OUT)
	while 1:
		print '>>time %f'%time.time()
#		print 'v1 on'
#		GPIO.output(pin_v1,1)
#		w=fix_wait(60)
#		w.next()
#		print 'v1 off'
#		GPIO.output(pin_v1,0)

		print 'pump on'
		GPIO.output(pin_pump,1)
		w=fix_wait(60)
                w.next()
		print 'pump off'
		GPIO.output(pin_pump,0)
		w=fix_wait(30)
		w.next()
		#capture
		print 'light on'
		GPIO.output(pin_light,1)
		capture()
		print 'light off'
		GPIO.output(pin_light,0)
		
		#pump on
#		print 'v2 on'
#		GPIO.output(pin_v2,1)
#		w=fix_wait(60)
 #               w.next()
		#pump off
		print 'v2 off'	
		GPIO.output(pin_v2,0)
		w=fix_wait(0)
                w.next()
		#upload
		print '>>upload'
		upload()
		#wait 10 mins
		w=fix_wait(600)
		w.next()
	#never reach here
	GPIO.cleanup()
