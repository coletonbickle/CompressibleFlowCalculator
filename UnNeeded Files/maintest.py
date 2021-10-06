from tkinter import *
import numpy as np
import math as math


class X:

    # x = np.array(np.zeros(10))

    def __init__(self, z, n, g):
        self.z = z
        self.n = n
        self.g = g


        i = z == m or z == T or z == P or z == rho or z == Asub or z == Asup or z == MA or z == PMang
        j = g > 1
        if i and j:
            if z == m:
                self.x = self.mach(self, n, g)
            # elif z == T:
            #     x = t0(n, g)
            # elif z == P:
            #     x = p0(n, g)
            # elif z == rho:
            #     x = r0(n, g)
            # elif z == Asub:
            #     x = 5
            # elif z == Asup:
            #     x = 5
            # elif z == MA:
            #     x = ma(n, g)
            # elif z == PMang:
            #     x = pmang(n, g)
            else:
            print('\nError - Please input Compatible Input')
            if i == 0:
                print('*Input Valid Input Type')
            if j == 0:
                print('*Gamma Must be Greater than 1\n')

    def mach(self, m, g):
        if m >= 1:
            self.ang = math.degrees(math.asin(1 / m))
            p_mang1 = math.sqrt((g + 1) / (g - 1)) * math.degrees(math.atan(math.sqrt((g - 1) / (g + 1) * (m ** 2 - 1))))
            p_mang2 = math.degrees(math.atan(math.sqrt(m ** 2 - 1)))
            self.p_mang = p_mang1 - p_mang2
        else:
            self.ang = None
            self.p_mang = None

        self.M = m
        self.tt0 = 1 / (1 + ((g - 1) / 2) * m ** 2)
        self.pp0 = 1 / ((1 / self.tt0) ** (g / (g - 1)))
        self.rr0 = 1 / ((1 / self.tt0) ** (1 / (g - 1)))
        self.ttst = 1 / ((1 / self.tt0) * (2 / (g + 1)))
        self.ppst = self.ttst ** (g / (g - 1))
        self.rrst = self.ttst ** (1 / (g - 1))
        self.aast = (((g + 1) / 2) ** ((-1 * g - 1) / (g - 1) / 2)) / m * (1 / tt0) ** ((g + 1) / (g - 1) / 2)

        return x

print('\nTypes to Choose From: Mach Number, T/T0, p/p0, rho/rho0, A/A* (sub), A/A* (sup), Mach Angle, P-M Angle')
print('Note: Type Exactly as Shown')
z = input("Enter Input type: ")
if z == "Mach Angle" or z == "P-M Angle":
    n = float(input("Input Value (in degrees): "))
else:
    n = float(input("Input Value: "))
g = float(input("Gamma Value: "))

m = "Mach Number"
T = "T/T0"
P = "p/p0"
rho = "rho/rho0"
Asub = "A/A* (sub)"
Asup = "A/A* (sup)"
MA = "Mach Angle"
PMang = "P-M Angle"

output = X(z, n, g)

i = z == m or z == T or z == P or z == rho or z == Asub or z == Asup or z == MA or z == PMang
j = g > 1
if i and j:
    print(f"\nMach Number = {output.mach():.5f}  Mach Angle = {self.ang:.5f}  P-M Angle = {self.p_mang:.5f}")
    # print(f"p/p0 = {x[3]:.5f}  rho/rho0 = {x[4]:.5f}  T/T0 = {x[5]:.5f}")
    # print(f"p/p* = {x[6]:.5f}  rho/rho* = {x[7]:.5f}  T/T* = {x[8]:.5f} A/A* = {x[9]:.5f}")
