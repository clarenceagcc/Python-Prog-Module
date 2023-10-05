import sys


def elfish(str):
    elfish_words = 'elf'
    count = 0
    for i in elfish_words:
        if i in str.lower():
            count += 1

    if count == len(elfish_words):
        return f'{str} is one elfish word!'
    else:
        return f'{str} is not an elfish word!'

print(elfish(sys.argv[1]))