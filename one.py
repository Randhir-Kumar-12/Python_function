def calculate_are(b,h):
    area=0.5*b*h
    '''
    we can write these ways
    are=1/2*b*h
    are=0.5*b*h
    '''
    return area


b=int(input("Enter base of triangle:"))
h=int(input("Enter hight of triangle:"))
are=calculate_are(b,h)
print("Area of triangle:" ,round(are,2))