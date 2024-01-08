# Given an int n, return True if it is within 10 of 100 or 200. Note: abs(num) computes the absolute 
# value of a number.


# near_hundred(93) → True
# near_hundred(90) → True
# near_hundred(89) → False

# Source: codingbat.com

def near_hundred(n):
  return abs(n - 100) <= 10 or abs(n - 200) <= 10