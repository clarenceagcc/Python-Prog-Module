import math

def add(x, y):
    return x + y

def subtraction(x, y):
    return x - y

def evenNum(x):
    evenNum = ([no for no in x if no % 2 == 0])
    return len(evenNum)

def maximum(x):
    return max(x)

def minimum(x):
    return min(x)

def absolute(x):
    return abs(x)

def sumTotal(x):
    return sum(x)

def clear(x):
    if min(x) < 5:
        for i in range(len(x)):
            x[i] = 0
    else: 
        pass
    return x