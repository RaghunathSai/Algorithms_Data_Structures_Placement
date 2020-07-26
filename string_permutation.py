#program to generate all permutation of an input string.  
# A recursive function and return the permutation of input string as set.

#input : word
#output : word wodr wrod wrdo wdro wdor owrd owdr orwd ordw odrw odwr rowd rodw rwod rwdo rdwo rdow 
#         dorw dowr drow drwo dwro dwor
         

def permutations(word,perm = 0):
    if (perm == len(word)-1):
        print(''.join(word))
    
    for i in range(perm,len(word)):
        word[perm],word[i] = word[i],word[perm]
        permutations(word,perm+1)
        word[perm],word[i] = word[i],word[perm]

if __name__ == "__main__":
    word = input("Enter the string : ")
    permutations(list(word))