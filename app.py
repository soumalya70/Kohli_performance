# a=7
# print("value of the variable",a)
# print("type of the variable",type(a))

# elements=[]
# for i in range(10):
#     elements.append(i)
# print(elements)

# fname=input()
# lname=input()
# print(fname+" "+lname)

# fname=int(input())
# lname=int(input())
# print(fname+lname)

# val="HUNTER"
# print(type(val))
# for i in range(len(val)):
#     print(val[i])

# ele=[12,7,"Thor","Dc"]
# print(len(ele))
# print(ele[-1])

# avengerslist=["Ironman","Thor","CaptainAmerica","BlackPanther"]
# ratinglist=[8,9,7,6]
# newlist=[]
# for i in range(len(avengerslist)):
#     newlist.append(avengerslist[i])
#     newlist.append(ratinglist[i])
# print(newlist)

# avengerlist={
#     "ironman":10,
#     "captainamerica":6,
#     "hulk":4
# }
# print(avengerlist)
# print(type(list(avengerlist.keys)))

avengerlist={
    "ironman":[
        {"spiderman":8},
        {"cap":7}
    ],
    "captainamerica":6,
    "hulk":4
}
print(avengerlist["ironman"])
print(avengerlist["ironman"][0]["spiderman"])