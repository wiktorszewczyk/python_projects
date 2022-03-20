# list = [<element1>, <element2>, <element3>]
# <element> can be of any type and can repeat itself
# each element is assigned to a specific number (starting from 0!) in order they are set in a list f.e. list[1] is equal to <element2>

## EXAMPLE 1 ##
print()
print("EXAMPLE 1: ")

list1 = [1, "text", 3.14, "string", 1, True, 1+3j]

for element in list1:
    print(element, " - ",  type(element))

# prints each element of list1 and its type in order they are set in list1

## EXAMPLE 1 ##



## EXAMPLE 2 ##
print()
print("EXAMPLE 2: ")

string = "some text"

for letter in string: 
    print(letter)

# string can be used as a list in which every single character is a single element

## EXAMPLE 2 ##



## EXAMPLE 3 ##
print()
print("EXAMPLE 3: ")

list = ["number1", "number2", "number3", "Easter Egg"]

for x in range(3):
    print (list[x])

# prints elements assigned to 0, 1 and 2

# to print Easter Egg we have to use:
print()
print(list[3])
# or change the range of list CARE: don't make the range bigger then lists size!!

## EXAMPLE 3 ##



# x.split(<repeating element>) - splits variable x when encounters <repeating element> creating a list

## EXAMPLE 4 ##
print()
print("EXAMPLE 4: ")

longstring = "some/text/divided/with/forward/slash"

word_list = longstring.split("/")

for word in word_list:
    print(word)

# prints all elements of word_list created by .split() function

print()
print (word_list[2])
# prints element assigned to 2 (3rd element) from list word_list created by .split() function

## EXAMPLE 4 ##



# x.replace(<something to be replaced>, <something to be replaced with>) - replaces variable <something to be replaced> with <something to be replaced with> in variable x

## EXAMPLE 5 ##
print()
print("EXAMPLE 5: ")

words = longstring.replace("/", " ")
print(words_divided_with_spaces)

words = words.replace("forward", "spaces")
print(words_divided_with_spaces)

words = words.replace("slash", "")

print()
print(words_divided_with_spaces)

word_list2 = words.split(" ")

for word in word_list2:
    print(word)

## EXAMPLE 5 ##
