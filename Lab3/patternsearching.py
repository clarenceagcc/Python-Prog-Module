import sys


def pattern_main():
    candidate = ''
    pattern = ''
    for i in sys.argv[1].split(','):
        candidate += i

    for i in sys.argv[2].split(','):
        pattern += i
    
    countpatterns = candidate.count(pattern)
    

    print(f'Patterns appears {countpatterns} time!')

pattern_main()