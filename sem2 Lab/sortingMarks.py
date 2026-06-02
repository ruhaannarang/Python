marks=[]
for i in range(6):
    marks.append(int(input("Enter marks")))
for i in range (0,5):
    for j in range(0,5-i):
        if marks[j]<marks[j+1]:
            temp=marks[j]
            marks[j]=marks[j+1]
            marks[j+1]=temp

print(marks)