import re
from itertools import combinations_with_replacement,permutations

string = input("Enter the string with $ sign : ")
numbers = list()
numbers = re.findall(r'[0-9]',string)

dollar_count = 0
for i in string:
    if (i == '$'):
        dollar_count+=1

comb = list(combinations_with_replacement(numbers,dollar_count))#combinations
perm = list(permutations(numbers,dollar_count))#permutations
comb += perm
comb = list(set(comb))#entire possible outcomes 
print(comb)

for k in range(len(comb)):
    index = 0
    for i in string:
        if(i!='$'):
            print(i,end="")
        else:
            print(comb[k][index],end="")
            index+=1
    print()