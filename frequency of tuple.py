n= (input(""))
t=tuple(n)
print (t)
j= 0
for i in t:
  if t.index(i)==j:
    print(i,t.count(i))
  j += 1