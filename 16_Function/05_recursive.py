""" 
4! = 4*3*2*1

4! = 4*3!
3! = 3*2!
2! =2*1

"""


def iterative_factorial(n):
    result = 1
    for i in range(2,n+1):
        result *= i

    return result


print(iterative_factorial(4))
    

####################################
def recursive_factorial(n):
    if n== 1:
        return 1
    else:
        return n* recursive_factorial(n-1)
# Caller
print(recursive_factorial(40))