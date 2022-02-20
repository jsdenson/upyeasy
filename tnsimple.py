# ping the telnet server
import telnetlib
import time

try:
    con = telnetlib.Telnet('10.0.0.123')
    #con = telnetlib.Telnet('10.0.0.138')
    con.write(b'\r')
    res = con.read_until(b'\r\n>>>', 2)
    print(res)
    time.sleep(0.1)
    con.close()

except TimeoutError:
    print('Cant connect.')