# def <function name>(<any number of variables needed to complete this function>) - defines a new function
# function must be defined before we use it

## EXAMPLE 1 ##
print()
print("EXAMPLE 1: ")

def count_symbols(variable):
    answer = len(variable)
    return answer

# function uses pre-defined function len() to count symbols

print(count_symbols("Any sentence I want"))

# calls a function count_symbols which returns counted number of symbols in sent variable

## EXAMPLE 1 ##



## EXAMPLE 2 ##
print()
print("EXAMPLE 1: ")

def loop (string, iterations):
    for x in range (iterations):
        print(string)

# function loop prints variable <string> <iteration> amount of times

loop("This is a loop", 7)

# prints "This is a loop" 7 times

## EXAMPLE 2 ##
