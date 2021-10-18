from tkinter import *


class X:

    def __init__(, master):
        self.label_1 = Label(master, text="Isentropic Flow Relations")  # Adds Labels
        self.label_2 = Label(master, text="Perfect Gas, Gamma")
        self.entry_2 = Entry(master)  # Adds Available entry spot
        self.entry_3 = Entry(master)

        self.entry_2.insert(END, 1.4)  # Adds Default Entry Value
        self.entry_3.insert(END, 2.0)

        # Places Things in GUI in grid fashion
        self.label_1.grid(row=0, sticky=W)
        self.label_2.grid(row=1, sticky=W)
        self.entry_2.grid(row=1, column=1, sticky=W)
        self.entry_3.grid(row=2, column=1, sticky=W)

        self.variable = StringVar(master)
        self.variable.set("Mach Number")  # default value
        # Drop Down Menu
        self.w = OptionMenu(master, self.variable, "Mach Number", "T/T0", "p/p0", "rho/rho0", "A/A* (sub)", "A/A* (sup)",
                       "Mach Angle", "P-M Angle")
        self.w.grid(row=2,sticky=W)

        # Button
        self.c = Button(master, text="Calculate")
        self.c.grid(row=4, column=1, sticky=W)

        self.quitButton = Button(master, text="Quit", command=master.quit)
        self.quitButton.grid(row=5, column=1)

        # GUI size
        frame = Frame(master, width=300, height=250)
        frame.grid()


root = Tk()
b = X(root)
root.mainloop()

# label_1 = Label(root, text="Name")
# label_2 = Label(root, text="Password")
# entry_1 = Entry(root)
# entry_2 = Entry(root)
#
# label_1.grid(row=0, sticky=E)
# label_2.grid(row=1, sticky=E)
# entry_1.grid(row=0, column=1)
# entry_2.grid(row=1, column=1)
#
# c = Checkbutton(root, text="Keep me logged in")
# c.grid(columnspan=2)

# one = Label(root, text="One", bg="red", fg="white")
# one.pack()
# two = Label(root, text="Two", bg="green", fg="black")
# two.pack(fill=X)
# three = Label(root, text="Three", bg="blue", fg="white")
# three.pack(side=LEFT, fill=Y)

# topframe = Frame(root)
# topframe.pack()
# bottomframe = Frame(root)
# bottomframe.pack(side=BOTTOM)
#
# button1 = Button(topframe, text="Button 1", fg="red")
# button2 = Button(topframe, text="Button 2", fg="blue")
# button3 = Button(topframe, text="Button 3", fg="green")
# button4 = Button(bottomframe, text="Button 4", fg="purple")
#
# button1.pack(side=LEFT)
# button2.pack(side=LEFT)
# button3.pack(side=LEFT)
# button4.pack(side=LEFT)