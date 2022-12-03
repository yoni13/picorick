import network
import machine
from time import sleep
import urequests as requests
print('init success')
led = machine.Pin("LED", machine.Pin.OUT)
def connect():
    led.on()
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect('SGGS_CS',"awawa87b")
    while wlan.isconnected() == False:
        print('Waiting for connection...')
        sleep(1)
    print('connected to wifi')
connect()
led.off()
while True:
        r26 = machine.ADC(26).read_u16()
        r27 = machine.ADC(27).read_u16()
        r28 = machine.ADC(28).read_u16()
        if r26 == 0 and r27 == 0 and r28 == 0:
            r26,r27,r28 = 99999,99999,99999
        # r < 200 = 1
        if r26 > 200 and r27 < 200 and r28 > 200:#rickroll is 0 1 0
            requests.get('http://192.168.1.107:5000/rickroll')
            print(str(r26) +' '+ str(r27) +' '+ str(r28))
            print('rickroll')
            sleep(5)
            
        if r26 < 200 and r27 > 200 and r28 > 200:#another rickroll is 1 0 0
            requests.get('http://192.168.1.107:5000/anotherrickroll')
            print(str(r26) +' '+ str(r27) +' '+ str(r28))
            print('another rickroll')
            sleep(5)
            
        if r26 > 200 and r27 > 200 and r28 < 200:#esc is 0 0 1
            requests.get('http://192.168.1.107:5000/esc')
            print(str(r26) +' '+ str(r27) +' '+ str(r28))
            print('esc')
            sleep(5)
            
        if r26 < 200 and r27 < 200 and r28 > 200:#herwegoagain is 1 1 0
            requests.get('http://192.168.1.107:5000/herewegoagain')
            print('here we go again')
            print(str(r26) +' '+ str(r27) +' '+ str(r28))
            sleep(5)
            
        if r26 < 200 and r27 < 200 and r28 < 200:#hh is 1 1 1
            requests.get('http://192.168.1.107:5000/hh')
            print(str(r26) +' '+ str(r27) +' '+ str(r28))
            print('hh')
            sleep(5)
            
        if r26 > 200 and r27 < 200 and r28 < 200:#4xuan is 0 1 1
            requests.get('http://192.168.1.107:5000/4xuan')
            print(str(r26) +' '+ str(r27) +' '+ str(r28))
            print('4xuan')
            sleep(5)
        print(str(r26) +' '+ str(r27) +' '+ str(r28))
        del r26,r27,r28
        sleep(0.5)

