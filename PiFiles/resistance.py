import RPi.GPIO as GPIO
import time, math

C = 0.33 # uF
R1 = 1000 # Ohms

a_pin = 18
b_pin = 23

def discharge():
    GPIO.setup(a_pin, GPIO.IN)
    GPIO.setup(b_pin, GPIO.OUT)
    GPIO.output(b_pin, False)
    time.sleep(0.01)

def charge_time():
    GPIO.setup(b_pin, GPIO.IN)
    GPIO.setup(a_pin, GPIO.OUT)
    GPIO.output(a_pin, True)
    t1 = time.time()
    while not GPIO.input(b_pin):
        pass
    t2 = time.time()
    return (t2 - t1) * 1000000

def analog_read():
    discharge()
    t = charge_time()
    discharge()
    return t

def read_resistance():
    n = 20
    total = 0
    for i in range(1, n):
        total = total + analog_read()
    t = total / float(n)
    T = t * 0.632 * 3.3
    r = (T / C) - R1
    return r

try:
    while True:
        print(read_resistance())
        time.sleep(0.5)

finally:
    print("Cleaning up")
    GPIO.cleanup()