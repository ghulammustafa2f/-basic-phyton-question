def bills(unit):

#For first 50 units Rs. 0.5/unit
#For next 100 units Rs. 0.75/unit
#For next 100 units Rs. 1.20/unit
#For unit above 250 Rs. 1.50/unit
#An additional surcharge of 20% is added to the bill

#45
#60
#220

    
 if   unit <= 50:
      amt = unit * 0.50 #  amt = 45*0.5 = 22.5
      print ("Bill =", amt+ amt*0.2) # Bill = 22.5

 elif unit <= 150:
      unit = unit - 50 # unit = 10
      amt  = unit * 0.75 # amt = 7.5
      amt  = amt + 25 # 7.5 + 25 = 35
      print ("Bill =", amt+ amt*0.2) #  Bill = 32.5

 elif unit <= 250:
      unit = unit - 150 #unit = 70
      amt  = unit * 1.20 #amt = 70*1.20 = 84
      amt  = amt  + 100 # 84+100 = 184
      print ("Bill =", amt + amt*0.2)
 
 elif unit >= 250:
      unit = unit - 250    
      amt  = unit * 1.50
      amt  =  amt + 220
    
      print ("Bill =", amt+ amt*0.2)




bills(150)    
bills(45)
bills(220)
bills(1000)