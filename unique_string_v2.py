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
