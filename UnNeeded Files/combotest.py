from tkinter import *
# from main import *
from Isentropic import *
# import numpy as np


def main(z, n, g):
    # print('\nTypes to Choose From: Mach Number, T/T0, p/p0, rho/rho0, A/A* (sub), A/A* (sup), Mach Angle, P-M Angle')
    # print('Note: Type Exactly as Shown')
    # z = input("Enter Input type: ")
    # if z == "Mach Angle" or z == "P-M Angle":
    #     n = float(input("Input Value (in degrees): "))
    # else:
    #     n = float(input("Input Value: "))
    # g = float(input("Gamma Value: "))

    # x = np.array(np.zeros(10))
    m = "Mach Number"
    T = "T/T0"
    P = "p/p0"
    rho = "rho/rho0"
    Asub = "A/A* (sub)"
    Asup = "A/A* (sup)"
    MA = "Mach Angle"
    PMang = "P-M Angle"

    i = z == m or z == T or z == P or z == rho or z == Asub or z == Asup or z == MA or z == PMang
    j = g > 1
    if i and j:
        fcn(z, n, g)
    #     print(f"\nMach Number = {x[0]:.5f}  Mach Angle = {x[1]:.5f}  P-M Angle = {x[2]:.5f}")
    #     print(f"p/p0 = {x[3]:.5f}  rho/rho0 = {x[4]:.5f}  T/T0 = {x[5]:.5f}")
    #     print(f"p/p* = {x[6]:.5f}  rho/rho* = {x[7]:.5f}  T/T* = {x[8]:.5f} A/A* = {x[9]:.5f}")
    # else:
    #     print('\nError - Please input Compatible Input')
    #     if i == 0:
    #         print('*Input Valid Input Type')
    #     if j == 0:
    #         print('*Gamma Must be Greater than 1\n')


class X:

    def __init__(self, master):
        self.label_1 = Label(master, text="Isentropic Flow Relations")  # Adds Labels
        self.label_2 = Label(master, text="Perfect Gas, Gamma")
        self.entry_2 = StringVar()
        self.entry_3 = StringVar()
        self.entry_2 = Entry(master)  # Adds Available entry spot
        self.entry_3 = Entry(master)

        self.entry_2.insert(END, 1.4)  # Adds Default Entry Value
        self.entry_3.insert(END, 2.0)

        # Places Things in GUI in grid fashion
        self.label_1.grid(row=0, sticky=W)
        self.label_2.grid(row=1, sticky=W)
        self.entry_2.grid(row=1, column=1)
        self.entry_3.grid(row=2, column=1)

        self.variable = StringVar(master)
        self.variable.set("Mach Number")  # default value
        # Drop Down Menu
        self.w = OptionMenu(master, self.variable, "Mach Number", "T/T0", "p/p0", "rho/rho0", "A/A* (sub)", "A/A* (sup)",
                       "Mach Angle", "P-M Angle")
        self.w.grid(row=2, sticky=W)

        self.calcButton = Button(master, text="Calculate", command=self.comp)  # Calculate Button
        self.calcButton.grid(row=4, column=6)

        self.machlabel = Label(master, text="Mach Number: ")  # Mach Number
        self.machlabel.grid(row=6, column=0, sticky=E)
        self.a = Entry(master)
        self.a.grid(row=6, column=1)

        self.MAlabel = Label(master, text="Mach Angle: ")  # Mach Angle
        self.MAlabel.grid(row=6, column=2)
        self.b = Entry(master)
        self.b.grid(row=6, column=3)

        self.PMlabel = Label(master, text="P-M Angle: ")  # P-M Angle
        self.PMlabel.grid(row=6, column=4)
        self.c = Entry(master)
        self.c.grid(row=6, column=5)

        self.pp0label = Label(master, text="p/p0: ")  # p/p0
        self.pp0label.grid(row=7, column=0, sticky=E)
        self.d = Entry(master)
        self.d.grid(row=7, column=1)

        self.rr0label = Label(master, text="rho/rho0: ")  # rho/rho0
        self.rr0label.grid(row=7, column=2, sticky=E)
        self.e = Entry(master)
        self.e.grid(row=7, column=3)

        self.tt0label = Label(master, text="T/T0: ")  # T/T0
        self.tt0label.grid(row=7, column=4, sticky=E)
        self.f = Entry(master)
        self.f.grid(row=7, column=5)

        self.ppstlabel = Label(master, text="p/p*: ")  # p/p*
        self.ppstlabel.grid(row=8, column=0, sticky=E)
        self.g = Entry(master)
        self.g.grid(row=8, column=1)

        self.rrstlabel = Label(master, text="rho/rho*: ")  # rho/rho*
        self.rrstlabel.grid(row=8, column=2, sticky=E)
        self.h = Entry(master)
        self.h.grid(row=8, column=3)

        self.ttstlabel = Label(master, text="T/T*: ")  # T/T*
        self.ttstlabel.grid(row=8, column=4, sticky=E)
        self.i = Entry(master)
        self.i.grid(row=8, column=5)

        self.aastlabel = Label(master, text="A/A*: ")  # A/A*
        self.aastlabel.grid(row=8, column=6, sticky=E)
        self.j = Entry(master)
        self.j.grid(row=8, column=7)

        self.quitButton = Button(master, text="Quit", command=master.quit)
        self.quitButton.grid(row=4, column=7)

        # GUI size
        frame = Frame(master)  # , width=300, height=250
        frame.grid()

    def clear_text(self):
        self.a.delete(0, END)
        self.b.delete(0, END)
        self.c.delete(0, END)
        self.d.delete(0, END)
        self.e.delete(0, END)
        self.f.delete(0, END)
        self.g.delete(0, END)
        self.h.delete(0, END)
        self.i.delete(0, END)
        self.j.delete(0, END)

    def comp(self):
        z = self.variable.get()
        n = float(self.entry_3.get())
        g = float(self.entry_2.get())
        main(z, n, g)
        self.clear_text()
        self.a.insert(0, f"{x[0]:.5f}")
        self.b.insert(0, f"{x[1]:.5f}")
        self.c.insert(0, f"{x[2]:.5f}")
        self.d.insert(0, f"{x[3]:.5f}")
        self.e.insert(0, f"{x[4]:.5f}")
        self.f.insert(0, f"{x[5]:.5f}")
        self.g.insert(0, f"{x[6]:.5f}")
        self.h.insert(0, f"{x[7]:.5f}")
        self.i.insert(0, f"{x[8]:.5f}")
        self.j.insert(0, f"{x[9]:.5f}")


root = Tk()
b = X(root)
root.mainloop()
