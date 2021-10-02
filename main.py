import math as math


class _Normal:
    def __init__(self, x=None):
        self.m1 = x
        self.m2 = x
        self.p02p01 = x
        self.p1p02 = x
        self.p2p1 = x
        self.r2r1 = x
        self.t2t1 = x
        self.msg = "None: All Values Converged"


def main():
    a = "m1"
    b = "m2"
    c = "p02/p01"
    e = "p2/p1"
    f = "rho2/rho1"
    h = "t2/t1"

    z = input("Enter input: ").lower()
    n = float(input("Enter Value: "))
    g = float(input("Enter Gamma Value: "))

    i = z == a or z == b or z == c or z == e or z == f or z == h  # or z == d
    j = g > 1
    if i and j:
        fcn(z, n, g)

    if _Normal.m1 is not None:
        print(f"\nM1: {_Normal.m1:8.8f} M2: {_Normal.m2:8.8f} p02/01: {_Normal.p02p01:8.8f}")
        print(f"p2/p1: {_Normal.p2p1:8.8f} rho2/rho1: {_Normal.r2r1:8.8f} T2/T1: {_Normal.t2t1:8.8f}")
    else:
        print(f"\nM1: {_Normal.m1} M2: {_Normal.m2} p02/01: {_Normal.p02p01}")
        print(f"p2/p1: {_Normal.p2p1} rho2/rho1: {_Normal.r2r1} T2/T1: {_Normal.t2t1}")


