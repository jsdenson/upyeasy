import time
import telnetlib


class Telnet:

    def __init__(self, ipaddr, ipport=23):
        self.con = telnetlib.Telnet('10.0.0.123')

    def close(self):
        self.con.close()

    def send(self, cmd):
        self.con.write(str(cmd + '\r').encode('utf-8'))

    def sendex(self, cmd, prmt, tout=1):
        self.send(cmd)
        return self.expect(prmt, tout)

    def expect(self, prmt, tout=1):
        res = self.con.read_until(prmt.encode('utf-8'), tout).decode('ascii')
        print(res)
        return res


class Moves():

    def __init__(self, telnet, prmt='\r\n#'):
        self.tn = telnet
        self.prmt = prmt

    def checkCal(self, secs, speed):
        tn.sendex('750 750', self.prmt)
        s = 'f %d' % speed
        tn.sendex(s, self.prmt)
        time.sleep(secs)
        tn.sendex('s', self.prmt)
        s = 'b %d' % speed
        tn.sendex(s, self.prmt)
        time.sleep(secs)
        tn.sendex('s', self.prmt)

    def stop(self):
        tn.sendex('s', self.prmt)

    def back(self, secs, speed=55):
        s = 'b %d' % speed
        tn.sendex(s, self.prmt)
        time.sleep(secs)

    def forward(self, secs, speed=44):
        s = 'f %d' % speed
        tn.sendex(s, self.prmt)
        time.sleep(secs)

    def left(self, angle=45):
        s = 'l %d' % angle
        tn.sendex(s, self.prmt)

    def right(self, angle=45):
        s = 'r %d' % angle
        tn.sendex(s, self.prmt)



if __name__ == '__main__':

    tn = Telnet('10.0.0.123')
    replprmt = '\r\n>>>'
    mbotprmt = '\r\n#'
    res = tn.sendex('', replprmt)

    if res.find(replprmt) > -1:
        tn.send('import mouse')
        tn.send('mouse.bot().run()')
        res = tn.sendex('', mbotprmt)
        print(res)

    if res.find(mbotprmt) < 0:
        print('Cant connect')
        quit()

    try:
        # time.sleep(30)
        mv = Moves(tn)
        res = tn.sendex('750 760', mbotprmt)
        mv.stop()
        mv.forward(2)
        mv.stop()
        tn.send('v')

        #quit()
        #while True: mv.forward(10, 55)

        #mv.checkCal(2, 19)
        '''
        mv.stop()
        j = 3
        while j:
            j -= 1
            mv.checkCal(2, 10)
        #'''

        j = 0
        while True:
            j += 1
            res = tn.sendex('i', mbotprmt)
            res = res.replace(mbotprmt, '')
            sp = res.split(' ')
            frnt = back = 0
            if len(sp) > 3:
                if sp[0].find('IR') > -1:
                    back = int(sp[1])
                    frnt = int(sp[3])
            if frnt != 0:
                mv.back(1)
                time.sleep(0.1)
            elif back != 0:
                mv.forward(1)
                time.sleep(0.1)
            if frnt or back:
                if not j % 4:
                    mv.left()
                if not j % 8:
                    mv.right()
            if not j % 10:
                tn.send('v')
            time.sleep(0.1)
            mv.stop()
            print(str(j))
        mv.stop()


    except:
        print('Exception')

    tn.close()

