# def avgarr(arr):
#  d = 0 
#  b = 0 
#  c = 0
#  for i in range (len(arr)):
#   if (arr[i] > 0):
#    d = d + 1 
#   if (arr[i] < 0):
#    b = b + 1 
#   if (arr[i] == 0):
#    c = c + 1 
#  sum = d / len(arr) 
#  sum1 = b / len(arr)
#  sum2 = c / len(arr)

  
  
  


#  print(sum)
#  print(sum1)
#  print(sum2)

# avgarr([1,-3,-4,2,0,0,9,-5])     
#hackrankquiz------------------------------------------------------------------
# def maxmin(arr):
#   arr.sort()
#   max = 0
#   min = 0
#   for i in range(1,len(arr)):
#     max = arr[i]+ max 

#   for j in range(0,len(arr)-1):
#     min = arr[j]+min
#   print(min,max)  
  

# maxmin([5,6,2,2])     
#hackrankquiz--------------------------------------------------------------------
def candle(candles):
    maximum = (max (candles))
    tallestcandles = 1
    for i in range(len(candles)):
     if candles[i] == maximum:
      tallestcandles += 1
    print(tallestcandles-1)

candle([])   