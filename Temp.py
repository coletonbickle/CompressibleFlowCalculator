import math as math


class _Comp:
    def __init__(self, z, n, g, x=None):
        self.z = z
        self.n = n
        self.g = g
        self.mch = x
        self.tt0 = x
        self.pp0 = x
        self.rr0 = x
        self.aast = x
        self.ma = x
        self.pma = x
        self.ttst = x
        self.ppst = x
        self.rrst = x
        self.msg = "None: All Values Converged"

    def fcn_comp(self):
        if self.g <= 1:
            self._error()
            self.msg = "Gamma Must be Greater than 1"
            return
        mch = "Mach Number".lower()
        T = "T/T0".lower()
        P = "p/p0".lower()
        rho = "rho/rho0".lower()
        Asub = "A/A* (sub)".lower()
        Asup = "A/A* (sup)".lower()
        MA = "Mach Angle".lower()
        PMang = "P-M Angle".lower()
        g = self.g
        n = self.n
        z = self.z.lower()

        if z == mch or z == T or z == MA:  # T/T0 between 0 and 1 and MA between 0 and 90
            if z == mch:
                m = n
                self.mch = m
                self.tt0 = 1 / (1 + ((g - 1) / 2) * m ** 2)
            elif z == T and 0 < n < 1:
                self.tt0 = n
                m = math.sqrt(((1 / self.tt0) - 1) * (2 / (g - 1)))
                self.mch = m
            elif z == T:
                self._error()
                self.msg = "T/T0 Must be Between 0 and 1"
                return

            if z != MA and self.mch >= 1:
                self.ma = math.degrees(math.asin(1 / m))
                p_mang1 = math.sqrt((g + 1) / (g - 1)) * \
                    math.degrees(math.atan(math.sqrt((g - 1) / (g + 1) * (m ** 2 - 1))))
                p_mang2 = math.degrees(math.atan(math.sqrt(m ** 2 - 1)))
                self.pma = p_mang1 - p_mang2
            elif z != MA:
                self.ma = None
                self.pma = None
            if z == MA and 0 < n < 90:
                self.ma = n
                m = 1 / math.sin(math.radians(self.ma))
                self.mch = m
                p_mang1 = math.sqrt((g + 1) / (g - 1)) * \
                    math.degrees(math.atan(math.sqrt((g - 1) / (g + 1) * (m ** 2 - 1))))
                p_mang2 = math.degrees(math.atan(math.sqrt(m ** 2 - 1)))
                self.pma = p_mang1 - p_mang2
                self.tt0 = 1 / (1 + ((g - 1) / 2) * m ** 2)
            elif z == MA:
                self._error()
                self.msg = "Mach Angle Must be Between 0 and 90 Degrees"
                return

            self.pp0 = 1 / ((1 / self.tt0) ** (g / (g - 1)))
            self.rr0 = 1 / ((1 / self.tt0) ** (1 / (g - 1)))

        elif z == P or z == rho:  # P/P0 and rho/rho0 Between 0 and 1
            if n <= 0 or n >= 1:
                self._error()
                if z == P:
                    self.msg = "p/p0 Must be Between 0 and 1"
                else:
                    self.msg = "rho/rho0 Must be Between 0 and 1"
                return

            if z == P:
                self.pp0 = n
                self.tt0 = 1 / (pp0 ** (-(g - 1) / g))
                self.rr0 = 1 / ((1 / tt0) ** (1 / (g - 1)))
            else:
                self.rr0 = n
                self.tt0 = 1 / (rr0 ** (-(g - 1) / 1))
                self.pp0 = 1 / ((1 / tt0) ** (g / (g - 1)))

            m = math.sqrt(((1 / tt0) - 1) * (2 / (g - 1)))
            self.mch = m
            if m >= 1:
                self.ma = math.degrees(math.asin(1 / m))
                p_mang1 = math.sqrt((g + 1) / (g - 1)) * \
                    math.degrees(math.atan(math.sqrt((g - 1) / (g + 1) * (m ** 2 - 1))))
                p_mang2 = math.degrees(math.atan(math.sqrt(m ** 2 - 1)))
                self.pma = p_mang1 - p_mang2
            else:
                self.ma = None
                self.pma = None

        elif z == PMang:
            self.pma = n
            m = 1
            if 0 < self.pma < 130.454076:  # 130.454076
                increment = 10000000
                while True:
                    temp1 = math.sqrt((g + 1) / (g - 1)) * math.degrees(
                        math.atan(math.sqrt((g - 1) / (g + 1) * (m ** 2 - 1))))
                    temp2 = math.degrees(math.atan(math.sqrt(m ** 2 - 1)))
                    temp = temp1 - temp2
                    if temp >= self.pma:
                        m = m - increment
                        increment = increment/10
                        if increment < 0.000001:
                            break
                    else:
                        m = m + increment
            else:
                self._error()
                self.msg = "Prandtl-Meyer Angle Must be Between 0 and 130.454076 Degrees"
                return

            self.mch = m
            self.ma = math.degrees(math.asin(1 / m))
            self.tt0 = 1 / (1 + ((g - 1) / 2) * m ** 2)
            self.pp0 = 1 / ((1 / tt0) ** (g / (g - 1)))
            self.rr0 = 1 / ((1 / tt0) ** (1 / (g - 1)))

        elif z == Asub or z == Asup:  # A/A* Greater than or equal to 1
            self.aast = n
            m = 1
            if n <= 1:
                self._error()
                self.msg = "A/A* Must be Greater than 1"
                return

            if z == Asub:
                while m >= 0.00002:
                    temp1 = 1 / (1 + ((g - 1) / 2) * m ** 2)
                    temp = (((g + 1) / 2) ** ((-1 * g - 1) / (g - 1) / 2)) / m * (1 / temp1) ** ((g + 1) / (g - 1) / 2)
                    if temp >= self.aast:
                        break
                    else:
                        m = m - 0.00001
            elif z == Asup:
                while True:
                    temp1 = 1 / (1 + ((g - 1) / 2) * m ** 2)
                    temp = (((g + 1) / 2) ** ((-1 * g - 1) / (g - 1) / 2)) / m * (1 / temp1) ** ((g + 1) / (g - 1) / 2)
                    if temp >= self.aast:
                        break
                    elif m >= 10:
                        break
                    else:
                        m = m + 0.00001

            if m >= 1:
                self.ma = math.degrees(math.asin(1 / m))
                p_mang1 = math.sqrt((g + 1) / (g - 1)) * \
                    math.degrees(math.atan(math.sqrt((g - 1) / (g + 1) * (m ** 2 - 1))))
                p_mang2 = math.degrees(math.atan(math.sqrt(m ** 2 - 1)))
                self.pma = p_mang1 - p_mang2
            else:
                self.ma = None
                self.pma = None
            self.mch = m
            self.tt0 = 1 / (1 + ((g - 1) / 2) * m ** 2)
            self.pp0 = 1 / ((1 / self.tt0) ** (g / (g - 1)))
            self.rr0 = 1 / ((1 / self.tt0) ** (1 / (g - 1)))

        self.ttst = 1 / ((1 / self.tt0) * (2 / (g + 1)))
        self.ppst = self.ttst ** (g / (g - 1))
        self.rrst = self.ttst ** (1 / (g - 1))
        self.aast = (((g + 1) / 2) ** ((-1 * g - 1) / (g - 1) / 2)) / m * (1 / self.tt0) ** ((g + 1) / (g - 1) / 2)


    def _error(self):
        self.mch = None
        self.tt0 = None
        self.pp0 = None
        self.rr0 = None
        self.aast = None
        self.ma = None
        self.pma = None

a = _Comp("A/A* (sub)",1,1.4)
a.fcn_comp()