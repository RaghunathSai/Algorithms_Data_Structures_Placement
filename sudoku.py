sudoku = []*2

def issafe(row,col,value):
    for i in range(9):
        if(sudoku[row][i] == value):
            return False
        if(sudoku[i][col] == value):
            return False
    row_cell = row - row%3
    col_cell = col - col%3
    for i in range(row_cell,row_cell+3):
        for j in range(col_cell,col_cell+3):
            if(sudoku[i][j] == value):
                return False
    return True

def sudoku_solved():
    flag = 1
    for i in range(9):
        for j in range(9):
            if(sudoku[i][j] == 0):
                flag = 0
                break
        if(flag == 0):
            break
    if(flag):
        return True
    for num in range(10):
        if(issafe(i,j,num)):
            sudoku[i][j] = num
            if(sudoku_solved()):
                return True
            sudoku[i][j] = 0
    return False



if __name__ == "__main__":
    
    temp = list()
    print("Enter the sudoku elements rowwise : ")
    for i in range(9):
        temp = list(map(int,input().split()))
        sudoku.append(temp)
    if(sudoku_solved()):
        print("The solution for the sudoku is : ")
        for i in range(9):
            for j in range(9):
                print(sudoku[i][j],end=" ")
            print()
    else:
        print("Not possible ! ")