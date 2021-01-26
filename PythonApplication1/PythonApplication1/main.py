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
import pickle
import os


'''
working on: 
- pickling file 

todo: 
- exceptionhandling -> filehandling
- multithreading (clock)
- 10 classes (now 9)
- client/netwerk app (send schedule to other thing???)

'''


gym = Gym('sportschool')
shown_day = datetime.today()
root = Tk()

root.title(gym.get_name())
root.geometry('700x500')
#root.resizable(width=FALSE, height=FALSE)

schedule_box = Frame(root)
schedule_box.grid(row=0, column=0, columnspan=6)
	
date_label = Label(schedule_box, text=shown_day)
date_label.grid()


navigation_box = Frame(root).grid(row=1, column=0)
week_back_btn = Button(navigation_box, text="<< Vorige week", command=lambda: change_day(-7)).grid(row=5, column=0, padx= 10)
day_back_btn = Button(navigation_box, text="< Gisteren", command=lambda: change_day(-1)).grid(row=5, column=1, padx= 10)
day_forward_btn = Button(navigation_box, text="Morgen >", command=lambda: change_day(1)).grid(row=5, column=2, padx= 10)
week_forward_btn = Button(navigation_box, text="Volgende weerk >>", command=lambda: change_day(7)).grid(row=5, column=3, padx= 10)




def change_day(days):
    global shown_day
    shown_day = shown_day + timedelta(days)
    date_label.config(text = shown_day)
    schedule()




def file_handling(day_obj):
    #exception handling!!!!!

    gym_data = []

    if os.stat("schedule.txt").st_size != 0:
        schedule_file = open('schedule.txt', 'rb')
        gym_data = pickle.load(schedule_file)
        schedule_file.close()
    

    #replace old day object with new day object
    if gym_data:
        for day in gym_data:
            if day.get_date() == day_obj.get_date():
                index = gym_data.index(day)
                gym_data[index] = day_obj
                break
            else: gym_data.append(day_obj)
    else:
        gym_data.append(day_obj)


    print(day_obj)
    print('--------------------')
    print(gym_data)
    print('====================')


    schedule_file = open('schedule.txt', 'wb')
    pickle.dump(gym_data, schedule_file)
    schedule_file.close()














def schedule():

    gym_day = gym.find_day(shown_day)
    #file_handling(gym_day)
    
    #a loop through the list of gym classes in a day, creating for each gym class an 
    for gym_class in gym_day.get_gymclasses():
        index = gym_day.get_gymclasses().index(gym_class)

        #placement of each gym class
        index_column = index
        index_row = 1
        if index>3:
            index_column= index-4
            index_row= 4

        #labels and listbox for each gym class
        class08_label = Label(schedule_box, text= gym_class.get_time())
        class08_label.grid(row=index_row, column= index_column)
        instructor08_label = Label(schedule_box, text='Instructor: - ')
        instructor08_label.grid(row=index_row+1, column= index_column)
        members08_listbox = Listbox(schedule_box)
        members08_listbox.grid(row=index_row+2, column= index_column)

        #load existing objects in the labels and listbox
        class08 = gym_day.find_class_by_time(gym_class.get_time())
        for mem in class08.get_members():
            members08_listbox.insert(END, mem.get_p_name())
        if class08.get_instructor():
            instructor08_label.config(text = 'Instructor: ' + class08.get_instructor().get_p_name())

        #bind listbox and instructor label
        members08_listbox.bind("<Double-Button-1>", lambda event, time= class08.get_time(): list_handler_add(event, time))
        members08_listbox.bind('<Double-Button-3>', lambda event, time= class08.get_time(): list_handler_delete(event, time))
        instructor08_label.bind('<Double-Button-1>', lambda event, time= class08.get_time(): instructor_handler(event, time))




def list_handler_add(event, time):
    print("add ", time)

    gym_day = gym.find_day(shown_day)
    
    gym_class = gym_day.find_class_by_time(time)

    member_dialog = tkinter.simpledialog.askstring('Add member', 'Enter name:')
    if (member_dialog):
        mem = Member(member_dialog)
        if gym_class.add_members(mem):

            event.widget.delete(0, END)
            for m in gym_class.get_members():
                event.widget.insert(END, m.get_p_name()) 
            file_handling(gym_day)

        else:
            messagebox.showerror("Error", "Gym class is full")
    else:
        messagebox.showwarning("Warning", "No changes were made")


def list_handler_delete(event, time):

    item = event.widget.curselection()
    print("delete ", time, item)

    if(item):

        gym_day = gym.find_day(shown_day)
        gym_class = gym_day.find_class_by_time(time)

        member = ''
        for m in gym_class.get_members():
            if m.get_p_name() == event.widget.get(item):
                member = m

        gym_class.remove_members(member)
        file_handling(gym_day)
        event.widget.delete(item)

def instructor_handler(event, time):
    print("instructor ", time)

    gym_day = gym.find_day(shown_day)
    gym_class = gym_day.find_class_by_time(time)

    ins_dialog = tkinter.simpledialog.askstring('Add instructor', 'Enter name:')
    if (ins_dialog):
        #TODO get all employees, no new object
        ins = Employee(ins_dialog)

        gym_class.set_instructor(ins)
        event.widget.config(text = 'Instructor: ' + ins.get_p_name())
        file_handling(gym_day)

    else:
        messagebox.showwarning("Warning", "No changes were made")



    



   
        









schedule()

root.mainloop()

