import sys

arr = [-2, -7, 3, 5, 1, 0, -2]

max_arr = -sys.maxsize - 1

size = len(arr)
while size > 0:
    for i in range(0, len(arr) + 1 - size):
        Sum = sum(arr[i:size + i])
        if Sum > max_arr:
            output_array = arr[i:size + i]
            max_arr = Sum
    size = size - 1
print(max_arr)
print(output_array)
