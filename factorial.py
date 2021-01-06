def factorial(num):
    fac = 1
    for x in range(1,num+1):
        fac = fac * x;
    return fac



number = int(input("Enter Number : "))
print('Factorial of ',number ,' is ',factorial(number))