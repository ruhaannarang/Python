import copy
class Point:
    def __init__(self,xcord,ycord):
        self.x=xcord
        self.y=ycord
    def __str__(self):
        return "{0},{1}".format(self.x,self.y)
def same_coordinates(p1,p2):
    return p1.x==p2.x and p1.y==p2.y
p1=Point(10,20)
p2=copy.copy(p1) #Shallow copy
# for deep copying copy.deepcopy() is used
# p2=p1

print(p1 is p2)
print(same_coordinates(p1,p2))