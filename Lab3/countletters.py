import sys


def count_letters_main():
    str_ = sys.argv[1].replace(',','')
    #   'Firefox,is,having,trouble,recovering,your,windows,and,tabs'
    strCount = letter_count(str_)
    outputstr = ''

    for key, value in strCount.items():
        outputstr += f'{key}:{value} '
    
    print(outputstr)


def letter_count(x):
    strCount = {}

    for i in sorted(x, reverse=True):
        if i in strCount:
            strCount[i] += 1
        else:
            strCount[i] = 1

    return strCount

def double_count(x, y):
    finStr = x+y
    strCount = {}

    for i in sorted(finStr, reverse=True):
        if i in strCount:
            strCount[i] += 1
        else:
            strCount[i] = 1

    return print(strCount)

def various_count(*x):
    finStr = ''
    strCount = {}
    
    for lt in x:
        finStr += lt

    for i in sorted(finStr, reverse=True):
        if i in strCount:
            strCount[i] += 1
        else:
            strCount[i] = 1

    return print(strCount)


count_letters_main()