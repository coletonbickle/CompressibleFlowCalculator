import math as math


class _Normal:
    def __init__(self, z, n, g, x=None):
        self.z = z
        self.n = n
        self.g = g
        self.m1 = x
        self.m2 = x
        self.p02p01 = x
        self.p1p02 = x
        self.p2p1 = x
        self.r2r1 = x
        self.t2t1 = x
        self.msg = "None: All Values Converged"

    def fcn_normal(self):
        # This Function includes all possible outcomes given possible inputs.
        # Multiple while-loops that optimize backward calculation time to calculate M1 for each input (excluding M1)
        g = self.g
        n = self.n
        z = self.z.lower()
        if z == 'm1':
            m = self.n
            self.m1 = self.n
            self.m2 = math.sqrt(((g - 1) * m ** 2 + 2) / ((2 * g * m ** 2) - (g - 1)))
            self.p2p1 = (2 * g * m ** 2 - (g - 1)) / (g + 1)
            self.t2t1 = (2 * g * m ** 2 - (g - 1)) * ((g - 1) * m ** 2 + 2) / ((g + 1) ** 2 * m ** 2)
            self.p02p01 = ((((g + 1) * m ** 2) / ((g - 1) * m ** 2 + 2)) ** (g / (g - 1))) * (
                        ((g + 1) / (2 * g * m ** 2 - (g - 1))) ** (1 / (g - 1)))
            self.r2r1 = ((g + 1) * m ** 2) / ((g - 1) * m ** 2 + 2)
            self.p1p02 = (1 + (g-1)/2*m**2)**(-g/(g-1))/self.p02p01

        elif z == 'm2':
            self.m2 = n
            m = 1
            increment = 100
            if 0.3779644739999999 < n < 1:
                while m > 0:  # Optimized while-loop to Calculate M1
                    temp = math.sqrt(((g - 1) * m ** 2 + 2) / ((2 * g * m ** 2) - (g - 1)))
                    if temp <= n:
                        m = m - increment
                        increment = increment / 10
                        if increment < 0.000001:
                            break
                    else:
                        m = m + increment
                self.m1 = m
                self.p2p1 = (2 * g * m ** 2 - (g - 1)) / (g + 1)
                self.t2t1 = (2 * g * m ** 2 - (g - 1)) * ((g - 1) * m ** 2 + 2) / ((g + 1) ** 2 * m ** 2)
                self.p02p01 = ((((g + 1) * m ** 2) / ((g - 1) * m ** 2 + 2)) ** (g / (g - 1))) * (
                            ((g + 1) / (2 * g * m ** 2 - (g - 1))) ** (1 / (g - 1)))
                self.r2r1 = ((g + 1) * m ** 2) / ((g - 1) * m ** 2 + 2)
                self.p1p02 = (1 + (g - 1) / 2 * m ** 2) ** (-g / (g - 1)) / self.p02p01
            else:
                self._error()
                self.msg = 'M2 Must be Between 0.377964474 and 1'

        elif z == 'p2/p1':
            self.p2p1 = n
            m = 1
            increment = 100
            if n <= 10000000000:
                while m > 0:  # Optimized while-loop to Calculate M1
                    temp = (2 * g * m ** 2 - (g - 1)) / (g + 1)
                    if temp >= n:
                        m = m - increment
                        increment = increment / 10
                        if increment < 0.000001:
                            break
                    else:
                        m = m + increment
                self.m1 = m
                self.m2 = math.sqrt(((g - 1) * m ** 2 + 2) / ((2 * g * m ** 2) - (g - 1)))
                self.t2t1 = (2 * g * m ** 2 - (g - 1)) * ((g - 1) * m ** 2 + 2) / ((g + 1) ** 2 * m ** 2)
                self.p02p01 = ((((g + 1) * m ** 2) / ((g - 1) * m ** 2 + 2)) ** (g / (g - 1))) * (
                            ((g + 1) / (2 * g * m ** 2 - (g - 1))) ** (1 / (g - 1)))
                self.r2r1 = ((g + 1) * m ** 2) / ((g - 1) * m ** 2 + 2)
                self.p1p02 = (1 + (g - 1) / 2 * m ** 2) ** (-g / (g - 1)) / self.p02p01
            else:
                self._error()
                self.msg = "p2/p1 Must be Between 1 and 10000000000"

        elif z == 'p02/p01':
            self.p02p01 = n
            m = 1
            increment = 10
            if 0 < n < 1:
                while m > 0:  # Optimized while-loop to Calculate M1
                    temp = ((((g + 1) * m ** 2) / ((g - 1) * m ** 2 + 2)) ** (g / (g - 1))) * (
                                ((g + 1) / (2 * g * m ** 2 - (g - 1))) ** (1 / (g - 1)))
                    if temp <= n:
                        m = m - increment
                        increment = increment / 10
                        if increment < 0.000001:
                            break
                    else:
                        m = m + increment
                self.m1 = m
                self.m2 = math.sqrt(((g - 1) * m ** 2 + 2) / ((2 * g * m ** 2) - (g - 1)))
                self.p2p1 = (2 * g * m ** 2 - (g - 1)) / (g + 1)
                self.t2t1 = (2 * g * m ** 2 - (g - 1)) * ((g - 1) * m ** 2 + 2) / ((g + 1) ** 2 * m ** 2)
                self.r2r1 = ((g + 1) * m ** 2) / ((g - 1) * m ** 2 + 2)
                self.p1p02 = (1 + (g - 1) / 2 * m ** 2) ** (-g / (g - 1)) / self.p02p01
            else:
                self._error()
                self.msg = "p02/p01 Must be Between 0 and 1"

        elif z == 'p1/p02':
            self.p1p02 = n
            m = 1
            increment = 10000
            if 0 < n < 0.52828178:
                while m > 0: # Optimized while-loop to Calculate M1
                    temp1 = ((((g + 1) * m ** 2) / ((g - 1) * m ** 2 + 2)) ** (g / (g - 1))) * (
                                             ((g + 1) / (2 * g * m ** 2 - (g - 1))) ** (1 / (g - 1)))
                    temp = (1 + (g - 1) / 2 * m ** 2) ** (-g / (g - 1)) / temp1
                    if temp <= n:
                        m = m - increment
                        increment = increment/10
                        if increment < 0.000001:
                            break
                    else:
                        m = m + increment
                self.m1 = m
                self.m2 = math.sqrt(((g - 1) * m ** 2 + 2) / ((2 * g * m ** 2) - (g - 1)))
                self.p2p1 = (2 * g * m ** 2 - (g - 1)) / (g + 1)
                self.t2t1 = (2 * g * m ** 2 - (g - 1)) * ((g - 1) * m ** 2 + 2) / ((g + 1) ** 2 * m ** 2)
                self.p02p01 = ((((g + 1) * m ** 2) / ((g - 1) * m ** 2 + 2)) ** (g / (g - 1))) * (
                        ((g + 1) / (2 * g * m ** 2 - (g - 1))) ** (1 / (g - 1)))
                self.r2r1 = ((g + 1) * m ** 2) / ((g - 1) * m ** 2 + 2)
            else:
                self._error()
                self.msg = "p1/p02 Must be Between 0 and 0.52828178"

        elif z == 'rho2/rho1':
            self.r2r1 = n
            m = 1
            increment = 100000
            if 1 <= n <= 6:
                while m > 0:  # Optimized while-loop to Calculate M1
                    temp = ((g + 1) * m ** 2) / ((g - 1) * m ** 2 + 2)
                    if temp >= n:
                        m = m - increment
                        increment = increment / 10
                        if increment < 0.000001:
                            break
                    else:
                        m = m + increment
                self.m1 = m
                self.m2 = math.sqrt(((g - 1) * m ** 2 + 2) / ((2 * g * m ** 2) - (g - 1)))
                self.p2p1 = (2 * g * m ** 2 - (g - 1)) / (g + 1)
                self.t2t1 = (2 * g * m ** 2 - (g - 1)) * ((g - 1) * m ** 2 + 2) / ((g + 1) ** 2 * m ** 2)
                self.p02p01 = ((((g + 1) * m ** 2) / ((g - 1) * m ** 2 + 2)) ** (g / (g - 1))) * (
                            ((g + 1) / (2 * g * m ** 2 - (g - 1))) ** (1 / (g - 1)))
                self.p1p02 = (1 + (g - 1) / 2 * m ** 2) ** (-g / (g - 1)) / self.p02p01
            else:
                self._error()
                self.msg = "rho2/rho1 Must be Between 1 and 6"

        elif z == 't2/t1':
            self.t2t1 = n
            m = 1
            increment = 1000
            if 1 <= n <= 1000000000:
                while m > 0:  # Optimized while-loop to Calculate M1
                    temp = (2 * g * m ** 2 - (g - 1)) * ((g - 1) * m ** 2 + 2) / ((g + 1) ** 2 * m ** 2)
                    if temp >= n:
                        m = m - increment
                        increment = increment / 10
                        if increment < 0.000001:
                            break
                    else:
                        m = m + increment
                self.m1 = m
                self.m2 = math.sqrt(((g - 1) * m ** 2 + 2) / ((2 * g * m ** 2) - (g - 1)))
                self.p2p1 = (2 * g * m ** 2 - (g - 1)) / (g + 1)
                self.p02p01 = ((((g + 1) * m ** 2) / ((g - 1) * m ** 2 + 2)) ** (g / (g - 1))) * (
                            ((g + 1) / (2 * g * m ** 2 - (g - 1))) ** (1 / (g - 1)))
                self.r2r1 = ((g + 1) * m ** 2) / ((g - 1) * m ** 2 + 2)
                self.p1p02 = (1 + (g - 1) / 2 * m ** 2) ** (-g / (g - 1)) / self.p02p01
            else:
                self._error()
                self.msg = "T2/T1 Must be Between 1 and 1000000000"
        return self

    def _error(self):
        self.m1 = None
        self.m2 = None
        self.p02p01 = None
        self.p1p02 = None
        self.p2p1 = None
        self.r2r1 = None
        self.t2t1 = None
