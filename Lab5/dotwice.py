import sys

def main():
    try:
        input, option = int(sys.argv[1]), int(sys.argv[2])
        if len(sys.argv) > 3 or (option > 3 or option < 1):
            print('It cannot be supported')
        else:
            match option:
                case 1:
                    output = double(double(input))
                case 2:
                    output = square(square(input))
                case 3:
                    output = cube(cube(input))

            print(output)
    except:
        print('It cannot be supported')


def double(x):
    return x * 2


def square(x):
    return x ** 2


def cube(x):
    return x ** 3


main()