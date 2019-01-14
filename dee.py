from tkinter import *

class dee:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.button = Button(
             frame,
             text= "quit",
             fg= "red",
             command= frame.quit
        )
        self.button.pack(side=RIGHT)
        self.hi_there = Button(
            frame,
            text= "sayHi",
            command=self.say_hi
        )
        self.hi_there.pack(side=LEFT)
        self.input = Entry(frame)
        self.input.pack()

    def say_hi(self):
        print("nice")

root = Tk()
deelian = dee(root)

root.mainloop()
# root.destory()