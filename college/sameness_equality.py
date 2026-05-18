class Point:
    def __init__(self,xcord,ycord):
        self.x=xcord
        self.y=ycord
    def __str__(self):
        return "{0},{1}".format(self.x,self.y)
p1=Point(10,20)
p2=Point(10,20)
print(p1==p2)
# the equality operator in the objects will always check for shallow equality
# it checks whether the two objects are pointing to the same memory location


p=p1
print(p1==p)
#now p is the alias of the  object p1

#to check the deep equality of two objects we can write the function called same coordinates
def same_coordinates(p1,p2):
    return p1.x==p2.x and p1.y==p2.y

print(same_coordinates(p1,p2))

#is operator is used to  check the shallow equality

print(p1 is p2)
print(p1 is p)


