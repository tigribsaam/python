from Model.person import Person
from Model.member import Member
from Model.employee import Employee
from Model.traininggoal import TrainingGoal



p1 = Person("p1", "p1@email.com")
print(p1)
print("\n==============================\n")

tg = TrainingGoal('Arnold Schwarzenegger wannabe', "elke dag sporten")
print(tg)
print("\n==============================\n")

m1 = Member("m1", "m1@email.com")
print(m1.__str__())
print("\n==============================\n")

m2 = Member("m2", "m2@email.com", tg)
print(m2)

e1 = Employee('e1', 'e1@email.com', 'instructor')
print(e1)


#print(tg.get_g_name() + tg.get_tr_name() + tg.get_des())
#print(tg.__repr__())
