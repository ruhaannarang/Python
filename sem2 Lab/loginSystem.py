password="DakuMangalSingh"
username=input("Enter your username:")
for i in range(3):
    inputpassword=input("Enter your password")
    if password==inputpassword:
        print("Login successfully")
        break
    else:
        print("Incorrect password")
        if i==2:
            print("Account locked")
