"""
You are given a non-empty array that represents the digits of a non-negative integer.

Write a function that increments the number by 1.

The digits are stored so that the digit representing the most significant place value is at the beginning of the array. Each element in the array only contains a single digit.

You will not receive a leading 0 in your input array (except for the number 0 itself).

Example 1:

Input: [1,3,2]
Output: [1,3,3]
Explanation: The input array represents the integer 132. 132 + 1 = 133.

Example 2:

Input: [3,2,1,9]
Output: [3,2,2,0]
Explanation: The input array represents the integer 3219. 3219 + 1 = 3220.

Example 3:

Input: [9,9,9]
Output: [1,0,0,0]
Explanation: The input array represents the integer 999. 999 + 1 = 1000.
"""

# UNACCEPTABLE SOLUTION
# def plus_one(digits):
#     # Your code here
#     # Convert array to strings - List comprehension
#     strings = [str(integer) for integer in digits]
#     print("STRINGS", strings)
#     # Join all strings in array together
#     a_string = "".join(strings)
#     print("A STRING", a_string)
#     # Convert string to integer
#     an_integer = int(a_string)
#     print("AN INTEGER", an_integer)
#     # Add 1 to integer
#     res = an_integer + 1
#     # Turn integer to array - List comprehension
#     return [int(integer) for integer in str(res)]

# print(plus_one([9,9,9])) 

# PLAN
# Loop until: the current number is not 9 
# if the current number is 9:
# set digits[index] = 0
# repeat with the previous number
# if it's not 9:
# add 1 to digits [index]

def plus_one(digits):
    index = len(digits) - 1
    # PLAN
        # loop until: the current number is not a 9 --> while the current number is 9
    while index >= 0 and digits[index] == 9:

        # If the number is a 9:
        # make it zero, and repeat w/ previous number
        # set digits[i] to 0
        digits[index] = 0
        # decrement index
        index -= 1
    # else if it's not a 9:
        # add 1 to digits[i]
# if we get to the first number (index == 0) and it's not a 9, make it a 10 (insert 1 at the 0th index)
    if index == -1:
        digits.insert(0,1)
    else:
        digits[index] += 1
    return digits

    # Add 1 to the last number if it's not a 9
    # if it is a 9, makei t a zero, and then repeat with the second to last number
    # If the first number is 9 make it a

print(plus_one([9,9,9]))
