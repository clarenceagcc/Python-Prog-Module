import sys


def elfish(str):
    elfish_words = 'elf'

    if elfish_words in str.lower():
        return f'{str} is one elfish word!'
    else:
        return f'{str} is not an elfish word!'
    

print(elfish(sys.argv[1]))