import sys
import math

def calc_main():
    no = sys.argv[1] # numbers
    try:
        noList = [int(x) for x in no.split(',')]
        evenNos = [no for no in noList if no % 2 == 0]
        oddNos = [num for num in noList if num % 2 == 1]
        calc_(evenNos, oddNos, noList)
    except ValueError:
        print('Please enter valid integers.')

def calc_(evenNos, oddNos, noList):
    
    diffLi = sorted(noList)
    evenNoSum = 0
    oddNoSum = 0
    difference = (diffLi[len(diffLi)-1] - diffLi[0])
    centered_avg = (sum(noList) - max(noList) - min(noList)) / (len(noList) - 2)
    #even calc
    for x in range(0,len(evenNos)):
        evenNoSum += evenNos[x]
    #odd calc
    for x in range(0,len(oddNos)):
        oddNoSum += oddNos[x]

    print(f'The sum of all even numbers is {evenNoSum}, '
            f'the sum of all odd numbers is {oddNoSum}, '
            f'the difference between the biggest and smallest number is {difference}, ' 
            f'the total number of even numbers is {len(evenNos)}, '
            f'the total number of odd numbers is {len(oddNos)}, '
            f'the centered average is {int(centered_avg)}. ')

calc_main()