data_set = [ 9,1,22,31,45,3,6,2,11 ]

for i in range(data_set.__len__()):
    while i>0 and data_set[i]<data_set[i-1]:
        tmp=data_set[i]
        data_set[i]=data_set[i-1]
        data_set[i-1]=tmp
        i-=1
print(data_set)
