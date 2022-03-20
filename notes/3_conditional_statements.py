# if <somthing happens>:
#        <do something>
# elif <if something else happens that isn't the first condition>:
#        <do something (else)>
# elif ...
#        ....
# else <if something happens that doesn't meet previous criteria>
#        <do something (else)>



## EXAMPLE 1 ##
print()
print("EXAMPLE 1: ")

day = "Wednesday"

if day == "Monday":
        print("Today is Monday.")
elif day == "Tuesday":
        print("Today is Tuesday.")
elif day == "Wednesday":
        print("Today is Wednesday.")
elif day == "Thursday":
        print("Today is Thursday.")
elif day == "Friday":
        print("Today is Friday!")
else:
        print("It's the weekend!")

## EXAMPLE 1 ##



## EXAMPLE 2 ##
print()
print("EXAMPLE 2: ")

day = "Sunday"

if day == "Monday":
        print("Today is Monday.")
elif day == "Tuesday":
        print("Today is Tuesday.")
elif day == "Wednesday":
        print("Today is Wednesday.")
elif day == "Thursday":
        print("Today is Thursday.")
elif day == "Friday":
        print("Today is Friday!")
else:
        print("It's the weekend!")

# CARE: Anything else than Saturday and Sunday, also returns "It's the weekend"
# example: day = "Day" or day = "wwijwioaiofj" return "It's the weekend!"

## EXAMPLE 2 ##



# x == y - x is the same as y / x is equal to y
# x != y - x is differen than y / x isn't equal to y

# for int and float type only:
# x > y - x is bigger than y
# x < y - x is smaller than y
# x >= y - x is bigger than y or equal to y
# x <= y - x is smaller than y or equal to y

## EXAMPLE 3 ##
print()
print("EXAMPLE 3: ")

x = 1
y = 3

if x > y:
    print("x is bigger than y")
elif x == y:
    print("x is equal to y")
else:
    print("x is smaller than y")

## EXAMPLE 3 ##



# if <x> in <y> - checks if variable x is a part of variable y

## EXAMPLE 4 ##
print()
print("EXAMPLE 4: ")

text = "There were several attempts to change the schooling system in our country"

search = "school"

if search in text:
        print("Your key word:", search, "got found")
else:
        print("Your key word didn't get found")

search = "successful"

if search in text:
        print("Your key word: ", search, "got found")
else:
        print("Your key word:", search, "didn't get found")

## EXAMPLE 4 ##



# if <one conditon> and <second condition> - both conditions must be true at the same time
# if <one conditon> or <second condition> - one of the condition must be true

## EXAMPLE 5 ##
print()
print("EXAMPLE 5: ")

x = 1
y = 100

if x < y and x <= y:
        print(True)
else:
        print(False)

# both conditions are met

if x > y and x <= y:            
        print(True)
else:
        print(False)

# only second conditon is met

if x > y and x == y:            
        print(True)
else:
        print(False)

# no condtions are met


print()


x = 5
y = 5

if x >= y or x <= y:
        print(True)
else:
        print(False)

# both conditions are  met

if x == y or x < y:
        print(True)
else:
        print(False)

# only first condition is met

if x > y or x < y:
        print(True)
else:
        print(False)

# no conditions are met

## EXAMPLE 5 ##