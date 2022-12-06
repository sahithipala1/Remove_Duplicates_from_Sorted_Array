def remove_duplicates(arr):
    n = len(arr)
    if n == 0 or n == 1:
        return arr
    
    pivot = 0
    for last_o in range(0, n - 1):
        if arr[last_o] != arr[last_o + 1]:
            arr[pivot] = arr[last_o]
            pivot = pivot + 1
    arr[pivot] = arr[n - 1]
    return arr[0:pivot + 1]


arr = [1, 1, 2, 2, 3, 3, 3, 45, 4, 5, 5, 6]
print(remove_duplicates(arr))
