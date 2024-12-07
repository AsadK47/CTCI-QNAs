# Is Unique: 
# Implement an algorithm to determine if a string has all unique characters. 
# What if you cannot use additional data structures?

def checkString(string):
  dictionary = {}
  stringAsList = list(string)

  for char in stringAsList:
    if char in dictionary.keys():
      print("String is not unique")
      return

    dictionary[char] = 1

  print("String is unique")

checkString("Dog")