class student:
    def __init__(self,name,age):
        self.naam=name
        self.aayu=age
class collegeStudent(student):
    def __init__(self, name, age,collegename):
        super().__init__(name,age)
        self.college=collegename
        
class engineeringStudent(collegeStudent):
    def __init__(self, name, age, collegename,branch):
        super().__init__(name, age, collegename)
        self.bramch=branch
    
    def display(self):
        print("""
            Student Name:{0}
            Student Age:{1}
            College Name:{2}
            Branch:{3}
        """.format(self.naam,self.aayu,self.college,self.bramch))

a=engineeringStudent("Ruhaan",18,"RIT","CSE")
a.display()

#Type of inheritance:Multi-Level