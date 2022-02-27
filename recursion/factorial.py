# factorial using recursion

# for recursion we follow 3 steps:
# 1) base case
# 2) recursive case
# 3) case which shouldnt be executed, I have used the assert keword for this condition in the below code.


def factorial(n):
    # assert keyyword works similar to a try and catch block....if the condititon below is not satisfied
    # the error messagge will be printed, I am using this
    assert n >= 0 and int(n) == n, "The number should be a positive integer only" 

    # factorial of 0! = 1 , 1! = 1
    if n in [0,1]:
        return 1

    else:
        return n * factorial(n-1)


print(factorial(6))