import myMath
import sys

def math_main():
    num = str.split((sys.argv[1]), ',')
    numList = [int(x) for x in num]
    
    maxNo = myMath.maximum(numList)
    minNo = myMath.minimum(numList)

    print(f'The difference is:{myMath.subtraction(maxNo, minNo)} '
          f'The summation is:{myMath.add(maxNo, minNo)} '
          f'The summation of all input is:{myMath.sumTotal(numList)} '
          f'The number of even numbers is:{myMath.evenNum(numList)} '
          f'The values in the list are: {myMath.clear(numList)}')

math_main()