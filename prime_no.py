count=0
num=int(input("Enter the number : "))
for i in range(1,num+1):
  if num%i==0:
    count+=1
if count==2:
  print(f" {num} is prime number")
else:
  print(f"{num} is not a prime number")
