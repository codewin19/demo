# function define
def isPrime(num):
    for x in range(2,num):
        if num % x == 0:
            return False
    return True

# calling of function
if isPrime(15):
    print("15 is prime Number ")
else:
    print("15 is not a prime Number ")
