# ratedAvenferList2D=[
#     ["spiderman",8],
#     ["groot",7],
#     ["black widow",8]
# ]
# for i in range (len(ratedAvenferList2D)): #for i in range (0,len(ratedAvenferList2D),1):
#     for j in range (len(ratedAvenferList2D[i])):
#             print(ratedAvenferList2D[i][j],end=" ")

employee_list = [
    {
        "name": "Tony Stark",
        "emp_id": 3,
        "address": [
            {
                "line1": "fff",
                "line2": "hhh",
                "state": "WB",
                "Pincode": "700107"
            },
            {
                "line1": "fff",
                "line2": "hhh",
                "state": "WB",
                "Pincode": "700107"
            }
        ]
    },
    {
        "name": "Steve Rogers",
        "emp_id": 6,
        "address": [
            {
                "line1": "fff",
                "line2": "hhh",
                "state": "WB",
                "Pincode": "700117"
            },
            {
                "line1": "fff",
                "line2": "hhh",
                "state": "WB",
                "Pincode": "700127"
            }
        ]
    }
]

# Create a list of dictionaries containing individual employees and their
# corresponding pincodes from the above employee_list
# emp_pin_list = []
# for emp in employee_list:
#     # print("Name: ", emp["name"])
#     # print("ID: ", emp["emp_id"])
#     emp_pin_list.append({"name": emp["name"]})
#     # print(emp_pin_list)
#     # print(employee_list.index(emp))
#     emp_pin_list[employee_list.index(emp)]["pincode"] = []
    
#     for address in emp["address"]:
#         # print(employee_list.index(emp))
        
#         emp_pin_list[employee_list.index(emp)]["pincode"].append(address["Pincode"])
#         print("Pindcode: ", address["Pincode"])
# print(emp_pin_list)
# def multiply(a,b):
#     return a*b
# c=int(input())
# d=int(input())
# print(multiply(c,d))

def get_employee_pin_list(employee_list,addresskey):
    emp_pin_list = []
    for emp in employee_list:
        emp_pin_list.append({"name": emp["name"]})
        emp_pin_list[employee_list.index(emp)][addresskey] = []
        for address in emp["address"]:
            emp_pin_list[employee_list.index(emp)][addresskey].append(address[addresskey])
    return emp_pin_list
print(get_employee_pin_list(employee_list,"line1"))
    
        