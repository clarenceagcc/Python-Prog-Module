import sys
import operator


def pop_char_main():
    strText = sys.argv[1] #whole str text
    strText = sorted(strText.lower())
    li1 = []
    li2 = []
    for i in strText:
        if i not in li1:
            li1.append(i)#appending unique characters of string
            li2.append(operator.countOf(strText,i))
    print(str_maker(li1,li2)[:-1])


def str_maker(li1,li2):
    li_top_out = ''
    li_top = sorted(range(len(li2)), key=lambda i: li2[i], reverse=True)[:5]
    for x in li_top:
        li_top_out += f'{li1[x]}:{li2[x]},'

    return li_top_out

pop_char_main()