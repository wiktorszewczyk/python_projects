# - Starts a comment, which is skipped by the code compiler 

# print(<something>)       
# prints <something>, which can be a variable of any type, in console           

print("text")
print(1)

number = 10
print(number)

string = "something"
print(string)

print(string, "and some text")      
# prints two variables next to each other, dividing them by default with space

string1 = "Hello"
string2 = "World!"
print(string1, string2)


# type(<variable>)        
# returns data type of variable

variable = "some text"
print(type(variable))       
# prints the data type of variable returned by the function type()

print(type("text"))
print(type(1))
print(type(3.14))
print(type(3j+1))


# import <library           
# imports a <library> to code f.e. import code.py - import code.py whichc means we can use all of its variables and functions


# Built-in mathematical operators:
# (+) - addition f.e. 2+2 return 4
# (-) - subtraction f.e. 4-2 return 2
# (*) - multiplication f.e. 3*4 returns 12
# (/) - division
# examples: 16/2 returns 8, 15/2 returns 7 BUT: (15.0/2), (15/2.0), (15.0/2.0) return 7.5, it depends it wanted variable if of int or float type
# (**) - power f.e. 2**5 returns 32
# (%) - modulo (returns a reminder)
# examples: 16%2 returns 0, 13%2 returns 2, 19%4 returns 3;