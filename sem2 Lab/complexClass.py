class Complex:
    def __init__(self):
        self.real=0.0
        self.imaginary=0.0
    def readComplex(self):
        self.real=float(input("Enter the real part: "))
        self.imaginary=float(input("Enter the imaginary part: "))
    def addComplex(self,other):
        realpart=self.real+other.real
        imaginarypart=self.imaginary+other.imaginary
        self.real=realpart
        self.imaginary=imaginarypart
    def displayComplex(self):
        print(f"{self.real}+{self.imaginary}i")

ans=Complex()
n=int(input("Enter number of complexes:"))
for i in range(0,n):
    r=Complex()
    r.readComplex()
    ans.addComplex(r)
    
ans.displayComplex()


