def checkString(string):
  stringAsList = list(string)
  stringAsList.sort()

  for i in range(len(string) - 1):
    if (stringAsList[i] == stringAsList[i + 1]):
      return False
    
  return True

if checkString("broski") == True:
  print("String is unique")
else:
  print("String is not unique")