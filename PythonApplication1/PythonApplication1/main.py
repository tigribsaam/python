from tkinter import *


root = Tk()

root.title('rbgsjrfl')
root.geometry('700x500')


a = Label(root,text='Hello, world!')
a.grid()
lbl = Label(root, text = "Are you a Geek?") 
lbl.grid() 

def clicked(): 
    lbl.configure(text = "I just got clicked") 
  
# button widget with red color text 
# inside 
btn = Button(root, text = "Click me" , 
             fg = "red", command=clicked) 
  
btn.grid(column=1, row=0) 

root.mainloop()
















#from Model.person import Person
#from Model.member import Member
#from Model.employee import Employee
#from Model.traininggoal import TrainingGoal
#from Model.gymclass import GymClass
#from Model.day import Day
#from datetime import datetime
#import time


#d1 = Day(datetime.today())

#tg = TrainingGoal('Arnold Schwarzenegger wannabe', "elke dag sporten")

#m1 = Member("m1", "m1@email.com")

#m2 = Member("m2", "m2@email.com", tg)

#e1 = Employee('e1', 'e1@email.com', 'instructor')

#yoga = d1.find_class_by_time('09:00')

#yoga.add_members(m1)
#yoga.add_members(m2)
#yoga.add_members(m1)
#yoga.set_instructor(e1)
#print(d1)





