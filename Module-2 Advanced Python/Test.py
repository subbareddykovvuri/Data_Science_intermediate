# with open("C:\\Users\\subba\\Documents\\GitHub\\Scalar-Data_Science_intermediate\\Module-2 Advanced Python\\essay.txt","r") as f:

#     count = 0

#     data = f.readlines()

#     words = data.split()

#     for word in words:

#         count += 1

#     print(count)



# with open('C:\\Users\\subba\\Documents\\GitHub\\Scalar-Data_Science_intermediate\\Module-2 Advanced Python\\essay.txt', 'r') as fr:
#   lines = fr.readlines()
#   with open('C:\\Users\\subba\\Documents\\GitHub\\Scalar-Data_Science_intermediate\\Module-2 Advanced Python\\new_data.txt', 'w') as fw:
#     for line in lines:
#       if 'hello' in line:
#         fw.writelines(line)



f = None 
for i in range (5): 
    with open("C:\\Users\\subba\\Documents\\GitHub\\Scalar-Data_Science_intermediate\\Module-2 Advanced Python\\essay.txt", "w") as f: 
        if i > 2: 
            break 
print(f.closed)