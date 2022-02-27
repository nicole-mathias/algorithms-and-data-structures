# Calculate power of any given number

def power(base,exp):
    assert exp >= 0 and int(exp) == exp, "The exponent should be a positive integer only"

    if exp == 0:
        return 1

    elif exp == 1:
        return base

    else:
        return base * power(base, exp-1)

print(power(-3,3))
print(power(3,3))
print(power(3.5,3))


# another way of writing the same

def powerFunction(base,exp):
    assert exp >= 0 and int(exp) == exp, "The exponent should be a positive integer only"

    if exp == 0:
        return 1

    if exp == 1:
        return base

    return base * powerFunction(base, exp-1)

print(powerFunction(-3,3))
print(powerFunction(3,3))
print(powerFunction(3.5,3))