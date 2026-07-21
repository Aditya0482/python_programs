def fact(num):
    if num<1:
        return 1
    else:
        num=num*fact(num-1)
        return num

num=int(input("Enter the number : "))
print(f"Factorial of {num} is {fact(num)}")