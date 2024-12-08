# One Away: 
# There are three types of edits that can be performed on strings: 
# insert a character, remove a character, or replace a character. 
# Given two strings, write a function to check if they are one edit (or zero edits) away.

# EXAMPLES
# pale, ple -> true
# pales, pale -› true
# pale, bale ›- true
# pale, bake →› false

def one_edit_away(s1: str, s2: str) -> bool:
  if abs(len(s1) - len(s2)) > 1:
    return False
  
  if len(s1) > len(s2):
    s1, s2 = s2, s1
  
  i, j = 0, 0
  found_difference = False

  while i < len(s1) and j < len(s2):
    if s1[i] != s2[j]:
      if found_difference:
        return False
      found_difference = True

      if len(s1) == len(s2):
        i += 1
    else:
      i += 1

    j += 1
  
  return True

print(one_edit_away("Cat", "Hat"))