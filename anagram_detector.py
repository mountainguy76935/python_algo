def find_ana(a, b):
  for letter in a:
    if letter not in b:
      return False
    b =b.replace(letter, '', 1)
  if not b:
    return True
  return False
