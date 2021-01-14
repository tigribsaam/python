from Model.member import Member
from Model.employee import Employee

class GymClass(object):
    def __init__(self, time="", class_name="", ins=None):
        self.__time = time
        self.__class_name = class_name
        if ins:
            ins = Employee(ins.get_p_name(), ins.get_email(), ins.get_job())
        self.__instructor = ins
        self.__members = []


    def get_time(self):
        return self.__time

    def set_time(self, tm):
        self.__time = tm
        self.__members = []

    def get_class_name(self):
        return self.__class_name

    def set_class_name(self, cn):
        self.__class_name = cn
        self.__members = []

    def get_instructor(self):
            return self.__instructor

    def set_instructor(self, ins):
        self.__instructor = Employee(ins.get_p_name(), ins.get_email(), ins.get_job())

    def get_members(self):
        return tuple(self.__members)

    def add_members(self, mem):
        if len(self.__members) < 5 and (mem not in self.__members):
            self.__members.append(mem)
            return True

    def remove_members(self, mem):
        self.__members.remove(mem)


    def __repr__(self):
        s = self.__time + ' ' + self.__class_name  
        if self.__instructor:
            s += '\nInstructor: ' + self.__instructor.get_p_name() + '\n'
        if self.__members:
            s += 'Participants:'
            for m in self.__members:
                s += '\n' + m.get_p_name() + '\t' + m.get_email()
        else: 
            s += 'This class has no participants'
        return s



