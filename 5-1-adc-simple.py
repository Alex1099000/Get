import RPi.GPIO as GPIO
import time
def decimal2binary(value):
    return [int(e) for e in bin(value)[2:].zfill(8)]

def num2dac(value):
    signal=decimal2binary(value)
    GPIO.output(dac,signal)
    return signal
    

GPIO.setmode(GPIO.BCM)
dac=[26,19,13,6,5,11,9,10]
comp=4
troyka=17
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka,GPIO.OUT,initial=1)
GPIO.setup(comp, GPIO.IN)

try:
    while True:
        for value in range(256):
            signal=num2dac(value)
            voltage=value/(2**8)*3.3
            time.sleep(0.005)
            c=GPIO.input(comp)
            if c==0:
                print("value",value,"voltage",voltage)
                break
finally:
    GPIO.output(dac,0)
    GPIO.cleanup(dac)