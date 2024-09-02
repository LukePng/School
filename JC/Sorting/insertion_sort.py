def insert_sort(arr):
    for i in range(1, len(arr)):
        val = arr[i]
        j = i-1
        while j >= 0 and val < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j + 1] = val
    return arr
        

arr = [5, 3, 6, 2, 10]
print(insert_sort(arr)) # [2, 3, 5, 6, 10]