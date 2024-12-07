# Palindrome Permutation: 
# Given a string, write a function to check if it is a permutation of a palin-drome. 
# A palindrome is a word or phrase that is the same forwards and backwards. 
# A permutation is a rearrangement of letters. 
# The palindrome does not need to be limited to just dictionary words.

# EXAMPLE
# Input:
# Tact Coa
# Output:
# True (permutations: "taco cat", "atco cta", etc.)

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