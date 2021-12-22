from machine import Pin, PWM

'''
Full-stop

p1.deinit()
p2.deinit()

p1 = PWM(Pin(25),freq=500,duty=760)

p1 stop     = 500, 760
p1 slow fwd = 500, 780
p1 slow bck = 500, 735

p2 = PWM(Pin(26),freq=500,duty=770)

p2 stop     = 500, 770
p2 slow fwd = 500, 750
p2 slow bck = 500, 800

Duty should depend largely on servo center adjustment.
'''

p1 = PWM(Pin(25),freq=500,duty=760)
p2 = PWM(Pin(26),freq=500,duty=770)

p1.deinit()
p2.deinit()



