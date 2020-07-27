#Given a dictionary of words and a string, 
# print True if the string can be split into the dictionary words if not print False.

#Input : 
#face placement is thinking focused
#focused thinking is placements


#Output:
#False


if __name__ == "__main__":
    dictionary = list(map(str,input("Enter the dictionary words : ").split()))
    li = input("Enter the sentence : ")
    for i in dictionary:
        if(i in li):
            li = li.replace(i,"")
        print(i,li)
    if(len(li) > 0):
        print("False")
    else:
        print("True")