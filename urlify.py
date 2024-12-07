# Write a method to replace all spaces in  a string '%20'. 
# You may assume that the string has sufficient space at the end
# to hold the additional characters, and that you given the 
# 'true' length of the string.

def urlify(url: str, trueLength: int):
  spaceCount = 0
  listUrl = list(url)

  for char in listUrl:
    spaceCount += 1 if char == ' ' else 0

  index = trueLength + (spaceCount * 2)
  listUrl = listUrl + [''] * spaceCount * 2

  for x in range(trueLength - 1, -1, -1):
    if (listUrl[x] == ' '):
      listUrl[index - 1] = '0'
      listUrl[index - 2] = '2'
      listUrl[index - 3] = '%'
      index -= 3
    else:
      listUrl[index - 1] = listUrl[x]
      index -= 1  
    
  return print(''.join(listUrl))


url = "My name is cat     "
urlify(url, len(url))