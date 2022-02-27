# find the sum of digits of a postive integer number using recursion

def sum(n):

    assert n >= 0 and int(n) == n, "The number should be a postive integer only"

    if n == 0:
        return 0

    else:
        return int(n%10) + sum(int(n/10))

print(sum(1123))
