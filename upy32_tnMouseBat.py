# This is a python file with embedded micropython code
import sys
import telnetlib as tn

CTLE = b'\5'
CTLD = b'\4'

HOST = "10.0.0.123"
PORT = "23"

upy32_code = b"""
import machine
from machine import ADC, Pin, PWM

adc = ADC(Pin(35))
adc.atten(ADC.ATTN_11DB)
value = adc.read_u16()/10000.0
print('<<< %1.2f VDC' % value)
"""

tcon = tn.Telnet(HOST, PORT)
tcon.write(b'\r')
try:
    output = tcon.read_until(b'>>>', 1)
except EOFError:
    print('Cant connect')
    tcon.close()
    quit()

# print(output)
tcon.write(CTLE)
upy32_code = upy32_code.replace(b'\n', b'\r')
tcon.write(upy32_code)
tcon.write(CTLD)

rbytes = tcon.read_until(b'>>>', 4)
output = rbytes.decode('ascii')
sp = output.split('\n')

for tk in sp:
    # print(tk)
    if tk.find('<<< ') == 0:
        print(tk[4:])

tcon.close()
