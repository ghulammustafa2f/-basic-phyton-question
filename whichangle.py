def whichangle(side1,side2,side3):
    if (side1 == side2 and side2 == side3 and side3 == side1):
     
      print("Equilateral triangle")

    elif (side1 == side2 or side2 == side3 or side3 == side1):
      
      print("Isosceles triangle")
    
    else:
      
      print("Scalene triangle") 


whichangle(20,30,20)

