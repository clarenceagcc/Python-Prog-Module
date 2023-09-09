import sys

def ave_calculator():
    n = [sys.argv[x] for x in range(1, len(sys.argv))]
    try:
        if len(n) == 3:
            avg = ((float(n[0]) + float(n[1]) + float(n[2])) / 3)
            print(f"average : {avg:.2f}")
        else:
            print("invalid input, input 3 numbers")
    except ValueError:
        print("invalid input, only use numbers")


def ave_calculatorv2():
    n = len(sys.argv)
    if n == 4:
        a = sys.argv[1]
        b = sys.argv[2]
        c = sys.argv[3]
        if a.isdigit() and b.isdigit() and c.isdigit():
            avg = ((float(a) + float(b) + float(c)) / 3)
            print(f"average : {avg:.2f}")
        else:
            print('invalid input, input 3 numbers')
    else:
        print("invalid input, input 3 numbers")


ave_calculatorv2()
