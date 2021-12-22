# this file assumes the utelnetserver is running on the target
import telnetlib

PRMT = b'\r\n>>>'
con = telnetlib.Telnet('10.0.0.123')
con.write(b'\r\r')
res = con.read_until(PRMT, 2)
print(res)
if res.find(PRMT) == 0:
    con.write(b'tnserver.stop()\r')
con.close()

