def get_last(i):
    return i[-1]

def sort(tuple):
    return sorted(tuple, key=get_last)

tuple=[(4,2,3), (5,32,2), (1,7,6,43,5,3456)]
print(sort(tuple))