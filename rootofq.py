def rootofq(a,b,c):
   #x = (-b ± √ (b2 - 4ac) )/2a
    
      y = (b*b-(4*a*c))
      x = -b + y**(1/2)
      x = x/(2*a) 
      print ("root1=",x)
  
      z=(-b-y**(1/2)) 
      z= z/(2*a) 
      print ("root2=",z)



rootofq(8,-4,-2)



      
