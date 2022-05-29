import RPi.GPIO as GPIO
import os
from pathlib import Path

printer = True

dwarves_imgs_dict = {
    "one": "one.png",
    "two": "two.png",
    "three": "three.png",
    "four": "four.png",
    "five": "five.png",
    "six": "six.png",
    "seven": "seven.png",
    "eight": "eight.png"
}


class Printer:
    def __init__(self):
        self.filepath = Path().absolute()
        print(f"filepath: {self.filepath}")
        path = self.filepath
        print_path = (f"lp {path}")
        print(F"PRINTER PATH:{print_path}")

    def print_level(self, level):
        print("inside printer_control.py")
        #/home/pi/SevenDaysOfRainn/images/eight.png
        try:
            printCmd = (f"lp {self.filepath}/images/{level}.png")
            print(printCmd)
            # os.system(printCmd)
        except Exception as err:
            print("error with printer " + str(err))
