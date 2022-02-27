# fibonacci using recursion

# this function gives the value of the n^th postition in the fibonacci series
# fibonacci series: 0,1,1,2,3,5,8,13......

def fibonacci(n):

    assert n >= 0  and int(n) == n, "The number should be a positive integer only"

    if n in [0,1]:
        return n

    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(8))

    

