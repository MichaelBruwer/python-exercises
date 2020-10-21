class Combine_Numbers:
   def Add(self, numba1, total):
        find = {}
        for i, num1 in enumerate(numba1):
            if total - num1 in find:
                return (find[total - num1], i )
            find[num1] = i
print("%d, %d" % Combine_Numbers().Add((1,2,1,4,5,6,7),11))
