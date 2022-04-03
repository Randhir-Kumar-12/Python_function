# Function-15
def cout_digit(n):
    count=0
    while n:
        count=count+1
        n//=10
    return count

def armstrong(n, digit):
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
        print(armstrong, end=' ')

def range_of_armstrong(m,n):
    for i in range(m,n+1):
        digit=cout_digit(i)
        armstrong(i,digit)
print("Armstrong numbers:")
range_of_armstrong(1000, 9999)