# String Compression: 
# Implement a method to perform basic string compression using the counts of repeated characters. 
# For example, the string aabccccaaa would become a2b1c5a3. 

# If the "compressed" string would not become smaller than the original string, your method should return
# the original string. You can assume the string has only uppercase and lowercase letters (a - z)

def compress_string(string: str) -> str:
  if not string:
    return string
  
  compressed = []
  count_consecutive = 1

  for i in range(1, len(string)):
    if string[i] == string[i - 1]:
      count_consecutive += 1
    else:
      compressed.append(string[i - 1] + str(count_consecutive))
      count_consecutive = 1

  compressed.append(string[-1] + str(count_consecutive))

  compressed_string = ''.join(compressed)

  return compressed_string if len(compressed_string < len(string)) else string