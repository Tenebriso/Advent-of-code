def get_number_to_right(engine, i, j):
  number = engine[i][j]
  length = 1
  while j + length < len(engine[i]) and engine[i][j+length].isdigit():
      number = number + engine[i][j+length]
      length += 1
  return int(number)

print(get_number_to_right([['1','2','*']], 0, 2))
