import numpy as np
x= np.array([
    [3,4,5],
    [2,6,3],
    [8,4,1]
])
v=np.array([1,0,1])

#for loop route
# y=np.empty_like(x)
# print(y)
# for i in range (len(x)):
#     y[i, :]=x[i, :] + v
# print(x)
# print(y)
stacked_v=np.tile(v,(3,1))
print(stacked_v)

print(x+stacked_v)
print("same as x+stacked 'x+stacked_v: " ,x+v)