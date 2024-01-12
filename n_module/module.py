import calc_add
# import calc.calc_sub
# import calc.calc_sub as sub
from calc.calc_sub import sub
from calc.calc import *

import os
import sys

print(sys.path)
print(os.path.abspath(os.path.dirname(__file__)))
# print(sys.path.append(os.path.abspath(os.path.dirname(__file__))))

# if __name__ == '__main__':
#     print(calc_add.add(2, 4))
#     # print(calc.calc_sub.sub(10, 5))
#     # print(sub.sub(10, 4))
#     print(sub(5, 1))
#
#     c = Calculator(10, 5)
#     print(c.add())
#     print(c.sub())
