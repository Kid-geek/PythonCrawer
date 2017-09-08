lists = [ 9,1,22,31,45,3,6,2,11 ]
count = len(lists)
for i in range(0, count):
    min = i
    for j in range(i + 1, count):
        if lists[min] > lists[j]:
            min = j
    lists[min], lists[i] = lists[i], lists[min]
print(lists)