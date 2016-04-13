def add( first, second):
    # TODO:
    # there's an error in this code, fix it
    return first + second#the word plus isnt a expression, replaced it with the expression +

def subtract( first, second):
    return first - second
    # TODO:
    # fill in code here that will return the difference between first and second

def multiply( first, second):
    return first * second
    # TODO:
    # fill in code here that will return the product of first and second

def divide( first, second):
    try:#checks the number
        return first/second          #RETURNS THE QUOTIENT
    except ZeroDivisionError:#Raised exception for the ZeroDivisionError
        print("I'm sorry, I can't divide by zero")#Printing instructed sentence


    # TODO:
    # fill in code here that:
    #   1. checks the second number to see if it is zero
    #   2. if the second number is zero, an exception is raised, the exception text must say exactly the following (make sure everything including casing and spaces match)
    #       I'm sorry, I can't divide by zero
    #   3. returns the quotient of first and second#


