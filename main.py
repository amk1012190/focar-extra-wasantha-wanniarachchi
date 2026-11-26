##########################
# wasantha wanniarachchi #
# 25.11.2026             #
# extra assignment 2     #
##########################

from machine import Pin, PWM
from time import sleep

e1 = PWM(Pin(28))
m1 = Pin(27, Pin.OUT)
e2 = PWM(Pin(26))
m2 = Pin(22, Pin.OUT)
e1.freq(1000)
e2.freq(1000)

led = Pin(25, Pin.OUT)

SPEED = 65535
SLOW = 22000

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

def turn_90(t=1.35):
    m1.value(1)
    m2.value(1)
    e1.duty_u16(65535)
    e2.duty_u16(22000)
    sleep(t)
    stop()

def flash_led_3_times():
    for _ in range(3):
        led.value(1)
        sleep(0.3)
        led.value(0)
        sleep(0.3)

def corner():
    stop()
    flash_led_3_times()
    turn_90()

straight(2.0)
corner()

straight(1.2)
corner()

straight(2.0)
corner()

straight(1.2)
stop()
led.value(0)