def fcn(z, n, g):
    # Find out how to Calculate p1/p02

    # This Function includes all possible outcomes given possible inputs.
    # Multiple nested while-loops that optimize backward calculation time to calculate M1 for each input (excluding M1)
    if z == 'm1':
        m = n
        _Normal.m1 = n
        _Normal.m2 = math.sqrt(((g-1)*m**2+2)/((2*g*m**2)-(g-1)))
        _Normal.p2p1 = (2*g*m**2-(g-1))/(g+1)
        _Normal.t2t1 = (2*g*m**2-(g-1))*((g-1)*m**2+2)/((g+1)**2*m**2)
        _Normal.p02p01 = ((((g+1)*m**2)/((g-1)*m**2+2))**(g/(g-1)))*(((g+1)/(2*g*m**2-(g-1)))**(1/(g-1)))
        _Normal.r2r1 = ((g+1)*m**2)/((g-1)*m**2+2)

    elif z == 'm2':
        _Normal.m2 = n
        m = 1
        while m > 0:  # Optimized nested while-loop to Calculate M1
            temp = math.sqrt(((g - 1) * m ** 2 + 2) / ((2 * g * m ** 2) - (g - 1)))
            if temp <= n:
                m = m - 100
                while m > 0:
                    temp = math.sqrt(((g - 1) * m ** 2 + 2) / ((2 * g * m ** 2) - (g - 1)))
                    if temp <= n:
                        m = m - 1
                        while m > 0:
                            temp = math.sqrt(((g - 1) * m ** 2 + 2) / ((2 * g * m ** 2) - (g - 1)))
                            if temp <= n:
                                m = m - 0.00001
                                break
                            else:
                                m = m + 0.00001
                        break
                    else:
                        m = m + 1
                break
            else:
                m = m + 100
        _Normal.m1 = m
        _Normal.p2p1 = (2*g*m**2-(g-1))/(g+1)
        _Normal.t2t1 = (2*g*m**2-(g-1))*((g-1)*m**2+2)/((g+1)**2*m**2)
        _Normal.p02p01 = ((((g+1)*m**2)/((g-1)*m**2+2))**(g/(g-1)))*(((g+1)/(2*g*m**2-(g-1)))**(1/(g-1)))
        _Normal.r2r1 = ((g+1)*m**2)/((g-1)*m**2+2)

    elif z == 'p2/p1':
        _Normal.p2p1 = n
        m = 1
        if n <= 10000000000:  # Optimized nested while-loop to Calculate M1
            while m > 0:
                temp = (2 * g * m ** 2 - (g - 1)) / (g + 1)
                if temp >= _Normal.p2p1:
                    m = m - 1
                    while m > 0:
                        temp = (2 * g * m ** 2 - (g - 1)) / (g + 1)
                        if temp >= _Normal.p2p1:
                            break
                        else:
                            m = m + 0.00001
                    break
                else:
                    m = m + 1
            _Normal.m1 = m
            _Normal.m2 = math.sqrt(((g-1)*m**2+2)/((2*g*m**2)-(g-1)))
            _Normal.t2t1 = (2*g*m**2-(g-1))*((g-1)*m**2+2)/((g+1)**2*m**2)
            _Normal.p02p01 = ((((g+1)*m**2)/((g-1)*m**2+2))**(g/(g-1)))*(((g+1)/(2*g*m**2-(g-1)))**(1/(g-1)))
            _Normal.r2r1 = ((g+1)*m**2)/((g-1)*m**2+2)
        else:
            _error()
            _Normal.msg = "p2/p1 Must be Between 1 and 10000000000"

    elif z == 'p02/p01':
        _Normal.p02p01 = n
        m = 1
        while m > 0:  # Optimized nested while-loop to Calculate M1
            temp = ((((g+1)*m**2)/((g-1)*m**2+2))**(g/(g-1)))*(((g+1)/(2*g*m**2-(g-1)))**(1/(g-1)))
            if temp <= _Normal.p02p01:
                m = m - 1
                while m > 0:
                    temp = ((((g + 1) * m ** 2) / ((g - 1) * m ** 2 + 2)) ** (g / (g - 1))) * (
                                ((g + 1) / (2 * g * m ** 2 - (g - 1))) ** (1 / (g - 1)))
                    if temp <= _Normal.p02p01:
                        break
                    else:
                        m = m + 0.00001
                break
            else:
                m = m + 1
        _Normal.m1 = m
        _Normal.m2 = math.sqrt(((g - 1) * m ** 2 + 2) / ((2 * g * m ** 2) - (g - 1)))
        _Normal.p2p1 = (2 * g * m ** 2 - (g - 1)) / (g + 1)
        _Normal.t2t1 = (2 * g * m ** 2 - (g - 1)) * ((g - 1) * m ** 2 + 2) / ((g + 1) ** 2 * m ** 2)
        _Normal.r2r1 = ((g + 1) * m ** 2) / ((g - 1) * m ** 2 + 2)

    elif z == 'rho2/rho1':
        _Normal.r2r1 = n
        m = 1
        if 1 <= n <= 6:
            if 1 <= n <= 5.9999999:  # Optimized nested while-loop to Calculate M1
                while m > 0:
                    temp = ((g + 1) * m ** 2) / ((g - 1) * m ** 2 + 2)
                    if temp >= n:
                        m = m - 100
                        while m > 0:
                            temp = ((g + 1) * m ** 2) / ((g - 1) * m ** 2 + 2)
                            if temp >= n:
                                m = m - 1
                                while m > 0:
                                    temp = ((g + 1) * m ** 2) / ((g - 1) * m ** 2 + 2)
                                    if temp >= n:
                                        break
                                    else:
                                        m = m + 0.00001
                                break
                            else:
                                m = m + 1
                        break
                    else:
                        m = m + 100
            elif 5.9999999 < n <= 6:  # Optimized nested while-loop to Calculate M1
                while m > 0:
                    temp = ((g + 1) * m ** 2) / ((g - 1) * m ** 2 + 2)
                    if temp >= n:
                        m = m - 10000
                        while m > 0:
                            temp = ((g + 1) * m ** 2) / ((g - 1) * m ** 2 + 2)
                            if temp >= n:
                                m = m - 1
                                while m > 0:
                                    temp = ((g + 1) * m ** 2) / ((g - 1) * m ** 2 + 2)
                                    if temp >= n:
                                        break
                                    else:
                                        m = m + 0.00001
                                break
                            else:
                                m = m + 1
                        break
                    else:
                        m = m + 10000
            _Normal.m1 = m
            _Normal.m2 = math.sqrt(((g-1)*m**2+2)/((2*g*m**2)-(g-1)))
            _Normal.p2p1 = (2 * g * m ** 2 - (g - 1)) / (g + 1)
            _Normal.t2t1 = (2 * g * m ** 2 - (g - 1)) * ((g - 1) * m ** 2 + 2) / ((g + 1) ** 2 * m ** 2)
            _Normal.p02p01 = ((((g+1)*m**2)/((g-1)*m**2+2))**(g/(g-1)))*(((g+1)/(2*g*m**2-(g-1)))**(1/(g-1)))
        else:
            _error()
            _Normal.msg = "rho2/rho1 Must be Between 1 and 6"

    elif z == 't2/t1':
        _Normal.t2t1 = n
        m = 1
        if 1 <= n <= 1000000000:
            while m is True:  # Optimized nested while-loop to Calculate M1
                temp = (2*g*m**2-(g-1))*((g-1)*m**2+2)/((g+1)**2*m**2)
                if temp >= n:
                    m = m - 1
                    while m is True:
                        temp = (2 * g * m ** 2 - (g - 1)) * ((g - 1) * m ** 2 + 2) / ((g + 1) ** 2 * m ** 2)
                        if temp >= n:
                            break
                        else:
                            m = m + 0.00001
                    break
                else:
                    m = m + 1
            _Normal.m1 = m
            _Normal.m2 = math.sqrt(((g - 1) * m ** 2 + 2) / ((2 * g * m ** 2) - (g - 1)))
            _Normal.p2p1 = (2 * g * m ** 2 - (g - 1)) / (g + 1)
            _Normal.p02p01 = ((((g+1)*m**2)/((g-1)*m**2+2))**(g/(g-1)))*(((g+1)/(2*g*m**2-(g-1)))**(1/(g-1)))
            _Normal.r2r1 = ((g+1)*m**2)/((g-1)*m**2+2)
        else:
            _error()
            _Normal.msg = "T2/T1 Must be Between 1 and 1000000000"
    # notation()


