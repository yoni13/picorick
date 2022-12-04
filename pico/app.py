import network
import machine
from time import sleep
import urequests as requests
print('init success')
led = machine.Pin("LED", machine.Pin.OUT)
def connect():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect('SGGS_CS',"awawa87b")
    while wlan.isconnected() == False:
        print('Waiting for connection...')
        sleep(1)
    print('connected to wifi')
connect()
led.on()
while True:
        r26 = machine.ADC(26).read_u16()
        r27 = machine.ADC(27).read_u16()
        r28 = machine.ADC(28).read_u16()
        # r < 200 = 1
        if r26 > 200 and r27 < 200 and r28 > 200:#rickroll is 0 1 0
            led.off()
            sleep(5)
            requests.get('http://192.168.1.107:5000/rickroll')
            print('rickroll')
            sleep(5)
            
        if r26 < 200 and r27 > 200 and r28 > 200:#another rickroll is 1 0 0
            led.off()
            sleep(5)
            requests.get('http://192.168.1.107:5000/anotherrickroll')
            print('another rickroll')
            sleep(5)
            
        if r26 > 200 and r27 > 200 and r28 < 200:#esc is 0 0 1
            led.off()
            sleep(5)
            requests.get('http://192.168.1.107:5000/esc')
            print('esc')
            sleep(5)
            
        if r26 < 200 and r27 < 200 and r28 > 200:#herwegoagain is 1 1 0
            led.off()
            sleep(5)
            requests.get('http://192.168.1.107:5000/herewegoagain')
            print('here we go again')
            sleep(5)
            
        if r26 < 200 and r27 < 200 and r28 < 200:#hh is 1 1 1
            led.off()
            sleep(5)
            requests.get('http://192.168.1.107:5000/hh')
            print('hh')
            sleep(5)
            
        if r26 > 200 and r27 < 200 and r28 < 200:#4xuan is 0 1 1
            led.off()
            sleep(5)
            requests.get('http://192.168.1.107:5000/4xuan')
            print('4xuan')
            sleep(5)
        del r26,r27,r28
        led.on()
        sleep(0.8)
        

