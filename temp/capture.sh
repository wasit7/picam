#!/bin/bash
#-ss 20000 -w 1080 -h 768
DATE=$(date +"%y%m%d_%H%M%S")
 raspistill -o ../img/$DATE.png -t 20000 -st -mm average -q 90 -v -awb none -co 0 -sh 80 -sa 0 -p 50,50,972,729 -ISO 500 -ev 0 -ifx none
