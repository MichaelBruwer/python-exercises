from collections import Counter

baabaablacksheep = [
   'baa', 'baa', 'black', 'sheep', 'have', 'you', 'any', 'wool',
   'yes', 'sir', 'yes', 'sir', 'three', 'bags', 'full', 'one', 'for',
   'the', "master", 'and', 'the', 'little', 'boy', 'too']

ammount_of_occurances = Counter(baabaablacksheep)
print(ammount_of_occurances)
