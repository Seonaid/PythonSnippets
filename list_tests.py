import timeit

def test1():
    l = []
    for i in range(1000):
        l = l+[i]

def test2():
    l = []
    for i in range(1000):
        l.append(i)

def test3():
    l  = [i for i in range(1000)]

def test4():
    l = list(range(1000))

t1 = timeit.Timer("test1()", "from __main__ import test1")
print("concatenation: " + str(t1.timeit(number=1000)) + " milliseconds")

t2 = timeit.Timer("test2()", "from __main__ import test2")
print("append: " + str(t2.timeit(number=1000)) + " milliseconds")

t3 = timeit.Timer("test3()", "from __main__ import test3")
print("comprehension: " + str(t3.timeit(number=1000)) + " milliseconds")

t4 = timeit.Timer("test4()", "from __main__ import test4")
print("list_constructor: " + str(t4.timeit(number=1000)) + " milliseconds")