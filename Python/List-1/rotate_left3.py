# Given an array of ints length 3, return an array with the elements "rotated left" so {1, 2, 3} 
# yields {2, 3, 1}.


# rotate_left3([1, 2, 3]) → [2, 3, 1]
# rotate_left3([5, 11, 9]) → [11, 9, 5]
# rotate_left3([7, 0, 0]) → [0, 0, 7]

# Source: codingbat.com

def rotate_left3(nums):
  new_nums = nums[1:]
  new_nums.append(nums[0])
  return new_nums