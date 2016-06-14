import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
led=24
GPIO.setup(led,GPIO.OUT)
for i in xrange(60):
    GPIO.setup(led,GPIO.OUT)
    print 'on'
    GPIO.output(led,1)
    time.sleep(0.5)
    print 'off'
    GPIO.output(led,0)
    time.sleep(0.5)
    GPIO.cleanup()
