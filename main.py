# This is a micropython file. Do not attempt to fix any highlighted errors.
# Micropython WebRepl enable main.py

## To enable automatic access, upload utelnetserver from
## https://github.com/cpopp/MicroTelnetServer
## A working copy is in this project

## IMPORTANT ! ##
# set wifi_ssid to your wifi id
# set wifi_pass to your wifi password
## REALLY IMPORTANT ! ##
# If the variables are not set properly, the server will not work
# Don't uncomment utelnetserver.start() until it is known to work properly!

## IMPORTANT ! ##
# Not setting up correctly will require RECOVERY:
# 1. Connect serial terminal
# 2. Hold CTRL+C while press/release the reset button.
# Good luck.

## IMPORTANT ! ##
# For testing the connection, disconnect the webrepl browser after startup

import network

wlan = network.WLAN(network.STA_IF) # create station interface
wlan.active(True)                   # activate the interface

wifi_ssid = 'your-wifi-ssid'
wifi_pass = 'your-wifi-password'

if not wlan.isconnected():
    print('Connecting to WLAN')
    wlan.connect(wifi_ssid, wifi_pass)
    while not wlan.isconnected():
        # print('Connecting to WLAN ...') # TMI
        pass

print(wlan.ifconfig())  # get the interface's IP/netmask/gw/DNS addresses

import tnserver

# uncomment the line below to start telnet server at boot once you're ready
## Important! Once you do this, Turn off with tndisable.py

tnserver.stop()
tnserver.start()

import webrepl
webrepl.start()

'''
# tndisable.py example
import telnetlib

PRMT = b'\r\n>>>'
con = telnetlib.Telnet('10.0.0.123')
con.write(b'\r')
res = con.read_until(PRMT, 2)
print(res)
if res.find(PRMT) == 0:
    con.write(b'tnserver.stop()\r')
#'''

