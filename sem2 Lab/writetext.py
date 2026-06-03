f=open("textsample.txt","r")
q=open("output.txt","w")
string = f.read()
ls=string.split()
sortedlist=sorted(ls)
a = " "
a=a.join(sortedlist)
print(a)
q.write(a)