import RPi.GPIO as GPIO
import os

printer = True

printCmd = "lp MemoryTraderImg-01.jpg"

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
        self.dwarves_imgs = dwarves_imgs_dict

    def print_dwarf(self, day):
        print("inside printer_control.py")
        try:
            dwarf_image = self.dwarves_imgs[day]
            printCmd = "lp " + str(dwarf_image)
            print(printCmd)
            # os.system(printCmd)
        except Exception as err:
            print("error with printer " + str(err))
