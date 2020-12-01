from Model.person import Person
from Model.member import Member
from Model.traininggoal import TrainingGoal



p1 = Person("p1", "p1@email.com")
print(p1)
print("\n==============================\n")

tg = TrainingGoal('hallo', "meer sporten")
print(tg)
print("\n==============================\n")

#m1 = Member("m1", "m1@email.com")
#print(m1.__str__())
#print("\n==============================\n")

m2 = Member("m2", "m2@email.com", tg)
print(m2)


#print(tg.get_g_name() + tg.get_tr_name() + tg.get_des())
#print(tg.__repr__())
