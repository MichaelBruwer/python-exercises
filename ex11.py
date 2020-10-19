def shape(a):
    for i in range(1, a):
        for j in range(1,i+1):
            print(i, end="")
        print("\r")

a = 8
shape(a)