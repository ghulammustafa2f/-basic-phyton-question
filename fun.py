def squareArea(length):
  areaOfSquare = length * length
  return areaOfSquare

def circleArea(radius):
  squareRadius = radius*radius
  areaOfCircle = 3.14159265359 * squareRadius 
  return areaOfCircle

def sumOfAreas(length,radius):
    areaOfSquare = squareArea(length)
    areaOfCircle = circleArea(radius)

    return areaOfCircle + areaOfSquare


length = float(input("ENTER ANY SIDE VALUE: "))
radius = float(input ("ENTER RADIUS:"))

sum = sumOfAreas(length, radius)
print(sum)