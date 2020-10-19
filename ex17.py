sleepscedule = ['Monday', 'Tuesday', 'Wednesday', 'Thrusday', 'friay', 'saterday', 'sunday']
sleepscedule = [x for (i,x) in enumerate(sleepscedule) if i not in (0,4,5)]
print(sleepscedule)

