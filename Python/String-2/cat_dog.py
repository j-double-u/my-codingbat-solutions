# Return True if the string "cat" and "dog" appear the same number of times in the given string.


# cat_dog('catdog') → True
# cat_dog('catcat') → False
# cat_dog('1cat1cadodog') → True

# Source: codingbat.com

def cat_dog(str):
  count = 0
  for i in range(len(str) - 2):
    if str[i:i+3] == "cat":
      count += 1
    elif str[i:i+3] == "dog":
      count -= 1
  return count == 0