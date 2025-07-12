n = int(input('enter your number:'))
def factorial(n):
    if n < 2 :
        return 1
    else:
        return n*factorial(n-1)

print('your factorial is: ',factorial(n))
