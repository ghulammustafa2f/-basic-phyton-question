def timeConversion(h):
 timewithoutformet=[1,2,3,4,5,6,7,8,9,10,11,12]
 timewithformet=[13,14,15,16,17,18,19,20,21,22,23,24]
 for i in range(12):
  if h == timewithoutformet[i]:
   for j in range(1,h):
    c=1
    c= c*timewithformet[j]
   print(c) 



timeConversion()