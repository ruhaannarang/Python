class point:
    def __int__(self):
        self.x=0.0
        self.y=0.0
    def read(self):
        self.x=float(input("Enter x value:"))
        self.y=float(input("Enter y value:"))
    def __add__(self, other):
        r=point()
        r.x=self.x+other.x
        r.y=self.y+other.y
        return r
    def __str__(self):
        return("({0},{1})".format(self.x,self.y))
p=point()
p.read()
q=point()
q.read()
print(p)
print(q)
print(p+q) #p.__add__(q)
