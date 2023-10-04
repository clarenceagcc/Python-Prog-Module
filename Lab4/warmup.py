def fac_iterative(n):
    facNum = 1
    for i in range(1, n+1): # 1 - 5
        facNum *= i
    return facNum
    

def fac(n):
    if n == 0:
        return 1
    else:
        return fac(n-1)*n
    
print(fac(4))   
print(fac_iterative(4))
print(fac(4))