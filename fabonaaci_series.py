a = 0
b = 1

num = int(input("Enter the number you want to print series: "))

print("Fibonacci Series.........!!")

for i in range(num):
    print(a, end=" ")
    c = a + b
    a = b
    b = c
