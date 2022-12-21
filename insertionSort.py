arr = [1, 20, 5, 8, 54, 98, 20, 6, 10, 14, 60]

for i in range(0, len(arr)):
    key = arr[i]
    j = i - 1
    while j >=0 and key < arr[j]:
        arr[j+1] = arr[j]
        j -= 1
    arr[j+1] = key

print(arr)