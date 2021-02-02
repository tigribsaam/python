from Model.gymclass import GymClass
from datetime import datetime

class Day(object):
    def __init__(self, dt):
        self.__date = dt

        #create gym class objects
        self.__gymclasses = [ 
            GymClass('07:00'),
            GymClass('08:00'),
            GymClass('09:00'),
            GymClass('10:00'),
            GymClass('19:00'),
            GymClass('20:00'),
            GymClass('21:00'),
            GymClass('22:00')]
    
    def get_date(self):
        return self.__date.strftime("%d/%m/%Y")

    def get_gymclasses(self):
        return self.__gymclasses

    def find_class_by_time(self, tm):
        wanted_class = ''
        for gc in self.__gymclasses:
            if gc.get_time() == tm:
                wanted_class = gc
        return wanted_class


    def __repr__(self):
        s = str(self.get_date())
        for g in self.__gymclasses:
            s += '\n' + g.get_time() + '\tIns: '
            if g.get_instructor(): 
                s += g.get_instructor().get_p_name() 
            else: 
                s +='-'
            s += '\nParticipants: ' + str(len(g.get_members()))
        return s

    def __str__(self):
        s = self.get_date()
        for g in self.__gymclasses:
            s += '\n' + g.get_time() + '\tIns: '
            if g.get_instructor(): 
                ins = g.get_instructor()
                s += ins.get_p_name() 
            else: 
                s +='-'
            s += '\nParticipants: ' 
            if len(g.get_members()) != 0:
                for p in g.get_members():
                    s += '\n' + p.get_p_name() + '\t' + p.get_email()
            else: 
                s+= '0'
            s+='\n'
        return s
