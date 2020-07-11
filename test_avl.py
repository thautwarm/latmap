from pyximport import install
from random import shuffle
install()

import avl

avl_t = avl.AVLTree()
xs = list(range(100))
shuffle(xs)

for i in xs:
    avl_t[i] = i
