# Is Unique: 
# Implement an algorithm to determine if a string has all unique characters. 
# What if you cannot use additional data structures?

def checkStringAgain(string):
  uniqueList = []

  stringAsList = list(string)

  for char in stringAsList:
    if char not in uniqueList:
      uniqueList.append(char)

  if (uniqueList == stringAsList):
    print("String is unique")
  else:
    print("String is not unique")


checkStringAgain("that")
