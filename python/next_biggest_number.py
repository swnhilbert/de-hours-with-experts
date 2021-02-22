#!/usr/bin/python3
import sys

def main():
    next_biggest_number(sys.argv[1])


def next_biggest_number(num):
    """
    Given a number, output the next largest number using the same digits.

    Args:
        num: value to get next largest number of

    """
    # Split the number to make comparisons easier
    split_num = [int(str_digit) for str_digit in str(num)]

    # Get a list of digits to rearrange
    seen_digits = [split_num[-1]]

    # Get the index to start replacing digits
    replace_idx = -1
    for i, digit in enumerate(split_num[-2::-1]):
        seen_digits.append(digit)
        if digit < max(seen_digits):
            # This is odd because it's looking at digits in reverse order
            replace_idx = len(split_num) - 2 - i
            break

    # If the index hasn't been updated, then there is no next biggest number
    if replace_idx == -1:
        return -1

    # Keep the first part of the original number until needing to replace
    next_biggest_number = [digit for digit in split_num[:replace_idx]]

    # Order the seen digits from least to greatest
    seen_digits.sort()

    # Once the first next largest digit was found, save it and break from the loop
    next_biggest_idx = -1
    for i, digit in enumerate(seen_digits):
        if digit > split_num[replace_idx]:
            next_biggest_idx = i
            break

    # Add the next biggest digit to the next biggest number
    next_biggest_number.append(seen_digits[next_biggest_idx])

    # Remove the occurrence of the next biggest digit
    del seen_digits[next_biggest_idx]

    # Since the seen digits are ordered, just concat the lists
    next_biggest_number = next_biggest_number + seen_digits

    # Join the numbers together and return
    return int(''.join([str(digit) for digit in next_biggest_number]))

if __name__ == "__main__":
    main()



