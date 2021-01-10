def factorial_rec(i, val=1):
  if i == 1:
    return val
  return factorial_rec(i-1, val*i)
# recursive

def factorial_iter(x):
  for y in range(1, x):
    x *= y
  return x
# iterative
