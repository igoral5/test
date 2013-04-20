#!/usr/bin/env python3.2
# -*- coding: utf-8 -*-
'''Моргаем светодиодом на Raspberry Pi'''
import RPi.GPIO as GPIO
import time
import signal
import sys
def signal_handler(signal, frame):
    GPIO.output(11, GPIO.HIGH)
    GPIO.cleanup()
    print()
    sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)
GPIO.setmode(GPIO.BOARD)  
GPIO.setup(11, GPIO.OUT)
GPIO.setup(12, GPIO.IN)
led_stat = GPIO.HIGH
GPIO.output(11, led_stat)
while True:
    GPIO.wait_for_edge(12, GPIO.RISING)
    time.sleep(0.1)
    led_stat = not led_stat
    GPIO.output(11, led_stat)
    if led_stat == GPIO.LOW:
        print("LED ON")
    else:
        print("LED OFF")
