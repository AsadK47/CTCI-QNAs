# URLify: 
# Write a method to replace al spaces in a string with '%20. 
# You may assume that the string has sufficient space at the end to hold the additional characters, 
# and that you are given the "true" length of the string. 

# (Note: If implementing in Java, please use a character array so 
# that you can perform this operation in place.)

# EXAMPLE
# Input:
# "Mr John Smith    ", 13 
# Output: "Mr%20John%20Smith"

def urlify(string):
  newString = string.replace(' ', "%20")
  print(newString)

# This version doesn't account for the spaces that need to be used and calculated to determine
# space and percentages

