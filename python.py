first_list = [15, 16, 17]

print("Predefined List : ", first_list)
num = int(input("Enter the number to divide : "))
    
second_list = []
for i in first_list:
    res = i%num
    second_list.append(res)
    
print("2nd List : ", [i%num for i in first_list])


num_m = int(input("Enter the number to multiply : "))

print("3rd List : ", [i*num_m for i in second_list])