import string


def characters_between(letter_range):

    first_letter, last_letter = letter_range.split('-')

    all_letters = string.ascii_letters

    first_index = all_letters.index(first_letter)
    last_index = all_letters.index(last_letter)
    result = all_letters[first_index:last_index + 1]
    return result

input_range = input("Введіть дві літери через дефіс: ")
output = characters_between(input_range)
print(output)