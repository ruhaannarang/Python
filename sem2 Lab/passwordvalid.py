password=input("enter your password")
uppercount,lowercount,digitcounnt,specialcount=0,0,0,0
for i in password:
    if i.isupper():
        uppercount+=1
    elif i.islower():
        lowercount+=1
    elif i.isdigit():
        digitcounnt+=1
    elif i in "@#$":
        specialcount+=1
if uppercount>0 and lowercount>0 and digitcounnt>0 and specialcount>0 and len(password)>6 and len(password)<16:
    print("Password is  valid")
else:
    print("Password is not valid")
