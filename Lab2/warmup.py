import operator


def qn1():
    print('LIST')
    List1 = ['abc', 'bcd', ['123', 567], 789]
    print(List1[1])     #bcd
    print(List1[2])     #'123', 567
    print(List1[2][1]) # out of range
    #print(List1[4])    # out of range
    print(List1[-3])    #bcd
    print(List1[2:])    #['123', 567], 789

    print('\nTUPLE')
    Tuple1 = ('23', 15, 8, 100)
    print(Tuple1[0])        # 23
    print(Tuple1[1:])       # 15, 8, 100
    print(Tuple1[:2])       # '23', 15
    #print(Tuple1[2]=23)    # does not allow for item assignment

    print('\nDICTIONARY & RANGE')
    Dic={'A01':'xiaoming', 'A02':['mie', 3]}
    print(Dic['A01'])       # xiaoming
    print(Dic['A02'])       # 'mie', 3
    print(Dic['A02'][0])    # mie
    print(range(10))        # range(0, 10)
    print(range(2,10,2))    # range(2, 10, 2) # start 2, end 10, step 2

    print('\nStrings')
    h_letters = [letter for letter in 'human']
    print(h_letters)        # 'h', 'u', 'n', 'a', 'n'
    number_list = [x for x in range(20) if x % 2 == 0]
    print(number_list)      # 2, 4, 6, 8, 10 .....
    num_list = [y for y in range(100) if y % 2 == 0 if y % 5 == 0]
    print(num_list)         # 0, 10, 20, 30 .....
    obj = ['Even' if i % 2 == 0 else 'Odd' for i in range(10)]
    print(obj)              # 'Even', 'Odd', 'Even', 'Odd' .....

qn1()


def tuples_and_lists():
    fruits_li = ['pear', 'apple', 'strawberry', 'banana', 'orange']
    fruits_tup = ('pear', 'apple', 'strawberry', 'banana', 'orange')

    print(f'LIST : {fruits_li}, TUPLE : {fruits_tup}')

    fruits_li[1] = 'papaya'     # updating item in list

    x = list(fruits_tup)        # update items in tuple, requires to convert to list first
    x[1] = 'papaya'
    fruits_tup = tuple(x)

    print(f'LIST : {fruits_li}, TUPLE : {fruits_tup}')  # show update list and tuples

    fruits_li.pop(0)            # delete item in list

    x = list(fruits_tup)        # delete item in tuple, requires to convert to list first
    x.pop(0)
    fruits_tup = tuple(x)

    print(f'LIST : {fruits_li}, TUPLE : {fruits_tup}') # show update list and tuples

    for x in sorted(fruits_li):
        print('FRUITS LIST : ', x)
    
    counter = 0
    while counter < len(fruits_tup):
        print('FRUITS TUPLE : ', sorted(fruits_tup)[counter])
        counter += 1 


def list_comprehensions():
    number_list = [x for x in range(1000) if x % 7 == 0]
    no_with3 = [n for n in range(1000) if '3' in str(n)]
    test_str = 'H ello  guise '     # 4 spaces
    space_count = test_str.count(' ')

def month():
    year={'January': 31, 'Febuary': 28, 'March': 31,
          'May': 30, 'April': 31, 'June': 30,
          'July': 31, 'August': 31, 'September': 30,
          'October': 31, 'November': 30, 'December': 31,}


    for x in year:
        print(f'Month : {x}, No of Days : {year[x]}')


def file_reading():
    with open('Lab2/Lab2_testData.txt') as f:
        contents = f.read()

    li = contents.split(',')
    li1 = []
    li2 = []
    for i in li:
        if i not in li1:
            li1.append(i)#appending unique characters of string
            li2.append(operator.countOf(li,i))
    print(str_maker(li1,li2)[:-1])

    with open('Lab2/top5.txt', 'w') as f:
        f.write(str_maker(li1,li2)[:-1])


def str_maker(li1,li2):
    li_top_out = ''
    li_top = sorted(range(len(li2)), key=lambda i: li2[i], reverse=True)[:5]
    for x in li_top:
        li_top_out += f'{li1[x]}:{li2[x]},'

    return li_top_out


file_reading()