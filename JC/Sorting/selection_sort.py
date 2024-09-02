def sel_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr





arr = [5, 3, 6, 2, 10]
print(sel_sort(arr)) # [2, 3, 5, 6, 10]