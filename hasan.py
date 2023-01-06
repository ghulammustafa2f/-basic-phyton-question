def diagonalvs(arr):
    sum = 0   
    for i in range(len(arr)):
        for j in  range(len(arr[i])):
         if i == j:
          sum = sum + arr[i][j]    
    return(sum)


print(diagonalvs([[2,4,6], [1,3,5], [3,2,1]]))