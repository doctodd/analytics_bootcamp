import math
import numpy as np
from sqrt import *

def test_sqrt():
    def check(n):
        assert np.isclose(sqrt(n), math.sqrt(n))

    check(125348)
    check(89.2342)
    check(100)
    check(1)
    #check(0)


test_sqrt()