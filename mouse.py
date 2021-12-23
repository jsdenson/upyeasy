
from machine import ADC, Pin, PWM, Timer
import time

class bot:

    def __init__(self):

        #'''
        self.adc = ADC(Pin(35))
        self.adc.atten(ADC.ATTN_11DB)

        self.freq = 500
        self.dutyL = 745
        self.dutyR = 770
        self.pwmL = PWM(Pin(25),freq=500,duty=self.dutyL)
        self.pwmR = PWM(Pin(26),freq=500,duty=self.dutyR)
        #'''

        self.speed = 0
        self.speedLimit = 100

    def power(self):

        #'''
        value = self.adc.read_u16()/10000.0
        print('<<< %1.2f VDC' % value)
        #'''

    def stop(self):
        self.pwmL.duty(self.dutyL)
        self.pwmR.duty(self.dutyR)
        self.speed = 0

    def forward(self, speed):
        speed = int(speed) #% self.speedLimit
        left = self.dutyL+speed
        rght = self.dutyR-speed
        self.speed = speed
        print('%d : %d | %d' % (speed, left, rght))
        self.pwmL.duty(left)
        self.pwmR.duty(rght)

    def back(self, speed):
        speed = int(speed) #% self.speedLimit
        left = self.dutyL-speed
        rght = self.dutyR+speed
        self.speed = speed
        print('%d : %d | %d' % (speed, left, rght))
        self.pwmL.duty(left)
        self.pwmR.duty(rght)

    def left(self, angle):
        angle = int(angle) % self.speedLimit
        #angle /= 3
        self.pwmL.duty(self.dutyL-int(angle))
        print('resume')
        self.resume()

    def right(self, angle):
        angle = int(angle) % self.speedLimit
        #angle /= 3
        self.pwmR.duty(self.dutyR+int(angle))
        print('resume')
        self.resume()

    def resume(self):
        time.sleep(1)
        print('resumed')
        if not self.speed:
            self.stop()
        elif self.speed > 0:
            self.forward(self.speed)
        elif self.speed < 0:
            self.back(self.speed)


    def run(self):

        while True:

            cmdstr : str = input('#')

            argv = cmdstr.split(' ')
            cmdt = argv[0]

            if len(argv) > 1:
                parm = argv[1]

                if cmdt == 'f':
                    self.forward(parm)

                elif cmdt == 'b':
                    self.back(parm)

                elif cmdt == 'l':
                    self.left(parm)

                elif cmdt == 'r':
                    self.right(parm)

            else:

                if cmdt == 'p':
                    self.power()

                elif cmdt == 's':
                    self.stop()

                elif cmdt == 'q':
                    return

if __name__ == '__main__':

    obj = mouse()

    '''
    try:
        obj.run()
    except:
        print('Mouse Exception')
    #'''
