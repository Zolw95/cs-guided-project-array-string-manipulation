"""
Given an array of integers `nums`, define a function that returns the "pivot" index of the array.

The "pivot" index is where the sum of all the numbers on the left of that index is equal to the sum of all the numbers on the right of that index.

If the input array does not have a "pivot" index, then the function should return `-1`. If there are more than one "pivot" indexes, then you should return the left-most "pivot" index.

Example 1:

Input: nums = [1,7,3,6,5,6]
Output: 3
Explanation:
The sum of the numbers to the left of index 3 (1 + 7 + 3 = 11) is equal to the sum of numbers to the right of index 3 (5 + 6 = 11).
Also, 3 is the first index where this occurs.

Example 2:

Input: nums = [1,2,3]
Output: -1
Explanation:
There is no index that satisfies the conditions in the problem statement.
"""
#UPER
#UNDERSTAND
# - don't include the actual index in either of the sums
# - Would a signer number return itself or -1? let's just assume -1

# PLAN:
# Default return variable is -1
# if nums is empty or size 1, return -1

# left = 0
# right = sum(nums)
# iterate through the array
#   add nums[i] to left_side_sum
#   right side = sum of the array - left - nums[i]
#   compare, and if they are the same, return i
#
# How / where do we calculate the right side sum?       

# The most straightforward:
# iterate through
# for each index, sum up the left side and right side and compare
def pivot_index(nums):
    # Your code here
    left_sum = 0
    right_sum = 0
    array_length = len(nums)
    #Get the left sum
    for i in range(array_length):
        left_sum = 0
        right_sum = 0

        # get left sum
        for j in range(i):
            left_sum += nums[j]
        
        # get right sum
        for j in range(i + 1, array_length):
            right_sum += nums[j]

        # if leftsum and rightsum are same,
        # then we are done
        if left_sum == right_sum:
            return i
        
    # return -1 if no index is found
    return -1

nums = [1,7,3,6,5,6]
print(pivot_index(nums))


def pivor_index(nums):
    for i in range(len(nums)):
        # for each index, sum up the left side and the right side and compare
        left_sum = sum(nums[0:1])
        right_sum = sum(nums[i+1:])
        if left_sum == right_sum:
            return i
nums = [1,7,3,6,5,6]
print(pivot_index(nums))
    
# TRY 3:
if len(nums) <= 1:
    return -1
# left = 0
left = 0
# right = sum of the entire array
right = sum(nums)
# iterate through the array
# We want the index, so use range
for i in range(len(nums)):
#   right side = sum of the entire array - left - nums[i]
    right -= nums[i]
# compare and check if they are the same
    if left == right:
        return i
#   add nums[i] to the left_side_sum
    left += nums[i]
#   compare, and if they are the same, return i

print(pivot_index([1,7,3,6,5,6]))
