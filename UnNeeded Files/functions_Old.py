import numpy as np
import math as math

x = np.array(np.zeros(10))
mch = "Mach Number"
T = "T/T0"
P = "p/p0"
rho = "rho/rho0"
Asub = "A/A* (sub)"
Asup = "A/A* (sup)"
MA = "Mach Angle"
PMang = "P-M Angle"


def fcn(z, n, g):
    m = 0
    ang = 0
    p_mang = 0
    pp0 = 0
    rr0 = 0
    tt0 = 0
    if z == mch or z == T or z == MA:
        if z == mch:
            m = n
            tt0 = 1 / (1 + ((g - 1) / 2) * m ** 2)
        elif z == T:
            tt0 = n
            m = math.sqrt(((1 / tt0) - 1) * (2 / (g - 1)))

        if z != MA and m >= 1:
            ang = math.degrees(math.asin(1 / m))
            p_mang1 = math.sqrt((g + 1) / (g - 1)) * \
                math.degrees(math.atan(math.sqrt((g - 1) / (g + 1) * (m ** 2 - 1))))
            p_mang2 = math.degrees(math.atan(math.sqrt(m ** 2 - 1)))
            p_mang = p_mang1 - p_mang2
        elif z != MA:
            ang = None
            p_mang = None
        if z == MA:
            ang = n
            m = 1 / math.sin(math.radians(ang))
            p_mang1 = math.sqrt((g + 1) / (g - 1)) * \
                math.degrees(math.atan(math.sqrt((g - 1) / (g + 1) * (m ** 2 - 1))))
            p_mang2 = math.degrees(math.atan(math.sqrt(m ** 2 - 1)))
            p_mang = p_mang1 - p_mang2
            tt0 = 1 / (1 + ((g - 1) / 2) * m ** 2)

        pp0 = 1 / ((1 / tt0) ** (g / (g - 1)))
        rr0 = 1 / ((1 / tt0) ** (1 / (g - 1)))

    elif z == P or z == rho:
        if z == P:
            pp0 = n
            tt0 = 1 / (pp0 ** (-(g - 1) / g))
            rr0 = 1 / ((1 / tt0) ** (1 / (g - 1)))
        else:
            rr0 = n
            tt0 = 1 / (rr0 ** (-(g - 1) / 1))
            pp0 = 1 / ((1 / tt0) ** (g / (g - 1)))

        m = math.sqrt(((1 / tt0) - 1) * (2 / (g - 1)))
        if m >= 1:
            ang = math.degrees(math.asin(1 / m))
            p_mang1 = math.sqrt((g + 1) / (g - 1)) * \
                math.degrees(math.atan(math.sqrt((g - 1) / (g + 1) * (m ** 2 - 1))))
            p_mang2 = math.degrees(math.atan(math.sqrt(m ** 2 - 1)))
            p_mang = p_mang1 - p_mang2
        else:
            ang = None
            p_mang = None

    elif z == PMang:
        p_mang = n
        m = 1
        if p_mang < 103:
            while m > 0:
                temp1 = math.sqrt((g + 1) / (g - 1)) * math.degrees(
                    math.atan(math.sqrt((g - 1) / (g + 1) * (m ** 2 - 1))))
                temp2 = math.degrees(math.atan(math.sqrt(m ** 2 - 1)))
                temp = temp1 - temp2
                if temp >= p_mang:
                    break
                elif m >= 10:
                    break
                else:
                    m = m + 0.00001

        ang = math.degrees(math.asin(1 / m))
        tt0 = 1 / (1 + ((g - 1) / 2) * m ** 2)
        pp0 = 1 / ((1 / tt0) ** (g / (g - 1)))
        rr0 = 1 / ((1 / tt0) ** (1 / (g - 1)))

    elif z == Asub or z == Asup:
        aast = n
        m = 1
        if z == Asub:
            while m >= 0.00002:
                temp1 = 1 / (1 + ((g - 1) / 2) * m ** 2)
                temp = (((g + 1) / 2) ** ((-1 * g - 1) / (g - 1) / 2)) / m * (1 / temp1) ** ((g + 1) / (g - 1) / 2)
                if temp >= aast:
                    break
                else:
                    m = m - 0.00001
        elif z == Asup:
            while m > 0:
                temp1 = 1 / (1 + ((g - 1) / 2) * m ** 2)
                temp = (((g + 1) / 2) ** ((-1 * g - 1) / (g - 1) / 2)) / m * (1 / temp1) ** ((g + 1) / (g - 1) / 2)
                if temp >= aast:
                    break
                elif m >= 10:
                    break
                else:
                    m = m + 0.00001

        if m >= 1:
            ang = math.degrees(math.asin(1 / m))
            p_mang1 = math.sqrt((g + 1) / (g - 1)) * \
                math.degrees(math.atan(math.sqrt((g - 1) / (g + 1) * (m ** 2 - 1))))
            p_mang2 = math.degrees(math.atan(math.sqrt(m ** 2 - 1)))
            p_mang = p_mang1 - p_mang2
        else:
            ang = None
            p_mang = None

        tt0 = 1 / (1 + ((g - 1) / 2) * m ** 2)
        pp0 = 1 / ((1 / tt0) ** (g / (g - 1)))
        rr0 = 1 / ((1 / tt0) ** (1 / (g - 1)))

    ttst = 1 / ((1 / tt0) * (2 / (g + 1)))
    ppst = ttst ** (g / (g - 1))
    rrst = ttst ** (1 / (g - 1))
    aast = (((g + 1) / 2) ** ((-1 * g - 1) / (g - 1) / 2)) / m * (1 / tt0) ** ((g + 1) / (g - 1) / 2)

    x[0] = m
    x[1] = ang
    x[2] = p_mang
    x[3] = pp0
    x[4] = rr0
    x[5] = tt0
    x[6] = ppst
    x[7] = rrst
    x[8] = ttst
    x[9] = aast
    return x

