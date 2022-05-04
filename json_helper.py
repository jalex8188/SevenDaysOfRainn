import json
import time


class UPDATE_JSON:
    def __init__(self, old_json = {}, current_json = {}):
        self.old_json = old_json
        self.current_json = current_json

    def check_json(self):
        with open('db.json', 'r') as seven_dwarves_json:
            self.current_json = json.load(seven_dwarves_json)
            if self.current_json != self.old_json:
                self.old_json = self.current_json
                return self.current_json
            else:
                return(None)


        # seven_dwarves = self.current_json
        # for i in seven_dwarves['dwarves']:
        #     for day in i.keys():
        #         if day != "id":
        #             print(f"this is from the check_json {day}, {i[day]})
        #             return(day, i[day])