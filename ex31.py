import operator
dict1 = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
sorted_dict = sorted(dict1.items(), key=operator.itemgetter(1))
print(sorted_dict)
sorted_dict = dict( sorted(dict1.items(), key=operator.itemgetter(1),reverse=True))
print(sorted_dict)

