import sys
import ast


def main():
    try:
        input, scaleFactor = [int(x) for x in sys.argv[1].split(',')], ast.literal_eval(sys.argv[2])

        scaled = scale(input, scaleFactor)
        sortedSales = sort(input)
        goodSales_ = goodSales(input)

        print(f'The scaled number is: {scaled}',
              f'The sorted sales numbers are: {sortedSales}',
              f'The good sales numbers are: {goodSales_}')
    except:
        print('value error')


def scale(li, x):
    scaled_list = [i * x for i in li]
    return scaled_list


def sort(li):
    return sorted(li, key=lambda x: x % 10)


def goodSales(li):
    avgSales = sum(li) / len(li)
    listRe = []
    for i in li:
        if i > avgSales:
            listRe.append(i)
    return listRe


main()