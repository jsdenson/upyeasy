# make upy device sleep
import telnetlib, time

if __name__ == '__main__':

    #con = telnetlib.Telnet('10.0.0.138')
    con = telnetlib.Telnet('10.0.0.123')
    con.write(b'\r')
    res = con.read_until(b'\r\n>>>', 2)
    print(res)
    con.write(b'import machine\r')
    con.write(b'machine.deepsleep()\r')
    time.sleep(0.1)  # print/close race ?
    con.close()
