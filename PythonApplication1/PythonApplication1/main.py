from Model.person import Person
from Model.member import Member
from Model.employee import Employee
from Model.traininggoal import TrainingGoal
from Model.gymclass import GymClass
from Model.day import Day
from Model.gym import Gym
from datetime import datetime, timedelta
from tkinter import *
import tkinter.simpledialog
from tkinter import messagebox


gym = Gym('sportschool')
shown_day = datetime.today()
root = Tk()

root.title(gym.get_name())
root.geometry('700x500')
root.resizable(width=FALSE, height=FALSE)

def change_day(days):
    global shown_day
    shown_day = shown_day + timedelta(days)
    date_label.config(text = shown_day)
    Label(root, text=shown_day).grid()
    schedule()

schedule_box = Frame(root)
schedule_box.grid(row=0, column=0)
	
date_label = Label(schedule_box, text=shown_day)
date_label.grid()



def schedule():
		
    #//Voor elke les wordt een Label en listview aangemaakt en een trainer label, met de actie  
    #//als je daar op drukt.
    class08_label = Label(schedule_box, text='08:00')
    class08_label.grid(row=1, column=0)
    instructor08_label = Label(schedule_box, text='Instructor: geen')
    instructor08_label.grid(row=1, column=1)
    members08_listbox = Listbox(schedule_box, )
    members08_listbox.insert(END, "hoi", 9086, 'gvd werk gwn')
    members08_listbox.grid(row=2, column=0, columnspan= 2)

    gym_day = Day(gym.find_day(shown_day))
    #print(gym_day)

    class08 = gym_day.find_class_by_time('08:00')
    for mem in class08.get_members():
        #gaat dit goed??
        members08_listbox.insert(mem)
    if class08.get_instructor():
        instructor08_label.config(text = class08.get_instructor())

    #bind listbox and instructor label
    members08_listbox.bind("<Button-1>", list_handler_left)







def list_handler_left(event):
    
    list = GymClass(event.widget.get(0, END))

    member_dialog = tkinter.simpledialog.askstring('Add member', 'Enter name:')
    if (member_dialog):
        #exception handling for when gym class is full
        try:
            if list.add_members(Member(member_dialog)):
                print('hdfsjfsjdfsj')
            else:
                raise Exception
        except Exception as e:
            messagebox.showerror("Error", "Gym class is full")

    print(list.get_members())
    event.widget.delete(0, END)

    for m in list.get_members():
        event.widget.insert(END, m)         







navigation_box = Frame(root).grid(row=1, column=0)
week_back_btn = Button(navigation_box, text="<< Vorige week", command=lambda: change_day(-7)).grid(row=3, column=0, padx= 10)
day_back_btn = Button(navigation_box, text="< Gisteren", command=lambda: change_day(-1)).grid(row=3, column=1, padx= 10)
day_forward_btn = Button(navigation_box, text="Morgen >", command=lambda: change_day(1)).grid(row=3, column=2, padx= 10)
week_forward_btn = Button(navigation_box, text="Volgende weerk >>", command=lambda: change_day(7)).grid(row=3, column=3, padx= 10)

schedule()













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





