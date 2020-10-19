def multiplyby(q):
 return lambda x : x * q
result = multiplyby(2)
print(result(20))

