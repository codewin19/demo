terms = int(input("Enter Number of terms : "))
a,b = 0,1
while terms>0:
    print(a)
    c = a + b
    a =  b
    b = c
    
    
    terms-=1