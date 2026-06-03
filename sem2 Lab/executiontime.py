import time
def calctime(func):
    start=time.time()
    # print(start)
    func()
    end=time.time()
    ans=end-start
    print(ans)
def samplefunction():
    sum=0
    for i in range(100):
        sum+=i
        
    

calctime(samplefunction)