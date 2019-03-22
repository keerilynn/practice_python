num = int(input("Enter a number:     "))

divisor_list = []
numbers = range(1, num + 1)
numbers_list = list(numbers)

for numbers in numbers_list:
    if num % numbers == 0:
        divisor_list.append(numbers)


print(divisor_list)