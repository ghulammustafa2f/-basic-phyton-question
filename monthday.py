def monthday(month):
   if month=='1' or month=='January':
     return '\n its contains 31 days'
   if month=='2' or month=='February':
     return '\n its contains 28 days in simple year and 29 days in leep year'
   if month=='3' or month=='March':
      return '\n its contains 31 days'  
   if month=='4' or month=='April':
      return '\n its contains 30 days'
   if month=='5' or month=='May':
      return '\n its contains 31 days'
   if month=='6' or month=='June':
      return '\n its contains 30 days'
   if month=='7' or month=='July':
       return '\n its contains 31 days'
   if month=='8' or month=='August':
       return '\n its contains 31 days'
   if month=='9' or month=='September':
       return '\n its contains 30 days'
   if month=='10' or month=='October':
       return '\n its contains 31 days'
   if month=='11' or month=='November':
       return '\n its contains 30 days'
   if month=='12' or month=='December':
       return '\n its contains 31 days'
   else:
       return '\n Number is out of order'
 
print(monthday('November')) 