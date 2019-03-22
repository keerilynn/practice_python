all_list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
even_list = []

for n in all_list:
    if n % 2 == 0:
        even_list.append(n)

print(even_list)