program = """import time
from machine import ADC, Pin
adc = ADC(Pin(35))
adc.atten(ADC.ATTN_11DB)
value = adc.read_u16()/10000.0
print('<<< %1.2f VDC' % value)
"""

from Micropytel import *
import sys

'''
program code should start on line 1 to make debug easier
code errors will show in micrpython REPL as editor line N 
'''


if __name__ == '__main__':

    if len(sys.argv) < 2:
        print('Usage: %s IP-Address MicroPy-File')
    else:
        upy = Micropy()
        upy.run(sys.argv[1], program)