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