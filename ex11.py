def shape(a):
    for i in range(0, a):
        for j in range(0,i+1):
            print(i, end="")
        print("\r")

a = 5
shape(a)