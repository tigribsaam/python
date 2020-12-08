from Model.gymclass import GymClass
from datetime import datetime

class Day(object):
    def __init__(self, dt):
        self.__date = dt
        self.__gymclasses = []

        self.__gymclasses.append([
            GymClass('08:00'),
            GymClass('09:00'),
            GymClass('10:00'),
            GymClass('19:00'),
            GymClass('20:00'),
            GymClass('21:00'),
            GymClass('22:00')])
    
    def get_date(self):
        return self.__date

    #returns interger of weekday monday = 0
    def get_day(self):
        return str(self.__date.weekday())

    def find_class_by_time(self, tm):
        wanted_class = ''
        for gc in self.__gymclasses:
            if gc.get_time() == tm:
                wanted_class = gc
        return wanted_class

    #todo
    def __repr__(self):
        s = self.get_day() + 'blabla'
        return s
