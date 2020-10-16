list = [34,243,32,1,64,23,86,222,43]
even = 0
odd = 0

for num in list:
    if num %2 == 0:
        even+=1
    else:
        odd +=1
print("even nums",even)
print("odd nums", odd)