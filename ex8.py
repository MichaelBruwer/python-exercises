import random

num = random.randint(0,10)

input1 =int(input("num between 1-9"))

while True:
    if num == input1:
        print("yay")
        break
    else:
        continue