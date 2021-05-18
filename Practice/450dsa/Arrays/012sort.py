arr = [0, 1, 2, 1, 2, 1, 2, 0, 0, 0, 2, 2, 2, 1, 1]
output_arr = []
count0 = count1 = count2 = 0
for index in range(0, len(arr)):
    if arr[index] == 0:
        count0 = count0 + 1
    elif arr[index] == 1:
        count1 = count1 + 1
    elif arr[index] == 2:
        count2 = count2 + 1

i = 0
while count0 > 0:
    output_arr.append(0)
    i = i + 1
    count0 = count0 - 1

while count1 > 0:
    output_arr.append(1)
    i = i + 1
    count1 = count1 - 1

while count2 > 0:
    output_arr.append(2)
    i = i + 1
    count2 = count2 - 1

print(output_arr)
