if __name__ == '__main__':
    a = [1, 3, 5, 7, 9, 2, 4, 8]
    b = [2, 4, 6, 8, 10, 3, 0, 11]
    a.sort()
    b.sort()
    union = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            union.append(a[i])
            i = i + 1
        elif a[i] > b[j]:
            union.append(b[j])
            j = j + 1
        else:
            union.append(a[i])
            i = i + 1
            j = j + 1
    while i < len(a):
        union.append(a[i])
        i = i + 1
    while j < len(b):
        union.append(b[j])
        j = j + 1
    print(union)
