"""
Class with different ways of qualifying the input.
"""


# input and check if int, return the int
def input_check_if_int(message):

    while True:
        string = input(message)
        try:
            int(string)
            return string
        except:
            print("Should be a whole number")


# input and check if number, return the number
def input_check_if_number(message):

    while True:
        string = input(message)
        try:
            float1 = float(string)
            return float1
        except:
            print("Should be a digit")


# prints amount of numbers in the string
def check_for_numbers():
    number_of_numbers = 0
    last_was_digit = False
    input1 = input("Enter string with letters:")
    for char in input1:
        if char.isdigit() and last_was_digit is False:
            number_of_numbers += 1
            last_was_digit = True
        elif not char.isdigit():
            last_was_digit = False
    if number_of_numbers > 0:
        print("There", "is a number" if number_of_numbers == 1 else "are " + str(number_of_numbers) + " numbers",
              "in the string.")
    else:
        print("no numbers in string")


# compares input with argument strings, and if correct, returns the input
def input_compare_w_string(message, return_message, strings):
    while True:
        user_input = input(message)
        if user_input not in strings:
            print("Incorrect input.")
            continue
        else:
            print(return_message)
            return user_input
