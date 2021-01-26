from Model.day import Day
from datetime import datetime
import pickle

class Gym(object):
    def __init__(self, nm):
        self.__name = nm
        self.__week_schedule = []

        # do not load days in the past????
        try:
            schedule_file = open('schedule.txt', 'rb')
            dates = pickle.load(schedule_file)
            for d in dates:
                self.__week_schedule.append(d)
        except Exception as e:
            print('Gym class, something went wrong: ', e)


    def get_name(self):
        return self.__name

    def set_name(self, nm):
        self.__name = nm

    def find_day(self, date):
        wanted_date = None

        for d in self.__week_schedule:
            
            if d.get_date() == date.strftime("%d/%m/%Y"):
                wanted_date = d
                break

        if wanted_date == None:
            wanted_date = Day(date)
            self.__week_schedule.append(wanted_date)

        return wanted_date

