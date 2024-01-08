# Return True if the given string contains an appearance of "xyz" where the xyz is not directly preceeded 
# by a period (.). So "xxyz" counts but "x.xyz" does not.


# xyz_there('abcxyz') → True
# xyz_there('abc.xyz') → False
# xyz_there('xyz.abc') → True

# Source: codingbat.com

def xyz_there(str):
  if len(str) <= 2:
    return False
  elif str[0] == ".":
    return xyz_there(str[2:])
  elif str[0:3] == "xyz":
    return True
  return xyz_there(str[1:])