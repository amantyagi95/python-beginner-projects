s = input("str")
s1 =""
i=0
for j in s:
  if s.index(j)==i:
    s1 +=j
  i+=1
  
print(s1)