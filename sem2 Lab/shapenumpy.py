import numpy as np
a=np.random.randint(0,21,(3,4))
# a.reshape(3,4)
print(a)
a=a.reshape(2,6)
print(a)
a[a>10]=99
print(a)
print(a.dtype)