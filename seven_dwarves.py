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

json_helper = Json_helper()



def set_all_dwarves(seven_dwarves):
    print(seven_dwarves)
    for i in seven_dwarves["dwarves"]:
        for day in i.keys():
            if day != "id":
                if i[day]:
                    print(i[day])
                    leds.set_dwarves(day)
                # print_level(day)
    time.sleep(1)
    # leds.pulse()

def reset_game(seven_dwarves):
    print("resetting game")
    seven_dwarves["gameState"][3]["alreadyPrinted"] = []
    seven_dwarves["dwarves"][0]["monday"] = False
    seven_dwarves["dwarves"][1]["tuesday"] = False
    seven_dwarves["dwarves"][2]["wednesday"] = False
    seven_dwarves["dwarves"][3]["thursday"] = False
    seven_dwarves["dwarves"][4]["friday"] = False
    seven_dwarves["dwarves"][5]["saturday"] = False
    seven_dwarves["dwarves"][6]["sunday"] = False
    seven_dwarves["gameState"][1]["gameState"] = "none"
    seven_dwarves["gameState"][0]["currentDay"] = "begin"
    print(seven_dwarves)
    json_helper.update_json(seven_dwarves)


def set_led(day):
    leds.set_dwarves(day)
    print(day)
    # print("hello")
    print("this is from set_led")

def check_printer_list(printer_list):
    for i in printer_list:
        if i == printer_state:
            print(f"Printer State {printer_state} is the same as already printed item {i}")
            old_print = True
    return(old_print)

def print_level(day):
    print("this is from print_level")
    printer.print_level(day)

def first_day():
    updated_json = json_helper.check_json()
    print("FIRST DAY OF SCHOOL")
    try:
        if updated_json is not None:
            try:
                seven_dwarves = updated_json
                current_day = seven_dwarves["gameState"][0]["currentDay"]
                if current_day == "begin":
                    printer.print_level("wednesdayLetter")
                    leds.set_dwarves(current_day)
            except Exception as err:
                print(f"problem with first day updated json: {err}")
    except Exception as err:
        print(f"problem with first day updated json: {err}")


def init():
    try:
        os.system("json-server -w db.json -H 192.168.1.28 --nc false>> /var/log/json-server.log 2>&1 &")
    except Exception as err:
        print(f"problem starting json-server:{err}")
    first_day()
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

                        printer_list = seven_dwarves["gameState"][3]["alreadyPrinted"]
                        print(f"the already printed list is {printer_list}")
                        if game_state == "start":
                            print("inside start")
                            leds.steps = 80
                            leds.clear_leds()
                            leds.set_dwarves(current_day)
                            leds.pulse()
                        if game_state == "movement":
                            leds.pulse_on = True
                            leds.steps = 30
                            # leds.pulse()
                        if game_state == "question":
                            leds.pulse_on = True
                            leds.steps = 10
                            # leds.pulse()
                        if game_state == "room":
                            leds.clear_leds()
                            leds.set_dwarves(current_day)
                            leds.pulse_on = False
                        if game_state == "finale":
                            leds.clear_leds()
                            leds.finale()
                        if game_state == "seven_room":
                            print("set to seven_room")
                            leds.clear_leds()
                            leds.steps = 80
                            set_all_dwarves(seven_dwarves)
                        if game_state == "end":
                            leds.clear_leds()
                        if game_state == "reset":
                            reset_game(seven_dwarves)
                        if printer_state != "none":
                            old_print = False
                            try:
                                # printer.print_level(printer_state)
                                seven_dwarves["gameState"][2]["printerState"] = "none"
                                json_helper.update_json(seven_dwarves)
                                old_print = check_printer_list(printer_list)
                                
                                # printer_state 
                                # already_printed =
                                if not old_print:
                                    seven_dwarves["gameState"][3]["alreadyPrinted"].append(printer_state)
                                    print(f"I'm printing {printer_state}")
                                    printer.print_level(printer_state)
                                    json_helper.update_json(seven_dwarves)
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
