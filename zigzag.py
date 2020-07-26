#Printing an array into Zigzag fashion is discussed here. Suppose you were given an array of integers,
#  and you are told to sort the integers in a zig-zag pattern. In general, in a zig-zag pattern, 
# the first integer is less than the second integer, which is greater than the third integer, 
# which is less than the fourth integer, and so on. Hence, the converted array should be 
# in the form of e1 < e2 > e3 < e4 > e5 < e6.

#Test cases:
#Input 1:                                            Output 1 :
#4 3 7 8 6 2 1                                       3 7 4 8 2 6 1

#Input 2:                                            Output 2 :
#1 4 3 2                                             1 4 2 3

def zigzag(li):
    for index in range(len(li)-1):
        if(index % 2 == 0):
            if(li[index] > li[index+1]):
                li[index],li[index+1] = li[index+1],li[index]
        else:
              if(li[index] < li[index+1]):
                  li[index],li[index+1] = li[index+1],li[index]
    print("The array in zig zag order is : ",li)

if __name__ == "__main__":
    li = list(map(int,input("Enter the array elements with space in between in one line : ").split()))
    zigzag(li)