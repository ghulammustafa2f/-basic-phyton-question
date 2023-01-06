#1st -------------------------------------------------------

# def area(n):
#  pi =3.14159
#  area = pi *(n*n)
#  print (area,"meter squar")


#  area(31)

#2nd-----------------------------------------------------------

# def temp(n):
#  x = 5/9 
#  y = n - 32 
#  temp = x *y
#  print (temp,"degree celsius")


# temp(120)
 

# 3rd-----------------------------------------------------------

# def weather(n):
#  if (n > 35):
#     print ("HOT DAY")
#  elif ( n > 25) and ( n < 35 ):
#     print ("PLEASANT DAY")
#  elif (n < 25 ):
#     print ("COOL DAY")


# weather(17)


#4th------------------------------------------------------------------
# def grades(n, obt):
#     xx = n * 100 
#     gr = xx/ obt
#     if (gr >= 80):
#      print ("A+") 
#     elif (gr >= 70) and ( gr < 80):
#      print ("A") 
#     elif (gr >= 60) and (gr < 70):
#      print ("B")
#     elif (gr >= 50) and (gr < 60):
#      print ("C")
#     elif (gr >= 40) and (gr < 50):
#      print ("D")
#     elif (gr >= 33) and (gr < 40 ):
#      print ("E")
#     else :
#      print ("F")


# grades(703,800) 


#5th-------------------------------------------------------------------------
# def cal(num1,num2):
 
#    num1 = int(input("Enter First Num: "))
#    num2 = int(input("Enter Second Num: "))
#    x = int(input("ENTER FUNCTION:")) 
#    if (x ==1): 
#         print (num1+num2)    
#    if (x ==2):
#         print (num1-num2) 
#    if (x ==3):
#         print (num1*num2)
#    if (x ==4):
#         print (num1/num2)
    



# cal("num1","num2")     

# 6th-----------------------------------------------------------------------

# def ans(num):
#        a = str(input("TYPE 1ST CHARACTER: ") )
#    if (a == "S"):
#     x = int(input("ENTER ANY SIDE VALUE: "))    
#     print ("AREA OF SQUARE IS =",x*x)
#    elif (a == "T"):
#      b =int(input("ENTER BASE:")) 
#      h = int (input("ENTER HEIGHT:"))
#      a = 1/2*b*h 
#      print("AREA OF TRIANGLE IS =",a)    
    

# ans("num")    


#7th---------------------------------------------------------------------------
# def pn(n):
#  for i in range(2,n):
#      if (n % i)==0:

#       print(n, "is not a prime number")
#       break   
#  else:
#      print(n, "is a prime number")

# pn(8)

#8th---------------------------------------------------------------
# def even(n):
#  if n > 1:
#      for i in range (2,n,2):
#       print (i)


# even(15)      
#9th------------------------------------------------------------------------
# def table(n):
#  c = 1
#  for p in range(1,10+1):
   
#    num = n * p 
#    print (n,"*", c,"=" ,num)
#    p +=1
#    c += 1
# table(63)1         
#10th----------------------------------------------------------------------------
# def st(n):
#     arr=[]
    
#     c = 0

#     for i in range (1,n+1):
#      g = i + c
      
#      arr.append(g)
    
#      print (*arr,sep ='')
# st(7)          
#11th-------------------------------------------------------------------------
# def out(n,m):
 
#  for c in range (1,n+1):
#   for j in range(1,m+1):
#    j = j+j
#   print (c,j)  
   
# out(6,6)          
#12th--------------------------------------------------------------------
# def factorial(n):
#  i = 1
#  ans = 1
#  while (i<=n):
#   ans = i*ans
#   i=i+1

#  return ans

# fact = factorial(10)
# print(fact)
#13th-------------------------------------------------------------------
# def box():
 
#  x = str(input("HORIZANTAL OR VERTICAL:"))
 
#  if x == "HORIZANTAL":
#    inp_hori = int(input("HOW MANY LINES:")) 
#    for i in range(1,inp_hori+1):
#     print ("-",end="")
 
#  elif x == "VERTICAL":
#    inp_ver = int(input("HOW MANY LINES:")) 
#    for j in range(1,inp_ver+1):
#     print("|")   

# box()        
# #fun------------------------------------
# print( '  '"--------")
# print (' ' "|        |")
# print(' '"|        |" )
# print (' '"|        |")
# print(' '" -------- "  )
#14--------------------------------------------------------------------- 
def distance():
 x1= int(input("x1 = "))
 x2 = int(input("x2 = "))
 y1 = int(input("y1 = "))
 y2 = int(input("y1 = "))
 dis = (x2-x1)**2 + (y2-y1)**2

 print()


distance() 