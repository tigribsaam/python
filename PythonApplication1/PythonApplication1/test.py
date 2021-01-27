import threading 
  
def print_cube(num): 
    """ 
    function to print cube of given num 
    """
    print("Cube: {}".format(num * num * num)) 
  
def print_square(num): 
    """ 
    function to print square of given num 
    """
    print("Square: {}".format(num * num)) 
  
if __name__ == "__main__": 
    # creating thread 
    t1 = threading.Thread(target=print_square, args=(10,)) 
    t2 = threading.Thread(target=print_cube, args=(10,)) 
  
    # starting thread 1 
    t1.start() 
    # starting thread 2 
    t2.start() 
  
    # wait until thread 1 is completely executed 
    t1.join() 
    # wait until thread 2 is completely executed 
    t2.join() 
  
    # both threads completely executed 
    print("Done!") 


















#from tkinter import *

#var = Tk()

#def leftclick(event):

#    print("left")

#def middleclick(event):

#    print("middle")

#def rightclick(event):

#    print("right")

#frame = Frame(var, width=300, height=250)

#frame.bind("<Button-1>", leftclick)

#frame.bind("<Button-2>", middleclick)

#frame.bind("<Button-3>", rightclick)

#frame.pack()

#var.mainloop()