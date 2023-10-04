import sys


def sum_recursive(x):
    if x == 1:
        return 1
    else:
        return sum_recursive(x-1) + x
    

def sum_iterative(x):
    sumno = 0
    for i in range(1, x+1):
        sumno += i

    return sumno


try:
    print(f'The SUM value calculated by recursive is {sum_recursive(int(sys.argv[1]))} and by iterative is {sum_iterative(int(sys.argv[1]))}')
except:
    print("Your input is invalid!")