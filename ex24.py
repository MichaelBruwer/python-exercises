class Add():
    def __init__(self):
        self.name = 'bill'
        self.grades = (90,95,85,69)

    def average(self):
        return sum(self.grades) / len(self.grades)

test = Add()
print(test.average())