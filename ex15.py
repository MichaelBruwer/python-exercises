def get_last(i):
    return i[-1]

def sort(Tuple1):
    return sorted(Tuple1, key=get_last)

Tuple1=[(4,2,3), (5,32,2), (1,7,6,43,5,3456)]
print(sort(Tuple1))