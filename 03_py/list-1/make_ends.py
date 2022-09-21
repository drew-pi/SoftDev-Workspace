# https://codingbat.com/prob/p124806

"""
Given an array of ints, return a new array length 2 containing the first and
last elements from the original array. The original array will be length 1 or
more.
"""
def make_ends(nums):
  return [nums[0]] + [nums[-1]] # Cast both first and last elements to a list so you can concatenate them together

    

# test cases: do not edit
print(make_ends([1, 2, 3])) # [1, 3]
print(make_ends([1, 2, 3, 4])) # [1, 4]
print(make_ends([7, 4, 6, 2])) # [7, 2]

