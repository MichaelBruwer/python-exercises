list2 = [82, 21,34,12,63,2,7,0]
list1 = [3,63,72,8,54,23,6]

def yeet(list2, list1):
    result = False
    for x in list2:
        for y in list1:
            if x == y:
                result = True
                return result
    return result

print(yeet(list2, list1))