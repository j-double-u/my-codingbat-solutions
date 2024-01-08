# Return the number of times that the string "hi" appears anywhere in the given string.


# count_hi('abc hi ho') → 1
# count_hi('ABChi hi') → 2
# count_hi('hihi') → 2

# Source: codingbat.com

def count_hi(str):
  if len(str) <= 1:
    return 0
  if str[0:2] == "hi":
    return 1 + count_hi(str[2:])
  return count_hi(str[1:])