# def mach(m, g):
#     if m >= 1:
#         ang = math.degrees(math.asin(1 / m))
#         p_mang1 = math.sqrt((g + 1) / (g - 1)) * math.degrees(math.atan(math.sqrt((g - 1) / (g + 1) * (m ** 2 - 1))))
#         p_mang2 = math.degrees(math.atan(math.sqrt(m ** 2 - 1)))
#         p_mang = p_mang1 - p_mang2
#     else:
#         ang = None
#         p_mang = None
#
#     tt0 = 1 / (1 + ((g - 1) / 2) * m ** 2)
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
#
# def t0(tt0, g):
#     m = math.sqrt(((1 / tt0) - 1) * (2 / (g - 1)))
#     if m >= 1:
#         ang = math.degrees(math.asin(1 / m))
#         p_mang1 = math.sqrt((g + 1) / (g - 1)) * math.degrees(math.atan(math.sqrt((g - 1) / (g + 1) * (m ** 2 - 1))))
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
#
# def p0(pp0, g):
#     tt0 = 1/(pp0 ** (-(g - 1) / g))
#     m = math.sqrt(((1/tt0)-1)*(2/(g-1)))
#     if m >= 1:
#         ang = math.degrees(math.asin(1 / m))
#         p_mang1 = math.sqrt((g + 1) / (g - 1)) * math.degrees(math.atan(math.sqrt((g - 1) / (g + 1) * (m ** 2 - 1))))
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
#
# def r0(rr0, g):
#     tt0 = 1/(rr0 ** (-(g - 1) / 1))
#     m = math.sqrt(((1/tt0)-1)*(2/(g-1)))
#     if m >= 1:
#         ang = math.degrees(math.asin(1 / m))
#         p_mang1 = math.sqrt((g + 1) / (g - 1)) * math.degrees(math.atan(math.sqrt((g - 1) / (g + 1) * (m ** 2 - 1))))
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
#
# def ma(ang, g):
#     m = 1/math.sin(math.radians(ang))
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
#
# def pmang(p_mang, g):
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
