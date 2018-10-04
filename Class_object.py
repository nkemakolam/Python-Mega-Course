class lotteryPlayer:
    def __init__(self, name):
        self.name = name
        self.numbers = (3,5,7,8,2,5,9)
    def total(self):
        return sum(self.numbers)



class Student:
    def __init__(self,name,school):
        self.name = name
        self.school = school
        self.marks = []
    def average(self):
        return sum(self.marks)/len(self.marks)
