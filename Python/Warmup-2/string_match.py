# Given 2 strings, a and b, return the number of the positions where they contain the same length 2 
# substring. So "xxcaazz" and "xxbaaz" yields 3, since the "xx", "aa", and "az" substrings appear in 
# the same place in both strings.


# string_match('xxcaazz', 'xxbaaz') → 3
# string_match('abc', 'abc') → 2
# string_match('abc', 'axc') → 0

# Source: codingbat.com

def string_match(a, b):
  if len(a) <= 1 or len(b) <= 1:
    return 0
  elif a[0:2] == b[0:2]:
    return 1 + string_match(a[1:], b[1:])
  else:
    return string_match(a[1:], b[1:])