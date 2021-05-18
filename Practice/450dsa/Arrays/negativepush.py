new_list = [-1, -3, 7, 3, -6, -8, 8, 10, 23, -5]
j = 0
for i in range(0, len(new_list)):
    if new_list[i] < 0:
        temp = new_list[i]
        new_list[i] = new_list[j]
        new_list[j] = temp
        j = j + 1
print(new_list)
