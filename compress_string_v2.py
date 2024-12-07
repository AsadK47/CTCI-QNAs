# String Compression: 
# Implement a method to perform basic string compression using the counts of repeated characters. 
# For example, the string aabccccaaa would become a2b1c5a3. 

# If the "compressed" string would not become smaller than the original string, your method should return
# the original string. You can assume the string has only uppercase and lowercase letters (a - z)

def compress_string(string: str) -> str:
  sorted_string = ''.join(sorted(string))

  compressed = []
  count = 1

  for i in range(1, len(sorted_string)):
    if sorted_string[i] == sorted_string[i - 1]:
      count += 1
    else:
      compressed.append(f"{sorted_string[i - 1]}{count}")
      count = 1

  compressed.append(f"{sorted_string[-1]}{count}")

  compressed_string = ''.join(compressed)

  return compressed_string if len(compressed_string) < len(string) else string