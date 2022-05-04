import json
import os
import time

from led_control import LEDS

from json_helper import UPDATE_JSON

def set_led(day):
    leds = LEDS()
    leds.set_day(day)
    # print(f"this is from set_led {day}")

def init():

    update_json = UPDATE_JSON()
    while True:
        updated_json = update_json.check_json()
        if updated_json is not None:
            seven_dwarves = updated_json
            for i in seven_dwarves['dwarves']:
                for day in i.keys():
                    if day != "id":
                        set_led(day)
                        # print(f"this is from the check_json {day}, {i[day]}")
                # print(updated_json)
        time.sleep(5)

init()   

