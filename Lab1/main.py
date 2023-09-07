# OR OPERATOR
def ortest():
    exp1 = 1 == 10
    print(exp1) # FALSE
    exp2 = 10 > 1
    print(exp2) # TRUE
    print(exp1 or exp2) # OR will return exp2 since its true
    exp3 = 12 == 1
    print(exp1 or exp3, "\n") # will return false cuz both are false

def printexp():
    # print("Hello") # unterminated string literal, need either 'str' or "str"
    print('Let\'s GO') # required to put "\" for ' or will have errors
    print("Let's go")
    # print 'hello' is missing parenthesis
    print("Hello World\n") # creates new line at the end of the str
    print("\nHello World") # creates new line at the start of the str
    print("Hello\nWorld") # creates new line inbetween "Hello" and "World"
    print(1, '\n', 2, '\n', 3)
    print('\n', 1, '\n', 2, '\n', 3)

def computetxp():
    a = 1976 / 10
    b = 1976 // 10
    c = 1976 % 10
    d = 1976.0 / 10
    e = 1976.0 / 10.0
    f = 1976.0 // 10
    g = 1976 % 10
    h = 4 ** 3

    answers = [a, b, c, d, e, f, g, h]
    for 


ortest()
printexp()