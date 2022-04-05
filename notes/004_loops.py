# for <variable> in <some range>:
#       <do something for each variable until it reaches the end of set range>

## EXAMPLE 1 ##
print()
print("EXAMPLE 1: ")

for x in range(6):  
    print(x)

# prints variable x in range of 6 numbers starting with 0 as default

## EXAMPLE 1 ##



## EXAMPLE 2 ##
print()
print("EXAMPLE 2: ")

for y in range(10):
    print(y+1)

# this way we get numbers listed in order normally

## EXAMPLE 2 ##



# continue - moves to next iteration instantly
# break - breaks the loop
# return(<variable>) - breaks the loop and returns variable

## EXAMPLE 3 ##
print()
print("EXAMPLE 3: ")

for z in range(5):
    
    if z == 3:
        continue
    
    print (z+1)

# skips 6th iteration, which means that number 4 isn't printed

## EXAMPLE 3 ##



## EXAMPLE 4 ##
print()
print("EXAMPLE 4: ")

for a in range(5):

    if a == 3:
        break

    print(a+1)

# stops before doing 3rd iteration tasks, which means that numbers after 3 aren't printed

## EXAMPLE 4 ## 



## EXAMPLE 5 ##
print()
print("EXAMPLE 5: ")

for b in range(5):

    print(b+1)

    if b == 3:
        break

# stops after doing 3rd iteration tasks, which means that numbers after 4 aren't printed

## EXAMPLE 5 ##
