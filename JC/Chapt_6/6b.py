#Q1
data = [5, 3, 7]

print(data[2]) #7
print(data[-1]) #7
print(len(data)) #3
print(data[0:2]) #[5, 3]
print(0 in data) #False
data.append([2, 10, 5])
print(data) #[5, 3, 7, [2, 10, 5]]
print(tuple(data)) #(5, 3, 7, [2, 10, 5])

#Q2
data = [5, 3, 7]
data[0] = -5
print(data) #[-5, 3, 7]
data.append(10)
print(data) #[-5, 3, 7, 10]
data.insert(2, 22) 
print(data) #[-5, 3, 22, 7, 10]
data.pop(1)
print(data) #[-5, 22, 7, 10]
newData = [1, 2, 3, 4]
data.extend(newData)
print(data) #[-5, 22, 7, 10, 1, 2, 3, 4]
print(data.index(7))
sortedData = sorted(data)
print(sortedData) #[-5, 1, 2, 3, 4, 7, 10, 22]  

#Q3
data = [5, 3, 7, 0, -1, -5]
result = []
for i in data:
    if i == 0:
        continue
    result.append(i)
print(result) #[5, 3, 7, -1, -5]

#Q4
data = [5, 3, 7, 0, -1, -5]
for i in range(len(data)):
    if data[i] < 0:
        data[i] = -data[i]
print(data) #[5, 3, 7, 0, 1, 5]
