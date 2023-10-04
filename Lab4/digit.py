import sys


def digit(x):
    if x < 10:
        return 1
    else:
        return 1 + digit(x / 10)
    

def digit_iterative(x):
    count = 1
    while x > 10:
        x = x / 10
        count += 1
    return count
try:
    print(f'The number of digit(s) calculated by recursive is {digit(int(sys.argv[1]))} and by iterative is {digit_iterative(int(sys.argv[1]))}')
except:
    print('Invalid input')