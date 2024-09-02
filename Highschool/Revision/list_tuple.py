

#Q3:
#method 1:
# def find_equi(lst):
#     result = []
#     for i in range(len(lst)):
#         if sum(lst[:i]) == sum(lst[i+1:]):
#             result.append(i)
    
#     if len(result) == 0:
#         return -1
#     return result

# print(find_equi([1,2,3,4,3,2,1]))

#method 2: (better) runtime = O(n)
def find_equi(lst):
    post_sum = sum(lst)
    prev_sum = 0
    result = []

    for i in range(len(lst)):
        post_sum -= lst[i]
        if prev_sum == post_sum:
            result.append(i)
        prev_sum += lst[i]

    if len(result) == 0:
        return -1
    return result