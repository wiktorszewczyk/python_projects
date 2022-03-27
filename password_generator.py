import random
import string
import math

def password_generator():
    # SYMBOLS
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits 
    punctuation = string.punctuation

    letters = string.ascii_letters
    all_symbols = letters + digits + punctuation


    # PASSWORD OPTIONS
    number_of_symbols = 20

    # minimum percentage
    percentage_of_lowercase = 0.1
    percentage_of_uppercase = 0.1
    percentage_of_digits = 0.1
    percentage_of_punctuation = 0.1

    # PASSWORD GENERATOR

    # lowercase
    number_of_lowercase = math.floor(number_of_symbols * percentage_of_lowercase)

    if number_of_lowercase > len(lowercase):
        multipier = number_of_lowercase // len(lowercase)

        lowercase = lowercase * (multipier + 1)

    generated_lowercase = random.sample(lowercase, number_of_lowercase)


    # uppercase 
    number_of_uppercase = math.floor(number_of_symbols * percentage_of_uppercase)

    if number_of_uppercase > len(uppercase):
        multipier = number_of_uppercase // len(uppercase)

        uppercase = uppercase * (multipier + 1)

    generated_uppercase = random.sample(uppercase, number_of_uppercase)


    # digits
    number_of_digits = math.floor(number_of_symbols * percentage_of_digits)

    if number_of_digits > len(digits):
        multipier = number_of_digits // len(digits)

        digits = digits * (multipier + 1)

    generated_digits = random.sample(digits, number_of_digits)


    # punctuation
    number_of_punctuation = math.floor(number_of_symbols * percentage_of_punctuation)

    if number_of_punctuation > len(punctuation):
        multipier = number_of_punctuation // len(punctuation)

        punctuation = punctuation * (multipier + 1)

    generated_punctuation = random.sample(punctuation, number_of_punctuation)


    # other (mix)
    number_of_other = number_of_symbols - (number_of_lowercase + number_of_uppercase + number_of_digits + number_of_punctuation)

    if number_of_other > len(all_symbols):
        multipier = number_of_other // len(all_symbols)

        all_symbols = all_symbols * (multipier + 1)

    generated_other = random.sample(all_symbols, number_of_other)

    # generate
    generated_symbols = generated_lowercase + generated_uppercase + generated_digits + generated_punctuation + generated_other

    generated_password = random.sample(generated_symbols, number_of_symbols)

    password = ''.join(generated_password)

    return(password)


# TESTS
print(password_generator())
