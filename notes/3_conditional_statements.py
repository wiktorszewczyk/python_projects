# if <somthing happens>:
#        <do something>
# elif <if something else happens that isn't the first condition>:
#        <do something (else)>
# elif ...
#        ....
# else <if something happens that doesn't meet previous criteria>
#        <do something (else)>

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

# x == y - x is the same as y / x is equal to y
# x != y - x is differen than y / x isn't equal to y

# for int and float type only:
# x > y - x is bigger than y
# x < y - x is smaller than y
# x >= y - x is bigger than y or equal to y
# x <= y - x is smaller than y or equal to y

x = 1
y = 3

if x > y:
    print("x is bigger than y")
elif x == y:
    print("x is equal to y")
else:
    print("x is smaller than y")
