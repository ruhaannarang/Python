class person:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname
    def printname(self):
        print(self.firstname,self.lastname)
class Student(person):
    def __init__(self,fname,lname,cg):
        person.__init__(self,fname,lname)
        self.cgpa=cg
    def printstud(self):
        self.printname()
        print("{0} ki CGPA:".format(self.firstname),self.cgpa)
x=person("aloo","baingan")
x.printname()
y=Student("alooKaBacha","baingan",9.5)
y.printstud()