from Model.person import Person
from Model.member import Member
from Model.employee import Employee
from Model.traininggoal import TrainingGoal
from Model.gymclass import GymClass
from Model.day import Day
from datetime import datetime
import time


d1 = Day(datetime.today())

tg = TrainingGoal('Arnold Schwarzenegger wannabe', "elke dag sporten")

m1 = Member("m1", "m1@email.com")

m2 = Member("m2", "m2@email.com", tg)

e1 = Employee('e1', 'e1@email.com', 'instructor')

yoga = d1.find_class_by_time('09:00')

yoga.add_members(m1)
yoga.add_members(m2)
yoga.add_members(m1)
yoga.set_instructor(e1)
print(d1)





