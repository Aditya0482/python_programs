text=input("Enter any string you want to check palindrome : ")
rev=""

for char in text:
  rev = char + rev

if(text==rev):
  print(f"{text} is a palindrome")
else:
  print(f"{text} is not a palindrome")
