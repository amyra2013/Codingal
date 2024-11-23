numm=int(input("Enter a number"))
flag=False
for x in range(2,numm):
 if   numm%x==0:
  flag=True
  break
 
if flag:
 print("This number is a composite number")
else:
 print("This number is a prime number") 

