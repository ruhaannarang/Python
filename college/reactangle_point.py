class Point:
    def __init__(self,xcord,ycord):
        self.x=xcord
        self.y=ycord
    def __str__(self):
        return "{0},{1}".format(self.x,self.y)
class Rectangle:
    def __init__(self,posn,w,h):
        self.corner=posn
        self.width=w
        self.height=h
    def __str__(self):
        return "Position:({0})\nWidth:{1}\nHeight:{2}".format(self.corner,self.width,self.height)
box=Rectangle(Point(100,40),12,34)
print(box)
