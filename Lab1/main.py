# OR OPERATOR
def or_test():
    exp1 = 1 == 10
    print(exp1)                         # FALSE
    exp2 = 10 > 1
    print(exp2)                         # TRUE
    print(exp1 or exp2)                 # OR will return exp2 since its true
    exp3 = 12 == 1
    print(exp1 or exp3, "\n")           # will return false cuz both are false

def print_exp():
    #print("Hello")                     # unterminated string literal, need either 'str' or "str"
    print('Let\'s GO')                  # required to put "\" for ' or will have errors
    print("Let's go")
    #print 'hello' is missing parenthesis
    print("Hello World\n")              # creates new line at the end of the str
    print("\nHello World")              # creates new line at the start of the str
    print("Hello\nWorld")               # creates new line inbetween "Hello" and "World"
    print(1, '\n', 2, '\n', 3)
    print('\n', 1, '\n', 2, '\n', 3)

def compute_exp():
    a = 1976 / 10       # 197.6
    b = 1976 // 10      # 197
    c = 1976 % 10       # 6
    d = 1976.0 / 10     # 197.6
    e = 1976.0 / 10.0   # 197.6
    f = 1976.0 // 10    # 197.0
    g = 1976 % 10       # 6
    h = 4 ** 3          # 64

    answers = [a, b, c, d, e, f, g, h]
    counter = 1
    for x in answers:
        print(counter ," : ", x)
        counter+=1

def type_conversions():
    a = int(5.7)        # 5
    b = int('5')        # 5
    # c = int('5.7')    # will have error
    d = float(5)        # 5.0
    e = float('5')      # 5.0
    f = float('5.7')    # 5.7
    
    answers = [a, b, d, e, f]
    counter = 1
    for x in answers:
        print(counter, ' : ', x)
        counter+=1

def logic_operations():
    print(True or False)        #Always will print true
    print(True or 0)            #Always will print true
    print(True or 1)            #Always will print true
    #print(true and False)      #py will think "true" is a variable
    print(True and True)        #Always will print true
    print(True and False)       #Always will print false
    print(True and 0)           #Always will print 0
    print(not True)             #Always will print false
    print(not False)            #Always will print true
    print(not 1)                #Always will print false
    print(not 0)                #Always will print true
    print(False and 1)          #Always will print false
    print(False or 1)           #Always will print 1
    #print(False or a = 1)      #Will have error, cannot assign to expression
    #print(False or (a = 0))    #Will have error, invalid syntax

def input_test():
    firstName = input("Input ur first name : ")
    age = int(input("Input ur age : "))
    age+=1
    print("Your name is :", firstName, ", and your age is :", age)

def salary():
    test = True
    while test:
        salary = input("What is ur salary : ")
        if salary.isnumeric():
            salary = int(salary)
            if salary < 1000:
                salary += 500
                test = False
            elif salary > 5000 and salary < 6000:
                salary -= 600
                test = False
            elif salary == 6000:
                pass
                test = False
            else:
                salary += 20
                test = False
        else:
            print("that is not a number")
    print(salary)



#or_test()
#print_exp()
#compute_exp()
#type_conversions()
#logic_operations()
#input_test()
salary()
