def palindrome_permutation(string: str) -> bool:
  char_count = {}

  for char in string:
    if char.isalpha():
      char = char.lower()
      if char in char_count:
        char_count[char] += 1
      else:
        char_count[char] = 1
  
  odd_count = 0
  for count in char_count.values():
    if count % 2 != 0:
      odd_count += 1
    
    if odd_count > 1:
      return False
  
  return True

print(palindrome_permutation("racecar"))
print(palindrome_permutation("bracecar"))