from machine import Pin, PWM
from time import sleep

e1 = PWM(Pin(28))
m1 = Pin(27, Pin.OUT)
e2 = PWM(Pin(26))
m2 = Pin(22, Pin.OUT)
e1.freq(1000)
e2.freq(1000)

led = Pin(25, Pin.OUT)

def stop():
    e1.duty_u16(0)
    e2.duty_u16(0)
    sleep(0.8)

def straight(t):
    m1.value(1)
    m2.value(1)
    e1.duty_u16(60000)
    e2.duty_u16(65535)
    sleep(t)
    stop()

def turn_90(t=1.0):
    m1.value(1)
    m2.value(1)
    e1.duty_u16(65535)
    e2.duty_u16(22000)
    sleep(t)
    stop()

def flash_led():
    for _ in range(3):
        led.value(1)
        sleep(0.3)
        led.value(0)
        sleep(0.3)
