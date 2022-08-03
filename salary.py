def salary(salary):

#Basic Salary <= 10000 : HRA = 20%, DA = 5%
#Basic Salary <= 20000 : HRA = 25%, DA = 10%
#Basic Salary > 20000 : HRA = 30%, DA = 15%
  

 if   salary <= 10000:
      salary = salary * 1.20
      total = (salary / 100) * 95
      print ("GROSS SALARY=",total)

 elif salary <= 20000:
      salary = salary - 10000
      salary = salary * 1.25
      total = (salary / 100) * 90
      total = total + 11400
      print ("GROSS SALARY=",total)

 elif salary > 20000:
      salary = salary - 20000
      salary = salary * 1.30
      total = (salary / 100) * 85
      total = total + 34050     
      print ("GROSS SALARY=",total)


salary(34000)     