def string_bits(str):
  s=""
  for i in range(len(str)):
    if i % 2 == 0:
      s = s + str[i]
  return s