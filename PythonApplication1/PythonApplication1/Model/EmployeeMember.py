from Model.member import Member
from Model.employee import Employee

#multiple inheritance
class EmployeeMember(Employee, Member):
    def __init__(self, nm, em=None, trg= None, jb=None):
        Employee.__init__(self, nm, em, jb)
        Member.__init__(self, nm, em, trg)

      
    def __str__(self):
        s = "Name: " + self.get_p_name()
        if self.get_email():
            s+= "\nemail: " + self.get_email()
        if self.get_training_goal():
            s+= '\ntraining goal: '+ self.get_training_goal().__str__()
        return  s