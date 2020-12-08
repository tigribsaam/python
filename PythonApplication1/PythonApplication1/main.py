from Model.person import Person
from Model.member import Member
from Model.employee import Employee
from Model.traininggoal import TrainingGoal
from Model.gymclass import GymClass
from Model.day import Day
from datetime import datetime, date
import time


d1 = Day(datetime.today())
print(d1)

#p1 = Person("p1", "p1@email.com")
#print(p1)
#print("\n==============================\n")

#tg = TrainingGoal('Arnold Schwarzenegger wannabe', "elke dag sporten")
#print(tg)
#print("\n==============================\n")

#m1 = Member("m1", "m1@email.com")
#print(m1.__str__())
#print("\n==============================\n")

#m2 = Member("m2", "m2@email.com", tg)
#print(m2)
#print("\n==============================\n")

#e1 = Employee('e1', 'e1@email.com', 'instructor')
#print(e1)
#print("\n==============================\n")

#gc1 = GymClass('08:00', 'yoga', e1)
#print(gc1)
#print("\n==============================\n")

#gc1.add_members(m1)
#print(gc1)

#gc1.add_members(m2)
#gc1.remove_members(m1)
#print(gc1)






