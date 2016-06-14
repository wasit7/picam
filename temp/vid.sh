#!/bin/bash
DATE=$(date +"%y%m%d_%H%M%S")
raspivid -w 1920 -h 1080 -awb fluorescent -k -v -o /home/pi/algaecstu/img/$DATE.h264

