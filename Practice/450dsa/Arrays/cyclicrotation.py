arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]

temp = arr[len(arr) - 1]
for index in range(len(arr) - 1, 0, -1):
    arr[index] = arr[index - 1]
arr[0] = temp

print(arr)
