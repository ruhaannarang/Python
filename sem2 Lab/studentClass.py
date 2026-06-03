class Student:
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll
        self.marks=[]
        self.avg=0
    def addmarks(self):
        n=int(input("Enter number of subjects"))
        for i in range(0,n):
            self.marks.append(int(input("Enter marks")))
        print("Marks Added successfully")
    def averagemarks(self):
        avg=sum(self.marks)/len(self.marks)
        self.avg=avg
    def __str__(self):
        return f"""
Name:{self.name}
Roll:{self.roll}
Marks:{self.marks}
Average:{self.avg}
"""
r=Student("ruhaan",163)
r.addmarks()
r.averagemarks()
print(r)
