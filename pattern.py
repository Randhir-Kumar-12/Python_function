def pattern_print(n):
    for i in range(n):
        for j in range(n):
            if i>=j:
                print("*", end='')
        print()

n=int(input("Enter star number:"))
pattern_print(n)