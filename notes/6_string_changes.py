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
