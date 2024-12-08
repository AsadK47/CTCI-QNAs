# Check Permutation: 
# Given two strings, write a method to decide if one is a permutation of the other.

def checkPermutation(s1, s2):
  permutation = "Is a permutation"
  notPermutation = "Is not a permutation"

  if (len(s1) != len(s2)):
    print(notPermutation)
    return 
  
  s1Set = set(list(s1.lower()))
  s2Set = set(list(s2.lower()))

  if (s1Set == s2Set):
    print(permutation)
  else:
    print(notPermutation)


checkPermutation("Dog", "Dog") 
checkPermutation("Dog", "dog") 
checkPermutation("dog", "cat")  
checkPermutation("dogcatdog", "dogdogcat")
