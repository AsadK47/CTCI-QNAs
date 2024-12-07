def one_edit_away(string1: str, string2: str) -> bool:
  if abs(len(string1) - len(string2)) > 1:
    return False
  
  if len(string1) > len(string2):
    string1, string2 = string2, string1
  
  i, j = 0, 0
  found_difference = False

  while i < len(string1) and j < len(string2):
    if string1[i] != string2[j]:
      if found_difference:
        return False
      found_difference = True

      if len(string1) == len(string2):
        i += 1
    else:
      i += 1

    j += 1
  
  return True

print(one_edit_away("Cat", "Hat"))