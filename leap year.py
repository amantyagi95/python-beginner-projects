n =int(input("enter a year"))
if n % 400 == 0 :
  print(" n: is a leap year")
else: 
  if n%4==0 and n%100 != 0 :
      print("n : is a Leap year")
  else:
    print("n: not a leap year")