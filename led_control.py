import threading
import os

import time

## comment all of this out
# import rpi_ws281x
# from rpi_ws281x import Color
# from rpi_ws281x import Adafruit_NeoPixel

MONDAY = 0
TUESDAY = 1
WEDNESDAY = 2
THURSDAY = 3
FRIDAY = 4
SATURDAY = 5
SUNDAY = 6

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
   led_strip = "ws.SK6812_STRIP_RGBW"




   
   def __init__(self, led_brightness = 255, led_brightness_low = 40, led_rfid_status = "disconnected", led_login_status = "loggedOut", led_boop_loading_timeout = 9999):
   ## This is a Dunder Methods
   ## This is also a Constructor (When you first start a class, these defaults must be set)
      self.led_brightness = led_brightness
      self.led_brightness_low = led_brightness_low
      # led_array is the new 'strip'
      # self.led_array = Adafruit_NeoPixel(self.led_count, self.led_pin, self.led_freq_hz,
      #                      self.led_dma, self.led_invert, led_brightness, self.led_channel, self.led_strip)
   # # Intialize the library (must be called once before other functions).
      # self.led_array.begin()
      
   

   ## This is a Dunder Methods
   def __str__(self) -> str:
       return "led class"

   # # Create NeoPixel object with appropriate configuration.

   def clear_leds(self, led_count):
      strip = self.led_array
      for i in range (0, led_count, 1):
         strip.setPixelColor(i, 0)
      strip.show()

   def set_day(self, day):
      if day == "Monday":
         print("ITS MONDAY")
      elif day == "Tuesday":
         print("ITS TUESDAY")
      elif day == "Wednesday":
         print("ITS WEDNESDAY")
      elif day == "Thursday":
         print("ITS THURSDAY")
      elif day == "Friday":
         print("ITS FRIDAY")
      elif day == "Saturday":
         print("ITS SATURDAY")
      elif day == "Sunday":
         print("ITS SUNDAY")
      else:
         print(f"NOT ANY DAY ITS {day}")

                
