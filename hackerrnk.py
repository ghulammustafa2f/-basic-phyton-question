# def summ(array):
   
# print(summ([476,859,584]))     



#Multidimensional arrays

#def printMultidimensionalArray(array):
 #    for i in range(len(array)):
  #       for j in range(len(array[i])):
   #          print(array[i][j])


#printMultidimensionalArray([
 #                     [2,4,6], [1,3,5], ['a', 'b', 'c']])
#def printMultidimensionalArray(arr):
 #   output = []
  #  for i in range(len(arr)):
   #     sum = 0
    #    for j in range(len(arr[i])):
     #       sum = sum + arr[i][j]   
      #  output.append(sum)
    #return output

#print(printMultidimensionalArray([[2,4,6], [1,3,5], [3,2,1]]))

# sum all values of multideminsional array



#def sumofmultidemarr(arr):
 #   sum = 0
  #  for i in range(len(arr)):
   #     
    #    for j in range(len(arr[i])):
     #    sum = sum + arr[i][j]
    #return sum


    # sum digonal values of multidimensional array of equal rows and columns
#def diagonalvls(arr):
    
 #   output = []
  #  sumi = 0 
   # sumj = 0
    #for i in range(len(arr)):
    # output.append(i)
    # i += 1
     #for j in range (len(arr)):
      #output.append(j)
      #j +=1
     #return output 


# def diagonalvls(arr):
#     d1 = 0
#    # d2 = 0
#     for i in range(len(arr)):     
#      for j in range(len(arr)):  
#       if (i == len(arr)-j-1) :
#        d1 += arr[i][j]  
#       if i == j:
#        d2 += arr[i][j]   
#     if d1 > d2 :
#       print (d1 - d2)
#     else : 
#       print(d2-d1)
#     print(d1) 


# diagonalvls([[5,3,7,1], 
#              [2,6,3,5],
#              [1,5,3,4], 
#              [9,2,7,8]])