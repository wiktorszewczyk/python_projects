# x.replace(<something to be replaced>, <something to be replaced with>) - replaces variable <something to be replaced> with <something to be replaced with> in variable x

## EXAMPLE 1 ##
print()
print("EXAMPLE 1: ")

longstring = "words/divided/with/forward/slashes"

words = longstring.replace("/", " ")
print(words)
words = words.replace("forward", "spaces")
print(words)

words = words.replace("slashes", "")
print(words)

## EXAMPLE 1 ##



# x.strip() - deletes whitespaces character like " ", \n (new line/enter)

## EXAMPLE 2 ##
print()
print("EXAMPLE 2: ")

text = "\n \n \n                     text       \n \n \n"
print("Old text:")
print(text)

print("New text:")
text = text.strip()
print(text)

## EXAMPLE 2 ##



# x.upper() - changes all letters in x to UPPER_CASE
# x.lower() - changes all leters in x to lower_case

## EXAMPLE 3 ##
print()
print("EXAMPLE 3: ")

string = "SOmE ranDOm COmBinaTion OF lowER aNd UPPer cAsE"

print(string.upper())
print(string.lower())

## EXAMPLE 3 ##



# x.join(<list>) - adds to string x each variable in <list> and combines the results in order they are set in list

## EXAMPLE 4 ##
print()
print("EXAMPLE 4: ")

letters_list = ['a', 'b', 'c', 'd']

x = "||"
x = x.join(letters_list)

print(x)

y = ''.join(letters_list)

print(y)

## EXAMPLE 4 ##
