class vector:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __add__(self, other):
        return vector(self.x+other.x,self.y+other.y)
    def display(self):
        print(f"({self.x},{self.y})")

v1=vector(10,-10)
v2=vector(15,25)
v3=v1+v2
v3.display()