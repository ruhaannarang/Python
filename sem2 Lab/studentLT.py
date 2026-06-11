class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def __lt__(self,other):
        return self.marks<other.marks
    
s1=Student("Ruhaan",100)
s2=Student("Tanmay",99)
if s1<s2:
    print("Tanmay has more marks than ruhaan")
else:
    print("Ruhaan has more marks than tanmay")