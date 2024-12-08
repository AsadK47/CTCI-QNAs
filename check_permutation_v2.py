# Check Permutation: 
# Given two strings, write a method to decide if one is a permutation of the other.

def checkPermutation(s1, s2):
  permutation = "Is a permutation"
  notPermutation = "Is not a permutation"

  if (len(s1) != len(s2)):
    print(notPermutation)
    return
  
  dictionary = {}
  listString = list(s1)

  for char in listString:
    dictionary[char] = dictionary.get(char, 0) + 1

  for char in s2:
    if char not in dictionary or dictionary[char] == 0:
      print(notPermutation)
      return
    dictionary[char] -= 1
  
  print(permutation)

checkPermutation("Permutation", "MutationPer")