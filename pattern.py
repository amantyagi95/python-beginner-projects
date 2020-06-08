for i in range(1,5):
  for j in range(1,5):
    if j<=i:
      print(j,end='')
    else:
      print(" ",end='')
  print()
 
 
print(" ")
 
for i in range(1,5):
  for j in range(1,8):
    if j>=5-i and j<=3+i :
      print("*",end='')
    else:
      print(" ",end='')
  print()
    
print("")  
   
   
for i in range(1,5):
  for j in range(1,8):
    if j<=5-i or j>=3+i :
      print("*",end='')
    else:
      print(" ",end='')
  print()
    
 
print("")


