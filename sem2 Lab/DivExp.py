def DivExp(a,b):
    if b==0:
        return("Division not possible")
    if(a<0):
        return("Invalid Input")
    else:
        return (a/b)

a=int(input("Enter value for a:"))
b=int(input("Enter value for b:"))
print(DivExp(a,b))