import statsutil as daaku
import random
ls=[]
for i in range(1,21):
    ls.append(random.randint(1,101))
print(ls)
print(daaku.maximum(ls))
print(daaku.minimum(ls))
print(daaku.mean(ls))
print(daaku.randsample(ls))