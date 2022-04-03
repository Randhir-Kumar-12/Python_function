# Function-1
def area_of_circle(r):
    return 3.14*r*r
area=area_of_circle(5)
print("Area of circle:",area)

# Function-2
def circumference_of_circle(r):
    return 2*3.14*r
circumference=circumference_of_circle(5)
print("Circumference of circle:",round(circumference,2)) 

# Function-3
def natural_number(n):
    for i in range(1,n+1):
        print(i, end=' ')
print("Natural number:")        
natural_number(5)       
print()

# Function-4
def even_natural_number(n):
    a=2*n+1
    for i in range(1,a):
        if i%2==0:
            print(i, end=' ')
print("Even natural number:")
even_natural_number(10) 
print()

# Function-5
def sum_natural(n):
    s=0
    for i in range(n+1):
        s=s+i
    return s

sum=sum_natural(5)
print("sum of natural no.:",sum)    

# Function-6
def sum_of_cubes(n):
    s=0
    for i in range(1,n+1):
        s=s+i*i
    return s
sum_cubes=sum_of_cubes(5)
print("Sum of cubes:",sum_cubes) 

# Function-7
def odd_even(n):
    if n%2:
        return  0
    else:
        return 1
res=odd_even(15)
print("Result:",res)   

# Function-8
def factorial(n):
    f=1
    while n:
        f=f*n
        n=n-1
    return f
fac1=factorial(5)
print("Factorial:",fac1)  

# Function-9
def permuntation(n, r):
    permuntation=factorial(n)/factorial(n-r)
    return permuntation

permuntation=permuntation(10,3)
print("Permuntation:",permuntation)


# Function-10
def combination(n,r):
    combination=factorial(n)/(factorial(r)*factorial(n-r))
    return combination
combination=combination(10,3)
print("Permuntation:",combination)  

# Function-11
def check_prime(n):
    count=1
    for i in range(2,n+1):
        count=count+1
        if n%i==0:
            break
    if count==n:
        return 1
    else:
        return 0

prime=check_prime(12)
print("Prime:",prime)


# Function-12
def next_prime(n):
    m=n+1
    while m:  # m is globle variable
        for j in range(2,m+1): # j is aslo global variale
            if m%j==0:
                break
        if j==m:
            print("Next prime number:",m)
            break    
        m=m+1
next_prime(15)
next_prime(11)

# Function-13
def prime_number_in_range(m,n):
    count=1
    for i in range(m+1, n):
        for j in range(2, i+1):
            count=count+1
            if i%j==0:
                break
        if count==i:
            print(i, end=' ')
        count=1
print("Prime number in range:")
prime_number_in_range(1,20)
print()


# Function-14
def check_armstrong(n, digit):
    armstrong=0
    temp=n
    while temp:
        last_digit=temp%10
        s=1
        for i in range(digit):
            s= s*last_digit
        armstrong=armstrong+s
        temp //=10
    if armstrong==n:
        return 1
    else:
        return 0

arms=check_armstrong(153,3)
print("Armstrong:",arms)
arms1=check_armstrong(123,3)
print("Armstrong:",arms1)


