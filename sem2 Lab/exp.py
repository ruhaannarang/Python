def power(base,exp):
    return base**exp
i=1
while(i<=5):
    num=int(input("Enter a number"))
    if num<0:
        continue
    if num==0:
        break
    print(power(num,2))
    i+=1