import random
import string

def password_generator()
    # SYMBOLS
    letters = string.ascii_letters # lower and upper case
    digits = string.digits 
    punctuation = string.punctuation
    # lowercase = string.ascii_lowercase
    # uppercase = string.ascii_uppercase

    all_symbols = letters + digits + punctuation


    # PASSWORD OPTIONS
    number_of_symbols = 24

    if number_of_symbols > len(all_symbols):
        number_of_symbols = len(all_symbols)
    elif number_of_symbols == 0:
        number_of_symbols = 1

    # OLD BASIC VERSION OF PASSWORD GEN
    # generated_symbols1 = random.sample(all_symbols, number_of_symbols)

    # password1 = ''.join(generated_symbols1)

    # PASSWORD GENERATOR
    number_of_letters = number_of_symbols // 2                                              # MAX: ~50%

    if number_of_letters > len(letters):
        number_of_letters = len(all_symbols)
    elif number_of_letters == 0:
        number_of_letters = 1

    number_of_digits = number_of_symbols // 4                                               # MAX: ~25%

    if number_of_digits > len(digits):
        number_of_digits = len(digits)
    elif number_of_digits == 0:
        number_of_digits = 1

    number_of_punctuation = number_of_symbols - number_of_letters - number_of_digits        # MIN: ~25% (remaining amount)

    if number_of_punctuation> len(punctuation):
        number_of_punctuation = len(punctuation)
    elif number_of_punctuation == 0:
        number_of_punctuation = 1

    generated_sample = random.sample(letters, number_of_letters) + random.sample(digits, number_of_digits) + random.sample(punctuation, number_of_punctuation)

    generated_symbols = random.sample(generated_sample, number_of_symbols)

    password = ''.join(generated_symbols)

    return password

    # TESTS
    # print(generated_symbols1)
    # print(password1)

    # print()
    # print(generated_sample)
    # print(generated_symbols)
    # print(password)

    # values
    # print(len(all_symbols))
    # print(number_of_symbols)
    # print()
    # print(len(letters))
    # print(number_of_letters)
    # print()
    # print(len(digits))
    # print(number_of_digits) 
    # print()
    # print(len(punctuation))
    # print(number_of_punctuation)
