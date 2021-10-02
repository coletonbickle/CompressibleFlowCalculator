from Isentropic import *
import numpy as np

print('\nTypes to Choose From: Mach Number, T/T0, p/p0, rho/rho0, A/A* (sub), A/A* (sup), Mach Angle, P-M Angle')
print('Note: Type Exactly as Shown')
z = input("Enter Input type: ")
if z == "Mach Angle" or z == "P-M Angle":
    n = float(input("Input Value (in degrees): "))
else:
    n = float(input("Input Value: "))
g = float(input("Gamma Value: "))

x = np.array(np.zeros(10))
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
    x = fcn(z, n, g)
    # if z == m:
    #     x = mach(n, g)
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
    print(f"\nMach Number = {x[0]:.5f}  Mach Angle = {x[1]:.5f}  P-M Angle = {x[2]:.5f}")
    print(f"p/p0 = {x[3]:.5f}  rho/rho0 = {x[4]:.5f}  T/T0 = {x[5]:.5f}")
    print(f"p/p* = {x[6]:.5f}  rho/rho* = {x[7]:.5f}  T/T* = {x[8]:.5f} A/A* = {x[9]:.5f}")
else:
    print('\nError - Please input Compatible Input')
    if i == 0:
        print('*Input Valid Input Type')
    if j == 0:
        print('*Gamma Must be Greater than 1\n')
input()




