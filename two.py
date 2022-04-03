def calculate_are(b,h, l=0):
    if (b+h>l and h+l>b and l+b>h):
        are=0.5*b*h
        print("Area of triangle:" ,round(are,2))
    elif (b==h or h==l or l==b):
        are=h*l
        print("Area of rectangle:" ,round(are,2))
    else:
        are=0.5*b*h
        print("Area of triangle:" ,round(are,2))
        



b=int(input("Enter base of triangle:"))
h=int(input("Enter hight of triangle:"))
l=int(input("Enter another side of triangle:"))

are=calculate_are(b,h,l)