#!/usr/bin/env python3.2
# -*- coding: utf-8 -*-
'''Моргаем светодиодом на Raspberry Pi'''
import RPi.GPIO as GPIO
import time
import signal
import sys
def signal_handler(signal, frame):
    GPIO.cleanup()
    print()
    sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)
GPIO.setmode(GPIO.BOARD)  
GPIO.setup(11, GPIO.OUT)
GPIO.setup(12, GPIO.IN)
old_stat = GPIO.HIGH
while True:
    new_stat = GPIO.input(12)
    if old_stat != new_stat:
        GPIO.output(11, new_stat)
        if new_stat == GPIO.LOW:
            print("LED ON")
        else:
            print("LED OFF")
        old_stat = new_stat
    time.sleep(0.1)
