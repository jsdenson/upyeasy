from machine import ADC, Pin

adc = ADC(Pin(35))
adc.atten(ADC.ATTN_11DB)
value = adc.read_u16()/10000.0
print('<<<%1.2f VDC' % value)