from Model.person import Person
from Model.traininggoal import TrainingGoal

class Member(Person):
    def __init__(self, nm, em, trg=None):
        super().__init__(nm, em)
        self.__training_goal = TrainingGoal(trg.get_g_name(), trg.get_des())

    #def __init__(self, nm, em):
    #    super().__init__(nm, em)



    def __repr__(self):
        return super.__repr__() + "\n" + repr(tr)

    def __str__(self):
        s = "Name: " + self.get_p_name() + "\nemail: " + self.get_email()
        #print("class memeber: " + s)
        if self.__training_goal:
            s += "\n" + self.__training_goal.__str__()
        return s

