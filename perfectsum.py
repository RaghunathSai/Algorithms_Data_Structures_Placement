#all the subsets of a given array which equals the sum input
#Input:
#Enter the sum value : 10
#Enter the array elements : 2 3 5 6 8 10

#Output:
#[[10],[2,3,5],[2,8]]

#Explanation:
#Testcase : possible subsets : (2,3,5) , (2,8) and (10)


final_set = []*2
def perfect_sum(li,sum_value,perm):
    if(perm == 0):
        return
    s = perm
    temp = [0]*len(li)
    temp_list = list()
    index = len(li)-1
    while(s>0):
        temp[index]=(s%2)
        s = s//2
        index -= 1
    total = 0
    for i in range(len(temp)):
        if(temp[i] == 1):
            total+=li[i]
            temp_list.append(li[i])

    if(total == sum_value):
        if(temp_list not in final_set):
            final_set.append(temp_list)

    perm -= 1
    perfect_sum(li,sum_value,perm)

if __name__ == "__main__":
    sum_value = int(input("Enter the sum value : "))
    li = list()
    li = list(map(int,input("Enter the array elements : ").split()))
    perfect_sum(li,sum_value,2**len(li))
    print(final_set)