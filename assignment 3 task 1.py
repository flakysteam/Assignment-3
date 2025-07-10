def factorial(num):
    result = 1
    while num > 1:
        result *= num
        num -= 1
    return result
fac = factorial(5)
print(fac)