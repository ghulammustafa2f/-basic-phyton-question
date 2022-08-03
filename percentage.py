def percentage(Physics, Chemistry, Biology, Mathematics,computer):
    
   x = (Physics + Chemistry + Biology + Mathematics + computer) 
   y = 500 
   per = (x/y)*100
   if per >= 90:
          print ("Grade A")
   elif per >= 80:
          print ("Grade B")
   elif per >= 70:
          print ("Grade C")
   elif per >= 60:
          print ("Grade D")
   elif per >= 40:
          print ("Grade E")
   else:
          print("Grade F")
       

percentage(34,84,32,87,74)               
