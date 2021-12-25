from machine import ADC, Pin, PWM, Timer
import time


class bot:

    def __init__(self):

        self.adc = ADC(Pin(35))
        self.adc.atten(ADC.ATTN_11DB)

        # IR out needs pullup?
        #self.ir1 = Pin(15, Pin.IN, Pin.PULL_UP)
        #self.ir2 = Pin(27, Pin.IN, Pin.PULL_UP)
        self.ir1 = Pin(15, Pin.IN)
        self.ir2 = Pin(27, Pin.IN)

        self.freq = 500
        self.dutyL = 750
        self.dutyR = 762
        self.pwmL = PWM(Pin(25), freq=500, duty=self.dutyL)
        self.pwmR = PWM(Pin(26), freq=500, duty=self.dutyR)

        self.speed = 0
        self.speedLimit = 100

    def zero(self, left, right):
        self.dutyL = int(left)
        self.dutyR = int(right)
        self.stop()

    def power(self):

        # '''
        value = self.adc.read_u16() / 10000.0
        print('<<< %1.2f VDC' % value)
        # '''

    def stop(self):
        self.pwmL.duty(self.dutyL)
        self.pwmR.duty(self.dutyR)
        self.speed = 0
        print('Zero L %d R %d' % (self.dutyL, self.dutyR))

    def forward(self, speed):
        speed = int(speed)  # % self.speedLimit
        left = self.dutyL + speed
        rght = self.dutyR - speed
        self.speed = speed
        print('%d : %d | %d' % (speed, left, rght))
        self.pwmL.duty(left)
        self.pwmR.duty(rght)

    def back(self, speed):
        speed = int(speed)  # % self.speedLimit
        left = self.dutyL - speed
        rght = self.dutyR + speed
        self.speed = speed
        print('%d : %d | %d' % (speed, left, rght))
        self.pwmL.duty(left)
        self.pwmR.duty(rght)

    def left(self, angle):
        angle = int(angle) % self.speedLimit
        # angle /= 3
        self.pwmL.duty(self.dutyL)  # -int(angle))
        print('pause left')
        self.resume(int(angle) / 100.0)

    def right(self, angle):
        angle = int(angle) % self.speedLimit
        # angle /= 3
        self.pwmR.duty(self.dutyR)  # +int(angle))
        print('pause right')
        self.resume(int(angle) / 100.0)

    def resume(self, secs):
        time.sleep(secs)
        print('resumed')
        if not self.speed:
            self.stop()
        elif self.speed > 0:
            self.forward(self.speed)
        elif self.speed < 0:
            self.back(self.speed)

    def getir(self):
        ir1 = self.ir1.value()
        ir2 = self.ir2.value()
        print('IR %d | %d' % (ir1, ir2))
        return ir1, ir2

    def getping(self):
        return

    def run(self):

        while True:

            cmdstr: str = input('#')

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
                    self.zero(cmdt, parm)

            else:

                if cmdt == 'i':
                    self.getir()

                elif cmdt == 'p':
                    self.power()

                elif cmdt == 'q':
                    return

                elif cmdt == 's':
                    self.stop()

                elif cmdt == 'v':
                    self.power()


if __name__ == '__main__':
    obj = bot()

    '''
    try:
        obj.run()
    except:
        print('Mouse Exception')
    #'''
