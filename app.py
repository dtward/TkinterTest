
'''
A simple app that uses Tkinter with python 2.
'''

# import the Tk interface
from Tkinter import *
from ttk import * # this one will override some things, style commands are now different

# set up a nice simple class
# inherit from Frame
class Application(Frame):
    # a member function to do something, print some text
    def say_hi(self):
        print("Hi there")
        
    # a member function to set up widgets, constructor will call this
    def create_widgets(self):
        # first create a button
        self.QUIT = Button(self, text="Quit", command=self.quit)
        # set its properties with dictionary
        #self.QUIT["text"] = "QUIT"
        # but nicer to do as above in the init

        # set location with pack, argument is dictionary
        self.QUIT.pack({"side": "left"})

        # another button
        self.hi_there = Button(self, text="say hi", command=self.say_hi)  
        self.hi_there.pack({"side": "left"})







    def click_question(self):
        # index
        print 'hi'
    def __init__(self, master=None):
        # call parent constructor
        Frame.__init__(self,master)

        # other data

        # we'll need a list of questions and answers
        self.pack()
        self.create_widgets()






# get going
root = Tk()
app = Application(master=root) # this makes a window appear
app.mainloop()
root.destroy()
