def reverse(old_str):
  new_str = ''
  middle = floor(len(old_str)/2)
  for x in range(0, middle):
    new_str+=old_str[(x+1)*-1]
  if new_str == old_str[0:middle]:
    return True
  return False
