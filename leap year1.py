#python 3.7.1
n = int(input(" enter a year"))
result = "leap year" if n%400==0 else "leap year" if n%4 ==0 and n%100 !=0 else "non leap year"
print(result)