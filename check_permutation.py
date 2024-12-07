def checkPermutation(string1, string2):
  permutation = "Is a permutation"
  notPermutation = "Is not a permutation"

  if (len(string1) != len(string2)):
    print(notPermutation)
    return 
  
  s1Set = set(list(string1.lower()))
  s2Set = set(list(string2.lower()))

  if (s1Set == s2Set):
    print(permutation)
  else:
    print(notPermutation)


checkPermutation("Dog", "Dog") 
checkPermutation("Dog", "dog") 
checkPermutation("dog", "cat")  
checkPermutation("dogcatdog", "dogdogcat")
