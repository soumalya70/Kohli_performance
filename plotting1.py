import numpy as np
import matplotlib.pyplot as plt
x=np.arange(-100,100,0.1)
def sqr(n):
    return n**2
y=[]
# for i in x:
#     y.append(sqr(i))
# print(y)
# plt.plot(y)
# plt.show()
def secnd(e):
    return -5*(e**2)+(4*e)+1
for i in x:
    y.append(secnd(i))
plt.plot(x,y)
plt.show()
