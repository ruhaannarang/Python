class employee:
    def __init__(self,name,eid,salary):
        self.name=name
        self.eid=eid
        self.salary=salary
    def calAnnualSalary(self):
        ans=self.salary*12
        return ans
    def displayEmp(self):
        print(self.name,self.eid,self.salary)
class programmer():
    def __init__(self,lang,exp):
        self.language=lang
        self.experience=exp
class teamlead(employee,programmer):
    def __init__(self, name, eid, salary,lang,exp,teamname):
        employee.__init__(self,name, eid, salary)
        programmer.__init__(self,lang,exp)
        self.teamname=teamname

    def displayTeamlead(self):
        print(f"""            
            Name:{self.name}
            Employee ID:{self.eid}
            Salary:{self.salary}
            Programming Language:{self.language}
            Experience:{self.experience}
            Team Name:{self.teamname}""")
        
e=employee("Ruhaan",12345,100000)
e.displayEmp()
print(e.calAnnualSalary())

t=teamlead("Ruhaan",12345,2000000,"java","15 yrs","OpBande")
t.displayTeamlead()