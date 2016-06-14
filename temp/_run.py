import subprocess
import time
from itertools import count

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
	w=fix_wait(10)
	while 1:
		print time.time()
		capture()
		upload()
		w.next()