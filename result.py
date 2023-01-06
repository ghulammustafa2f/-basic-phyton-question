def subjectsNames(subjectsNo):
    
    sub = subjectsNo
    namesOfSub = []
    for i in range (sub):
     subjectsName = str(input("ENTER SUBJECT NAME:"))
     namesOfSub.append(subjectsName)
    return namesOfSub  
    
def totalMarksOfSubjetcs():    
    
    for j in namesOfSub:
      totalMarks = int(input("TOTALMARKS IN " +j+":"))
      totalMarksOfsubs.append(totalMarks)
    return totalMarksOfsubs

def obtainMArksOfSub():     
   
    for k in namesOfSub:
      obtMarks=float(input("OBT-MARKS IN "+k+":"))  
      obtMArksOfSub.append(obtMarks)
    return obtMArksOfSub

def percentage(obtMarks,totalMarks):      
    n = subjectsNo
    for i in range(n):
      percentage =obtMarks[i] / totalMarks[i] * 100;
      
      percentages.append(percentage)
    return percentages

def grades(percentages):

    n = subjectsNo
    for i in range(n):
     if percentages[i] >= 90:
      grade = "A+"
     elif percentages[i] >= 80 and percentages[i] < 90 :
      grade="A"
     elif percentages[i] >= 70 and percentages[i] < 80:
      grade="B"
     elif percentages[i] >= 60 and percentages[i] < 70:
      grade="C"
     elif percentages[i] >= 33 and percentages[i] < 60:
      grade ="D"
     elif percentages[i] < 33:
      grade="F"           
     gradesOfSub.append(grade)
    return (grades)

def total(totalMarks):

    n = subjectsNo
    totalall=0
    for i in range(n):
     totalall =totalall+ totalMarks[i]
    return(totalall)

def obtain(obtainMarks):
    
    n = subjectsNo
    obtainall=0
    for i in range(n):
     obtainall =obtainall+ obtainMarks[i]
    return(obtainall)

def overAllPercentage(obtainMarks,totalMarks):
    
    OverAllPer =  obtainMarks/totalMarks
    OverAllPer = OverAllPer*100
    return(OverAllPer)

def overAllGrade(overlallpercentage):
    
    PERCE=overlallpercentage
    if  PERCE>= 90:
     OverAllGrade = "A+"
    elif PERCE >= 80 and PERCE < 90 :
      OverAllGrade="A"
    elif PERCE >= 70 and PERCE < 80:
      OverAllGrade="B"
    elif PERCE >= 60 and PERCE < 70:
      OverAllGrade="C"
    elif PERCE >= 33 and PERCE < 60:
      OverAllGrade ="D"
    elif PERCE < 33:
      OverAllGrade="F"           
    return ( OverAllGrade)    
   
gradesOfSub=[]
totalMarksOfsubs=[]
obtMArksOfSub=[]
percentages = []

subjectsNo = int(input("ENTER SUBJECTS NUMBERS:"))
namesOfSub = subjectsNames(subjectsNo)
totalMarksOfSubjects = totalMarksOfSubjetcs()
obtainedMarks = obtainMArksOfSub()
percentageOfEachSub=percentage(obtMArksOfSub,totalMarksOfsubs)
TotalAll=total(totalMarksOfSubjects)
obtainAll=obtain(obtainedMarks)
grades(percentageOfEachSub)
TOT=total(totalMarksOfsubs)
OBT=obtain(obtMArksOfSub)
per=overAllPercentage(obtainAll,TotalAll)
GRAD=overAllGrade(per)

print("SUBJECTS NAMES",'  ',"TOTAL MARKS",'    ',"OBTAIN MARKS",'  ',"PERCENTAGE",'    ',"GRADES")
for v,w,x,y,z in zip(namesOfSub,totalMarksOfsubs,obtMArksOfSub,percentages,gradesOfSub):
 print (v,'            ',w,'               ',x,'           ',y,'          ',z)
print ('   ',"TOTAL MARKS",'   ',"OBTAIN MARKS",'   ',"PERCENTAGE",'   ',"GRADE"   )
print('     ',TOT ,'          ',OBT,'            ',per,'   ',GRAD) 
