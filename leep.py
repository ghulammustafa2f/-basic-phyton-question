def leep(year):
    if (year % 4 == 0 and year % 100 !=0 and year % 400==0):
        return "leep year"
    else: 
        return "not a leep year"    
print(leep(2000))        