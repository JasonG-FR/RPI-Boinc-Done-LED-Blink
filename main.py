#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  main.py
#
#  Copyright 2017 JasonG-FR <jason.gombert@gmail.com>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#

import time
import subprocess
import RPi.GPIO as GPIO  # Import GPIO library


def boinc_is_working():
    # Show the tasks being or waiting to be calculated : boinccmd --get_tasks | grep 'state: downloaded'
    process = subprocess.Popen("/usr/bin/boinccmd --get_tasks | /usr/bin/grep 'state: downloaded'",
                               stdout=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    remaining_tasks = len(output.decode().split("\n")) - 1
    
    if remaining_tasks > 0:
        return True
    else:
        return False


def flash_led(pin):
    for i in range(10):
        GPIO.output(pin, True)  # Turn on GPIO pin
        time.sleep(0.1)
        GPIO.output(pin, False)  # Turn off GPIO pin
        time.sleep(0.4)


def blink_led(pin):
    start = int(time.time())
    while True:
        now = int(time.time())
        if now - start >= 60:
            if boinc_is_working():
                break
            else:
                start = now
        else:
            GPIO.output(pin, True)  # Turn on GPIO pin
            time.sleep(0.1)
            GPIO.output(pin, False)  # Turn off GPIO pin
            time.sleep(1.9)
    

def main():
    pin = 40  # Setting the pin to 40
    GPIO.setmode(GPIO.BOARD)  # Use board pin numbering
    GPIO.setup(pin, GPIO.OUT)  # Setup GPIO pin to OUT
    
    # Flash the LED to show the system is working
    flash_led(pin)
    
    # Check every minute if Boinc is still working (using boinccmd)
    while True:
        if not boinc_is_working():
            # If not, blink the LED until Boinc is working again (checks every minute)
            blink_led(pin)
        else:
            # Sleep for a minute
            time.sleep(60)


if __name__ == '__main__':
    main()
