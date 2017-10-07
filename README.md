# RPI-Boinc-Done-LED-Blink
Blink an LED when all Boinc jobs are done using GPIO (Raspberry PI A+, B+, 2 B and 3 B).

This script is used to monitor Boinc's jobs status on a Raspberry PI without a connection to the Internet.
When the LED is flashing, it's time to connect the Rasperry PI to the Internet for uploading the completed tasks and for downloading the new ones.

It is usefull for setting it up and forgetting it, you can download several weeks of work and then let the Raspberry PI crunch on it's own. When you see the LED blinking, you know that the work is over.

The GPIO Pin 40 (Board Numbering) will be used to blink the LED.

This script needs to be launched as **root** by cron at each reboot.

You can find the documentation for the numbering of the GPIOs here : https://www.raspberrypi.org/documentation/usage/gpio-plus-and-raspi2/
