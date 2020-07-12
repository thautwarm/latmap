from pyximport import install
from random import shuffle
from sortedcontainers import SortedDict
from collections import OrderedDict
install()

import avl

# N = 10000
# avl_t = avl.AVLTree()
# xs = list(range(N))
# shuffle(xs)

# for v, i in enumerate(xs):
#     avl_t[i] = v

# print(sorted(avl_t[i].key for i in xs) == list(range(N)))
# print(sorted(avl_t[i].value for i in xs) == list(range(N)))

# for i in xs:
#     del avl_t[i]

# for i in xs:
#     assert avl_t[i] is None, (avl_t[i].key, avl_t[i].value)

# print(True)

# avl_t[1] = 3
# avl_t[2] = 10

# avl_t[10] = 10

# for i in xs:
#     avl_t[i] = i

# for i in xs:
#     avl_t[i].key

# print([i.key for i in avl_t] == sorted(xs))
    
# from timeit import timeit

# xs = list(range(100))
# d = avl.AVLTree()

# dd = SortedDict()

# for v, i in enumerate(xs):
#     d[i] = v
#     dd[i] = v

# def test():
#     for i in xs:
#         d[i]

# print(timeit("test()", globals=dict(test=test), number=1000))
# d = dd
# print(timeit("test()", globals=dict(test=test), number=1000))
    

# for i in avl_t.since(500):
#     i.key += 1


# for each in avl_t:
#     assert avl_t[each.key] is each

# for i in avl_t.since_bisect(N):
#     print(i.key, 'should be unique')

# print('ok')

# intervals = avl.AVLTree()
# xs = list(range(10000))
# for each in xs:
#     intervals[each] = each

# from random import shuffle
# shuffle(xs)
# for i, each in enumerate(intervals):
#     each.key = xs[i]

# intervals.rebalance()

# print(sorted([each.key for each in intervals]) == sorted(xs))


intervals = avl.OrthogonalIntervals()

intervals.insert(0, 13, False)
intervals.insert(13, 14, True)
intervals.insert(14, 50, False)
print(intervals.affect_edit(13, 0, 2))

print(list(intervals))


intervals = avl.OrthogonalIntervals()

intervals.insert(0, 17, True)
intervals.insert(17, 33, True)
intervals.insert(33, 36, False)
print(intervals.affect_edit(15, 0, 2))

print(list(intervals))
# print(intervals.affect_delete(13, 11))
# print([node.key for node in intervals])
## <>

# z = avl.Point(0)
# print(z < avl.Interval(0, 0), z < avl.Interval(0, 0))

# start, end = intervals.affect_insert(0, 5)

# for each in intervals:
#     print(each.value)


# print('after insert')
# intervals.insert(start, end, None)
# for each in intervals:
#     print(each.key)

# start, end = intervals.affect_edit(1, 3, 6)
# print('after delete&insert')
# for each in intervals:
#     print(each.key)

# print('after insert')
# intervals.insert(start, end, None)
# for each in intervals:
#     print(each.key)

# print('oo')