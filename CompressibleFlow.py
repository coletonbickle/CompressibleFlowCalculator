from tkinter import *
from Isentropic import *
from NormalShock import *
from NormalShock import _Normal


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
        # Below is all code for output boxes relevant to Isentropic Flow Relations
        #
        self.machLabel = Label(master, text="Mach Number: ")  # Mach Number
        self.machLabel.grid(row=6, column=0, sticky=E)
        self.isen_a = Entry(master)
        self.isen_a.grid(row=6, column=1)
        self.isen_a.configure(state="readonly")

        self.MALabel = Label(master, text="Mach Angle: ")  # Mach Angle
        self.MALabel.grid(row=6, column=2, sticky=E)
        self.isen_b = Entry(master)
        self.isen_b.grid(row=6, column=3)
        self.isen_b.configure(state="readonly")

        self.PMLabel = Label(master, text="P-M Angle: ")  # P-M Angle
        self.PMLabel.grid(row=6, column=4)
        self.isen_c = Entry(master)
        self.isen_c.grid(row=6, column=5)
        self.isen_c.configure(state="readonly")

        self.pp0label = Label(master, text="p/p0: ")  # p/p0
        self.pp0label.grid(row=7, column=0, sticky=E)
        self.isen_d = Entry(master)
        self.isen_d.grid(row=7, column=1)
        self.isen_d.configure(state="readonly")

        self.rr0label = Label(master, text="rho/rho0: ")  # rho/rho0
        self.rr0label.grid(row=7, column=2, sticky=E)
        self.isen_e = Entry(master)
        self.isen_e.grid(row=7, column=3)
        self.isen_e.configure(state="readonly")

        self.tt0label = Label(master, text="T/T0: ")  # T/T0
        self.tt0label.grid(row=7, column=4, sticky=E)
        self.isen_f = Entry(master)
        self.isen_f.grid(row=7, column=5)
        self.isen_f.configure(state="readonly")

        self.ppstLabel = Label(master, text="p/p*: ")  # p/p*
        self.ppstLabel.grid(row=8, column=0, sticky=E)
        self.isen_g = Entry(master)
        self.isen_g.grid(row=8, column=1)
        self.isen_g.configure(state="readonly")

        self.rrstLabel = Label(master, text="rho/rho*: ")  # rho/rho*
        self.rrstLabel.grid(row=8, column=2, sticky=E)
        self.isen_h = Entry(master)
        self.isen_h.grid(row=8, column=3)
        self.isen_h.configure(state="readonly")

        self.ttstLabel = Label(master, text="T/T*: ")  # T/T*
        self.ttstLabel.grid(row=8, column=4, sticky=E)
        self.isen_i = Entry(master)
        self.isen_i.grid(row=8, column=5)
        self.isen_i.configure(state="readonly")

        self.aastLabel = Label(master, text="A/A*: ")  # A/A*
        self.aastLabel.grid(row=8, column=6, sticky=E)
        self.isen_j = Entry(master)
        self.isen_j.grid(row=8, column=7)
        self.isen_j.configure(state="readonly")

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

        self.normErrorMsg = Label(master, text="Error: ").grid(row=15, sticky=E)
        self.normMsg = StringVar()
        self.NormError = Entry(master, textvariable=self.msg, width=57)
        self.NormError.grid(row=15, column=1, columnspan=5, sticky=W)
        self.NormError.configure(state="readonly")
        #
        # Below is all code for output boxes relevant to Normal Shock Relations
        #
        self.mOneLabel = Label(master, text="M1: ")  # M1
        self.mOneLabel.grid(row=13, column=0, sticky=E)
        self.norm_a = Entry(master)
        self.norm_a.grid(row=13, column=1)
        self.norm_a.configure(state="readonly")

        self.mTwoLabel = Label(master, text="M2: ")  # M2
        self.mTwoLabel.grid(row=13, column=2, sticky=E)
        self.norm_b = Entry(master)
        self.norm_b.grid(row=13, column=3)
        self.norm_b.configure(state="readonly")

        self.p02p01Label = Label(master, text="p02/p01: ")  # p02/p01
        self.p02p01Label.grid(row=13, column=4)
        self.norm_c = Entry(master)
        self.norm_c.grid(row=13, column=5)
        self.norm_c.configure(state="readonly")

        self.p2p1label = Label(master, text="p2/p1: ")  # p2/p1
        self.p2p1label.grid(row=14, column=0, sticky=E)
        self.norm_d = Entry(master)
        self.norm_d.grid(row=14, column=1)
        self.norm_d.configure(state="readonly")

        self.r2r1label = Label(master, text="rho2/rho1: ")  # rho2/rho1
        self.r2r1label.grid(row=14, column=2, sticky=E)
        self.norm_e = Entry(master)
        self.norm_e.grid(row=14, column=3)
        self.norm_e.configure(state="readonly")

        self.t2t1label = Label(master, text="T2/T1: ")  # T2/T1
        self.t2t1label.grid(row=14, column=4, sticky=E)
        self.norm_f = Entry(master)
        self.norm_f.grid(row=14, column=5)
        self.norm_f.configure(state="readonly")

        # GUI Frame size
        frame = Frame(master)
        frame.grid()

    def clear_isen(clear):
        clear.isen_a.configure(state=NORMAL)
        clear.isen_a.delete(0, END)
        clear.isen_b.configure(state=NORMAL)
        clear.isen_b.delete(0, END)
        clear.isen_c.configure(state=NORMAL)
        clear.isen_c.delete(0, END)
        clear.isen_d.configure(state=NORMAL)
        clear.isen_d.delete(0, END)
        clear.isen_e.configure(state=NORMAL)
        clear.isen_e.delete(0, END)
        clear.isen_f.configure(state=NORMAL)
        clear.isen_f.delete(0, END)
        clear.isen_g.configure(state=NORMAL)
        clear.isen_g.delete(0, END)
        clear.isen_h.configure(state=NORMAL)
        clear.isen_h.delete(0, END)
        clear.isen_i.configure(state=NORMAL)
        clear.isen_i.delete(0, END)
        clear.isen_j.configure(state=NORMAL)
        clear.isen_j.delete(0, END)

    def read_isen(self):
        self.isen_a.configure(state="readonly")
        self.isen_b.configure(state="readonly")
        self.isen_c.configure(state="readonly")
        self.isen_d.configure(state="readonly")
        self.isen_e.configure(state="readonly")
        self.isen_f.configure(state="readonly")
        self.isen_g.configure(state="readonly")
        self.isen_h.configure(state="readonly")
        self.isen_i.configure(state="readonly")
        self.isen_j.configure(state="readonly")

    def set_error(self):
        self.error.configure(state=NORMAL)
        self.error.delete(0, END)
        self.error.insert(0, self.msg)
        self.error.configure(state="readonly")

    def isen(self):
        z = self.variable1.get()
        n = float(self.entry_3.get())
        g = float(self.entry_2.get())
        x, msg = fcn_comp(z, n, g)
        self.clear_isen()
        self.isen_a.insert(0, f"{x[0]:.5f}")
        self.isen_b.insert(0, f"{x[1]:.5f}")
        self.isen_c.insert(0, f"{x[2]:.5f}")
        self.isen_d.insert(0, f"{x[3]:.5f}")
        self.isen_e.insert(0, f"{x[4]:.5f}")
        self.isen_f.insert(0, f"{x[5]:.5f}")
        self.isen_g.insert(0, f"{x[6]:.5f}")
        self.isen_h.insert(0, f"{x[7]:.5f}")
        self.isen_i.insert(0, f"{x[8]:.5f}")
        self.isen_j.insert(0, f"{x[9]:.5f}")
        self.read_isen()
        self.msg = msg
        self.set_error()

    def norm(self):
        z = self.variable2.get()
        n = float(self.entry_3norm.get())
        g = float(self.entry_2norm.get())
        fcn_normal(z, n, g)  # Fix Error where fcn_normal()/main() cannot return class: _Normal


root = Tk()
b = GUI(root)
root.title("Isentropic Flow Calculator")
root.mainloop()
