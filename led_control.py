import threading
import os

import time

## comment all of this out
import rpi_ws281x
from rpi_ws281x import Color
from rpi_ws281x import Adafruit_NeoPixel
from rpi_ws281x import *


MONDAY = 0
MONDAY_COLOR = rpi_ws281x.Color(0, 0, 255)
TUESDAY = 1
TUESDAY_COLOR = rpi_ws281x.Color(0, 0, 255)
WEDNESDAY = 2
WEDNESDAY_COLOR = rpi_ws281x.Color(0, 0, 255)
THURSDAY = 3
THURSDAY_COLOR = rpi_ws281x.Color(0, 0, 255)
FRIDAY = 4
FRIDAY_COLOR = rpi_ws281x.Color(0, 0, 255)
SATURDAY = 5
SATURDAY_COLOR = rpi_ws281x.Color(0, 0, 255)
SUNDAY = 6
SUNDAY_COLOR = rpi_ws281x.Color(0, 0, 255)

class LEDS:
   # LED strip configuration:
   ## Any state i need to track should be in here
   ## 
   # *****CHANGE VARS TO BE ALL lowercase
   led_count = 7      # Number of LED pixels.
   led_pin = 12      # GPIO pin connected to the pixels (must support PWM!).
   led_freq_hz = 800000  # LED signal frequency in hertz (usually 800khz)
   led_dma = 10      # DMA channel to use for generating signal (try 10)
   # Set to 0 for darkest and led_brightness for brightest
   led_brightness = 255
   # Set to 0 for darkest and led_brightness for brightest
   led_brightness_low = 40
   led_steps = led_brightness - led_brightness_low
   # True to invert the signal (when using NPN transistor level shift)
   led_invert = False
   led_channel = 0
   led_strip = ws.SK6812_STRIP_RGBW

   def __init__(self, led_brightness = 255, led_brightness_low = 40):
   ## This is a Dunder Methods
   ## This is also a Constructor (When you first start a class, these defaults must be set)
      self.led_brightness = led_brightness
      self.led_brightness_low = led_brightness_low
      # led_array is the new 'strip'
      print(self.led_count)
      print(self.led_pin)
      print(self.led_freq_hz)
      print(self.led_dma)
      print(self.led_invert)
      print(self.led_brightness)
      print(self.led_channel)
      print(self.led_strip)
      self.led_array = Adafruit_NeoPixel(self.led_count, self.led_pin, self.led_freq_hz, self.led_dma, self.led_invert, led_brightness, self.led_channel, self.led_strip)
   # # Intialize the library (must be called once before other functions).
      print("initializing led array")
      self.led_array.begin()

      self.clear_leds(self.led_count)

   # ## This is a Dunder Methods
   # def __str__(self) -> str:
   #     return "led class"

   # # Create NeoPixel object with appropriate configuration.

   def clear_leds(self, led_count):
      strip = self.led_array
      for i in range (0, led_count, 1):
         strip.setPixelColor(i, 0)
      strip.show()

   def set_day(self, day):
      strip = self.led_array
      if day == "Monday":
         strip.setPixelColor(MONDAY, MONDAY_COLOR)
         print("ITS MONDAY")
      elif day == "Tuesday":
         strip.setPixelColor(TUESDAY, TUESDAY_COLOR)
         print("ITS TUESDAY")
      elif day == "Wednesday":
         strip.setPixelColor(WEDNESDAY, WEDNESDAY_COLOR)
         print("ITS WEDNESDAY")
      elif day == "Thursday":
         strip.setPixelColor(THURSDAY, THURSDAY_COLOR)
         print("ITS THURSDAY")
      elif day == "Friday":
         strip.setPixelColor(FRIDAY, FRIDAY_COLOR)
         print("ITS FRIDAY")
      elif day == "Saturday":
         strip.setPixelColor(SATURDAY, SATURDAY_COLOR)
         print("ITS SATURDAY")
      elif day == "Sunday":
         strip.setPixelColor(SUNDAY, SUNDAY_COLOR)
         print("ITS SUNDAY")
      strip.show()
      # else:
      #    print(f"NOT ANY DAY ITS {str(day)}")

                
