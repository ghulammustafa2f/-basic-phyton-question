def largest(array):
  n = len(array)
  max = 0
  for x in range(0 , n):
    if array[x] > max :
     secMax = max #0, 1, 2, 5
     max = array[x] #1, 2, 5, 4 
    elif array[x] > secMax and max != array[x] :
        secMax = array[x]    
      
  return secMax 


# print(largest([6563,574574,4525246,8956,58965,5954957,79497,9463,544,5231]))
# print(largest([63746,7367,462763,6732676]))
print(largest([1,2,5,4]))
