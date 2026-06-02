n=int(input("Enter number of numbers"))
ls=[]
for i in range(0,n):
    ls.append(int(input()))
mean=sum(ls)/len(ls)
print(mean)
variancesum=0
for i in ls:
    variancesum+=(i-mean)**2
variance=variancesum/len(ls)
print(variance)
print(variance**0.5)