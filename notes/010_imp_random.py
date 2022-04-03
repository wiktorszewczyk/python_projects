import random

# random.choice(<list>) - chooses random variable from a list (string)

## EXAMPLE 1 ##
print()
print("EXAMPLE 1: ")

variables_list = ["string", True, 123, 3.14, [1, 2, 3]]

print(random.choice(variables_list))
print(random.choice(variables_list))
print(random.choice(variables_list))

# returns random variable from a list thrice

## EXAMPLE 1 ##



# random.sample(<list>, <number of samples>) - takes number of samples of random variables from a list (string)

## EXAMPLE 2 ##
print()
print("EXAMPLE 2: ")

letters = "abcdef"

print(random.sample(letters, 3))
print(random.sample(letters, 3))
print(random.sample(letters, 5))
print(random.sample(letters, 5))

# returns a list of 3, 3, 5, 5 random variables

## EXAMPLE 2 ##
