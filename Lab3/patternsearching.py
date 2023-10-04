import sys


def pattern_main():
    candidate = ''
    pattern = ''
    count = 0
    
    for i in sys.argv[1].split(','):
        candidate += i

    for i in sys.argv[2].split(','):
        pattern += i
    print(len(candidate), print(len(pattern)))
    for i in range(len(candidate)):
        print(i)
        if candidate[i:i+len(pattern)] == pattern:
            count+=1

    print(f'Pattern appears {count} time!')

pattern_main()