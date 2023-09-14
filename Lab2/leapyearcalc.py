import sys

def leap_year_main():
    start = sys.argv[1]
    end = sys.argv[2]

    yearli = list(range(int(start), int(end)+1))
    leapyears = ''
    counter = 0
    for x in yearli:
        if (x % 4 == 0) and (x % 100 != 0) or (x % 400 == 0):
            counter += 1
            leapyears += f'{x}, '
    print(f'The number of Leap Years is {counter}, the Leap Years are {leapyears}'[:-2])


leap_year_main()