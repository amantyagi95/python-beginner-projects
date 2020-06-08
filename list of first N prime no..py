def nextprime(n):
  while True:
    n +=1
    for i in range(2,n):
      if n%i==0 :
        break
    else :
      return n
      
def prime_no(N):
   nun,c= 1,1
   while c<=N:
     nun = nextprime(nun)
     yield  nun 
     c +=1
no=int(input("enter N no.:"))     
print(list(prime_no(no)))