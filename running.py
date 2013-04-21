#!/usr/bin/env python3.2
# -*- coding: utf-8 -*-
'''Бегущий огонь из светодиодов на Raspberry Pi'''
import RPi.GPIO as GPIO
import time
import signal
import sys
def signal_handler(signal, frame):
    GPIO.output(11, GPIO.HIGH)
    GPIO.output(12, GPIO.HIGH)
    GPIO.output(13, GPIO.HIGH)
    GPIO.output(15, GPIO.HIGH)
    GPIO.output(16, GPIO.HIGH)
    GPIO.cleanup()
    print()
    sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)
GPIO.setmode(GPIO.BOARD)  
GPIO.setup(11, GPIO.OUT)    # зеленый светодиод
GPIO.output(11, GPIO.LOW)
GPIO.setup(12, GPIO.OUT)    # желтый светодиод
GPIO.output(12, GPIO.HIGH)
GPIO.setup(13, GPIO.OUT)    # голубой светодиод
GPIO.output(13, GPIO.HIGH)
GPIO.setup(15, GPIO.OUT)    # белый светодиод
GPIO.output(15, GPIO.HIGH)
GPIO.setup(16, GPIO.OUT)    # красный светодиод
GPIO.output(16, GPIO.HIGH)
GPIO.setup(18, GPIO.IN)     # кнопка
current_led = 11
print("Зеленый")
while True:
    GPIO.wait_for_edge(18, GPIO.RISING)
    time.sleep(0.1)     # Задержка для подавления дребезга контактов
    if current_led == 11:
        GPIO.output(11, GPIO.HIGH)
        GPIO.output(12, GPIO.LOW)
        current_led = 12
        print("Желтый")
    elif current_led == 12:
        GPIO.output(12, GPIO.HIGH)
        GPIO.output(13, GPIO.LOW)
        current_led = 13
        print("Голубой")
    elif current_led == 13:
        GPIO.output(13, GPIO.HIGH)
        GPIO.output(15, GPIO.LOW)
        current_led = 15
        print("Белый")
    elif current_led == 15:
        GPIO.output(15, GPIO.HIGH)
        GPIO.output(16, GPIO.LOW)
        current_led = 16
        print("Красный")
    elif current_led == 16:
        GPIO.output(16, GPIO.HIGH)
        GPIO.output(11, GPIO.LOW)
        current_led = 11
        print("Зеленый")
    else:
        print("Что то идет совсем не так")
