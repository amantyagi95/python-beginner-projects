n =(30,4.5,23,4.7,'sty',True,1+6j,1-1j)
t1,t2,t3,t4,t5=[],[],[],[],[]
for e in n:
  if type(e)==int:
    t1.append(e)
  elif type(e)==float:
    t2.append(e)
  elif type(e)==str:
    t3.append(e)
  elif type(e)==complex:
    t4.append(e)
  elif type(e)==bool:
    t5.append(e)
    
t1=tuple(t1)
t2=tuple(t2)
t3=tuple(t3)
t4=tuple(t4)
t5=tuple(t5)
print(t1,t2,t3,t4,t5 ,sep='\n')