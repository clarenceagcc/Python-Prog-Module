def division(a, b):
    return a / b

# QN 2
li = ['ass', 'bruh', 'cla']

def listprintout(li_):
    print(li_)

# QN 3
def print_max(a, b):
    if a > b:
        print(a, 'is maximum')
    elif a == b:
        print(a, 'is equal to', b)
    else:
        print(b, 'is maximum')


# QN 4
def say(message, times=2):
    print(message * times)


# QN 5
def func(a, b=5, c=10):
    print('a is', a, 'and b is', b, 'and c is', c)


# QN 6
def func_(a, b, names):
    a = a+10
    b = b+20
    names[0] = 12
    names[1] = 18
    return a,b
x,y=10,30
fruits=['apple', 'orange', 'banana']
num1, num2=func_(x,y,fruits)

# QN 7
def leap_year_main():
    non_lyear = 2029
    lyear = 2000
    print(leap_year_calc(non_lyear))
    print(leap_year_calc(lyear))


def leap_year_calc(year):
    if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False
    

# QN 8
def func8(x):
    return x+5


def print_welcome():
    return 'Welcome:'


def messager(func, str1): 
    print(func, str1)   # change func() to func to it will point the the 
                        # argument in the function


# QN 9
def increment(x):
    return x + 100


def double(x):
    return x * 2


def get_bonus(func, salary):
    bonus = 1000
    if func(salary) > 5000:
        return func(salary)+bonus*2
    else:
        return func(salary)+bonus
    




# QN 1
print(division(2, 4))
# QN 2
listprintout(li)
# QN 3
print_max(3, 4)
print_max(3, 3)
print_max(4, 4)
#print_max(3)           # Error
#print_max(3, 4, 5)     # Error because the function only has 2 positional arguments
print_max('charlie', 'hello') 
# QN 4
say('Hello')            # HelloHello
say('Hello', 5)         # HelloHelloHelloHelloHello
# QN 5
func(3, 7)              # a is 3 and b is 7 and c is 10
func(25, c = 24)        # a is 25 and b is 5 and c is 24
func(c = 50, a = 100)   #a is 100 and b is 5 and c is 50
# QN 6
print(num1, num2)
for fruit in fruits:
    print(fruit)
# QN 7
leap_year_main()
# QN 8
print(func8(20))
print(sorted([100,-800,400,-200,50])) # Remove 'abs' because sorted() only takes in 1 positional argument
messager(print_welcome(), 'Python')
# QN 9
print (get_bonus(increment, 3000))
print (get_bonus(double, 3000))
print (get_bonus(increment, 6000))
print (get_bonus(double, 6000))