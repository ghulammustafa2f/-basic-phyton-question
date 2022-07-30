def maxbtthree(num1,num2,num3):
    if (num1>num2):
      if (num1>num3):
            return num1
    if (num2>num1):
      if(num2>num3):
            return num2 
    else:
       return num3

print(maxbtthree(7586,8765894,97589))  