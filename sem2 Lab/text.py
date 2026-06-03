f=open("textsample.txt","r")
para=f.read()
words=para.split()
print(words)
freq={}
for word in words:
    if word in freq:
        freq[word]+=1
    else:
        freq[word]=1
sortedDict=dict(sorted(freq.items(),key=lambda x:x[1],reverse=True))
print(sortedDict)
i=1
for k,v in sortedDict.items():
    if i<=10:
        print(k,v)
    i+=1