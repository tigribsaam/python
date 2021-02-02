'''
verander in de 'properties' van dit project de startup file naar console.py

dit bestand laat zien dat alle classes werken
'''

from Model.goal import Goal
from Model.training import Training
from Model.person import Person
from Model.member import Member
from Model.employee import Employee
from Model.traininggoal import TrainingGoal
from Model.gymclass import GymClass
from Model.day import Day
from Model.gym import Gym
from Model.EmployeeMember import EmployeeMember

from datetime import datetime

print('\nGoal:')
g1 = Goal('Meer spiermassa')
print(g1)

print('\nTraining:')
t1 = Training('afvallen', 'licht gewicht pakken en veel herhalingen maken')
print(t1)

print('\nTraining Goal:')
trg1 = TrainingGoal(t1.get_tr_name(), t1.get_des())
print(trg1)

print('\nPerson:')
p1 = Person('Ad Random', 'addrandom@gamil.com')
print(p1)

print('\nMember:')
m1 = Member(p1.get_p_name(), p1.get_email(), trg1)
print(m1)

print('\nEmployee:')
e1 = Employee('Aaron Niem', 'Aaronniem@live.nl', 'instructeur')
print(e1)

print('\nEmployee Member:')
em1 = EmployeeMember(e1.get_p_name(), e1.get_email(), trg1, e1.get_job())
print(em1)

print('\nGym Class:')
gc1 = GymClass('10:00', 'spinnen', e1)
gc1.add_members(m1)
print(gc1)
gc1.remove_members(m1)
print('\n' + str(gc1))

print('\nDay:')
d1 = Day(datetime.today())
gc2 = d1.find_class_by_time('10:00')
gc2.add_members(m1)
print(d1)

print('\nGym:')
gym = Gym('Eendags sportschool')
gym_day = gym.find_day(datetime.today())
gym_day.find_class_by_time(gc1.get_time()).add_members(m1)
print(gym_day)





