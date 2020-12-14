from Model.person import Person
from Model.traininggoal import TrainingGoal

class Member(Person):
    def __init__(self, nm, em, trg=None):
        super().__init__(nm, em)
        if trg:
            self.__training_goal = TrainingGoal(trg.get_g_name(), trg.get_des())
        else:
            self.__training_goal = trg


    def get_training_goal(self):
        return self.__training_goal

    def set_training_goal(self, trg):
        self.__training_goal = TrainingGoal(trg.get_g_name(), trg.get_des())


    def __repr__(self):
        return "name: " + self.get_p_name() + ", email: " + self.get_email() + "\n" + self.__training_goal.__repr__()

    def __str__(self):
        s = "Name: " + self.get_p_name() + "\nemail: " + self.get_email()
        #print("class member: " + s)
        if self.__training_goal:
            s += "\n" + self.__training_goal.__str__()
        return s

