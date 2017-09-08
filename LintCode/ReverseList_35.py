data_set = [ 9,1,22,31,45,3,6,2,11 ]
loop_count=0
for i in range(len(data_set)):
    for j in range(len(data_set)-i-1):
        if data_set[j]>data_set[j+1]:
            temp=data_set[j]
            data_set[j]=data_set[j+1]
            data_set[j+1]=temp
    loop_count+=1
    # print(data_set)
print(data_set,loop_count)