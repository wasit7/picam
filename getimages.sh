#!/bin/bash
DATE=$(date +"%y%m%d")
TIME=$(date +"%H%M%S")
mkdir -p /media/algae/$DATE

raspistill -o /media/algae/$DATE/[$TIME]_%02d.jpg -st -t 0 -k -mm average -q 90 -v -awb none -p 50,50,972,729 -ifx none
