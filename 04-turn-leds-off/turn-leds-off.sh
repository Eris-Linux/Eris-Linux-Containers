#! /bin/sh
#
# This script turns all LEDs off.
#
# Christophe BLAESS 2026.
#
# License: MIT.
#

for led in /sys/class/leds/*
do
	if [ -f "${led}/trigger" ]
	then
		echo "none" > "${led}/trigger"
	fi
done
