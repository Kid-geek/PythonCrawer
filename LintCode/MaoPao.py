data_set = [ 9,1,22,31,45,3,6,2,11 ]
loop_count=0

for i in range(data_set.__len__()):
    for j in range(data_set.__len__()-i-1):
        if data_set[j]>data_set[j+1]:
            tmp=data_set[j]
            data_set[j]=data_set[j+1]
            data_set[j+1]=tmp
            loop_count+=1
print(data_set)
print('次数：'+str(loop_count))
