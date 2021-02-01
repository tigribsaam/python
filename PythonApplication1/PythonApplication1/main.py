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
import threading
from time import sleep
import socket


'''
working on: 
client/netwerk app (send schedule to another thing???)

todo: 
- exceptionhandling -> filehandling opening file
- 10 classes (now 9)
- client/netwerk app (send schedule to another thing???)

could:
- no new employees or members in schedule select from list
- create button for members and employee
- gym class add name

'''




gym = Gym('sportschool')
shown_day = datetime.today()
the_time = True
root = Tk()

root.title(gym.get_name())
root.geometry('700x500')
root.resizable(width=FALSE, height=FALSE)

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345                # Reserve a port for your service.
s.bind((host, port))        # Bind to the port




def server():
    print('1')
    
    
    info_label.config(text='probeert verbinding te maken...')
    

    try:
        print('2')
        
        s.settimeout(5)
        listen = s.listen(1)

        schedule = bytes(gym.find_day(shown_day).__str__(),'utf-8')
                       # Now wait for client connection.
        while True:
           c, addr = s.accept()     # Establish connection with client.
           print('Got connection from', addr)
           c.send(schedule)
           c.close() 
    except Exception as e:
        print(e)
        info_label.config(text='verbinding maken mislukt')
        #change 'label' failed to connect or sum
        s.timeout

    




def change_day(days):
    global shown_day
    shown_day = shown_day + timedelta(days)
    date_label.config(text = shown_day.strftime("%d/%m/%Y"))
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


    #print(day_obj)
    #print('--------------------')
    #print(gym_data)
    #print('====================')


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
        instructor08_label = Label(schedule_box, text='Instructeur: - ')
        instructor08_label.grid(row=index_row+1, column= index_column, sticky='WE')
        members08_listbox = Listbox(schedule_box)
        members08_listbox.grid(row=index_row+2, column= index_column)

        #load existing objects in the labels and listbox
        class08 = gym_day.find_class_by_time(gym_class.get_time())
        for mem in class08.get_members():
            members08_listbox.insert(END, mem.get_p_name())
        if class08.get_instructor():
            instructor08_label.config(text = 'Instructeur: ' + class08.get_instructor().get_p_name())

        #bind listbox and instructor label
        members08_listbox.bind("<Double-Button-1>", lambda event, time= class08.get_time(): list_handler_add(event, time))
        members08_listbox.bind('<Double-Button-3>', lambda event, time= class08.get_time(): list_handler_delete(event, time))
        instructor08_label.bind('<Double-Button-1>', lambda event, time= class08.get_time(): instructor_handler(event, time))




def list_handler_add(event, time):
    print("add ", time)

    gym_day = gym.find_day(shown_day)
    
    gym_class = gym_day.find_class_by_time(time)

    member_dialog = tkinter.simpledialog.askstring('Voeg deelnemer toe', 'Voer naam in: ')
    if (member_dialog):
        mem = Member(member_dialog)
        if gym_class.add_members(mem):

            event.widget.delete(0, END)
            for m in gym_class.get_members():
                event.widget.insert(END, m.get_p_name()) 
            file_handling(gym_day)

        else:
            messagebox.showerror("Foutmelding", "De les zit vol")
    else:
        messagebox.showwarning("Waarschuwing", "Er is niks veranderd")


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

    ins_dialog = tkinter.simpledialog.askstring('Voer instructeur toe', 'Voer naam in: ')
    if (ins_dialog):
        #TODO get all employees, no new object
        ins = Employee(ins_dialog)

        gym_class.set_instructor(ins)
        event.widget.config(text = 'Instructeur: ' + ins.get_p_name())
        file_handling(gym_day)

    else:
        messagebox.showwarning("Waarschuwing", "Er is niks veranderd")


def useless_clock():
    global the_time
    the_time = True
    
    while the_time:
        clock.config(text= datetime.today().strftime("%H:%M:%S"))
        sleep(0.99999999999)
        


schedule_box = Frame(root)
schedule_box.grid(row=0, column=0, columnspan=6, padx=20, pady=10)
	
date_label = Label(schedule_box, text=shown_day.strftime("%d/%m/%Y"))
date_label.grid()


clock = Label(schedule_box, text= the_time)
clock.grid(row=0, column=3)

server_btn = Button(schedule_box, text='stuur rooster', command= server) 
server_btn.grid(row=1, column=5, padx=10)

info_label = Label(schedule_box, text='up to date')
info_label.grid(row=3, column=5, columnspan=2, padx=10)



#navigation_box = Frame(root).grid(row=1, column=0)
week_back_btn = Button(root, text="<< Vorige week", command=lambda: change_day(-7)).grid(row=1, column=0, padx= 10)
day_back_btn = Button(root, text="< Gisteren", command=lambda: change_day(-1)).grid(row=1, column=1, padx= 10)
day_forward_btn = Button(root, text="Morgen >", command=lambda: change_day(1)).grid(row=1, column=2, padx= 10)
week_forward_btn = Button(root, text="Volgende week >>", command=lambda: change_day(7)).grid(row=1, column=3, padx= 10)




#server_thread = threading.Thread(target=server)


clock_thread = threading.Thread(target=useless_clock)
#clock_thread.setDaemon(True)
clock_thread.start()
schedule()


root.mainloop()
the_time= False
