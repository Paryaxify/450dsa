new_list = [1, 6, 3, 7, 2, 9, 10, 5, 34]
N = int(input('Enter value of K: '))
if N > len(new_list):
    exit('invalid element')
new_list.sort()
print(new_list[N-1])
