# multiply=lambda var1,var2: var1*var2
# print(multiply(5,6))
temp=56
print("Value of temp before the function: ",temp)

def test():
    global temp #takes the global value
    temp=9
    print("Value of temp inside the function: ",temp)
test()
print("value of temp aafter jthe function: ",temp)