import sys

n = [sys.argv[x] for x in range(1, len(sys.argv))]
try:
    if len(n) == 3:
        avg = ((float(n[0]) + float(n[1]) + float(n[2])) / 3)
        print(f"average : {avg:.2f}")
    else:
        print("invalid input, input 3 numbers")
except ValueError:
    print("invalid input, only use numbers")