import threading
import os

import time

## comment all of this out
import rpi_ws281x
from rpi_ws281x import Color
from rpi_ws281x import Adafruit_NeoPixel
from rpi_ws281x import *

LED_BRIGHTNESS = 255

MONDAY = 0
MONDAY_COLOR = rpi_ws281x.Color(LED_BRIGHTNESS, LED_BRIGHTNESS, LED_BRIGHTNESS)  # white
TUESDAY = 1
TUESDAY_COLOR = rpi_ws281x.Color(4, LED_BRIGHTNESS, 4)  # red coral
WEDNESDAY = 2
WEDNESDAY_COLOR = rpi_ws281x.Color(0, 0, LED_BRIGHTNESS)  # green
THURSDAY = 3
THURSDAY_COLOR = rpi_ws281x.Color(0, LED_BRIGHTNESS, LED_BRIGHTNESS)  # yellow
FRIDAY = 4
FRIDAY_COLOR = rpi_ws281x.Color(1, LED_BRIGHTNESS, 1)  # pink
SATURDAY = 5
SATURDAY_COLOR = rpi_ws281x.Color(LED_BRIGHTNESS, 0, 0)  # blue
SUNDAY = 6
SUNDAY_COLOR = rpi_ws281x.Color(0, LED_BRIGHTNESS, 0)  # red


class Leds:
    # LED strip configuration:
    ## Any state i need to track should be in here
    ##
    # *****CHANGE VARS TO BE ALL lowercase
    led_count = 7  # Number of LED pixels.
    led_pin = 12  # GPIO pin connected to the pixels (must support PWM!).
    led_freq_hz = 800000  # LED signal frequency in hertz (usually 800khz)
    led_dma = 10  # DMA channel to use for generating signal (try 10)
    # Set to 0 for darkest and led_brightness for brightest
    led_brightness = LED_BRIGHTNESS
    # Set to 0 for darkest and led_brightness for brightest
    led_brightness_low = 40
    led_steps = led_brightness - led_brightness_low
    # True to invert the signal (when using NPN transistor level shift)
    led_invert = False
    led_channel = 0
    led_strip = ws.SK6812_STRIP_RGBW

    pulse_on = False

    def __init__(self, led_brightness=255, led_brightness_low=40):
        ## This is a Dunder Methods
        ## This is also a Constructor (When you first start a class, these defaults must be set)
        self.led_brightness = led_brightness
        self.led_brightness_low = led_brightness_low
        # led_array is the new 'strip'
        # print(self.led_count)
        # print(self.led_pin)
        # print(self.led_freq_hz)
        # print(self.led_dma)
        # print(self.led_invert)
        # print(self.led_brightness)
        # print(self.led_channel)
        # print(self.led_strip)
        self.led_array = Adafruit_NeoPixel(
            self.led_count,
            self.led_pin,
            self.led_freq_hz,
            self.led_dma,
            self.led_invert,
            led_brightness,
            self.led_channel,
            self.led_strip,
        )
        # # Intialize the library (must be called once before other functions).
        print("initializing led array")
        self.led_array.begin()

        self.clear_leds()

    # ## This is a Dunder Methods
    # def __str__(self) -> str:
    #     return "led class"

    # # Create NeoPixel object with appropriate configuration.

    def clear_leds(self):
        strip = self.led_array
        self.pulse_on = False
        for i in range(0, self.led_count, 1):
            strip.setPixelColor(i, 0)
        strip.show()

    def set_dwarves(self, day):
        strip = self.led_array
        strip.setBrightness(255)
        # print(
        #     "setting leds for set_day"
        # )
        if day == "monday":
            strip.setPixelColor(MONDAY, MONDAY_COLOR)
            print("MONDAY COMPLETE")
        if day == "tuesday":
            strip.setPixelColor(TUESDAY, TUESDAY_COLOR)
            print("TUESDAY COMPLETE")
        if day == "wednesday":
            strip.setPixelColor(WEDNESDAY, WEDNESDAY_COLOR)
            print("WEDNESDAY COMPLETE")
        if day == "thursday":
            strip.setPixelColor(THURSDAY, THURSDAY_COLOR)
            print("THURSDAY COMPLETE")
        if day == "friday":
            strip.setPixelColor(FRIDAY, FRIDAY_COLOR)
            print("FRIDAY COMPLETE")
        if day == "saturday":
            strip.setPixelColor(SATURDAY, SATURDAY_COLOR)
            print("SATURDAY COMPLETE")
        if day == "sunday":
            strip.setPixelColor(SUNDAY, SUNDAY_COLOR)
            print("SUNDAY COMPLETE")
        strip.show()
        # else:
        #    print(f"NOT ANY DAY ITS {str(day)}")

    def pulse(self):
        print(f"pulse_on is {self.pulse_on}")
        if self.pulse_on:
            print("pulse thread already running")
        else:
            p = threading.Thread(target=self.pulse_thread, args=())
            self.pulse_on = True
            try:
                p.start()
            except Exception as err:
                print(err)
        pass
    
    def pulse_thread(self):
        print("starting pulse thread")
        strip = self.led_array
        steps = 40
        self.pulse_on = True
        while self.pulse_on:
            for k in range(1, steps):
                pulse_value = round(
                    ((self.led_brightness * (steps - k)) + (0 * k)) / steps
                )
                strip.setBrightness(pulse_value)
                self.show_pulse()
            for k in range(1, steps):
                pulse_value = round(
                    ((0 * (steps - k)) + (self.led_brightness * k)) / steps
                )
                strip.setBrightness(pulse_value)
                self.show_pulse()
        strip.setBrightness(self.led_brightness)
        strip.show()
    
    def show_pulse(self):
        strip = self.led_array
        # print("showing pulse")
        if self.pulse_on:
            strip.show()
            time.sleep(0.03)
