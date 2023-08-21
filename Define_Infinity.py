# What value will be defined for an infinity number?

# One of assume is define infinity as the large enough value:
INF = 99999

# Another assume to make sure that it is handled the maximum possible value,
# is the value of INF can be taken as a positive infinite integer value
# from the math module (as math.inf) or
# from NumPy module (as np.inf) or
# from the Decimal() function in the decimal module (as Decimal('Infinity')) or
# from the float() function (as float('inf'))
#

# importing math module
import math

# importing NumPy module:
# this library is designed to work efficiently with arrays in Python.
# It is fast, simple to learn, and efficient in storage.
'''
To install NumPy on PyCharm, click on File and go to the Settings.
Under Settings, choose your Python project and select Python Interpreter.
Then, search for the NumPy package and click Install Package.

'''
import numpy as np

# importing Decimal function from the decimal module
from decimal import Decimal
INF = math.inf


def check_number_isInfinite():
    # creating a positive infinite integer value:

    # using the float(inf) function
    f_infinity = float('inf')

    # using numpy.inf
    np_infinity = np.inf

    # using the Decimal() function from the decimal module
    d_infinity = Decimal('Infinity')

    # using math.inf
    np_infinity = math.inf

    # To determine whether a given number is infinite or not,
    # use the math library's isinf() method, which returns a boolean value.
    list_infinity = [f_infinity, np_infinity, d_infinity, np_infinity]

    for i in list_infinity:
        print(f'If {i} is infinite number?', math.isinf(i))


if __name__ == '__main__':
    check_number_isInfinite()