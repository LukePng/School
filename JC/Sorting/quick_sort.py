def quick_sort(arr):
    for i in range(len(arr)):
        print('i:' + str(i) + ' ' + str(arr[i]))
        pivot = arr[i]
        j = i-1
        print('j:' + str(j) + ' ' + str(arr[j]))
        while j >= 0 and pivot < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
            print('j in while loop:' + str(j) + ' ' + str(arr[j]))
        print('j after while loop:' + str(j) + ' ' + str(arr[j]))
        arr[j + 1] = pivot
    return arr

arr = [5, 3, 6, 2, 10]
print(quick_sort(arr)) # [2, 3, 5, 6, 10]