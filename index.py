import numpy as np
arr=np.array([
    [5,4,3,1],
    [7,3,9,3],
    [6,4,7,4]
])
# print(arr,arr.shape)
# s_arr=arr[:2,1:3]
# print(s_arr)
#last row and col0,col1
# s1_arr=arr[2:,0:2]
# print(s1_arr)
#second row
# row2=arr[1:2]
# print(row2)
#col1 and col2
# col12=arr[:3,0:2]
# print(col12)
#col3
# print(arr[:,2:3])

bool_idx=[arr>3]
# print(bool_idx)
# print(arr[arr>3])

x=np.array([
    [2,4],
    [5,3]
])
print(x)
y=np.array([
    [6,7],
    [3,5]
])
print(y)
# print(x+y)
# print(np.add(x,y))
# print(np.subtract(x,y))
# print(np.multiply(x,y))
# print(np.divide(x,y))
# print(np.sqrt(x))
v=np.array([4,5])
w=np.array([3,6])
print(v.dot(w))
print(np.dot(v,w))
print(x.dot(w))
print(np.dot(x,w))
#for transpose
# print(x.T)

print("sum of all elements",np.sum(x))
print("Sum of all columns",np.sum(x,axis=0))
print("Sum of all rows",np.sum(x,axis=1))