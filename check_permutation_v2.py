# Check Permutation: 
# Given two strings, write a method to decide if one is a permutation of the other.

def checkPermutation(string, string2):
  permutation = "Is a permutation"
  notPermutation = "Is not a permutation"

  if (len(string) != len(string2)):
    print(notPermutation)
    return
  
  dictionary = {}
  listString = list(string)

  for char in listString:
    dictionary[char] = dictionary.get(char, 0) + 1

  for char in string2:
    if char not in dictionary or dictionary[char] == 0:
      print(notPermutation)
      return
    dictionary[char] -= 1
  
  print(permutation)

checkPermutation("Blash", "Blah")