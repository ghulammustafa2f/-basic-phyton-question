# dataTypes (integer, string, float, double, chars, arrays)
# variables/constants 


# conditional statements (if/else, switch)
# loops (while, for, do/while)

#Q1. write a function which takes an integer input and outputs returns E if number is even
# and return O if number is odd


def isEvenOrOdd(num):
    if(num%2 == 1):
        return "O"
    else:
        return "E"


print(isEvenOrOdd(4))
print(isEvenOrOdd(5))
print(isEvenOrOdd(1234351451245))


#Q2. write a function which takes an integer input 