# Author: Kristin Towns
# GitHub username: kristinlashun
# Date: November 24th, 2023
# Description: This program contains a function count_letters that takes a string as input 
# and returns a dictionary tabulating how many of each letter is in that string. 
# The keys of the dictionary are upper-case letters.

def count_letters(input_string):
    """
    Counts the occurrences of each letter in a given string and returns a dictionary.

    The function counts both lower-case and upper-case versions of a letter as part of the same count.
    The keys in the resulting dictionary are upper-case letters. Non-letter characters are ignored.
    If a letter does not appear in the string, it is not added to the dictionary.

    :param input_string: The string to be analyzed.
    :return: A dictionary with upper-case letters as keys and their counts as values.
    """
    letter_counts = {}

    for char in input_string:
        # Check if the character is a letter and ignore non-letter characters
        if char.islower() or char.isupper():
            # Convert character to upper-case
            upper_char = char.upper()
            # Count the letter
            if upper_char in letter_counts:
                letter_counts[upper_char] += 1
            else:
                letter_counts[upper_char] = 1

    return letter_counts


