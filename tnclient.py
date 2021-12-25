import sys
import telnetlib as tn
import time

CTLE = b'\5'
CTLD = b'\4'
PRMT = b'\r\n>>>'
OUTD = '<<<'

# modify source print to use [ as output detection

def run(ipaddr, pyfile, port=23):

    tcon = tn.Telnet(ipaddr, port)
    tcon.write(b'\r')
    try:
        output = tcon.read_until(PRMT, 1)
    except EOFError:
        print('Cant connect')
        tcon.close()
        quit()

    program = ''
    with open(pyfile,'r') as f:
        program = f.read()
        #f.readlines()
        #program = ''.join(program)

    tcon.write(CTLE)
    program = program.replace('\n', '\r')
    #tcon.write(str(program).encode('utf-8'))
    plist = program.split('\r')
    for line in plist:
        tcon.write(str(line+'\r').encode('utf-8'))
        time.sleep(0.1)

    tcon.write(CTLD)

    rbytes = tcon.read_until(b'>>>', 4)
    output = rbytes.decode('ascii')
    sp = output.split('\n')

    for tk in sp:
        #print(tk)
        if tk.find(OUTD) == 0:
            olen = len(OUTD)
            print(tk[olen:])

    tcon.close()

if __name__ == '__main__':

    if len(sys.argv) < 3:
        print('Usage: %s IP-Address MicroPy-File')
    else:
        run(sys.argv[1], sys.argv[2])