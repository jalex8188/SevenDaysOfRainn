import json
import os
import time

from led_control import Leds
from printer_control import Printer

from json_helper import Json_helper

leds = Leds()
printer = Printer()


def set_all_dwarves(seven_dwarves):
    # print(seven_dwarves)
    for i in seven_dwarves["dwarves"]:
        for day in i.keys():
            if day != "id":
                if i[day]:
                    print(i[day])
                    leds.set_dwarves(day)
                # print_level(day)
    time.sleep(1)
    leds.pulse()


def set_led(day):
    leds.set_dwarves(day)
    print(day)
    # print("hello")
    print("this is from set_led")


def print_level(day):
    print("this is from print_level")
    printer.print_level(day)


def init():

    json_helper = Json_helper()
    try:
        while True:
            updated_json = json_helper.check_json()
            try:
                if updated_json is not None:
                    try:
                        seven_dwarves = updated_json
                        current_day = seven_dwarves["gameState"][0]["currentDay"]
                        print(f"the current day is {current_day}")

                        game_state = seven_dwarves["gameState"][1]["gameState"]
                        print(f"the game state is {game_state}")

                        printer_state = seven_dwarves["gameState"][2]["printerState"]
                        print(f"the printer state is {printer_state}")

                        if game_state == "start":
                            print("inside start")
                            leds.clear_leds()
                            leds.set_dwarves(current_day)
                            leds.pulse()
                        if game_state == "active":
                            print("inside active")
                            leds.clear_leds()
                            leds.set_dwarves(current_day)
                        if game_state == "end":
                            print("game state is end")
                            leds.clear_leds()
                            set_all_dwarves(seven_dwarves)
                        
                        if printer_state != "none":
                            try:
                                # printer.print_level(printer_state)
                                seven_dwarves["gameState"][2]["printerState"] = "none"
                                json_helper.update_json(seven_dwarves)
                                print(f"I'm printing {printer_state}")
                                printer.print_level(printer_state)
                            except Exception as err:
                                print(f"problem with the printer state {err}")

                    except Exception as err:
                        print(f"problem IN UPDATE!!!!! {err}")
                        print(seven_dwarves)
            except Exception as err:
                print(f"problem ON WHILE!!!!! {err}")
    except Exception as err:
        print(f"problem IN MAIN!!!!! {err}")


init()
