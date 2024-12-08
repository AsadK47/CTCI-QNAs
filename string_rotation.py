# String Rotation: 
# Assume you have a method isSubstring which checks if one word is a substring of another. 
# Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using only one call to isSubstring 
# (e.g.,"waterbottle"is a rotation of "erbottlewat"

def is_rotation(s1, s2):
  if len(s1) != len(s2):
    return False
  
  concatenated = s1 + s1
  return isSubstring(concatenated, s2)

def isSubstring(s1, s2):
  return s2 in s1

print(is_rotation("waterbottle", "erbottlewat"))