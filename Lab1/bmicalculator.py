import sys


def bmi_calc_main():
    try:
        if len(sys.argv) == 4:
            metric = sys.argv[1]
            height = sys.argv[2]
            weight = sys.argv[3]
            if metric.lower() in ('metric', 'imperial'):
                if metric.lower() == 'metric':
                    bmi = bmi_calculator(height, weight, True)
                else:
                    bmi = bmi_calculator(height, weight, False)
                bmi_cat = bmi_table(bmi)
                print(f"{bmi:.2f}\t{bmi_cat}")
            else:
                print("Your input is invalid!")
        else:
            print("Your input is invalid!")
    except ValueError:
        print("Your input is invalid!")


def bmi_calculator(height, weight, ismetric):
    if ismetric:
        bmi = float(weight)/pow(float(height), 2)
    else:
        bmi = 703*float(weight)/pow(float(height), 2)
    return bmi


def bmi_table(bmi):
    if bmi < 16:
        bmi_cat = 'Severe Thinness'
    elif bmi < 17:
        bmi_cat = 'Moderate Thinness'
    elif bmi < 18.5:
        bmi_cat = 'Mild Thinness'
    elif bmi < 25:
        bmi_cat = 'Normal'
    elif bmi < 30:
        bmi_cat = 'Overweight'
    elif bmi < 35:
        bmi_cat = 'Obese Class I'
    elif bmi < 40:
        bmi_cat = 'Obese Class II'
    else:
        bmi_cat = 'Obese Class III'
    return bmi_cat

bmi_calc_main()



