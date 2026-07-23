li=[]
num=int(input("Enter the n numbers : "))

for n in range(num):
  numbers=int(input("Enter the numbers : "))
  li.append(numbers)

print("Maximum number is : ",max(li))
print("Minimum number is : ",min(li))
