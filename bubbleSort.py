arr = [1, 20, 5, 8, 54, 98, 20, 6, 10, 14, 60]

def bubbleSort():
    for i in range(len(arr)):
        for j in range(len(arr) -1):
            if (arr[j] > arr[j +1]):
                arr[j], arr[j +1] = arr[j +1], arr[j]

bubbleSort()
print(arr)
