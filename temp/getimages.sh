#!/bin/bash
#raspistill -o test.jpg -w 3456 -h 2592 -t 999999
#raspistill -o test.png -w 1920 -h 1080 -t 99999
DATE=$(date +"%y%m%d_%H%M%S")
# raspistill -o ../img/[$DATE]_%02d.jpg -st -t 0 -k -mm average -q 90 -v -awb none -co 0 -sh 90 -sa 50 -p 50,50,972,729 -ISO 200 -ev 0 -ifx none
#raspistill -o ../img/[$DATE]_%02d.jpg -t 0 -k -ex off -mm average -q 90 -v -awb off -co 0 -sh 80 -p 100,100,972,729 -ISO 800
raspistill -o ../img/[$DATE]_%02d.jpg -st -t 0 -k -mm average -q 90 -v -awb none -p 50,50,972,729 -ifx none
