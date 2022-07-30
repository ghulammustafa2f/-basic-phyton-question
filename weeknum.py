import re


def weeknum(num):
  if num==1:
    return '\n Monday'
  if num==2:
    return '\n Tuesday'
  if num==3:
    return '\n Wednesday'
  if num ==4:
    return '\n Tuesday' 
  if num==5:
    return '\n Friday'
  if num==6:
    return '\n Saturday'
  if num==7:
    return '\n Sunday'
  else:
    return '\n out of order'

print(weeknum(8))