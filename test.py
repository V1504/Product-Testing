import math_util

import MyPack
from MyPack.calculator import add

#print(math_util.add(5,4))

from math_util import multi, PI
print(multi(3,2))
print(f"Value of PI: {PI}")

#impot with aliasing
import math_util as mu
print(mu.sub(10,4))