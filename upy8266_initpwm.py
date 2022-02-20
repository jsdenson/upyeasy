from machine import Pin, PWM
p1 = PWM(Pin(12),freq=500,duty=0)
p2 = PWM(Pin(14),freq=500,duty=0)

#Full-stop
#p1.deinit()
#p2.deinit()

#p1 = Pin(12,Pin.OUT)
#p2 = Pin(14,Pin.OUT)
#p1.off()
#p2.off()

#p1 = PWM(Pin(12),freq=500,duty=1050)
#p2 = PWM(Pin(14),freq=500,duty=1050)






