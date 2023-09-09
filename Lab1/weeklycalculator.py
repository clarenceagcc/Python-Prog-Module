import sys


def weekly_calculator_main():
    n = len(sys.argv)
    if n == 4:
        workinghrs = sys.argv[1]
        normrate = sys.argv[2]
        overrate = sys.argv[3]
        if (workinghrs.isdigit() and normrate.isdigit() and overrate.isdigit()) and int(workinghrs) < 168:
            if int(workinghrs) > 40:
                calculator(workinghrs, normrate, overrate, True)
            else:
                calculator(workinghrs, normrate, overrate, False)
        else:
            print('invalid input!')
    else:
        print("invalid input!")


def calculator(workhrs, normrate, overrate, if_overtime):
    if if_overtime:
        overtimehrs = int(workhrs) - 40
        extrasal = int(overrate) * int(overtimehrs)
        normsal = int(normrate) * 40
        total = int(normsal) + int(extrasal)
        print(f"Normal Salary:{normsal:.2f}, Extra Salary:{extrasal:.2f}, Total Salary:{total:.2f}")
    else:
        normsal = int(workhrs) * int(normrate)
        print(f"Normal Salary:{normsal:.2f}, Extra Salary:0.0, Total Salary:{normsal:2f}")


weekly_calculator_main()