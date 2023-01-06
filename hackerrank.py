def compareTriplets(a, b):
  alice = 0
  bob = 0
  for x in range(len(a)):
        
        if a[x] > b[x]:
            alice += 1
        elif a[x] < b[x]:
            bob += 1
        elif a[x] == b[x]:
            alice += 0
        else:
           alice += 0
  
  return [alice, bob]
  #return a ,b


print(compareTriplets([5,9,7,7,5,4,6    ],[5,3,6,8,3,2,1]))
  
