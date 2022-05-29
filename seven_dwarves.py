import json
import os
import time

from led_control import Leds
from printer_control import Printer

from json_helper import Json_helper


START_PULSE_STEPS = 80
MOVE_PULSE_STEPS = 80
QUESTION_PULSE_STEPS = 80
ROOM_PULSE_STEPS = 80
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
    # leds.pulse()


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
        os.system("json-server -w db.json -H 192.168.0.28 >> /var/log/json-server.log 2>&1 &")
    except Exception as err:
        print(f"problem starting json-server:{err}")
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
                            leds.steps = 80
                            leds.clear_leds()
                            leds.set_dwarves(current_day)
                            leds.pulse()
                        if game_state == "movement":
                            leds.steps = 50
                        if game_state == "question":
                            leds.steps = 10
                        if game_state == "room":
                            leds.clear_leds()
                            leds.set_dwarves(current_day)
                        if game_state == "seven_room":
                            leds.clear_leds()
                            leds.steps = 80
                            set_all_dwarves(seven_dwarves)
                        if game_state == "end":
                            leds.clear_leds()

                        if printer_state != "none":
                            try:
                                # printer.print_level(printer_state)
                                seven_dwarves["gameState"][2]["printerState"] = "none"
                                seven_dwarves["gameState"][3]["alreadyPrinted"].append(printer_state)
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
