from machine import Pin, I2C
 
import utime
 
trigger = Pin(3, Pin.OUT)
echo = Pin(2, Pin.IN)
 
 
def ultrasonnic():
    timepassed=0
    trigger.low()
    utime.sleep_us(2)
    trigger.high()
    utime.sleep_us(10)
    trigger.low()
    while echo.value() == 0:
        signaloff = utime.ticks_us()
    while echo.value() == 1:
        signalon = utime.ticks_us()
    timepassed = signalon - signaloff
    
    return timepassed
 
 
 
while True:
   
    measured_time = ultrasonnic()     
    distance_cm = (measured_time * 0.0343) / 2
    distance_cm = round(distance_cm,2)
    utime.sleep(1)
