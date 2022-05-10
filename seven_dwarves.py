import json
import os
import time

from led_control import Leds
from printer_control import Printer

from json_helper import UPDATE_JSON

leds = LEDS()

leds = Leds()
printer = Printer()


def set_all_dwarves(seven_dwarves):
    for i in seven_dwarves["dwarves"]:
        for day in i.keys():
            if day != "id":
                set_led(day)
                print_dwarf(day)
        time.sleep(1)
        leds.pulse()


def set_led(day):
    leds.set_day(day)
    # print("hello")
    print("this is from set_led")


def print_dwarf(day):
    print("this is from print_dwarf")
    printer.print_dwarf(day)


def init():

    update_json = UPDATE_JSON()
    while True:
        updated_json = update_json.check_json()
        if updated_json is not None:
            seven_dwarves = updated_json
            current_day = seven_dwarves["gameState"][0]["currentDay"]
            print(current_day)
            set_all_dwarves(seven_dwarves)


init()
