num = int(input("Enter a number:     "))

if num%4 == 0:
    print("This number is divisible by 4 and even")
elif num%2 == 0:
    print("This number is even")
else:
    print("This number is odd")


num_one = int(input("Enter a number:     "))
num_two = int(input("Enter another number:     "))

if num_one%num_two==0:
    print("This number is divisible by the other")
else:
    print("This number is not divisible by the other")

    