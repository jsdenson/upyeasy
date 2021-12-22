
# Micropython Easy-uPy
- A methodology for programming and controlling WiFi enabled devices remotely in Pycharm.

### Enhances the WebRepl Experience
 - Fast prototyping projects without manual WebRepl uploads
 - Telnet client/server based REPL
 - Python automates copy/paste of upy code to device
 - Use WebRepl file upload only when saving code to device
 - Pycharm/IDE integration and project management 
 - Easy code storage and maintenance with github
 - Programming examples taylored for Huzzah Feather ESP32

### Requirements
 - Micropython Wifi/WebRepl enabled board
 - WiFi Access
 - GitHub Access
 - Some Python Programming Knowledge
 - PyCharm Community Edition

### Simple Example

    # Python client telnet access
    # Prototyped on my phone!
    # Assumes Micropython Telnet Server running on device
    
    import telnetlib
    con = telnetlib.Telnet('10.0.0.123')
    con.write(b'\r')
    res = con.read_until(b'>>>', 2000)
    print(res)
    con.close()

### Telnet Server Setup

1. Setup [WebRepl](https://docs.micropython.org/en/latest/esp32/quickref.html?highlight=webrepl#webrepl-web-browser-interactive-prompt)
2. Send tnserver.py to device
3. Send main.py to device
4. Reboot device



    