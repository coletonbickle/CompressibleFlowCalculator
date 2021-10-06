from tkinter import *
from Isentropic import *
from NormalShock import *


class GUI:
    m = "Mach Number"
    T = "T/T0"
    P = "p/p0"
    rho = "rho/rho0"
    Asub = "A/A* (sub)"
    Asup = "A/A* (sup)"
    MA = "Mach Angle"
    PMang = "P-M Angle"
    msg = ""

    def __init__(self, master):
        self.IsentropicTitle = Label(master, text="Isentropic Flow Relations", font='Helvetica 12 bold').grid(
            row=0, columnspan=2, sticky=W)
        self.label_2 = Label(master, text="Perfect Gas, Gamma: ").grid(row=1, sticky=W)
        self.entry_2 = StringVar()
        self.entry_3 = StringVar()
        self.entry_2 = Entry(master)  # Adds Available entry spot
        self.entry_3 = Entry(master)
        self.angle = Label(master, text="Angles in Degrees").grid(row=2, column=2, sticky=W)

        self.entry_2.insert(END, 1.4)  # Adds Default Entry Value
        self.entry_3.insert(END, 2.0)
        self.entry_2.grid(row=1, column=1, sticky=W)
        self.entry_3.grid(row=2, column=1, sticky=W)

        self.variable1 = StringVar(master)
        self.variable1.set("Mach Number")  # default value

        self.Drop1 = OptionMenu(master, self.variable1, "Mach Number", "T/T0", "p/p0", "rho/rho0", "A/A* (sub)",
                                "A/A* (sup)", "Mach Angle", "P-M Angle")  # Drop Down Menu
        self.Drop1.grid(row=2, sticky=W)

        self.errorMsg = Label(master, text="Error: ").grid(row=9, sticky=E)
        self.msg = StringVar()
        self.error = Entry(master, textvariable=self.msg, width=57)
        self.error.grid(row=9, column=1, columnspan=5, sticky=W)
        self.error.configure(state="readonly")

        self.calcButton = Button(master, text="Calculate", width=20, command=self.isen)  # Calculate Button
        self.calcButton.grid(row=2, column=3, columnspan=2)

        self.empty1 = Label(master, text="").grid(row=3)
        self.empty2 = Label(master, text="").grid(row=10)
        #
        # Output Labels for isentropic flow relations
        #
        self.machLabel = Label(master, text="Mach Number: ")  # Mach Number
        self.machLabel.grid(row=6, column=0, sticky=E)
        self.a = Entry(master)
        self.a.grid(row=6, column=1)
        self.a.configure(state="readonly")

        self.MALabel = Label(master, text="Mach Angle: ")  # Mach Angle
        self.MALabel.grid(row=6, column=2, sticky=E)
        self.b = Entry(master)
        self.b.grid(row=6, column=3)
        self.b.configure(state="readonly")

        self.PMLabel = Label(master, text="P-M Angle: ")  # P-M Angle
        self.PMLabel.grid(row=6, column=4)
        self.c = Entry(master)
        self.c.grid(row=6, column=5)
        self.c.configure(state="readonly")

        self.pp0label = Label(master, text="p/p0: ")  # p/p0
        self.pp0label.grid(row=7, column=0, sticky=E)
        self.d = Entry(master)
        self.d.grid(row=7, column=1)
        self.d.configure(state="readonly")

        self.rr0label = Label(master, text="rho/rho0: ")  # rho/rho0
        self.rr0label.grid(row=7, column=2, sticky=E)
        self.e = Entry(master)
        self.e.grid(row=7, column=3)
        self.e.configure(state="readonly")

        self.tt0label = Label(master, text="T/T0: ")  # T/T0
        self.tt0label.grid(row=7, column=4, sticky=E)
        self.f = Entry(master)
        self.f.grid(row=7, column=5)
        self.f.configure(state="readonly")

        self.ppstLabel = Label(master, text="p/p*: ")  # p/p*
        self.ppstLabel.grid(row=8, column=0, sticky=E)
        self.g = Entry(master)
        self.g.grid(row=8, column=1)
        self.g.configure(state="readonly")

        self.rrstLabel = Label(master, text="rho/rho*: ")  # rho/rho*
        self.rrstLabel.grid(row=8, column=2, sticky=E)
        self.h = Entry(master)
        self.h.grid(row=8, column=3)
        self.h.configure(state="readonly")

        self.ttstLabel = Label(master, text="T/T*: ")  # T/T*
        self.ttstLabel.grid(row=8, column=4, sticky=E)
        self.i = Entry(master)
        self.i.grid(row=8, column=5)
        self.i.configure(state="readonly")

        self.aastLabel = Label(master, text="A/A*: ")  # A/A*
        self.aastLabel.grid(row=8, column=6, sticky=E)
        self.j = Entry(master)
        self.j.grid(row=8, column=7)
        self.j.configure(state="readonly")

        self.quitButton = Button(master, text="Quit", width=15, command=master.quit)
        self.quitButton.grid(row=1, column=7)
        #
        # Normal Shock Relations
        #
        self.NormalTitle = Label(master, text="Normal Shock Relations", font='Helvetica 12 bold').grid(
            row=10, columnspan=2, sticky=W)
        self.label_2 = Label(master, text="Perfect Gas, Gamma: ").grid(row=11, sticky=W)
        self.entry_2norm = StringVar()
        self.entry_3norm = StringVar()
        self.entry_2norm = Entry(master)  # Adds Available entry spot
        self.entry_3norm = Entry(master)
        self.angle = Label(master, text="").grid(row=12, column=2, sticky=W)

        self.entry_2norm.insert(END, 1.4)  # Adds Default Entry Value
        self.entry_3norm.insert(END, 2.0)
        self.entry_2norm.grid(row=11, column=1)
        self.entry_3norm.grid(row=12, column=1)

        self.variable2 = StringVar(master)
        self.variable2.set("M1")  # default value
        self.Drop2 = OptionMenu(master, self.variable2, "M1", "M2", "p02/p01", "p1/p02", "p2/p1",
                                "rho2/rho1", "T2/T1")  # Drop Down Menu
        self.Drop2.grid(row=12, sticky=W)

        self.calcButton2 = Button(master, text="Calculate", width=20, command=self.norm)  # Calculate Button
        self.calcButton2.grid(row=12, column=3, columnspan=2)

        # GUI size
        frame = Frame(master)
        frame.grid()

    def clear_text(clear):
        clear.a.configure(state=NORMAL)
        clear.a.delete(0, END)
        clear.b.configure(state=NORMAL)
        clear.b.delete(0, END)
        clear.c.configure(state=NORMAL)
        clear.c.delete(0, END)
        clear.d.configure(state=NORMAL)
        clear.d.delete(0, END)
        clear.e.configure(state=NORMAL)
        clear.e.delete(0, END)
        clear.f.configure(state=NORMAL)
        clear.f.delete(0, END)
        clear.g.configure(state=NORMAL)
        clear.g.delete(0, END)
        clear.h.configure(state=NORMAL)
        clear.h.delete(0, END)
        clear.i.configure(state=NORMAL)
        clear.i.delete(0, END)
        clear.j.configure(state=NORMAL)
        clear.j.delete(0, END)

    def set_error(self):
        self.error.configure(state=NORMAL)
        self.error.delete(0, END)
        self.error.insert(0, self.msg)
        self.error.configure(state="readonly")

    def isen(Isen):
        z = Isen.variable1.get()
        n = float(Isen.entry_3.get())
        g = float(Isen.entry_2.get())
        x, msg = fcn_comp(z, n, g)
        Isen.clear_text()
        Isen.a.insert(0, f"{x[0]:.5f}")
        Isen.a.configure(state="readonly")
        Isen.b.insert(0, f"{x[1]:.5f}")
        Isen.b.configure(state="readonly")
        Isen.c.insert(0, f"{x[2]:.5f}")
        Isen.c.configure(state="readonly")
        Isen.d.insert(0, f"{x[3]:.5f}")
        Isen.d.configure(state="readonly")
        Isen.e.insert(0, f"{x[4]:.5f}")
        Isen.e.configure(state="readonly")
        Isen.f.insert(0, f"{x[5]:.5f}")
        Isen.f.configure(state="readonly")
        Isen.g.insert(0, f"{x[6]:.5f}")
        Isen.g.configure(state="readonly")
        Isen.h.insert(0, f"{x[7]:.5f}")
        Isen.h.configure(state="readonly")
        Isen.i.insert(0, f"{x[8]:.5f}")
        Isen.i.configure(state="readonly")
        Isen.j.insert(0, f"{x[9]:.5f}")
        Isen.j.configure(state="readonly")
        Isen.msg = msg
        Isen.set_error()

    def norm(norm):
        # z = Isen.variable1.get()
        # n = float(Isen.entry_3.get())
        # g = float(Isen.entry_2.get())
        main()  # z, n, g

root = Tk()
b = GUI(root)
root.title("Isentropic Flow Calculator")
root.mainloop()
