from Model.day import Day
from datetime import datetime

class Gym(object):
    def __init__(self, nm):
        self.__name = nm
        self.__week_schedule = []

    def get_name(self):
        return self.__name

    def set_name(self, nm):
        self.__name = nm

    def find_day(self, date):
        wanted_date = None

        for  d in self.__week_schedule:
            if d.get_date() == date:
                wanted_date = d
                break

        if wanted_date == None:
            wanted_date = Day(date)
            self.__week_schedule.append(wanted_date)

        return wanted_date

