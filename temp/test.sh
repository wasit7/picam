#!/bin/bash
#raspistill -o test.jpg -w 3456 -h 2592 -t 999999
#raspistill -o test.png -w 1920 -h 1080 -t 99999
DATE=$(date +"%y%m%d_%H%M%S")
raspistill -o ../img/[$DATE]_%02d.png -t 0 -k -mm bachlit -sa 100 -q 90 -awb fluorescent -co -0 -sh 100 -sa 0 -v -p 100,100,810,540
