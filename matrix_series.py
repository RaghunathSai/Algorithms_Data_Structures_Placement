#python code to generate the n*n matrix of the below form
#    1   2    3   4   5    6  
# 1  1   4    8  14  23   37  
# 2  3   6   10  16  25   39    
# 3  6   9   13  19  28   42  
# 4  11  14  18  24  33   47  
# 5  18  21  25  31  40   54
# 6  29  32  36  42  51   65


def prime(n):  #function that generates n prime numbers and stores them in prime_arr
    count = 1
    start = 2
    prime_arr = list()
    prime_arr.append(2)
    while(count < n):
        start += 1 
        if start > 1: 
              for i in range(2, start): 
                  if (start % i) == 0: 
                     break
                  else: 
                       if i == start//2 + 1: 
                          prime_arr.append(start) 
                          count += 1
    return prime_arr

def fibnocci(n): # generates a n number of fibonacci series elements starting with 1,1,2,3,... in fib_arr
    start_one = 1
    start_two = 1
    n -= 2
    fib_arr = list()
    fib_arr.append(int(1))
    fib_arr.append(int(1))
    for i in range(n+1):
        fib_arr.append(fib_arr[i]+fib_arr[i+1])
    return fib_arr

def staging(n):  # generates the series elements 
    stage_one = list()
    stage_two = list()
    stage_three = list()
    stage_one.append(int(1))
    index = 0
    for i in range(n):
        stage_one.append(stage_one[i]+fib_arr[index])
        index += 1
    stage_two.append(int(3))
    index = 0
    for i in range(n):
        stage_two.append(stage_two[i]+stage_one[index])
        index += 1
    index = 0
    stage_three.append(int(1))
    for i in range(n):
        stage_three.append(stage_three[i]+prime_arr[index])
        index += 1
    return stage_one,stage_two,stage_three

def form_matrix(stage_two,stage_three,n): #forms the resultant matrix series of n*n form
    final_arr = []*2
    prime_index = 0
    for i in range(n):
        index = 0
        temp = list()
        for j in range(n):
            if(j == 0):
                temp.append(stage_three[prime_index])
                prime_index += 1
            else:
                temp.append(temp[j-1] + stage_two[index])
                index += 1
        final_arr.append(temp)
    for i in range(n):
        for j in range(n):
            print(final_arr[i][j],end=" ")
        print()
           
if __name__ == "__main__":
    n = int(input("Enter the square matrtix dimension : "))
    prime_arr = prime(n) #gets n prime numbers
    fib_arr = fibnocci(n) #gets n fibonacci elements
    stage_one = list()
    stage_two = list()
    stage_three = list()
    stage_one,stage_two,stage_three = staging(n) #generates the series
    form_matrix(stage_two,stage_three,n) #ultimatley the m,atrtix is formed