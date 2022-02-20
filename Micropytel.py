import telnetlib as tn
import time


class Micropy:

    def __init__(self):

        self.CTLE = b'\5'
        self.CTLD = b'\4'
        self.PRMT = b'\r\n>>>'
        self.OUTD = '<<<'

    def run(self, ipaddr, code, port=23):

        tcon = tn.Telnet(ipaddr, port)
        tcon.write(b'\r')
        try:
            output = tcon.read_until(self.PRMT, 1)
        except EOFError:
            print('Cant connect')
            tcon.close()
            quit()

        tcon.write(self.CTLE)
        code = code.replace('\n', '\r')
        plist = code.split('\r')
        for line in plist:
            tcon.write(str(line+'\r').encode('utf-8'))
            time.sleep(0.1)

        tcon.write(self.CTLD)
        print()

        rbytes = tcon.read_until(b'>>>', 4)
        output = rbytes.decode('ascii')
        sp = output.split('\n')

        for tk in sp:
            if tk.find(self.OUTD) == 0:
                olen = len(self.OUTD)+1
                print(tk[olen:])

        time.sleep(0.1) # print/close race ?
        tcon.close()

