# a=input("Enter a sentence")
a="AloolA"
vowels,consonents=0,0
for i in a:
    if i.isalpha():
        if i in "aeiouAIOUE":
            vowels+=1
        else:
            consonents+=1
print(vowels,consonents)
# word=input()
# replacment=input()
b=a.replace("aloo","bhindi")
print(a.strip())
print(a.split())
c=a[::-1]
if a==c:
    print("isPalindrome")
else:
    print("NOO")