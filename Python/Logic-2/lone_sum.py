# Given 3 int values, a b c, return their sum. However, if one of the values is the same as another of the 
# values, it does not count towards the sum.


# lone_sum(1, 2, 3) → 6
# lone_sum(3, 2, 3) → 2
# lone_sum(3, 3, 3) → 0

# Source: codingbat.com

def lone_sum(a, b, c):
  a_1 = a 
  b_1 = b 
  c_1 = c
  if a == b:
    a_1 = 0
    b_1 = 0
  if a == c:
    a_1 = 0
    c_1 = 0
  if b == c:
    b_1 = 0
    c_1 = 0
  return a_1 + b_1 + c_1