else:
    print('\nError - Please input Compatible Input')
    if i == 0:
        print('*Input Valid Input Type')
    if j == 0:
        print('*Gamma Must be Greater than 1\n')


    # def t0(self, tt0, g):
    #     m = math.sqrt(((1 / tt0) - 1) * (2 / (g - 1)))
    #     if m >= 1:
    #         ang = math.degrees(math.asin(1 / m))
    #         p_mang1 = math.sqrt((g + 1) / (g - 1)) * math.degrees(
    #             math.atan(math.sqrt((g - 1) / (g + 1) * (m ** 2 - 1))))
    #         p_mang2 = math.degrees(math.atan(math.sqrt(m ** 2 - 1)))
    #         p_mang = p_mang1 - p_mang2
    #     else:
    #         ang = None
    #         p_mang = None
    #     pp0 = 1 / ((1 / tt0) ** (g / (g - 1)))
    #     rr0 = 1 / ((1 / tt0) ** (1 / (g - 1)))
    #     ttst = 1 / ((1 / tt0) * (2 / (g + 1)))
    #     ppst = ttst ** (g / (g - 1))
    #     rrst = ttst ** (1 / (g - 1))
    #     aast = (((g + 1) / 2) ** ((-1 * g - 1) / (g - 1) / 2)) / m * (1 / tt0) ** ((g + 1) / (g - 1) / 2)
    #
    #     x[0] = m
    #     x[1] = ang
    #     x[2] = p_mang
    #     x[3] = pp0
    #     x[4] = rr0
    #     x[5] = tt0
    #     x[6] = ppst
    #     x[7] = rrst
    #     x[8] = ttst
    #     x[9] = aast
    #     return x
    #
    # def p0(self, pp0, g):
    #     tt0 = 1 / (pp0 ** (-(g - 1) / g))
    #     m = math.sqrt(((1 / tt0) - 1) * (2 / (g - 1)))
    #     if m >= 1:
    #         ang = math.degrees(math.asin(1 / m))
    #         p_mang1 = math.sqrt((g + 1) / (g - 1)) * math.degrees(
    #             math.atan(math.sqrt((g - 1) / (g + 1) * (m ** 2 - 1))))
    #         p_mang2 = math.degrees(math.atan(math.sqrt(m ** 2 - 1)))
    #         p_mang = p_mang1 - p_mang2
    #     else:
    #         ang = None
    #         p_mang = None
    #     rr0 = 1 / ((1 / tt0) ** (1 / (g - 1)))
    #     ttst = 1 / ((1 / tt0) * (2 / (g + 1)))
    #     ppst = ttst ** (g / (g - 1))
    #     rrst = ttst ** (1 / (g - 1))
    #     aast = (((g + 1) / 2) ** ((-1 * g - 1) / (g - 1) / 2)) / m * (1 / tt0) ** ((g + 1) / (g - 1) / 2)
    #
    #     x[0] = m
    #     x[1] = ang
    #     x[2] = p_mang
    #     x[3] = pp0
    #     x[4] = rr0
    #     x[5] = tt0
    #     x[6] = ppst
    #     x[7] = rrst
    #     x[8] = ttst
    #     x[9] = aast
    #     return x
    #
    # def r0(self, rr0, g):
    #     tt0 = 1 / (rr0 ** (-(g - 1) / 1))
    #     m = math.sqrt(((1 / tt0) - 1) * (2 / (g - 1)))
    #     if m >= 1:
    #         ang = math.degrees(math.asin(1 / m))
    #         p_mang1 = math.sqrt((g + 1) / (g - 1)) * math.degrees(
    #             math.atan(math.sqrt((g - 1) / (g + 1) * (m ** 2 - 1))))
    #         p_mang2 = math.degrees(math.atan(math.sqrt(m ** 2 - 1)))
    #         p_mang = p_mang1 - p_mang2
    #     else:
    #         ang = None
    #         p_mang = None
    #     pp0 = 1 / ((1 / tt0) ** (g / (g - 1)))
    #     ttst = 1 / ((1 / tt0) * (2 / (g + 1)))
    #     ppst = ttst ** (g / (g - 1))
    #     rrst = ttst ** (1 / (g - 1))
    #     aast = (((g + 1) / 2) ** ((-1 * g - 1) / (g - 1) / 2)) / m * (1 / tt0) ** ((g + 1) / (g - 1) / 2)
    #     return x
    #
    # def ma(self, ang, g):
    #     m = 1 / math.sin(math.radians(ang))
    #     p_mang1 = math.sqrt((g + 1) / (g - 1)) * math.degrees(math.atan(math.sqrt((g - 1) / (g + 1) * (m ** 2 - 1))))
    #     p_mang2 = math.degrees(math.atan(math.sqrt(m ** 2 - 1)))
    #     p_mang = p_mang1 - p_mang2
    #
    #     tt0 = 1 / (1 + ((g - 1) / 2) * m ** 2)
    #     pp0 = 1 / ((1 / tt0) ** (g / (g - 1)))
    #     rr0 = 1 / ((1 / tt0) ** (1 / (g - 1)))
    #     ttst = 1 / ((1 / tt0) * (2 / (g + 1)))
    #     ppst = ttst ** (g / (g - 1))
    #     rrst = ttst ** (1 / (g - 1))
    #     aast = (((g + 1) / 2) ** ((-1 * g - 1) / (g - 1) / 2)) / m * (1 / tt0) ** ((g + 1) / (g - 1) / 2)
    #
    #     return x
    #
    # def pmang(self, p_mang, g):
    #     m = 1
    #     while m > 0:
    #         temp1 = math.sqrt((g + 1) / (g - 1)) * math.degrees(math.atan(math.sqrt((g - 1) / (g + 1) * (m ** 2 - 1))))
    #         temp2 = math.degrees(math.atan(math.sqrt(m ** 2 - 1)))
    #         temp = temp1 - temp2
    #         if temp >= p_mang:
    #             break
    #         else:
    #             m = m + 0.00001
    #
    #     ang = math.degrees(math.asin(1 / m))
    #     tt0 = 1 / (1 + ((g - 1) / 2) * m ** 2)
    #     pp0 = 1 / ((1 / tt0) ** (g / (g - 1)))
    #     rr0 = 1 / ((1 / tt0) ** (1 / (g - 1)))
    #     ttst = 1 / ((1 / tt0) * (2 / (g + 1)))
    #     ppst = ttst ** (g / (g - 1))
    #     rrst = ttst ** (1 / (g - 1))
    #     aast = (((g + 1) / 2) ** ((-1 * g - 1) / (g - 1) / 2)) / m * (1 / tt0) ** ((g + 1) / (g - 1) / 2)
    #
    #     return x

# root = Tk()
# b = X(root)
# root.mainloop()
