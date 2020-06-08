def sum(n):
  if n==1:
    return 1
  return n**2 + sum(n-1)
  
print(sum(5))

#2nd method

sum = lambda n: 1 if n==1 else n**2+sum(n-1)
print(sum(12))