# def notation():
#     a = "m1"
#     b = "m2"
#     c = "p02/p01"
#     d = "p1/p02"
#     e = "p2/p1"
#     f = "rho2/rho1"
#     h = "t2/t1"
#     _aprn = "{.8f}".format(_Normal.m1)
#     _bprn = "{.8f}".format(_Normal.m2)
#     _cprn = "{.8f}".format(_Normal.p02p01)
#     _eprn = "{.8f}".format(_Normal.p2p1)
#     _fprn = "{.8f}".format(_Normal.r2r1)
#     _hprn = "{.8f}".format(_Normal.t2t1)
#
#     if _Normal.m1 >= 1e6:
#         _aprn = "{:5e}".format(_Normal.m1)
#     if _Normal.m2 >= 1e6:
#         _bprn = "{:5e}".format(_Normal.m2)
#     if _Normal.p02p01 >= 1e6:
#         _cprn = "{:5e}".format(_Normal.p02p01)
#     if _Normal.p2p1 >= 1e6:
#         _eprn = "{:5e}".format(_Normal.p2p1)
#     if _Normal.r2r1 >= 1e6:
#         _fprn = "{:5e}".format(_Normal.r2r1)
#     if _Normal.t2t1 >= 1e6:
#         _hprn = "{:5e}".format(_Normal.t2t1)

def _error():
    _Normal.m1 = None
    _Normal.m2 = None
    _Normal.p02p01 = None
    _Normal.p1p02 = None
    _Normal.p2p1 = None
    _Normal.r2r1 = None
    _Normal.t2t1 = None


if __name__ == '__main__':
    main()
