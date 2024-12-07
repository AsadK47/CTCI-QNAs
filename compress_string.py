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