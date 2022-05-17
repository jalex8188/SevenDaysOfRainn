import RPi.GPIO as GPIO
import os
from pathlib import Path

printer = True

dwarves_imgs_dict = {
    "monday": "monday.jpg",
    "tuesday": "tuesday.jpg",
    "wednesday": "wednesday.jpg",
    "thursday": "thursday.jpg",
    "friday": "friday.jpg",
    "saturday": "saturday.jpg",
    "sunday": "sunday.jpg",
}


class Printer:
    def __init__(self):
        self.filepath = Path().absolute()
        print(f"filepath: {self.filepath}")
        path = self.filepath
        print_path = (f"lp {path}")
        print(print_path)

    def print_dwarf(self, day):
        print("inside printer_control.py")
        try:
            dwarf_image = self.dwarves_imgs[day]
            printCmd = (f"lp {self.filepath}/{str(dwarf_image)}/{day}.jpg")
            print(printCmd)
            # os.system(printCmd)
        except Exception as err:
            print("error with printer " + str(err))
