#!/bin/bash

ping -c 1 8.8.8.8
if [ $? != 0 ]; then
	echo "Restarting Wifi" >> /home/pi/Pi-Dashboard/wifi_restarts.log
	date >> /home/pi/Pi-Dashboard/wifi_restarts.log
	ifdown wlan0
	sleep 1
	ifup wlan0
fi
