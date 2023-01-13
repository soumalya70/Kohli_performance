import numpy as np
arr=np.array(
    [1,2,4]
)
# print(arr,type(arr))
# print("Shape of the array: ",arr.shape)
arr2d=np.array([
    [2,3],
    [3,4]]
)
# print(arr2d,arr2d.shape)
# print(arr[0],arr[1])
# print(arr2d[0,1])
arr3d=np.array([
    [
        [1,2,3],
        [5,6,7],
        [2,4,6]
    ],
    [
        [9,8,7],
        [2,1,7],
        [5,6,10]
    ],
    [
        [7,2,5],
        [4,3,8],
        [11,6,0]
    ]
])
# print(arr3d[0,0,0])
arr2d[0]=[4,5]
# print(arr2d)

zeros=np.zeros([4,5])
# print(zeros)

ones=np.ones([3,3])
# print(ones)
consts=np.full((3,3),9)
# print(consts)  
'''
output-
[[9 9 9]
 [9 9 9]
 [9 9 9]]'''
rand=np.random.random((4,4))
print(rand)